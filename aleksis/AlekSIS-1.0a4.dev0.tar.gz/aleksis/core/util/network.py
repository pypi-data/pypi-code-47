import re

import requests
from django.utils import timezone, formats
from ics import Calendar
from requests import RequestException

from dashboard import settings
from dashboard.caches import LATEST_ARTICLE_CACHE, CURRENT_EVENTS_CACHE

WP_DOMAIN: str = "https://katharineum-zu-luebeck.de"

VS_COMPOSER_REGEX = re.compile(r"\[[\w\s\d!\"§$%&/()=?#'+*~’¸´`;,·.:…\-_–]*\]")


def get_newest_articles(domain: str = WP_DOMAIN,
                        limit: int = 5,
                        author_whitelist: list = None,
                        author_blacklist: list = None,
                        category_whitelist: list = None,
                        category_blacklist: list = None
                        ):
    """
    This function returns the newest articles/posts of a WordPress site.

    :param domain: The domain to get the newest posts from (for example https://wordpress.com). Don't put a slash (/) at the end!
    :param limit: if 0: all posts will be shown, else nly the certain number
    :param author_whitelist: If this list is filled, only articles which are written by one of this authors will be shown
    :param author_blacklist: If the author's id (an integer) is in this list, the article won't be shown
    :param category_whitelist: If this list is filled, only articles which are in one of this categories will be shown
    :param category_blacklist: If the category's id (an integer) is in this list, the article won't be shown
    :return: a list of the newest posts/articles
    """
    # Make mutable default arguments unmutable
    if category_whitelist is None:
        category_whitelist = []
    if category_blacklist is None:
        category_blacklist = []
    if author_whitelist is None:
        author_whitelist = []
    if author_blacklist is None:
        author_blacklist = []

    suffix: str = "/wp-json/wp/v2/posts"
    url: str = domain + suffix
    try:
        site: requests.request = requests.get(url, timeout=10)
        data: dict = site.json()
    except RequestException as e:
        print("E", str(e))
        return []
    posts: list = []

    for post in data:
        if post["author"] not in author_blacklist:
            if len(author_whitelist) > 0 and post["author"] not in author_whitelist:
                continue

            if post["categories"][0] not in category_blacklist:
                if len(category_whitelist) > 0 and post["categories"][0] not in category_whitelist:
                    continue

                # Now get the link to the image
                if post["_links"].get("wp:featuredmedia", False):
                    media_site: requests.request = requests.get(post["_links"]["wp:featuredmedia"][0]["href"]).json()
                    image_url: str = media_site["guid"]["rendered"]
                else:
                    image_url: str = ""

                # Replace VS composer tags if activated
                if settings.latest_article_settings.replace_vs_composer_stuff:
                    excerpt = VS_COMPOSER_REGEX.sub("", post["excerpt"]["rendered"])
                else:
                    excerpt = post["excerpt"]["rendered"]

                posts.append(
                    {
                        "title": post["title"]["rendered"],
                        "short_text": excerpt,
                        "link": post["link"],
                        "image_url": image_url,
                    }
                )
        if len(posts) >= limit and limit >= 0:
            break

    return posts


@LATEST_ARTICLE_CACHE.decorator
def get_newest_article_from_news(domain=WP_DOMAIN):
    newest_articles: list = get_newest_articles(domain=domain, limit=1, category_whitelist=[1, 27])
    if len(newest_articles) > 0:
        return newest_articles[0]
    else:
        return None


def get_current_events(calendar: Calendar, limit: int = 5) -> list:
    """
    Get upcoming events from calendar
    :param calendar: The calendar object
    :param limit: Count of events
    :return: List of upcoming events
    """
    i: int = 0
    events: list = []
    for event in calendar.timeline.start_after(timezone.now()):
        # Check for limit
        if i >= limit:
            break
        i += 1

        # Create formatted dates and times for begin and end
        begin_date_formatted = formats.date_format(event.begin)
        end_date_formatted = formats.date_format(event.end)
        begin_time_formatted = formats.time_format(event.begin.time())
        end_time_formatted = formats.time_format(event.end.time())

        if event.begin.date() == event.end.date():
            # Event is only on one day
            formatted = begin_date_formatted

            if not event.all_day:
                # No all day event
                formatted += " " + begin_time_formatted

            if event.begin.time != event.end.time():
                # Event has an end time
                formatted += " – " + end_time_formatted

        else:
            # Event is on multiple days
            if event.all_day:
                # Event is all day
                formatted = "{} – {}".format(begin_date_formatted, end_date_formatted)
            else:
                # Event has begin and end times
                formatted = "{} {} – {} {}".format(begin_date_formatted, begin_time_formatted, end_date_formatted,
                                                   end_time_formatted)

        events.append({
            "name": event.name,
            "begin_timestamp": event.begin.timestamp,
            "end_timestamp": event.end.timestamp,
            "formatted": formatted
        })

    return events


@CURRENT_EVENTS_CACHE.decorator
def get_current_events_with_cal(limit: int = 5) -> list:
    # Get URL
    calendar_url: str = settings.current_events_settings.calendar_url
    if calendar_url is None or calendar_url == "":
        return []

    # Get ICS
    try:
        calendar: Calendar = Calendar(requests.get(calendar_url, timeout=3).text)
    except RequestException as e:
        print("E", str(e))
        return []

    # Get events
    return get_current_events(calendar, settings.current_events_settings.events_count)
