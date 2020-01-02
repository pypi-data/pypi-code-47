import json
import math
import re
import string

from deprecated import deprecated

import pandas as pd

from .. import _common

from seeq.spy.workbooks import Analysis, AnalysisWorksheet


class DependenciesNotBuilt(Exception):
    def __init__(self, descriptors):
        self.descriptors = descriptors


class WorkbookNotBuilt(Exception):
    def __init__(self, workbook, worksheet):
        self.workbook = workbook
        self.worksheet = worksheet


def do_paths_match_criteria(criteria, names):
    return do_lists_match_criteria(re.split(r'\s*>>\s*', criteria), re.split(r'\s*>>\s*', names))


def do_lists_match_criteria(criteria, names):
    end = max(len(criteria), len(names))
    for i in range(0, end):
        if i > len(criteria) - 1:
            return False

        criterion = criteria[i]
        if criterion == '**':
            remaining_criteria = criteria[i + 1:]
            for j in range(i, len(names) + 1):
                remaining_names = names[j:]
                if do_lists_match_criteria(remaining_criteria, remaining_names):
                    return True

        if i > len(names) - 1:
            return False

        name = names[i]
        if not _common.does_query_fragment_match(criterion, name, contains=False):
            return False

    return True


class ItemGroup(list):
    def __init__(self, _list=None, relative_to=None):
        super().__init__(list(ItemGroup.flatten(_list) if _list else list()))
        self.relative_to = relative_to

    @staticmethod
    def flatten(l):
        for el in l:
            if isinstance(el, list):
                yield from ItemGroup.flatten(el)
            else:
                yield el

    def pick(self, criteria):
        picked = ItemGroup()

        for definition in self:
            good = True
            for prop, criterion in criteria.items():
                if prop not in definition:
                    good = False
                    break

                val = definition[prop]

                if prop == 'Path':
                    if not do_paths_match_criteria(criterion, val):
                        good = False
                        break
                elif not _common.does_query_fragment_match(criterion, val, contains=False):
                    good = False
                    break

            if good:
                picked.append(definition)

        return picked

    def as_parameters(self):
        parameters = dict()
        zero_padding = int(math.log10(len(self))) + 1 if len(self) > 0 else 1
        for i in range(len(self)):
            definition = self[i]
            string_spec = '$p{0:0%dd}' % zero_padding
            parameters[string_spec.format(i)] = definition

        return parameters

    def roll_up(self, statistic):
        _common.get_signal_statistic_function_map()
        parameters = self.as_parameters()
        types = {p['Type'] for p in parameters.values()}
        if len(types) == 0:
            return None

        if len(types) > 1:
            debug_string = '\n'.join([json.dumps(p, indent=2) for p in parameters.values()])
            raise RuntimeError('Cannot compute statistics across different types of items:\n%s' % debug_string)

        _type = types.pop()
        if 'Condition' in _type:
            fns = _common.get_condition_rollup_function_map()
        else:
            fns = _common.get_signal_rollup_function_map()

        if statistic.lower() not in fns:
            raise ValueError('Statistic "%s" not recognized. Valid statistics:\n%s' %
                             (statistic, '\n'.join([string.capwords(s) for s in fns.keys()])))

        fn = fns[statistic.lower()]

        if fn == 'union':
            formula = ' || '.join(parameters.keys())
        elif fn == 'intersect':
            formula = ' && '.join(parameters.keys())
        else:
            formula = '%s(%s)' % (fn, ', '.join(parameters.keys()))

        return {
            'Type': _type,
            'Formula': formula,
            'Formula Parameters': parameters
        }


