import re
import six

import pandas as pd
import numpy as np

from seeq.sdk import *
from seeq import spy

from . import _common
from . import _config
from . import _login
from . import _metadata

from ._common import Status


def push(data=None, *, metadata=None, workbook=_common.DEFAULT_WORKBOOK_PATH,
         worksheet=_common.DEFAULT_WORKSHEET_NAME, datasource=None, archive=False, type_mismatches='raise',
         errors='raise', quiet=False, status=None):
    """
    Imports metadata and/or data into Seeq Server, possibly scoped to a 
    workbook and/or datasource.

    The 'data' and 'metadata' arguments work together. Signal and condition 
    data cannot be mixed together in a single call to spy.push().

    Successive calls to 'push()' with the same 'metadata' but different 'data' 
    will update the items (rather than overwrite them); however, pushing a new 
    sample with the same timestamp as a previous one will overwrite the old 
    one.

    Metadata can be pushed without accompanying data. This is common after 
    having invoked the spy.assets.build() function. In such a case, the 
    'metadata' DataFrame can contain signals, conditions, scalars or assets.

    Parameters
    ----------
    data : pandas.DataFrame, optional
        A DataFrame that contains the signal or condition data to be pushed. 
        If 'metadata' is also supplied, it will have specific formatting 
        requirements depending on the type of data being pushed.

        For signals, 'data' must have a pandas.Timestamp-based index with a 
        column for each signal.

        For conditions, 'data' must have an integer index and two 
        pandas.Timestamp columns named 'Capsule Start' and 'Capsule End'.

    metadata : pandas.DataFrame, optional
        A DataFrame that contains the metadata for signals, conditions, 
        scalars, or assets. If 'metadata' is supplied, in conjunction with a 
        'data' DataFrame, it has specific requirements depending on the kind 
        of data supplied.

        For signals, the 'metadata' index (ie, rows) must have the same names 
        as the column names of the 'data' DataFrame.

        For conditions, the 'metadata' DataFrame must have only one row with 
        metadata for the condition.

        Metadata for each object type includes:

        Type Key: Si = Signal, Sc = Scalar, C = Condition, A = Asset

        ===================== ==================================== ============
        Metadata Term         Definition                           Types
        ===================== ==================================== ============
        Name                  Name of the signal                   Si, Sc, C, A
        Description           Description of the signal            Si, Sc, C, A
        Maximum Interpolation Maximum interpolation between        Si
                              samples
        Unit of Measure       Unit of measure of the values, or    Si, Sc, C
                              keys for conditions
        Formula               Formula for a calculated item        Si, Sc, C
        Formula Parameters    Parameters for a formula             Si, Sc, C
        Interpolation Method  Interpolation method between points  Si
                              Options are Linear, Step, PILinear
        Maximum Duration      Maximum expected duration for a      C
                              capsule
        Number Format         Formatting string ECMA-376           Si, Sc
        Path                  Asset tree path where the item's     Si, Sc, C, A
                              parent asset resides
        Asset                 Parent asset name. Parent asset      Si, Sc, C, A
                              must be in the tree at the
                              specified path, or listed in
                              'metadata' for creation.
        ===================== ==================================== ============

    workbook : {str, None}, default 'Data Lab >> Data Lab Analysis'
        The path to a workbook (in the form of 'Folder >> Path >> Workbook
        Name') or an ID that all pushed items will be 'scoped to'. Items scoped
        to a certain workbook will not be visible/searchable using the data
        panel in other workbooks. If None, items can also be 'globally scoped',
        meaning that they will be visible/searchable in all workbooks. Global
        scoping should be used judiciously to prevent search results becoming
        cluttered in all workbooks. The ID for a workbook is visible in the URL
        of Seeq Workbench, directly after the "workbook/" part.

    worksheet : str, default 'From Data Lab'
        The name of a worksheet within the workbook to create/update that will
        render the data that has been pushed so that you can see it in Seeq
        easily.

    datasource : dict, optional
        A dictionary defining the datasource within which to contain all the
        pushed items. By default, all pushed items will be contained in a "Seeq
        Data Lab" datasource. Do not create new datasources unless you really
        want to and you have permission from your administrator. The dictionary
        must have 'Datasource Class' and 'Datasource Name' keys.

    archive : bool, default False
        If 'True', archives any items in the datasource that previously existed
        but were not part of this push call. This can only be used if you also
        specify a 'datasource' argument.

    type_mismatches : {'raise', 'drop', 'invalid'}, default 'raise'
        If 'raise' (default), any mismatches between the type of the data and
        its metadata will cause an exception. For example, if string data is
        found in a numeric time series, an error will be raised. If 'drop' is
        specified, such data will be ignored while pushing. If 'invalid' is
        specified, such data will be replaced with an INVALID sample, which
        will interrupt interpolation in calculations and displays.


    errors : {'raise', 'catalog'}, default 'raise'
        If 'raise', any errors encountered will cause an exception. If
        'catalog', errors will be added to a 'Push Result' column in the
        passed-in 'items' DataFrame.

    quiet : bool, default False
        If True, suppresses progress output.

    status : spy.Status, optional
        If supplied, this Status object will be updated as the command
        progresses.

    Returns
    -------
    pandas.DataFrame
        A DataFrame with the metadata for the items pushed, along with any
        errors and statistics about the operation.

    """
    _common.validate_argument_types([
        (data, 'data', pd.DataFrame),
        (metadata, 'metadata', pd.DataFrame),
        (workbook, 'workbook', str),
        (worksheet, 'worksheet', str),
        (datasource, 'datasource', dict),
        (archive, 'archive', bool),
        (type_mismatches, 'type_mismatches', str),
        (errors, 'errors', str),
        (quiet, 'quiet', bool),
        (status, 'status', _common.Status)
    ])

    status = Status.validate(status, quiet)
    _common.validate_errors_arg(errors)

    signals_api = SignalsApi(_login.client)
    conditions_api = ConditionsApi(_login.client)
    datasources_api = DatasourcesApi(_login.client)

    if type_mismatches not in ['drop', 'raise', 'invalid']:
        raise RuntimeError("'type_mismatches' must be either 'drop', 'raise' or 'invalid'")

    if data is not None:
        if not isinstance(data, pd.DataFrame):
            raise RuntimeError("'data' must be a DataFrame")

    if metadata is not None:
        if not isinstance(metadata, pd.DataFrame):
            raise RuntimeError('"metadata" must be a DataFrame')

    if archive and datasource is None:
        raise RuntimeError('"datasource" must be supplied when "archive" is true')

    item_type = 'Signal'
    if data is not None:
        if 'Capsule Start' in data.columns or 'Capsule End' in data.columns:
            item_type = 'Condition'

    if datasource is not None:
        if not isinstance(datasource, dict):
            raise RuntimeError('"datasource" parameter must be dict')

        if 'Datasource Class' not in datasource:
            raise RuntimeError('"Datasource Class" required for datasource. This is the type of data being pushed. '
                               'For example, "WITSML"')

        if 'Datasource Name' not in datasource:
            raise RuntimeError('"Datasource Name" required for datasource. This is the specific data set being pushed. '
                               'For example, "Permian Basin Well Data"')

        datasource_input = DatasourceInputV1()
        _metadata.dict_to_datasource_input(datasource, datasource_input)

        if datasource_input.datasource_id is None:
            datasource_input.datasource_id = datasource_input.name
    else:
        datasource_input = _common.get_data_lab_datasource_input()

    datasource_output = datasources_api.create_datasource(body=datasource_input)  # type: DatasourceOutputV1

    primary_workbook = None
    workbook_id = None
    workbook_path = None
    if workbook is not None:
        if worksheet is None or not isinstance(worksheet, str):
            raise RuntimeError('When workbook is supplied, worksheet must also be supplied as a string')

        if _common.is_guid(workbook):
            primary_workbook = spy.workbooks.pull(pd.DataFrame([{
                'ID': _common.sanitize_guid(workbook),
                'Type': 'Workbook',
                'Workbook Type': 'Analysis'
            }]), include_inventory=False, status=status.create_inner(quiet=True))[0]
            workbook_path = primary_workbook.path
        else:
            search_query, workbook_name = create_analysis_search_query(workbook)
            search_df = spy.workbooks.search(search_query, quiet=True)
            workbook_path = _common.get(search_query, 'Path')
            if len(search_df) == 0:
                primary_workbook = spy.workbooks.Analysis({'Name': workbook_name})
                primary_workbook.worksheet(worksheet)
                spy.workbooks.push(primary_workbook, path=workbook_path, include_inventory=False,
                                   status=status.create_inner(quiet=True))
            else:
                primary_workbook = spy.workbooks.pull(search_df, include_inventory=False,
                                                      status=status.create_inner(quiet=True))[0]

        workbook_id = primary_workbook.id

    push_result_df = pd.DataFrame()
    if metadata is not None:
        push_result_df = _metadata.push(metadata, workbook_id, datasource_output, archive, errors, status)

    earliest_sample_in_ms = None
    latest_sample_in_ms = None

    if data is not None:
        def _put_item_defaults(d):
            if 'Datasource Class' not in d:
                d['Datasource Class'] = datasource_output.datasource_class

            if 'Datasource ID' not in d:
                d['Datasource ID'] = datasource_output.datasource_id

            if 'Type' not in d:
                d['Type'] = item_type

            d['Data ID'] = _metadata.get_scoped_data_id(d, workbook_id)

        status_columns = list()
        if 'ID' in push_result_df:
            status_columns.append('ID')
        if 'Path' in push_result_df:
            status_columns.append('Path')
        if 'Asset' in push_result_df:
            status_columns.append('Asset')
        if 'Name' in push_result_df:
            status_columns.append('Name')

        status.df = push_result_df[status_columns].copy()
        status.df['Count'] = 0
        status.df['Time'] = 0
        status.df['Result'] = 'Pushing'
        status_columns.extend(['Count', 'Time', 'Result'])

        push_result_df['Push Count'] = np.int64(0)
        push_result_df['Push Time'] = 0
        push_result_df['Push Result'] = ''

        def _update_push_data_status():
            status.update(
                'Pushing data to datasource <strong>%s [%s]</strong> scoped to workbook ID <strong>%s</strong>' % (
                    datasource_output.name, datasource_output.datasource_id, workbook_id),
                Status.RUNNING)

        _update_push_data_status()

        if item_type == 'Signal':
            for column in data:
                try:
                    index = column
                    if index in push_result_df.index:
                        signal_metadata = push_result_df.loc[index].to_dict()
                    else:
                        ad_hoc_status_df = pd.DataFrame({'Count': 0, 'Time': 0, 'Result': 'Pushing'}, index=[index])
                        status.df = status.df.append(ad_hoc_status_df, sort=True)
                        _update_push_data_status()
                        signal_metadata = dict()

                    if 'Name' not in signal_metadata:
                        if '>>' in column:
                            raise RuntimeError('Paths in column name not currently supported. Supply a metadata '
                                               'argument if you would like to put signal(s) directly in an asset tree.')

                        signal_metadata['Name'] = column

                    _put_item_defaults(signal_metadata)

                    earliest_sample_in_ms, latest_sample_in_ms, signal_id = _push_signal(column, signal_metadata, data,
                                                                                         earliest_sample_in_ms,
                                                                                         latest_sample_in_ms,
                                                                                         signals_api, type_mismatches,
                                                                                         index,
                                                                                         status,
                                                                                         _update_push_data_status)

                    if signal_id is None:
                        # This can happen if the column has only nan values. In that case, we don't know whether it's
                        # a string or numeric signal and we couldn't create the signal item.
                        # Check to see if it was created by push_metadata.
                        if 'ID' in signal_metadata:
                            signal_id = signal_metadata['ID']

                    push_result_df.at[column, 'Push Result'] = 'Success' if signal_id is not None else 'No Data'
                    push_result_df.at[column, 'Push Count'] = status.df.at[index, 'Count']
                    push_result_df.at[column, 'Push Time'] = status.df.at[index, 'Time']
                    push_result_df.at[column, 'ID'] = signal_id
                    push_result_df.at[column, 'Type'] = 'StoredSignal'
                    push_result_df.at[column, 'Name'] = signal_metadata['Name']

                except Exception as e:
                    if errors == 'raise':
                        raise

                    push_result_df.at[column, 'Push Result'] = e

        elif item_type == 'Condition':
            try:
                if metadata is None or len(metadata) != 1:
                    raise RuntimeError('Condition requires "metadata" input of DataFrame with single row')

                condition_metadata = metadata.iloc[0].to_dict()

                if 'Name' not in condition_metadata or 'Maximum Duration' not in condition_metadata:
                    raise RuntimeError('Condition metadata requires "Name" and "Maximum Duration" columns')

                if 'Capsule Start' not in data or 'Capsule End' not in data:
                    raise RuntimeError('Condition data requires "Capsule Start" and "Capsule End" columns')

                _put_item_defaults(condition_metadata)
                earliest_sample_in_ms, latest_sample_in_ms, condition_id = _push_condition(condition_metadata,
                                                                                           conditions_api, data,
                                                                                           earliest_sample_in_ms,
                                                                                           latest_sample_in_ms,
                                                                                           metadata.index[0], status,
                                                                                           _update_push_data_status)
                push_result_df.at[0, 'Push Result'] = 'Success'
                push_result_df.at[0, 'Push Count'] = status.df.at[0, 'Count']
                push_result_df.at[0, 'Push Time'] = status.df.at[0, 'Time']
                push_result_df.at[0, 'ID'] = condition_id
                push_result_df.at[0, 'Type'] = 'StoredCondition'

            except Exception as e:
                if errors == 'raise':
                    raise

                push_result_df.at[0, 'Push Result'] = str(e)

    workbooks_to_push = list()
    if metadata is not None:
        workbook_rows = metadata[metadata['Type'] == 'Workbook']
        for _, workbook_row in workbook_rows.iterrows():
            workbook_object = workbook_row['Object']  # type: spy.workbooks.Workbook
            if workbook_object.name is None:
                workbook_object.name = primary_workbook.name if primary_workbook else _common.DEFAULT_WORKBOOK_NAME
            if isinstance(workbook_object, spy.workbooks.Analysis) and \
               workbook_object.name == primary_workbook.name if primary_workbook else _common.DEFAULT_WORKBOOK_NAME:
                primary_workbook = workbook_object

            for worksheet_object in workbook_object.worksheets:
                if worksheet_object.name is None:
                    worksheet_object.name = worksheet if worksheet else _common.DEFAULT_WORKSHEET_NAME

            workbooks_to_push.append(workbook_object)

    if primary_workbook and len([w for w in workbooks_to_push if isinstance(w, spy.workbooks.Analysis)]) == 0:
        workbooks_to_push.append(primary_workbook)
        primary_worksheet = primary_workbook.worksheet(worksheet)
        _auto_populate_worksheet(earliest_sample_in_ms, latest_sample_in_ms, push_result_df, primary_worksheet)

    if metadata is not None and len(metadata) > 0 and 'Asset Object' in metadata.columns:
        for _, _row in metadata.iterrows():
            asset_object = _row['Asset Object']
            if not pd.isna(asset_object):
                asset_object.context.push_df = push_result_df

    workbook_push_df = _push_workbooks(push_result_df, workbook_path, workbooks_to_push, status)

    if primary_workbook:
        primary = workbook_push_df[workbook_push_df['ID'] == primary_workbook.id].iloc[0]
        scope_string = 'and scoped to workbook ID <strong>%s</strong><br>Click the following link to see what ' \
                       'you pushed in Seeq:<br><a href="%s" target="_new">%s</a>' % (primary['Pushed Workbook ID'],
                                                                                     primary['URL'],
                                                                                     primary['URL'])
    else:
        scope_string = 'and globally scoped.'

    status.update(
        'Pushed successfully to datasource <strong>%s [%s]</strong> %s' % (
            datasource_output.name, datasource_output.datasource_id, scope_string),
        Status.SUCCESS)

    return push_result_df


