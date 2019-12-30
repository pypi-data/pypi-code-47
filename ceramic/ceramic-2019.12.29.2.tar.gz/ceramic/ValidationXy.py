from .Xy import Xy
from .get_cross_validation_by_group import get_cross_validation_by_group
from .TrainingTestXy import TransformedTrainingTestXy
from nightingale.feature_importance import get_feature_importances
from nightingale.feature_importance import get_coefficients
from nightingale.tuning import ModelGrid
from nightingale.evaluation import evaluate_classification, evaluate_regression
from ravenclaw.wrangling import bring_to_front
from copy import deepcopy
from pandas import DataFrame
from joblib import Parallel, delayed
import warnings
from chronometry.progress import ProgressBar, iterate


class ValidationXy(TransformedTrainingTestXy):
	def __init__(
			self, data, x_columns, y_column, id_columns=None,
			holdout_ratio=0.2, num_validation_splits=5, random_state=None,
			transformer=None, num_threads=-1, echo=1
	):
		self._echo = echo
		self._num_threads = num_threads
		progress_bar = ProgressBar(total=num_validation_splits + 1, echo=self._echo)
		progress_amount = 0
		progress_bar.show(amount=progress_amount, text='preparing validation Xy')
		cross_validation = get_cross_validation_by_group(
			data=data, id_columns=id_columns, num_splits=num_validation_splits,
			holdout_ratio=holdout_ratio, random_state=random_state
		)

		super().__init__(
			data=data, x_columns=x_columns, y_column=y_column, id_columns=id_columns,
			training_rows=cross_validation['validation'], training_name='validation',
			test_rows=cross_validation['holdout'], test_name='holdout', transformer=deepcopy(transformer)
		)
		progress_amount += 1
		progress_bar.show(amount=progress_amount, text='preparing folds')

		def transform_training_test_xy(fold):
			return TransformedTrainingTestXy(
				data=data, x_columns=x_columns, y_column=y_column, id_columns=id_columns,
				training_rows=fold['training'], test_rows=fold['test'], transformer=deepcopy(transformer)
			)

		if self._num_threads == 1:
			self._folds = [
				transform_training_test_xy(fold=fold)
				for fold in iterate(cross_validation['folds'], text='preparing folds (single-threaded)')
			]
		else:
			processor = Parallel(n_jobs=self._num_threads, backend='threading', require='sharedmem')
			self._folds = processor(
				delayed(transform_training_test_xy)(fold=fold)
				for fold in iterate(cross_validation['folds'], text='preparing folds (multi-threaded)')
			)

	@property
	def validation(self):
		"""
		:rtype: Xy
		"""
		return self['validation']

	@property
	def holdout(self):
		"""
		:rtype: Xy
		"""
		return self['holdout']

	@property
	def folds(self):
		"""
		:rtype: list[TransformedTrainingTestXy]
		"""
		return self._folds

	def represent_data(self, max_columns=None, max_rows=None):
		"""
		:type max_columns: NoneType or int
		:type max_rows: NoneType or int
		:rtype: dict[str, DataFrame]
		"""

		result = {'full_data': super().represent_data(max_columns=max_columns, max_rows=max_rows)}
		for i, fold in enumerate(self.folds):
			result[f'fold_{i + 1}'] = fold.represent_data(max_columns=max_columns, max_rows=max_rows)
		return result

	def validate(
			self, problem_type, evaluation_function=None, model=None, model_name=None, model_grid=None,
			num_threads=None, return_models=True, raise_error=False, main_metric=None, best_model_criteria=None,
			measure_influence=True, num_influence_points=400,
			echo=None
	):
		"""
		:param callable evaluation_function:
		:param str problem_type: either 'regression' of 'classification'
		:param model: a regressor or classifier
		:param str or NoneType model_name:
		:param ModelGrid or NoneType model_grid:
		:param dict[str, list or str or int or float] parameter_grid: a dictionary telling how the grid of models should be built
		:param int num_threads: for parallel computing
		:param bool return_models: whether or not trained models should be returned
		:param bool raise_error:
		:param str main_metric: the metric to be used for choosing the best model
		:param str best_model_criteria: 'highest' means the model with the highest metric value should be chosen
		:param int or bool or ProgressBar echo:
		:rtype: dict[str,]
		"""
		echo = echo or self._echo
		num_threads = num_threads or self._num_threads

		if model is not None:
			try:
				model_class_name = model.__name__
			except AttributeError:
				model_class_name = None
		else:
			model_class_name = None

		if problem_type.lower().startswith('class'):
			model_name = model_name or model_class_name or 'classifier'
			main_metric = main_metric or 'f1_score'
			best_model_criteria = best_model_criteria or 'highest'
			evaluation_function = evaluation_function or evaluate_classification
		else:
			model_name = model_name or model_class_name or 'regressor'
			main_metric = main_metric or 'rmse'
			best_model_criteria = best_model_criteria or 'lowest'
			evaluation_function = evaluation_function or evaluate_regression

		if model is not None and model_grid is None:
			models = {model_name: model}
			parameters_data = None
			parameters_dictionary = None

		elif model is None and model_grid is not None:
			models = model_grid.models
			parameters_data = model_grid.parameter_table
			parameters_dictionary = model_grid.parameters

		else:
			raise ValueError('either a preset model should be given or a model grid')


		def validate_fold(model_fold, shared_memory):
			"""
			:type fold: TransformedTrainingTestXy
			:type evaluation_function: callable
			:type model:
			:rtype: DataFrame
			"""
			shared_memory['progress_bar'].show(amount=shared_memory['progress_amount'], text='validating ...')
			with warnings.catch_warnings():
				warnings.simplefilter('ignore')

				this_model = deepcopy(model_fold['model'])
				fold = model_fold['fold']
				fold_num = model_fold['fold_num']
				model_name = model_fold['model_name']

				this_model.fit(X=fold.training.X, y=fold.training.y)
				training_evaluation = evaluation_function(this_model.predict(fold.training.X), fold.training.y)
				test_evaluation = evaluation_function(this_model.predict(fold.test.X), fold.test.y)
			shared_memory['progress_amount'] += 1
			return {
				'model': this_model,
				'model_name': model_name,
				'fold_num': fold_num,
				'training_evaluation': training_evaluation,
				'test_evaluation': test_evaluation
			}

		model_folds = [
			{'model_name': model_name, 'model': model, 'fold_num': fold_num + 1, 'fold': fold}
			for model_name, model in models.items() for fold_num, fold in enumerate(self.folds)
		]

		shared_memory = {
			'progress_bar': ProgressBar(total=1 + len(models) * len(self.folds), echo=echo),
			'progress_amount': 0
		}

		with warnings.catch_warnings():
			warnings.simplefilter("ignore")
			if num_threads == 1:
				result = [
					validate_fold(model_fold=model_fold, shared_memory=shared_memory) for model_fold in model_folds
				]
			else:
				result = Parallel(
					n_jobs=num_threads, backend='threading', require='sharedmem'
				)(delayed(validate_fold)(model_fold, shared_memory) for model_fold in model_folds)


		training = []
		test = []
		trained_models = []
		feature_importances_list = []
		coefficients_list = []

		for record in result:
			model = record['model']
			training_evaluation = record['training_evaluation']
			test_evaluation = record['test_evaluation']
			training_evaluation['fold_num'] = record['fold_num']
			test_evaluation['fold_num'] = record['fold_num']
			training_evaluation['model_name'] = record['model_name']
			test_evaluation['model_name'] = record['model_name']
			training.append(training_evaluation)
			test.append(test_evaluation)

			feature_importances = get_feature_importances(
				model=model, columns=self.x_columns, model_name=record['model_name'], fold_num=record['fold_num'],
				raise_error=raise_error
			)
			if feature_importances is not None:
				feature_importances_list.append(feature_importances)

			coefficients = get_coefficients(
				model=model, columns=self.x_columns, model_name=record['model_name'], fold_num=record['fold_num'],
				raise_error=raise_error
			)
			if coefficients is not None:
				coefficients_list.append(coefficients)

			trained_models.append(model)

		with warnings.catch_warnings():
			warnings.simplefilter("ignore")

			feature_importances = DataFrame.from_records(feature_importances_list)
			coefficients = DataFrame.from_records(coefficients_list)

			training = bring_to_front(data=DataFrame.from_records(training), columns=['model_name', 'fold_num'])
			test = bring_to_front(data=DataFrame.from_records(test), columns=['model_name', 'fold_num'])

			result = {
				'training': training,
				'test': test
			}

			if feature_importances.shape[1] > 0:
				result['feature_importances'] = bring_to_front(
					data=feature_importances, columns=['model_name', 'fold_num']
				)
				result['mean_feature_importances'] = result['feature_importances'].drop(
					columns='fold_num'
				).groupby(['model_name']).mean().reset_index()

			if coefficients.shape[1] > 0:
				result['coefficients'] = bring_to_front(
					data=coefficients, columns=['model_name', 'fold_num']
				)
				result['mean_coefficients'] = result['coefficients'].drop(
					columns='fold_num'
				).groupby(['model_name']).mean().reset_index()

			if return_models:
				result['models'] = trained_models

			shared_memory['progress_amount'] += 1
			shared_memory['progress_bar'].show(amount=shared_memory['progress_amount'], text='validation complete.')

			if main_metric is not None and main_metric in result['test'].columns:
				aggregated_training = training[['model_name', main_metric]].groupby('model_name').mean().reset_index()
				aggregated_test = test[['model_name', main_metric]].groupby('model_name').mean().reset_index()
				aggregated_result = aggregated_training.merge(
					right=aggregated_test, on='model_name', how='outer', suffixes=['_training', '_test']
				)
				if parameters_data is not None:
					aggregated_result = parameters_data.merge(right=aggregated_result, on='model_name', how='outer', suffixes=['_parameter', ''])

				aggregated_result = aggregated_result.sort_values(
					f'{main_metric}_test', ascending=best_model_criteria != 'highest'
				)

				result['aggregate'] = aggregated_result
				best_model_name = aggregated_result.head(1)['model_name'].values[0]

				if parameters_dictionary is not None:
					result['best_model_parameters'] = parameters_dictionary[best_model_name]

				best_model = models[best_model_name]
				trained_best_model = deepcopy(best_model)
				trained_best_model.fit(X=self.validation.X, y=self.validation.y)
				best_model_performance = evaluation_function(
					trained_best_model.predict(self.holdout.X), self.holdout.y
				)
				result['best_model'] = best_model
				result['best_model_trained'] = trained_best_model
				result['best_model_performance'] = best_model_performance

				best_model_feature_importances = get_feature_importances(
					model=trained_best_model, columns=self.validation.x_columns, model_name=best_model_name,
					raise_error=raise_error
				)

				best_model_coefficients = get_coefficients(
					model=trained_best_model, columns=self.validation.x_columns, model_name=best_model_name,
					raise_error=raise_error
				)

				if best_model_feature_importances is not None:
					result['best_model_feature_importances'] = best_model_feature_importances

				if best_model_coefficients is not None:
					result['best_model_coefficients'] = best_model_coefficients

				if measure_influence:
					result['influence'] = self.get_influence(
						model=trained_best_model, num_threads=num_threads, num_points=num_influence_points, echo=echo
					)

		return result
