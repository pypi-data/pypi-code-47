import pytest
import sys

import numpy as np

from seeq import spy
from seeq.sdk import *
from seeq.spy.assets import Asset, Mixin

from . import test_common


def setup_module():
    test_common.login()


class HVAC(Asset):

    @Asset.Attribute()
    def Temperature(self, metadata):
        # We use simple Pandas syntax to select for a row in the DataFrame corresponding to our desired tag
        return metadata[metadata['Name'].str.endswith('Temperature')]

    @Asset.Attribute()
    def Relative_Humidity(self, metadata):
        # All Attribute functions must take (self, metadata) as parameters
        return metadata[metadata['Name'].str.contains('Humidity')]


class Compressor(Asset):

    @Asset.Attribute()
    def Power(self, metadata):
        return metadata[metadata['Name'].str.endswith('Power')]


class Airflow_Attributes(Mixin):
    @Asset.Attribute()
    def Airflow_Rate(self, metadata):
        return {
            'Type': 'Signal',
            'Formula': 'sinusoid()'
        }


class HVAC_With_Calcs(HVAC):

    @Asset.Attribute()
    def Temperature_Rate_Of_Change(self, metadata):
        return {
            'Type': 'Signal',

            # This formula will give us a nice derivative in F/h
            'Formula': '$temp.lowPassFilter(150min, 3min, 333).derivative() * 3600 s/h',

            'Formula Parameters': {
                # We can reference the base class' Temperature attribute here as a dependency
                '$temp': self.Temperature(metadata),
            }
        }

    @Asset.Attribute()
    def Too_Hot(self, metadata):
        return {
            'Type': 'Condition',
            'Formula': '$temp.valueSearch(isGreaterThan($threshold))',
            'Formula Parameters': {
                '$temp': self.Temperature(metadata),

                # We can also reference other attributes in this derived class
                '$threshold': self.Hot_Threshold(metadata)
            }
        }

    @Asset.Attribute()
    def Hot_Threshold(self, metadata):
        return {
            'Type': 'Scalar',
            'Formula': '80F'
        }

    @Asset.Attribute()
    def Equipment_ID(self, metadata):
        return {
            'Type': 'Scalar',
            'Formula': '"%s"' % self.definition['Name']
        }

    # Returning an instance as a Component allows you to include a child asset with its own set of attributes
    @Asset.Component()
    def Compressor(self, metadata):
        return Compressor(parent=self)

    @Asset.Component()
    def Pump(self, metadata):
        return [
            {
                'Name': 'Pump Volume',
                'Type': 'Scalar',
                'Formula': '1000L'
            },
            {
                'Name': 'Pump Voltage',
                'Type': 'Scalar',
                'Formula': '110V'
            }
        ]

    @Asset.Component()
    def Airflow(self, metadata):
        return Airflow_Attributes(self)


def build_and_push_hvac_tree():
    hvac_metadata_df = get_hvac_metadata_df()
    build_df = spy.assets.build(HVAC_With_Calcs, hvac_metadata_df)
    spy.push(metadata=build_df, errors='catalog')


def get_hvac_metadata_df():
    hvac_metadata_df = spy.search({
        'Name': 'Area ?_*',
        'Datasource Class': 'Time Series CSV Files'
    })

    hvac_metadata_df['Build Asset'] = hvac_metadata_df['Name'].str.extract('(Area .)_.*')

    hvac_metadata_df['Build Path'] = 'My HVAC Units >> Facility #1'

    return hvac_metadata_df


