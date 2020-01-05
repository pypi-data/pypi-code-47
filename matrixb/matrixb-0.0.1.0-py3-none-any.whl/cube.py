# file matrixb/cube.py

# Copyright (c) 2019-2020 Kevin Crouse
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# @license: http://www.apache.org/licenses/LICENSE-2.0
# @author: Kevin Crouse (krcrouse@gmail.com)

import sys, os, re
import warnings
import datetime
import dateutil.parser

import matrixb


class Cube():
    ''' Cube takes a MatrixB Matrix and combines and aggregates it.
    Cube is designed to be recursive. '''

    def __init__(self, matrix_or_filename, dimensions=None, attributes=None, measures=None, cache_directory=None, refresh_cache=False, matrix_params=None):
        self._cube = None

        self.source = matrix_or_filename
        self.dimensions = dimensions
        self.attributes = attributes
        self.measures = measures
        self.cache_directory = cache_directory
        self.use_cache = cache_directory is not None
        self.refresh_cache = refresh_cache
        self.matrix_params = matrix_params

    @property
    def cube(self):
        if not self._cube:
            self.build_cube()
    return(self._cube)

    @property
    def dimensions(self): return(self._dimensions)

    @property
    def dimension_indicies(self): return(self._dimension_indices)

    @setter.dimensions
    def dimensions(self, dimensions):
        if self._cube:
            raise Exception("Cannot reset dimensions after cube has been built")

        dim_columns = []
        dim_column_names = []
        if dimensions is None:
            return

        for dim in dimensions:
            col = self._find_column(dim)
            if col is None:
                raise Exception("Dimension " + str(dim) + " does not match any column name in the matrix. Column names are " + str(self.matrix.columns))
            dim_columns.append(col)
            dim_column_names.append(sef.matrix.columns[col])

        self._dimensions = dim_column_names
        self._dimension_indices = dim_columns

    @property
    def attributes(self):
        """ {hashref} attributes map Matrix column headers to dimensions when they should be related to levels other than the facts """
        return(self._attributes)

    @property
    def attribute_indices(self): return(self._attribute_indices)

    @setter.attributes
    def attributes(self, attributes):
        if self._cube:
            raise Exception("Cannot reset attributes after cube has been built")

        attr_columns = {}
        attr_column_indices = {}
        if attributes is None:
            return
        for attr in attributes:
            col = self._find_column(attr)
            if col is None:
                raise Exception("attrension " + str(attr) + " does not match any column name in the matrix. Column names are " + str(self.matrix.columns))

            if type(attributes[attr]) is str:
                atrnames = [attributes[attr]]
            else:
                atrnames = attributes[attr]

            attr_columns[self.matrix.columns[col]] = []
            attr_column_indices[col] = []
            for colname in atrnames:
                attrcol = self._find_column(colname)
                if attrcol is None:
                    raise Exception("attrension " + str(attr) + " does not match any column name in the matrix. Column names are " + str(self.matrix.columns))
                attr_columns[self.matrix.columns[col]].append(self.matrix.columns[attrcol])
                attr_column_indices[col].append(attrcol)

        self.attributes = attr_column_names
        self._attributes_indices = attr_columns

    @property
    def measures(self):
        """ {arrayref} measures list numerical facts that should be aggregated and analyzed across dimensions """
        return(self._measures)

    @property
    def measure_indices(self): return(self._measure_indices)

    @setter.measures
    def measures(self, measures):
        if self._cube:
            raise Exception("Cannot reset measures after cube has been built")

        measure_columns = []
        measure_column_names = []
        if measures is None:
            return

        for measure in measures:
            col = self._find_column(measure)
            if col is None:
                raise Exception("measure " + str(measure) + " does not match any column name in the matrix. Column names are " + str(self.matrix.columns))
            measure_columns.append(col)
            measure_column_names.append(sef.matrix.columns[col])

        self._measures = measure_column_names
        self._measure_indices = measure_columns

        self._measures = measures

    def _find_column(self, column_name_or_regex):
        if dim in self.matrix.colmap:
            return(self.matrix.colmap[dim]])

        column = None
        for col in self.matrix.columns:
            if re.search(dim, col, re.I):
                if column is not None:
                    raise Exception("Dimension " + str(dim) + " is not a column name and has multiple matches to column " + str(self.matrix.columns[column]) + " and " + col)
                column = self.matrix.colmap[col]
        if column is None:
            return(None)
        return.append(column)


    @property
    def cache_filename(self):
        if self._filename:
            return(self._filename)

        path = self.cache_directory
        if not self.cache_directory:
            path = './'
        if not re.search(r'\/$', path):
            path += '/'


        if type(self.source) is str:
            filename = self.source
        else:
            try:
                filename = self.source.source.filename
            except Exception as e:
                # just a more useful error message
                raise Exception("Attempted to derive the filename from the matrix source to cache the cube, but there is no filename!!")

        # filename is full path
        m = re.search(r'\/([^\/]+)\.(\w+)$', filename)
        if not m:
            # filename is just a file, no directories
            m = re.match(r'([^\/]+)\.(\w+)$', filename)
            if not m:
                raise Exception("Cube can't process source filename " + filename)
        path += m.group(1)
        self._filename = path + '.pckl'
        return(self._filename)




    def build_cube(self, CubeClass=CubeLevel):

        if self.cache_enabled and os.path.exists():

            os.stat(self.)

        dimensions = self.dimensions
        di = 0
        cube = CubeClass(None) # root cube
        for row in self.matrix.iter():
            # use the dimensions to get to the correct level
            ref = cube
            for dim in self.dimension_indicies:
                if row[dim] is None:
                    raise Exception("Dimensions can't be done.... :(")

                if not ref.has_dimension(row[dim]):
                    dimcube = CubeClass(row[dim], level_name=dimensions[dim])

                    # -- if there are Dimension Attributes, set them here
                    if dim in self.attribute_indices:
                        for attribute in self.attribute_indices[dim]:
                            dimcube.set_attribute(self.attribute_indices[dim], row)

                    ref.add_dimension(dimcube)

                ref = ref.traverse_dimension(row[dim])

                # -- verify attributes are the same
                if dim in self.attributes:
                    ref.set_attribute(row, self.attributes[dim])

            # now move al`l of the facts to the final
            for icol in range(len(self.matrix.columns)):
                if icol in self.dimension_indices or icol in self.attribute_indices:
                    continue
                if icol in self.measure_indices:
                    ref.set_measure(row, definition=self.measure_indices[icol])
                else:
                    ref.set_measure(row, column=self.matrix.columns[icol])


