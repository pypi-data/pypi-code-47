import re

from urllib.parse import urlencode, urljoin

import bs4
import requests

from .exceptions import MovieNotFound


class Backend(object):
    gross_pattern = re.compile(r'\$\d[\d,]+')

    def search_movies(self, search_term):
        document = self.get_page(
            'http://www.boxofficemojo.com/search/',
            params={'q': search_term})
        return self.parse_search_results(document, search_term)

    def parse_search_results(self, document, search_term):
        raise NotImplementedError

    def get_box_office(self, movie_id):
        raise NotImplementedError

    # --- Helper methods ---

    def get_page(self, url, **kwargs):
        # Translate relative paths to absolute URLs.
        if not re.match(r'^https?://', url):
            url = urljoin('https://www.boxofficemojo.com', url)
        response = requests.get(url, **kwargs)
        response.raise_for_status()
        return bs4.BeautifulSoup(response.content, 'html.parser')

    def follow_link(self, document, link_text, parent_selector=None,):
        container = document
        if parent_selector:
            container = container.select_one(parent_selector)
        link = container.find('a', text=link_text)
        return self.get_page(link['href'])


class LegacyBackend(Backend):
    def parse_search_results(self, document, search_term):
        movie_link_pattern = re.compile(r'/movies/\?id=([\w\-\.]+)')

        def movie_from_row(row):
            first_cell = row.select_one('td:nth-of-type(1)')
            if first_cell is None:
                return None, None

            movie_link = first_cell.find('a')
            if movie_link is None:
                return None, None

            movie_link_match = movie_link_pattern.search(movie_link['href'])
            if movie_link_match is None:
                return None, None

            return movie_link_match.group(1), first_cell.text.strip()

        results = []
        for row in document.find_all('tr'):
            movie_id, title = movie_from_row(row)
            if movie_id:
                # If there's a highlighted row, that's an exact match.
                results.append({
                    'movie_id': movie_id,
                    'title': title,
                    'exact': row['bgcolor'] == '#FFFF99'
                })

        return results

    def get_box_office(self, movie_id):
        url = 'http://www.boxofficemojo.com/movies/?' + urlencode({
            'id': movie_id,
            'page': 'daily',
            'view': 'chart'
        })
        document = self.get_page(url)

        title_match = re.search(r'(.*) - Daily Box Office Results',
                                document.title.text)
        if title_match is None:
            raise MovieNotFound(movie_id)

        result = {
            'title': title_match.group(1),
            'href': url,
            'box_office': []
        }

        chart = document.find(id='chart_container')

        if chart is None:
            return result

        table = chart.next_sibling
        rows = table.find_all('tr')

        box_office = result['box_office']

        for row in rows:
            cells = row.find_all('td')
            if len(cells) < 10:
                continue

            day, date, rank, gross, _, _, theaters, _, cumulative = [
                cell.text for cell in cells[:9]]
            if not self.gross_pattern.match(gross):
                continue

            box_office.append({
                'day': day,
                'date': date,
                'rank': parse_int(rank),
                'gross': parse_int(gross),
                'theaters': parse_int(theaters),
                'cumulative': parse_int(cumulative)
            })

        return result


class Dec2019Backend(Backend):
    def parse_search_results(self, document, search_term):
        movie_link_pattern = re.compile(r'/title/(\w+)')

        results = []
        for link in document.select('.titles a.a-size-medium'):
            movie_link_match = movie_link_pattern.search(link['href'])
            if movie_link_match is None:
                continue

            results.append({
                'movie_id': movie_link_match.group(1),
                'title': link.text,
                'exact': link.text.lower() == search_term.lower()
            })

        return results

    def get_box_office(self, movie_id):
        url = 'https://www.boxofficemojo.com/title/{}'.format(movie_id)
        title_page = self.get_page(url)

        result = {
            'title': title_page.find('h1').text,
            'href': url,
            'box_office': []
        }

        release_page = self.follow_link(title_page, 'Original Release')
        box_office_page = self.follow_link(
            release_page, 'Domestic', parent_selector='.releases-by-region')

        rows = box_office_page.select('#table tr')

        box_office = result['box_office']

        for row in rows:
            cells = row.find_all('td')
            if len(cells) < 9:
                continue

            date, day, rank, gross, _, _, theaters, _, cumulative = [
                cell.text for cell in cells[:9]]
            if not self.gross_pattern.match(gross):
                continue

            box_office.append({
                'day': day,
                'date': date,
                'rank': parse_int(rank),
                'gross': parse_int(gross),
                'theaters': parse_int(theaters),
                'cumulative': parse_int(cumulative)
            })

        return result


def parse_int(value):
    try:
        return int(re.sub(r'[$,]', '', value))
    except ValueError:
        return None
