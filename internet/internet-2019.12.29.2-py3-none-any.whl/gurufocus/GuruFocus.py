import requests
from requests.adapters import SSLError
import warnings
from pandas import concat
from bs4 import BeautifulSoup
from silverware import read_table
from ravenclaw import standardize_columns
from chronometry.progress import ProgressBar
from chronometry import get_elapsed, get_now
from time import sleep
from .countries import COUNTRIES as _COUNTRIES

NUM_RECORDS_PER_PAGE = 5000


class GuruFocus:
	def __init__(self, rate_limit_wait_seconds=0.01, cache=None, num_request_tries=4):
		self._rate_limit_wait = rate_limit_wait_seconds
		self._rate_limit_last_call = None
		self._num_request_tries = num_request_tries

		self._cache = cache
		if self._cache:
			self.request = self._cache.make_cached(
				id='gurufocus_request',
				function=self._request,
				sub_directory='gf_request'
			)
			self.get_table = self._cache.make_cached(
				id='gurufocus_get_table',
				function=self._get_table,
				sub_directory='gf_get_table'
			)

		else:
			self.request = self._request
			self.get_by_country = self._get_by_country
			self.get_table = self._get_table

	COUNTRIES = _COUNTRIES

	@property
	def cache(self):
		"""
		:rtype: disk.Cache or NoneType
		"""
		return self._cache

	def _request(self, url):
		for i in range(1, self._num_request_tries + 1):
			try:
				if self._rate_limit_wait and self._rate_limit_last_call:
					wait_time = self._rate_limit_wait - get_elapsed(start=self._rate_limit_last_call, unit='s')
					if wait_time > 0:
						sleep(wait_time)
				result = requests.get(url)
				break
			except SSLError as e:
				print(f'try {i}, error with get request with url="{url}"')
				warnings.warn(str(e))
				sleep(0.001 * 10 ** i)
		else:
			raise e

		if self._rate_limit_wait:
			self._rate_limit_last_call = get_now()

		return result

	@staticmethod
	def get_request_url(country, n, page=None):
		if page is None:
			return f'https://www.gurufocus.com/stock_list.php?n={n}&r={country}'
		else:
			return f'https://www.gurufocus.com/stock_list.php?n={n}&r={country}&p={page}'

	def _get_table(self, url):
		request = self.request(url)
		content = request.content
		soup = BeautifulSoup(content, "lxml")
		html_table = soup.find(name='table', attrs={'id': 'R1', 'class': 'R5'})
		table = read_table(html_table, parse_links=True, base_url='https://www.gurufocus.com')
		return standardize_columns(
			table.rename(columns={'': 'summary'})
		)

	def _get_by_country(self, country, n=None, page=None, echo=1):
		test = self.request(self.get_request_url(country=country, n=5)).content
		zzzz = self.request(self.get_request_url(country='ZZZZ', n=5)).content
		test_soup = BeautifulSoup(test, "lxml")
		zzzz_soup = BeautifulSoup(zzzz, "lxml")
		test_body = test_soup.find(name='table', attrs={'id': 'R1', 'class': 'R5'}).find(name='tbody')
		zzzz_body = zzzz_soup.find(name='table', attrs={'id': 'R1', 'class': 'R5'}).find(name='tbody')
		if test_body == zzzz_body:
			raise ValueError(country)

		test_page_links = test_soup.find(name='div', attrs={'class': 'page_links'})
		if test_page_links.text.lower().startswith('total records'):
			total_records = int(test_page_links.find(name='strong').text)
		else:
			raise ValueError('missing total records')

		if n is not None:
			url = self.get_request_url(country=country, n=n, page=page)
			return self.get_table(url=url)

		else:
			records = 0
			result = []
			this_page = None
			if total_records > NUM_RECORDS_PER_PAGE:
				progress_bar = ProgressBar(total=total_records, echo=echo)
			else:
				progress_bar = None

			while records < total_records:
				if progress_bar is not None:
					progress_bar.show(amount=records, text=f'{country}: {records} records')
				data = self._get_by_country(country=country, n=NUM_RECORDS_PER_PAGE, page=this_page)
				if len(data) < 1:
					break
				result.append(data)
				records += len(data)
				if page is None:
					page = 1
				else:
					page += 1
			if progress_bar is not None:
				progress_bar.show(amount=records, text=f'{country}: {records} records collected!')
			return concat(result).reset_index(drop=True)

	def get(self, country=None, n=None, echo=2):
		if country is not None:
			return self._get_by_country(country=country, n=n, echo=echo)
		else:
			progress_bar = ProgressBar(total=len(self.COUNTRIES), echo=echo)
			amount = 0
			results = []
			for country in self.COUNTRIES:
				progress_bar.show(amount=amount, text=country)
				result = self.get(country=country, n=n, echo=progress_bar - 1)
				result['country'] = country
				amount += 1
				results.append(result)
			results_data = concat(results).reset_index(drop=True)
			progress_bar.show(amount=amount, text=f'{len(results_data)} records collected!')
			return results_data