@pytest.mark.system
def test_build():
    hvac_metadata_df = get_hvac_metadata_df()

    hvac_metadata_df['Build Template'] = 'HVAC'

    # It won't like the "Build Template" column since we're specifying the HVAC class directly
    with pytest.raises(ValueError):
        spy.assets.build(HVAC, hvac_metadata_df)

    hvac_metadata_df = hvac_metadata_df.drop(columns=['Build Template'])
    build_df = spy.assets.build(HVAC, hvac_metadata_df)

    # We'll get an error the first time because Area F doesn't have the signals we need
    with pytest.raises(RuntimeError):
        spy.push(metadata=build_df)

    # Now we'll catalog the errors instead of stopping on them
    spy.push(metadata=build_df, errors='catalog')

    hvac_with_calcs_metadata_df = hvac_metadata_df.copy()

    build_with_calcs_df = spy.assets.build(HVAC_With_Calcs, hvac_with_calcs_metadata_df)

    push_results_df = spy.push(metadata=build_with_calcs_df, errors='catalog')

    errors_df = push_results_df[push_results_df['Push Result'] != 'Success']

    # Should only be 4 errors (associated with Area F)
    assert len(errors_df) == 4

    search_results_df = spy.search({
        'Path': 'My HVAC Units >> Facility #1'
    })

    areas = [
        'Area A',
        'Area B',
        'Area C',
        'Area D',
        'Area E',
        'Area F',
        'Area G',
        'Area H',
        'Area I',
        'Area J',
        'Area K',
        'Area Z',
    ]

    for area in areas:
        assertions = [
            ('My HVAC Units >> Facility #1', area, 'Temperature', 'CalculatedSignal'),
            ('My HVAC Units >> Facility #1', area, 'Temperature Rate Of Change', 'CalculatedSignal'),
            ('My HVAC Units >> Facility #1', area, 'Relative Humidity', 'CalculatedSignal'),
            ('My HVAC Units >> Facility #1', area, 'Too Hot', 'CalculatedCondition'),
            ('My HVAC Units >> Facility #1', area, 'Hot Threshold', 'CalculatedScalar'),
            ('My HVAC Units >> Facility #1', area, 'Pump Voltage', 'CalculatedScalar'),
            ('My HVAC Units >> Facility #1', area, 'Pump Volume', 'CalculatedScalar'),
            ('My HVAC Units >> Facility #1 >> ' + area, 'Compressor', 'Power', 'CalculatedSignal'),
            ('My HVAC Units >> Facility #1', area, 'Airflow Rate', 'CalculatedSignal'),
        ]

        # Area F is special!
        if area == 'Area F':
            assertions = [
                ('My HVAC Units >> Facility #1', area, 'Hot Threshold', 'CalculatedScalar'),
                ('My HVAC Units >> Facility #1', area, 'Pump Voltage', 'CalculatedScalar'),
                ('My HVAC Units >> Facility #1', area, 'Pump Volume', 'CalculatedScalar'),
                ('My HVAC Units >> Facility #1 >> ' + area, 'Compressor', 'Power', 'CalculatedSignal'),
            ]

        assert_instantiations(search_results_df, assertions)


def assert_instantiations(search_results_df, assertions):
    for _path, _asset, _name, _type in assertions:
        assertion_df = search_results_df[
            (search_results_df['Path'] == _path) &
            (search_results_df['Asset'] == _asset) &
            (search_results_df['Name'] == _name) &
            (search_results_df['Type'] == _type)]

        assert len(assertion_df) == 1, \
            'Instantiated item not found: %s, %s, %s, %s' % (_path, _asset, _name, _type)


@pytest.mark.system
def test_build_with_module():
    hvac_metadata_df = spy.search({
        'Name': 'Area ?_*',
        'Datasource Class': 'Time Series CSV Files'
    })

    hvac_metadata_df['Build Path'] = 'My HVAC Units >> Facility #2'

    def _template_chooser(name):
        if 'Compressor' in name:
            return 'Compressor'
        else:
            return 'HVAC'

    hvac_metadata_df['Build Template'] = hvac_metadata_df['Name'].apply(_template_chooser)

    hvac_metadata_df['Area'] = hvac_metadata_df['Name'].str.extract('(Area .)_.*')
    hvac_metadata_df['Build Asset'] = hvac_metadata_df['Area'] + ' ' + hvac_metadata_df['Build Template']

    build_df = spy.assets.build(sys.modules[__name__], hvac_metadata_df)

    spy.push(metadata=build_df)

    search_results_df = spy.search({
        'Path': 'My HVAC Units >> Facility #2'
    })

    # There should be a "Area X HVAC" and "Area X Compressor" signals
    assert len(search_results_df) == 57


@pytest.mark.system
def test_no_path():
    hvac_metadata_df = spy.search({
        'Name': 'Area A_*',
        'Datasource Class': 'Time Series CSV Files'
    })

    hvac_metadata_df['Build Asset'] = 'Asset Without Path'

    # Zero-length / blank Build Path will not be allowed
    hvac_metadata_df['Build Path'] = ''
    build_df = spy.assets.build(HVAC, hvac_metadata_df)
    with pytest.raises(ValueError, match='Path contains blank / zero-length segments'):
        spy.push(metadata=build_df)

    # Both np.nan and None should result in the same thing-- the asset is the root of the tree

    hvac_metadata_df['Build Path'] = np.nan
    build_df = spy.assets.build(HVAC, hvac_metadata_df)
    assert len(build_df) == 3
    assert len(build_df.dropna(subset=['Path'])) == 0

    hvac_metadata_df['Build Path'] = None
    build_df = spy.assets.build(HVAC, hvac_metadata_df)
    assert len(build_df) == 3
    assert len(build_df.dropna(subset=['Path'])) == 0

    spy.push(metadata=build_df)

    search_results_df = spy.search({
        'Path': 'Asset Without Path'
    })

    assert len(search_results_df) == 2
    assert len(search_results_df.dropna(subset=['Path'])) == 0
    assert len(search_results_df.drop_duplicates(subset=['Asset'])) == 1
    assert search_results_df.iloc[0]['Asset'] == 'Asset Without Path'