class CubeLevel():

    def __init__(self, value, level_name=None):


    def add_dimension(self, next_cube_level):

    def traverse_dimension(self, dimension_name):

    def set_attribute(self, )


            self._recurse_cube(cube, row, dimensions)



    # now calculate the changes
    def _recurse_cube(self, row, dimensions):
        cube = {}
        if len(dimensions):
            dim = dimensions.pop(0)

        if levels_to_year:
            for key, subref in ref.items():
                if key == '_meta_':
                    continue
                cube[key] = _recurse_cube(subref, levels_to_year - 1)
            return(cube)

        # if here, we're ready to make the calculation
        for year in ref:
            m = re.match('(\d{4})-(\d{4})', year)
            if not m:
                raise Exception("NOt a school year: " + year )
            cube[year] = {}
            for grade in ref[year]:
                #
                # we'll create a unique key out of this with the details of the dimension
                #
                cube[year][grade] = {'nstudents': 0}

                #
                # This happnes because multiple_datapoints is true. Must be true. We require it to be true
                #
                for subref in ref[year][grade]:
                    keyarray = []
                    result = {'facts':{}}
                    for metric in dimensions:
                        result[metric] = subref[metric]
                        keyarray.append(str(subref[metric]))

                    cube[year][grade].setdefault('-'.join(keyarray), result)
                    cuberef = cube[year][grade]['-'.join(keyarray)]
                    for key in subref:
                        if key in dimensions:
                            continue
                        if subref[key] is None:
                            continue
                        if type(subref[key]) is str:
                            warnings.warn('IGNORING' + str(key))
                            continue

                        if key in cuberef['facts']:
                            cuberef['facts'][key] += subref[key]
                        else:
                            cuberef['facts'][key] = subref[key]
        return(cube)