class _AssetBase:
    DEFAULT_WORKBOOK_NEEDED = '__DEFAULT_WORKBOOK_NEEDED__'

    def __init__(self, definition=None, *, parent=None, workbooks=None):
        """
        Instantiates an Asset or Mixin.

        :param definition: A dictionary of property-value pairs that make up the definition of the Asset. Typically
        you will want to supply 'Name' at minimum.
        :type definition: dict, pd.DataFrame, pd.Series
        :param parent: An instance of either an Asset or Mixin that represents the parent of this instance. Typically
        this is supplied when @Asset.Component is used to define child assets.
        :type parent: Asset, Mixin
        """
        self.definition = dict()

        if isinstance(definition, _AssetBase):
            self.definition = definition.definition
        elif isinstance(definition, pd.DataFrame):
            if len(definition) != 1:
                raise ValueError('DataFrame must be exactly one row')
            self.definition = definition.iloc[0].to_dict()
        elif isinstance(definition, pd.Series):
            self.definition = definition.to_dict()
        elif definition is not None:
            self.definition = definition

        self.definition['Type'] = 'Asset'
        if 'Name' in self.definition:
            # For an Asset, its name and the Asset column are made identical for clarity
            self.definition['Asset'] = self.definition['Name']

        self.parent = parent  # type: _AssetBase
        self.workbooks = workbooks  # type: dict

        if self.parent is not None:
            # Passing in a parent will relieve the user from having to construct the right path
            if _common.present(self.parent.definition, 'Path'):
                self.definition['Path'] = self.parent.definition['Path'] + ' >> ' + self.parent.definition['Name']
            else:
                self.definition['Path'] = self.parent.definition['Name']

        self._build_cache = dict()

    @property
    @deprecated(reason="Use self.definition instead")
    def asset_definition(self):
        return self.definition

    @property
    @deprecated(reason="Use self.parent.definition instead")
    def parent_definition(self):
        return self.parent.definition if self.parent is not None else None

    def build(self, metadata):
        definitions = list()

        # Filter out deprecated members so that the Deprecated library doesn't produce warnings as we iterate over them
        method_names = [m for m in dir(self) if m not in ['asset_definition', 'parent_definition']]

        # Assemble a list of all functions on this object instance that are callable so that we can iterate over them
        # and find @Asset.Attribute() and @Asset.Component() functions
        object_methods = [getattr(self, method_name) for method_name in method_names
                          if callable(getattr(self, method_name))]

        # The "spy_model" attribute is added to any @Asset.Attribute() and @Asset.Component() decorated
        # functions so that they are processed during build
        remaining_methods = [func for func in object_methods if hasattr(func, 'spy_model')]

        while len(remaining_methods) > 0:
            at_least_one_built = False
            dependencies_not_built = list()
            workbooks_not_built = list()
            for func in remaining_methods.copy():
                try:
                    attribute = func(metadata)

                except DependenciesNotBuilt as e:
                    dependencies_not_built.extend(e.descriptors)
                    continue

                except WorkbookNotBuilt as e:
                    workbooks_not_built.append(e)
                    continue

                at_least_one_built = True
                remaining_methods.remove(func)

                if attribute is None:
                    continue

                if isinstance(attribute, list):
                    # This is the @Asset.Component case
                    definitions.extend(attribute)
                else:
                    # This is the @Asset.Attribute case
                    definitions.append(attribute)

            if not at_least_one_built:
                if len(workbooks_not_built) > 0:
                    for not_built in workbooks_not_built:
                        if not_built.workbook not in self.workbooks:
                            workbook = Analysis({'Name': not_built.workbook})
                            self.workbooks[not_built.workbook] = workbook
                        else:
                            workbook = self.workbooks[not_built.workbook]  # type: Analysis

                        if (not_built.workbook, not_built.worksheet) not in self.workbooks:
                            worksheet = workbook.get_worksheet(not_built.worksheet)
                            if worksheet is None:
                                worksheet = workbook.create_worksheet({'Name': not_built.worksheet})
                            self.workbooks[(not_built.workbook, not_built.worksheet)] = worksheet

                    at_least_one_built = True

            if not at_least_one_built:
                raise DependenciesNotBuilt(dependencies_not_built)

        return definitions

    def build_components(self, template, metadata, column_name):
        """
        Builds a set of components by identifying the unique values in the
        column specified by column_name and then instantiating the supplied
        template for each one and building it with the subset of metadata
        for that column value.

        Useful when constructing a rich model whereby a root asset is composed
        of unique components, possibly with further sub-components. For
        example, you may have a Plant asset that contains eight Refigerator
        units that each have two associated Compressor units.

        Parameters
        ----------
        template : {Asset, Mixin}
            A DataFrame or Series containing ID and Type columns that can be
            used to identify the items to pull. This is usually created via a
            call to spy.search().

        metadata : pd.DataFrame
            The metadata DataFrame containing all rows relevant to all
            (sub-)components of this asset. The DataFrame must contain the
            column specified by column_name.

        column_name : str
            The name of the column that will be used to discover the unique
            (sub-)components of this asset. For example, if column_name=
            'Compressor', then there might be values of 'Compressor A12' and
            'Compressor B74' in the 'Compressor' column of the metadata
            DataFrame.

        Returns
        -------
        list(dict)
            A list of definitions for each component.

        Examples
        --------
        Define a Refrigerator template that has Compressor subcomponents.

        >>> class Refrigerator(Asset):
        >>>     @Asset.Attribute()
        >>>     def Temperature(self, metadata):
        >>>         return metadata[metadata['Name'].str.endswith('Temperature')]
        >>>
        >>>     @Asset.Component()
        >>>     def Compressor(self, metadata):
        >>>         return self.build_components(Compressor, metadata, 'Compressor')
        >>>
        >>> class Compressor(Asset):
        >>>
        >>>     @Asset.Attribute()
        >>>     def Power(self, metadata):
        >>>         return metadata[metadata['Name'].str.endswith('Power')]
        """
        component_names = metadata[column_name].dropna().drop_duplicates().tolist()
        component_definitions = ItemGroup()
        for component_name in component_names:
            instance = template({
                'Name': component_name,
            }, parent=self, workbooks=self.workbooks)
            component_definition = instance.build(metadata[metadata[column_name] == component_name])
            component_definitions.extend(component_definition)
        return component_definitions

    def build_displays(self):
        pass