@pytest.mark.system
def test_components():
    class Processing_Plant(Asset):
        @Asset.Component()
        def Refrigerators(self, metadata):
            return self.build_components(Refrigerator, metadata, 'Refrigerator')

    class Refrigerator(Asset):
        @Asset.Attribute()
        def Temperature(self, metadata):
            return metadata[metadata['Name'].str.endswith('Temperature')]

        @Asset.Component()
        def Compressor(self, metadata):
            return self.build_components(Compressor, metadata, 'Compressor')

    metadata_df = spy.search({
        'Name': '/Area [A-E]_.*/',
        'Datasource Class': 'Time Series CSV Files'
    })

    metadata_df['Build Path'] = np.nan
    metadata_df['Build Asset'] = 'Processing Plant'

    metadata_df.at[metadata_df['Name'] == 'Area A_Temperature', 'Refrigerator'] = 'Refrigerator 1'
    metadata_df.at[metadata_df['Name'] == 'Area A_Compressor Power', 'Refrigerator'] = 'Refrigerator 1'
    metadata_df.at[metadata_df['Name'] == 'Area A_Compressor Power', 'Compressor'] = 'Compressor 1'
    metadata_df.at[metadata_df['Name'] == 'Area B_Compressor Power', 'Refrigerator'] = 'Refrigerator 1'
    metadata_df.at[metadata_df['Name'] == 'Area B_Compressor Power', 'Compressor'] = 'Compressor 2'

    metadata_df.at[metadata_df['Name'] == 'Area C_Temperature', 'Refrigerator'] = 'Refrigerator 2'
    metadata_df.at[metadata_df['Name'] == 'Area C_Compressor Power', 'Refrigerator'] = 'Refrigerator 2'
    metadata_df.at[metadata_df['Name'] == 'Area C_Compressor Power', 'Compressor'] = 'Compressor 3'
    metadata_df.at[metadata_df['Name'] == 'Area D_Compressor Power', 'Refrigerator'] = 'Refrigerator 2'
    metadata_df.at[metadata_df['Name'] == 'Area D_Compressor Power', 'Compressor'] = 'Compressor 4'

    metadata_df.at[metadata_df['Name'] == 'Area E_Temperature', 'Refrigerator'] = 'Refrigerator 3'

    build_df = spy.assets.build(Processing_Plant, metadata_df)

    spy.push(metadata=build_df)

    search_results_df = spy.search({
        'Path': 'Processing Plant'
    })

    assert_instantiations(search_results_df, [
        ('Processing Plant', 'Refrigerator 1', 'Temperature', 'CalculatedSignal'),
        ('Processing Plant >> Refrigerator 1', 'Compressor 1', 'Power', 'CalculatedSignal'),
        ('Processing Plant >> Refrigerator 1', 'Compressor 2', 'Power', 'CalculatedSignal'),
        ('Processing Plant', 'Refrigerator 2', 'Temperature', 'CalculatedSignal'),
        ('Processing Plant >> Refrigerator 2', 'Compressor 3', 'Power', 'CalculatedSignal'),
        ('Processing Plant >> Refrigerator 2', 'Compressor 4', 'Power', 'CalculatedSignal'),
        ('Processing Plant', 'Refrigerator 3', 'Temperature', 'CalculatedSignal')
    ])


