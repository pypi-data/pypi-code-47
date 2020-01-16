"""
This module contains Python wrapper for PAL Addtive Model Forecast (Prophet) algorithm.

The following class are available:

    * :class:`AdditiveModelForecast`
"""

#pylint: disable=too-many-lines, line-too-long
import logging
import uuid

from hdbcli import dbapi
from hana_ml.ml_exceptions import FitIncompleteError

from hana_ml.algorithms.pal.pal_base import (
    PALBase,
    ParameterTable,
    ListOfStrings,
    pal_param_register
)

logger = logging.getLogger(__name__)#pylint: disable=invalid-name

class _ProphetBase(PALBase):#pylint: disable=too-many-instance-attributes, too-few-public-methods
    """
    Additive model forecast base class.
    """

    seasonality_map = {'auto': -1, 'false': 0, 'true': 1}
    def __init__(self,#pylint: disable=too-many-arguments, too-many-locals
                 conn_context,
                 growth=None,
                 logistic_growth_capacity=None,
                 seasonality_mode=None,
                 seasonality=None,
                 num_changepoints=None,
                 changepoint_range=None,
                 regressor=None,
                 changepoints=None,
                 yearly_seasonality=None,
                 weekly_seasonality=None,
                 daily_seasonality=None,
                 seasonality_prior_scale=None,
                 holiday_prior_scale=None,
                 changepoint_prior_scale=None):
        super(_ProphetBase, self).__init__(conn_context)
        setattr(self, 'hanaml_parameters', pal_param_register())
        #P, D, Q in PAL has been combined to be one parameter `order`
        self.growth = self._arg('growth', growth, str)
        self.logistic_growth_capacity = self._arg('logistic_growth_capacity', logistic_growth_capacity, float)
        if self.growth == 'logistic' and self.logistic_growth_capacity is None:
            msg = "`logistic_growth_capacity` is mandatory when `growth` is 'logistic'."
            logger.error(msg)
            raise ValueError(msg)

        self.seasonality_mode = self._arg('seasonality_mode', seasonality_mode, str)
        self.seasonality = self._arg('seasonality', seasonality, str)
        self.num_changepoints = self._arg('num_changepoints', num_changepoints, int)
        self.changepoint_range = self._arg('changepoint_range', changepoint_range, float)
        self.regressor = self._arg('regressor', regressor, str)
        self.changepoints = self._arg('changepoints', changepoints, ListOfStrings)
        self.yearly_seasonality = self._arg('yearly_seasonality', yearly_seasonality, self.seasonality_map)
        self.weekly_seasonality = self._arg('weekly_seasonality', weekly_seasonality, self.seasonality_map)
        self.daily_seasonality = self._arg('daily_seasonality', daily_seasonality, self.seasonality_map)
        self.seasonality_prior_scale = self._arg('seasonality_prior_scale', seasonality_prior_scale, float)
        self.holidays_prior_scale = self._arg('holiday_prior_scale', holiday_prior_scale, float)
        self.changepoint_prior_scale = self._arg('changepoint_prior_scale', changepoint_prior_scale, float)

    def _fit(self, data, holiday=None):
        """
        Additive model forecast fit function.
        """
        unique_id = str(uuid.uuid1()).replace('-', '_').upper()
        holiday_tbl = None
        if holiday is None:
            holiday_tbl = "#PAL_ADDITIVE_MODEL_FORECAST_HOLIDAY_TBL_{}_{}".format(self.id, unique_id)
            with self.conn_context.connection.cursor() as cur:
                cur.execute('CREATE LOCAL TEMPORARY COLUMN TABLE {} ("ts" TIMESTAMP, "NAME" VARCHAR(255),\
                "LOWER_WINDOW" INTEGER, "UPPER_WINDOW" INTEGER)'.format(holiday_tbl))
                holiday = self.conn_context.table(holiday_tbl)
        model_tbl = '#PAL_ADDITIVE_MODEL_FORECAST_MODEL_TBL_{}_{}'.format(self.id, unique_id)
        outputs = [model_tbl]
        param_rows = [
            ('GROWTH', None, None, self.growth),
            ('CAP', None, self.logistic_growth_capacity, None),
            ('SEASONALITY_MODE', None, None, self.seasonality_mode),
            ('SEASONALITY', None, None, self.seasonality),
            ('NUM_CHANGEPOINTS', self.num_changepoints, None, None),
            ('CHANGEPOINT_RANGE', None, self.changepoint_range, None),
            ('REGRESSOR', None, None, self.regressor),
            ('YEARLY_SEASONALITY', self.yearly_seasonality, None, None),
            ('WEEKLY_SEASONALITY', self.weekly_seasonality, None, None),
            ('DAILY_SEASONALITY', self.daily_seasonality, None, None),
            ('SEASONALITY_PRIOR_SCALE', None, self.seasonality_prior_scale, None),
            ('HOLIDAYS_PRIOR_SCALE', None, self.holidays_prior_scale, None),
            ('CHANGEPOINT_PRIOR_SCALE', None, self.changepoint_prior_scale, None)
            ]
        if self.changepoints is not None:
            for changepoint in self.changepoints:
                param_rows.extend([('CHANGE_POINT', None, None, changepoint)])
        try:
            param_t = ParameterTable(name='#PARAM_TBL')
            self._call_pal_auto('PAL_ADDITIVE_MODEL_ANALYSIS',
                                data,
                                holiday,
                                param_t.with_data(param_rows),
                                *outputs)
        except dbapi.Error as db_err:
            msg = str(self.conn_context.hana_version())
            logger.exception("HANA version: %s. %s", msg, str(db_err))
            if holiday_tbl is not None:
                self._try_drop(holiday_tbl)
            self._try_drop('#PARAM_TBL')
            self._try_drop(outputs)
            raise

        #pylint: disable=attribute-defined-outside-init
        self.model_ = self.conn_context.table(model_tbl)

    def _predict(self, data, logistic_growth_capacity=None, interval_width=None, uncertainty_samples=None):
        """
        Makes time series forecast based on the estimated additive regression analysis model.
        """
        if getattr(self, 'model_', None) is None:
            raise FitIncompleteError("Model not initialized. Perform a fit first.")

        unique_id = str(uuid.uuid1()).replace('-', '_').upper()
        data_tbl = None
        result_tbl = "#PAL_ADDITIVE_MODEL_FORECAST_RESULT_TBL_{}_{}".format(self.id, unique_id)
        param_rows = [
            ("CAP", None, logistic_growth_capacity, None),
            ("INTERVAL_WIDTH", None, interval_width, None),
            ("UNCERTAINTY_SAMPLES", uncertainty_samples, None, None)]
        try:
            if data is None:
                data_tbl = "#PAL_ADDITIVE_MODEL_FORECAST_DATA_TBL_{}_{}".format(self.id, unique_id)
                with self.conn_context.connection.cursor() as cur:
                    cur.execute('CREATE LOCAL TEMPORARY COLUMN TABLE {} ("TIMESTAMP" {},"SERIES" DOUBLE)'\
                    .format(data.dtypes()[0][1], data_tbl))
                    data = self.conn_context.table(data_tbl)

            param_t = ParameterTable(name='#PARAM_TBL')
            self._call_pal_auto('PAL_ADDITIVE_MODEL_PREDICT',
                                data,
                                self.model_,
                                param_t.with_data(param_rows),
                                result_tbl)
        except dbapi.Error as db_err:
            msg = str(self.conn_context.hana_version())
            logger.exception("HANA version: %s. %s", msg, str(db_err))

            if data_tbl is not None:
                self._try_drop(data_tbl)

            self._try_drop('#PARAM_TBL')
            self._try_drop(result_tbl)
            raise

        return self.conn_context.table(result_tbl)

