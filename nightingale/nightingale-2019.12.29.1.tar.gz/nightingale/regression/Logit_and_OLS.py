import statsmodels.formula.api as smf
from .exceptions import BrokenModel
from .Regression import Regression


class Logit(Regression):

	def __init__(
			self, data, formula, significance_level=0.05, model_builder=None, family=None, groups=None, parent=None
	):
		super().__init__(
			data=data, formula=formula, model_builder=smf.logit, significance_level=significance_level, parent=parent
		)

	@property
	def coefficient_table(self):
		"""
		:rtype: DataFrame
		"""
		return super().coefficient_table.rename(columns={'P>|z|': 'p'})

	@property
	def fit(self):
		"""
		:rtype: Logit
		"""
		if self._fit is None:
			try:
				self._fit = self.model.fit(disp=False)
			except Exception as e:
				self._fit = BrokenModel(exception=e, regression=self)

		return self._fit

	@property
	def name(self):
		"""
		:rtype: str
		"""
		return 'logit'

class OLS(Regression):

	def __init__(self, data, formula, significance_level=0.05, model_builder=None, family=None, groups=None, parent=None):
		super().__init__(data=data, formula=formula, model_builder=smf.ols, significance_level=significance_level, parent=parent)

	@property
	def fit(self):
		"""
		:rtype: OLS
		"""
		if self._fit is None:
			try:
				self._fit = self.model.fit(disp=False)
			except Exception as e:
				self._fit = BrokenModel(exception=e, regression=self)

		return self._fit

	@property
	def name(self):
		"""
		:rtype: str
		"""
		return 'ols'

	@property
	def coefficient_table(self):
		"""
		:rtype: DataFrame
		"""
		return super().coefficient_table.rename(columns={'P>|t|': 'p'})