def _auto_populate_worksheet(earliest_sample_in_ms, latest_sample_in_ms, push_result_df, worksheet_object):
    display_items = push_result_df[push_result_df['Type'].isin(['StoredSignal', 'CalculatedSignal',
                                                                'StoredCondition', 'CalculatedCondition',
                                                                'CalculatedScalar', 'Chart',
                                                                'ThresholdMetric'])]
    worksheet_object.display_items = display_items.head(10)
    if earliest_sample_in_ms is not None and latest_sample_in_ms is not None:
        _range = {
            'Start': pd.Timestamp(int(earliest_sample_in_ms) * 1000000),
            'End': pd.Timestamp(int(latest_sample_in_ms) * 1000000)
        }
        worksheet_object.display_range = _range
        worksheet_object.investigate_range = _range


def create_analysis_search_query(workbook):
    workbook_spec_parts = re.split(r'\s+>>\s+', workbook)
    search_query = dict()
    if len(workbook_spec_parts) > 1:
        search_query['Path'] = ' >> '.join(workbook_spec_parts[0:-1])
        workbook_name = workbook_spec_parts[-1]
    else:
        workbook_name = workbook_spec_parts[0]
    search_query['Name'] = '/^%s$/' % workbook_name
    search_query['Workbook Type'] = 'Analysis'
    return search_query, workbook_name