class AdditiveModelForecast(_ProphetBase):#pylint: disable=too-many-instance-attributes
    r"""
    PAL Additive Model Forecast.

    Parameters
    ----------

    conn_context : ConnectionContext

        The connection to the SAP HANA system.

    growth : {'linear', 'logistic'}, optional

        Specify a trend, which could be either linear or logistic.

        Defaults to 'linear'.

    logistic_growth_capacity: float, optional

        Specify the carrying capacity for logistic growth.

        Mandatory and valid only when ``growth`` is 'logistic'.

    seasonality_mode : {'additive', 'multiplicative'}, optional

        Mode for seasonality, either additive or muliplicative.

    seasonality : str, optional

        Add seasonality to model, is a json format, include NAME, PERIOD, FOURIER_ORDER, PRIOR_SCALE,MODE,\
        for example: '{ "NAME": "MONTHLY", "PERIOD":30, "FOURIER_ORDER":5 }'.

        No seasonality will be added to the model if this parameter is not provided.

    num_changepoints : int, optional

        Number of potential changepoints.

        Defaults to 25 if not provided.

        Not effective if ``changepoints`` is provided.

    changepoint_range : float, optional

        Proportion of history in which trend changepoints will be estimated.

        Defaults to 0.8.

        Not effective if ``changepoints`` is provided.

    regressor : str, optional

        Specify the regressor, include PRIOR_SCALE, STANDARDIZE, and MODE, it is json format \
        such as '{ "NAME": "X1", "PRIOR_SCALE":4, "MODE": "additive" }'.

    changepoints : list of str, optional,

        Specify a list of changepoints in the format of timestamp, such as ['2019-01-01 00:00:00, '2019-02-04 00:00:00']

    yearly_seasonality : {'auto', 'false', 'true'}, optional

        Specify whether or not to fit yearly seasonality.

        'false' and 'true' simply corresponds to their logical meaning, while 'auto' means automatically determined from the input data.

    weekly_seasonality : {'auto', 'false', 'true'}, optional

        Specify whether or not to fit the weekly seasonality.

        'auto' means automatically determined from input data.

    daily_seasonality : {'auto', 'false', 'true'}, optional

        Specify whether or not to fit the daily seasonality.

        'auto' means automatically determined from input data.

    seasonality_prior_scale : float, optional

        Parameter modulating the strength of the seasonality model.

        Defaults to 10 if not provided.

    holiday_prior_scale : float, optional

        Parameter modulating the strength of the holiday components model.

        Defaults to 10 if not provided.

    changepoint_prior_scale : float, optional

        Parameter modulating the flexibility of the automatic changepoint selection.
        Defaults to 0.05 if not provided.


    Attributes
    ----------

    model_ : DataFrame

        Model content.


    Examples
    --------

    Additive Model Forecast example:

    Input dataframe df:

    >>> df.collect()
        ts      val
    2012-01-01 23:35:45 3.0
    2012-01-01 23:40:45 2.0
    2012-01-01 23:45:45 1.0
    2012-01-01 23:50:45 2.0
    2012-01-01 23:55:45 3.0
    2012-01-02 00:00:45 4.0
    2012-01-02 00:05:45 5.0
    Create an Additive Model Forecast model:

    >>> amf = additive_model_forecast.AdditiveModelForecast(connection_context)
    Perform fit on the given data:

    >>> amf.fit(data=df)

    Expected output:

    >>> amf.model_.collect().head(5)
    ROW_INDEX   MODEL_CONTENT
            0   {"FLOOR":0.0,"GROWTH":"linear","SEASONALITY_MO...

    Perform predict on the model:

    >>> result = amf.predict(forecast_method='innovations_algorithm', forecast_length=10)

    Expected output:

    >>> result.collect().head(6)
        ts                  YHAT        YHAT_LOWER  YHAT_UPPER
    0   2012-01-01 23:35:45 1.917860    0.559639    3.269494
    1   2012-01-01 23:40:45 2.179848    0.846120    3.541307
    2   2012-01-01 23:45:45 2.441836    1.022167    3.788882
    3   2012-01-01 23:50:45 2.703824    1.335432    4.101667
    4   2012-01-01 23:55:45 2.965812    1.546318    4.276872
    5   2012-01-02 00:00:45 3.227801    1.775130    4.621328
    6   2012-01-02 00:05:45 3.489789    2.113276    4.896699
    """
    def fit(self, data, holiday=None):#pylint: disable=too-many-arguments,too-many-branches
        """
        Additive model forecast.

        Parameters
        ----------

        data : DataFrame

            Input data. The structure is as follows.

            - The first column: index (ID), timestamp.
            - The second column: raw data, int or float.
            - Other columns: external data, int or float.

        holiday : DataFrame

            Input holiday data. The structure is as follows.

            - The first column : index, timestamp
            - The second column : name, varchar
            - The third column : lower window of holiday, int
            - The last column : upper window of holiday, int

        """
        super(AdditiveModelForecast, self)._fit(data, holiday)

    def predict(self, data, logistic_growth_capacity=None, interval_width=None, uncertainty_samples=None):
        """
        Makes time series forecast based on the estimated Additive Model Forecast model.

        Parameters
        ----------

        data : DataFrame, optional

            Index and exogenous variables for forecast. \
            The structure is as follows.

            - First column: Index (ID), timestamp.
            - Other columns : external data, int or float.

        logistic_growth_capacity: float, optional

            specify the carrying capacity for logistic growth.

        interval_width : float, optional

            Width of the uncertainty intervals.

        uncertainty_samples : int, optional

            Number of simulated draws used to estimate uncertainty intervals.

        Returns
        -------

        DataFrame
            Forecasted values, structured as follows:

              - ID, type timestamp.
              - YHAT, type DOUBLE, forecast value.
              - YHAT_LOWER, type DOUBLE, lower bound of confidence region.
              - YHAT_UPPER, type DOUBLE, higher bound of confidence region.
        """
        if getattr(self, 'model_', None) is None:
            raise FitIncompleteError("Model not initialized. Perform a fit first.")

        return super(AdditiveModelForecast, self)._predict(data, logistic_growth_capacity, interval_width, uncertainty_samples)
