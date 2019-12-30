from pandas import DataFrame
from fuzzywuzzy import fuzz
from joblib import Parallel, delayed
from chronometry.progress import ProgressBar, iterate


def _get_fuzz_ratio_of_strings(s1, s2, na_ratio, two_na_ratio, case_sensitivity):
	if s1 is None and s2 is None:
		return two_na_ratio
	elif s1 is None or s2 is None:
		return na_ratio
	else:
		if case_sensitivity == 0:
			return fuzz.ratio(s1.lower(), s2.lower()) / 100.0
		elif case_sensitivity == 1:
			return fuzz.ratio(s1, s2) / 100.0
		elif case_sensitivity > 1 or case_sensitivity < 0:
			raise ValueError('case_sensitivity should be between 0 and 1')
		else:
			csw = case_sensitivity
			ciw = 1 - case_sensitivity
			return (fuzz.ratio(s1.lower(), s2.lower()) * csw) + (fuzz.ratio(s1, s2) * ciw) / 100


def _get_fuzz_ratio(strings1, strings2, na_ratio, two_na_ratio, case_sensitivity):
	"""
	:type strings1: str or list[str] or tuple[str]
	:type strings2: str or list[str] or tuple[str]
	:type na_ratio: float
	:type two_na_ratio: float
	:rtype: float
	"""
	if not isinstance(strings1, (list, tuple, str)) or not isinstance(strings2, (list, tuple, str)):
		raise TypeError('strings1 and strings2 should be lists or tuples or strings')

	if isinstance(strings1, str):
		strings1 = [strings1]
	if isinstance(strings2, str):
		strings2 = [strings2]

	if len(strings1) != len(strings2):
		raise ValueError('strings1 and strings2 should be of the same size')

	ratios = [
		_get_fuzz_ratio_of_strings(
			s1=s1, s2=s2, na_ratio=na_ratio, two_na_ratio=two_na_ratio, case_sensitivity=case_sensitivity
		)
		for s1, s2 in zip(strings1, strings2)
	]
	return sum(ratios) / len(ratios)


def _get_ratio_between_strings_and_row(strings, row, right_on, na_ratio, two_na_ratio, case_sensitivity):
	return _get_fuzz_ratio(
		strings1=strings, strings2=[row[x] for x in right_on], na_ratio=na_ratio, two_na_ratio=two_na_ratio,
		case_sensitivity=case_sensitivity
	)


def _find_best_matching_row(strings, right, right_on, na_ratio, two_na_ratio, case_sensitivity, score_name, num_threads, echo):
	right = right.copy()

	if num_threads == 1:

		right[score_name] = ProgressBar.apply(
			data=right,
			function=lambda row: _get_ratio_between_strings_and_row(
				strings=strings, row=row, right_on=right_on, na_ratio=na_ratio, two_na_ratio=two_na_ratio,
				case_sensitivity=case_sensitivity
			),
			echo=echo
		)

	else:

		parallel = Parallel(n_jobs=num_threads, backend='threading', require='sharedmem')
		progress_bar = ProgressBar(total=len(right) + 1, echo=echo)
		right[score_name] = parallel(
			delayed(_get_ratio_between_strings_and_row)(
				strings=strings, row=row, right_on=right_on, na_ratio=na_ratio, two_na_ratio=two_na_ratio,
				case_sensitivity=case_sensitivity
			)
			for index, row in iterate(right.iterrows(), progress_bar=progress_bar)
		)
		progress_bar.show(amount=len(right) + 1)

	right = right.sort_values(by=score_name, ascending=False)
	return right.iloc[0]


def _match_rows(row, right, left_on, right_on, na_ratio, two_na_ratio, score_name, case_sensitivity, num_threads, echo):
	strings = [row[x] for x in left_on]

	return _find_best_matching_row(
		strings=strings, right=right, right_on=right_on, na_ratio=na_ratio, two_na_ratio=two_na_ratio,
		case_sensitivity=case_sensitivity, score_name=score_name, num_threads=num_threads, echo=echo
	)


def fuzzy_left_merge(
		left, right, left_on=None, right_on=None, on=None, suffixes=None, score_name='match_ratio',
		na_ratio=0.5, two_na_ratio=0.75, case_sensitivity=0.5, num_threads=-1, echo=1
):
	"""
	:type left: DataFrame
	:type right: DataFrame
	:type left_on:
	:type right_on:
	:type on:
	:type how:
	:type num_threads:
	:rtype:
	"""
	suffixes = suffixes or ['_x', '_y']
	if score_name in left.columns or score_name in right.columns:
		raise ValueError('use a score_name different from column names.')

	data1 = left.copy()
	data2 = right.copy()

	if on is None:
		on = data1.columns & data2.columns

	if left_on is None:
		left_on = on
	if right_on is None:
		right_on = on

	data2['fuzzy_id'] = range(len(data2))

	def match_rows_function(**kwargs):
		return _match_rows(**kwargs)['fuzzy_id']

	if num_threads == 1:
		data1['fuzzy_id'] = ProgressBar.apply(
			data=data1,
			echo=echo,
			function=lambda row: match_rows_function(
				row=row, right=data2, left_on=left_on, right_on=right_on, na_ratio=na_ratio, two_na_ratio=two_na_ratio,
				case_sensitivity=case_sensitivity, score_name=score_name, num_threads=1, echo=echo - 1
			)
		)

	else:
		parallel = Parallel(n_jobs=num_threads, backend='threading', require='sharedmem')
		progress_bar = ProgressBar(total=len(data1) + 1, echo=echo)



		data1['fuzzy_id'] = parallel(
			delayed(match_rows_function)(
				row=row, right=data2,
				left_on=left_on, right_on=right_on, na_ratio=na_ratio, two_na_ratio=two_na_ratio,
				case_sensitivity=case_sensitivity, score_name=score_name,
				num_threads=1, echo=echo - 1
			)
			for index, row in iterate(data1.iterrows(), progress_bar=progress_bar)
		)
		progress_bar.show(amount=len(data1) + 1)

	data1['fuzzy_id'] = data1['fuzzy_id'].astype(str)
	data2['fuzzy_id'] = data2['fuzzy_id'].astype(str)

	return data1.merge(right=data2, on='fuzzy_id', how='left', suffixes=suffixes)