def _push_signal(column, signal_metadata, data, earliest_sample_in_ms, latest_sample_in_ms, signals_api,
                 type_mismatches, status_index, status, update_status):
    signal_input = SignalInputV1()
    _metadata.dict_to_signal_input(signal_metadata, signal_input)
    put_samples_input = PutSamplesInputV1()
    put_samples_input.samples = list()
    count = 0
    is_string = None
    # noinspection PyTypeChecker
    signal_output = None
    timer = _common.timer_start()
    for index, row in data.iterrows():
        if pd.isna(row[column]):
            continue

        # noinspection PyUnresolvedReferences
        if not isinstance(index, pd.Timestamp):
            raise RuntimeError('data index must only be pd.Timestamp objects, but %s found instead' %
                               type(index))

        sample_value = row[column]

        if is_string is None:
            if 'Value Unit Of Measure' in signal_metadata:
                is_string = (signal_metadata['Value Unit Of Measure'] == 'string')
            else:
                is_string = isinstance(sample_value, six.string_types)

        if is_string != isinstance(sample_value, six.string_types):
            # noinspection PyBroadException
            try:
                if is_string:
                    sample_value = six.text_type(sample_value)
                else:
                    if data[column].dtype.name == 'int64':
                        sample_value = int(sample_value)
                    else:
                        sample_value = float(sample_value)
            except BaseException:
                # Couldn't convert it, fall through to the next conditional
                pass

        if is_string != isinstance(sample_value, six.string_types):
            if type_mismatches == 'drop':
                continue
            elif type_mismatches == 'raise':
                raise RuntimeError('Column "%s" was detected as %s, but %s value at (%s, %s) found. Supply '
                                   'type_mismatches parameter as "drop" to ignore the sample entirely or '
                                   '"invalid" to insert an INVALID sample in its place.' %
                                   (column, 'string-valued' if is_string else 'numeric-valued',
                                    'numeric' if is_string else 'string',
                                    index, sample_value))
            else:
                sample_value = None

        if isinstance(sample_value, np.number):
            sample_value = sample_value.item()

        if not signal_output:
            if is_string:
                signal_input.value_unit_of_measure = 'string'

            signal_output = signals_api.put_signal_by_data_id(datasource_class=signal_metadata['Datasource Class'],
                                                              datasource_id=signal_metadata['Datasource ID'],
                                                              data_id=signal_metadata['Data ID'],
                                                              body=signal_input)  # type: SignalOutputV1

        sample_input = SampleInputV1()
        key_in_ms = index.value / 1000000
        earliest_sample_in_ms = min(key_in_ms,
                                    earliest_sample_in_ms) if earliest_sample_in_ms is not None else key_in_ms
        latest_sample_in_ms = max(key_in_ms, latest_sample_in_ms) if latest_sample_in_ms is not None else key_in_ms

        sample_input.key = index.value
        sample_input.value = sample_value
        put_samples_input.samples.append(sample_input)

        if len(put_samples_input.samples) >= _config.options.push_page_size:
            signals_api.put_samples(id=signal_output.id,
                                    body=put_samples_input)
            count += len(put_samples_input.samples)
            status.df.at[status_index, 'Count'] = count
            status.df.at[status_index, 'Time'] = _common.timer_elapsed(timer)
            status.df.at[status_index, 'Result'] = 'Pushed to %s' % index
            update_status()

            put_samples_input.samples = list()

    if len(put_samples_input.samples) > 0:
        signals_api.put_samples(id=signal_output.id,
                                body=put_samples_input)
        count += len(put_samples_input.samples)

    status.df.at[status_index, 'Count'] = count
    status.df.at[status_index, 'Time'] = _common.timer_elapsed(timer)
    status.df.at[status_index, 'Result'] = 'Success'
    update_status()

    return earliest_sample_in_ms, latest_sample_in_ms, signal_output.id if signal_output is not None else None


