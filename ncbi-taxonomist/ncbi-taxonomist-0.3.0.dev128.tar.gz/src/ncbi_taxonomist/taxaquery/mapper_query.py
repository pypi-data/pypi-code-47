#-------------------------------------------------------------------------------
#  \author Jan P Buchmann <jan.buchmann@sydney.edu.au>
#  \copyright 2019 The University of Sydney
#  \description
#-------------------------------------------------------------------------------

from typing import Type, Iterable


import ncbi_taxonomist.taxon


class MapperQuery:

  def __init__(self, queries:Iterable):
    self.queries = set(queries)

  def map_query(self, taxon:Type[ncbi_taxonomist.taxon.Taxon]):
    raise NotImplementedError