@pytest.mark.system
def test_metrics():
    class HVAC_With_Metrics(HVAC):
        @Asset.Attribute()
        def Too_Humid(self, metadata):
            return {
                'Type': 'Condition',
                'Name': 'Too Humid',
                'Formula': '$relhumid.valueSearch(isGreaterThan(70%))',
                'Formula Parameters': {
                    '$relhumid': self.Relative_Humidity(metadata),
                }
            }

        @Asset.Attribute()
        def Humidity_Upper_Bound(self, metadata):
            return {
                'Type': 'Signal',
                'Name': 'Humidity Upper Bound',
                'Formula': '$relhumid + 10',
                'Formula Parameters': {
                    '$relhumid': self.Relative_Humidity(metadata),
                }
            }

        @Asset.Attribute()
        def Humidity_Lower_Bound(self, metadata):
            return {
                'Type': 'Signal',
                'Name': 'Humidity Lower Bound',
                'Formula': '$relhumid - 10',
                'Formula Parameters': {
                    '$relhumid': self.Relative_Humidity(metadata),
                }
            }

        @Asset.Attribute()
        def Humidity_Statistic_KPI(self, metadata):
            return {
                'Type': 'Metric',
                'Measured Item': self.Relative_Humidity(metadata),
                'Statistic': 'Range'
            }

        @Asset.Attribute()
        def Humidity_Simple_KPI(self, metadata):
            return {
                'Type': 'Metric',
                'Measured Item': self.Relative_Humidity(metadata),
                'Thresholds': {
                    'HiHi': self.Humidity_Upper_Bound(metadata),
                    'LoLo': self.Humidity_Lower_Bound(metadata)
                }
            }

        @Asset.Attribute()
        def Humidity_Condition_KPI(self, metadata):
            return {
                'Type': 'Metric',
                'Measured Item': self.Relative_Humidity(metadata),
                'Statistic': 'Maximum',
                'Bounding Condition': self.Too_Humid(metadata),
                'Bounding Condition Maximum Duration': '30h'
            }

        @Asset.Attribute()
        def Humidity_Continuous_KPI(self, metadata):
            return {
                'Type': 'Metric',
                'Measured Item': self.Relative_Humidity(metadata),
                'Statistic': 'Minimum',
                'Duration': '6h',
                'Period': '4h',
                'Thresholds': {
                    'HiHiHi': 60,
                    'HiHi': 40,
                    'LoLo': 20
                }
            }

    hvac_metadata_df = spy.search({
        'Name': 'Area A_*',
        'Datasource Class': 'Time Series CSV Files'
    })

    hvac_metadata_df['Build Asset'] = 'Metrics Area A'
    hvac_metadata_df['Build Path'] = 'test_metrics'
    build_df = spy.assets.build(HVAC_With_Metrics, hvac_metadata_df)

    push_df = spy.push(metadata=build_df)

    assert (push_df['Push Result'] == 'Success').all()

    search_df = spy.search({
        'Path': 'test_metrics'
    })

    relative_humidity_id = search_df[search_df['Name'] == 'Relative Humidity'].iloc[0]['ID']

    metrics_api = MetricsApi(test_common.get_client())

    metric_id = search_df[search_df['Name'] == 'Humidity Statistic KPI'].iloc[0]['ID']
    metric_output = metrics_api.get_metric(id=metric_id)  # type: ThresholdMetricOutputV1
    assert metric_output.measured_item.id == relative_humidity_id
    assert metric_output.aggregation_function == 'range()'
    assert len(metric_output.thresholds) == 0

    metric_id = search_df[search_df['Name'] == 'Humidity Simple KPI'].iloc[0]['ID']
    metric_output = metrics_api.get_metric(id=metric_id)  # type: ThresholdMetricOutputV1
    assert metric_output.measured_item.id == relative_humidity_id
    assert not metric_output.aggregation_function
    assert len(metric_output.thresholds) == 2
    assert metric_output.thresholds[0].priority.name == 'HiHi'
    assert metric_output.thresholds[0].item.id == search_df[search_df['Name'] == 'Humidity Upper Bound'].iloc[0]['ID']
    assert metric_output.thresholds[1].priority.name == 'LoLo'
    assert metric_output.thresholds[1].item.id == search_df[search_df['Name'] == 'Humidity Lower Bound'].iloc[0]['ID']

    metric_id = search_df[search_df['Name'] == 'Humidity Condition KPI'].iloc[0]['ID']
    metric_output = metrics_api.get_metric(id=metric_id)  # type: ThresholdMetricOutputV1
    assert metric_output.measured_item.id == relative_humidity_id
    assert metric_output.aggregation_function == 'maxValue()'
    assert len(metric_output.thresholds) == 0
    assert metric_output.bounding_condition.id == search_df[search_df['Name'] == 'Too Humid'].iloc[0]['ID']
    assert metric_output.bounding_condition_maximum_duration.value == 30
    assert metric_output.bounding_condition_maximum_duration.uom == 'h'

    metric_id = search_df[search_df['Name'] == 'Humidity Continuous KPI'].iloc[0]['ID']
    metric_output = metrics_api.get_metric(id=metric_id)  # type: ThresholdMetricOutputV1
    assert metric_output.measured_item.id == relative_humidity_id
    assert metric_output.aggregation_function == 'minValue()'
    assert len(metric_output.thresholds) == 3
    assert metric_output.duration.value == 6
    assert metric_output.duration.uom == 'h'
    assert metric_output.period.value == 4
    assert metric_output.period.uom == 'h'
    assert metric_output.thresholds[0].priority.name == 'HiHiHi'
    assert metric_output.thresholds[0].value.value == 60
    assert metric_output.thresholds[1].priority.name == 'HiHi'
    assert metric_output.thresholds[1].value.value == 40
    assert metric_output.thresholds[2].priority.name == 'LoLo'
    assert metric_output.thresholds[2].value.value == 20