def _push_condition(condition_metadata, conditions_api, data, earliest_sample_in_ms, latest_sample_in_ms, status_index,
                    status,
                    update_status):
    condition_batch_input = ConditionBatchInputV1()
    condition_input = ConditionInputV1()
    _metadata.dict_to_condition_input(condition_metadata, condition_input)
    condition_batch_input.conditions = [condition_input]
    condition_input.datasource_class = condition_metadata['Datasource Class']
    condition_input.datasource_id = condition_metadata['Datasource ID']
    items_batch_output = conditions_api.put_conditions(body=condition_batch_input)  # type: ItemBatchOutputV1
    item_update_output = items_batch_output.item_updates[0]  # type: ItemUpdateOutputV1
    capsules_input = CapsulesInputV1()
    capsules_input.capsules = list()
    capsules_input.key_unit_of_measure = 'ns'
    count = 0
    timer = _common.timer_start()
    for index, row in data.iterrows():
        capsule = CapsuleV1()
        _dict_to_capsule(row.to_dict(), capsule)
        capsule.start = row['Capsule Start'].value
        capsule.end = row['Capsule End'].value
        capsules_input.capsules.append(capsule)
        # noinspection PyTypeChecker
        key_in_ms = capsule.start / 1000000
        earliest_sample_in_ms = min(key_in_ms,
                                    earliest_sample_in_ms) if earliest_sample_in_ms is not None else key_in_ms
        # noinspection PyTypeChecker
        key_in_ms = capsule.end / 1000000
        latest_sample_in_ms = max(key_in_ms, latest_sample_in_ms) if latest_sample_in_ms is not None else key_in_ms

        if len(capsules_input.capsules) > _config.options.push_page_size:
            conditions_api.add_capsules(id=item_update_output.item.id, body=capsules_input)
            count += len(capsules_input.capsules)
            status.df.at[status_index, 'Count'] = count
            status.df.at[status_index, 'Time'] = _common.timer_elapsed(timer)
            status.df.at[status_index, 'Result'] = 'Pushed to %s' % index
            update_status()
            capsules_input.capsules = list()

    if len(capsules_input.capsules) > 0:
        conditions_api.add_capsules(id=item_update_output.item.id, body=capsules_input)
        count += len(capsules_input.capsules)

    status.df.at[status_index, 'Count'] = count
    status.df.at[status_index, 'Time'] = _common.timer_elapsed(timer)
    status.df.at[status_index, 'Result'] = 'Success'
    update_status()

    return earliest_sample_in_ms, latest_sample_in_ms, item_update_output.item.id