class Asset(_AssetBase):
    """
    A class derived from Asset can have @Asset.Attribute and @Asset.Component decorated functions that are executed
    as part of the call to build() which returns a list of definition dicts for the asset.
    """

    def __init__(self, definition=None, *, parent=None, workbooks=None):
        super().__init__(definition, parent=parent, workbooks=workbooks)

        # 'Template' is set on the asset with the hope that, in the future, we will be able to search for items in
        # the asset tree that are derived from a particular template.
        self.definition['Template'] = self.__class__.__name__.replace('_', ' ')

    def build(self, metadata):
        definitions = super().build(metadata)
        definitions.append(self.definition)
        self.definition['Build Result'] = 'Success'
        return definitions

    @staticmethod
    def _add_asset_metadata(asset, attribute_definition, error):
        if _common.present(asset.definition, 'Path') and not _common.present(attribute_definition, 'Path'):
            attribute_definition['Path'] = asset.definition['Path']

        if _common.present(asset.definition, 'Asset') and not _common.present(attribute_definition, 'Asset'):
            attribute_definition['Asset'] = asset.definition['Asset']

        if _common.present(asset.definition, 'Template') and not _common.present(attribute_definition, 'Template'):
            attribute_definition['Template'] = asset.__class__.__name__.replace('_', ' ')

        attribute_definition['Build Result'] = 'Success' if error is None else error

    # noinspection PyPep8Naming
    @classmethod
    def Attribute(cls):
        """
        This decorator appears as @Asset.Attribute on a function with a class that derives from Asset.
        """

        def attribute_decorator(func):
            def attribute_wrapper(self, metadata=None):
                # type: (Asset, pd.DataFrame) -> dict
                if func.__name__ in self._build_cache:
                    return self._build_cache[func.__name__]

                if metadata is None:
                    raise DependenciesNotBuilt(['"%s" attribute for class "%s" and instance %s' % (
                        func.__name__, self.__class__.__name__, json.dumps(self.definition, indent=2))])

                func_results = func(self, metadata)

                attribute_definition = dict()

                error = None

                if func_results is None:
                    error = 'None returned by Attribute function'

                def _preserve_originals():
                    for key in ['Name', 'Path']:
                        if _common.present(attribute_definition, key):
                            attribute_definition['Referenced ' + key] = attribute_definition[key]
                            del attribute_definition[key]

                if isinstance(func_results, pd.DataFrame):
                    if len(func_results) == 1:
                        attribute_definition.update(func_results.iloc[0].to_dict())
                        _preserve_originals()
                        attribute_definition['Reference'] = True
                    elif len(func_results) > 1:
                        error = 'Multiple attributes returned by "%s":\n%s' % (func.__name__, func_results)
                    else:
                        error = 'No matching metadata row found for "%s"' % func.__name__

                elif isinstance(func_results, dict):
                    attribute_definition.update(func_results)
                    if _common.present(func_results, 'ID'):
                        # If the user is supplying an identifier, they must intend it to be a reference, otherwise
                        # it can't be in the tree.
                        attribute_definition['Reference'] = True

                if not _common.present(attribute_definition, 'Name'):
                    attribute_definition['Name'] = func.__name__.replace('_', ' ')

                attribute_definition['Asset'] = self.definition['Name']

                Asset._add_asset_metadata(self, attribute_definition, error)

                self._build_cache[func.__name__] = attribute_definition

                return attribute_definition

            # Setting this attribute on the function itself makes it discoverable during build()
            setattr(attribute_wrapper, 'spy_model', 'attribute')

            return attribute_wrapper

        return attribute_decorator

    # noinspection PyPep8Naming
    @classmethod
    def Component(cls):
        """
        This decorator appears as @Asset.Component on a function with a class that derives from Asset.
        """

        def component_decorator(func):
            def component_wrapper(self, metadata=None):
                # type: (Asset, pd.DataFrame) -> ItemGroup
                if func.__name__ in self._build_cache:
                    return self._build_cache[func.__name__]

                if metadata is None:
                    raise DependenciesNotBuilt(['"%s" component for class "%s" and instance %s' % (
                        func.__name__, self.__class__.__name__, json.dumps(self.definition, indent=2))])

                func_results = func(self, metadata)

                component_definitions = ItemGroup(list(), self)
                if func_results is None:
                    return component_definitions

                if not isinstance(func_results, list):
                    func_results = [func_results]

                for func_result in func_results:
                    if isinstance(func_result, _AssetBase):
                        _asset_obj = func_result  # type: _AssetBase
                        if not _common.present(_asset_obj.definition, 'Name'):
                            _asset_obj.definition['Name'] = func.__name__.replace('_', ' ')
                        build_results = _asset_obj.build(metadata)
                        component_definitions.extend(build_results)
                    elif isinstance(func_result, dict):
                        component_definition = func_result  # type: dict
                        Asset._add_asset_metadata(self, component_definition, None)
                        component_definitions.append(component_definition)

                self._build_cache[func.__name__] = component_definitions

                return component_definitions

            # Setting this attribute on the function itself makes it discoverable during build()
            setattr(component_wrapper, 'spy_model', 'component')

            return component_wrapper

        return component_decorator

    # noinspection PyPep8Naming
    @classmethod
    def Display(cls, workbook=None, worksheet=None):
        """
        < NEED INFO >
        """

        def display_decorator(func):

            # noinspection PyUnusedLocal
            def display_wrapper(self, metadata):
                if func.__name__ in self._build_cache:
                    # We've already built this
                    return

                if (workbook, worksheet) not in self.workbooks:
                    raise WorkbookNotBuilt(workbook, worksheet)

                worksheet_object = self.workbooks[(workbook, worksheet)]  # type: AnalysisWorksheet

                workstep_object = worksheet_object.create_workstep({'Name': func.__name__})

                # noinspection PyBroadException
                try:
                    func(self, workstep_object)
                except BaseException:
                    worksheet_object.remove_workstep(workstep_object)
                    raise

                self.workbooks[(workbook, worksheet, func.__name__)] = workstep_object

                self._build_cache[func.__name__] = workstep_object

            # Setting this attribute on the function itself makes it discoverable during build()
            setattr(display_wrapper, 'spy_model', 'display')

            return display_wrapper

        return display_decorator


class Mixin(_AssetBase):
    """
    A Mixin is nearly identical to an Asset, but it adds attributes/components to an otherwise-defined Asset. The
    definition argument that is passed into the constructor should be the definition of the otherwise-defined Asset.

    This allows asset tree designers to add a set of "special" attributes to a particular instance of an asset
    without "polluting" the main asset definition with attributes that most of the instances shouldn't have.
    """

    def __init__(self, definition, *, workbooks=None):
        super().__init__(definition, workbooks=workbooks)

    def build(self, metadata):
        definitions = super().build(metadata)
        return definitions