def _dict_to_capsule(d, capsule):
    _metadata.dict_to_input(d, capsule, 'properties', {
        'Capsule Start': None,
        'Capsule End': None
    })


def _push_workbooks(push_result_df, workbook_path, workbooks, status):
    for workbook in workbooks:  # type: spy.workbooks.Analysis
        if not isinstance(workbook, spy.workbooks.Analysis):
            continue

        for worksheet in workbook.worksheets:  # type: spy.workbooks.AnalysisWorksheet
            for workstep in worksheet.worksteps.values():  # type: spy.workbooks.AnalysisWorkstep
                display_items = workstep.display_items
                for index, display_item in display_items.iterrows():
                    if not _common.present(display_item, 'ID') or _common.get(display_item, 'Reference', False):
                        pushed_item = get_from_push_df(display_item, push_result_df)

                        display_items.at[index, 'ID'] = pushed_item['ID']

                workstep.display_items = display_items
                workstep.set_as_current()

    return spy.workbooks.push(workbooks, path=workbook_path, refresh=False, include_inventory=False,
                              status=status.create_inner())


def get_from_push_df(display_item, push_result_df):
    item_path = _common.get(display_item, 'Path')
    item_asset = _common.get(display_item, 'Asset')
    item_name = _common.get(display_item, 'Name')
    clause = (push_result_df['Asset'] == item_asset) & (push_result_df['Name'] == item_name)
    if item_path:
        clause &= (push_result_df['Path'] == item_path)
    pushed_item = push_result_df[clause]
    if len(pushed_item) == 0:
        raise RuntimeError('Could not find ID for workstep with display item where\n'
                           'Path = "%s"\nAsset = "%s"\nName = "%s"' %
                           (item_path, item_asset, item_name))
    if len(pushed_item) > 1:
        raise RuntimeError('Multiple IDs for workstep with display item where\n'
                           'Path = "%s"\nAsset = "%s"\nName = "%s"\n%s' %
                           (item_path, item_asset, item_name, pushed_item))
    return pushed_item.iloc[0]
