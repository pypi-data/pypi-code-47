#-------------------------------------------------------------------------------
#  \author Jan P Buchmann <jan.buchmann@sydney.edu.au>
#  \copyright 2019 The University of Sydney
#  \description
#-------------------------------------------------------------------------------

from typing import Type, Mapping, AbstractSet, Iterable


import ncbi_taxonomist.taxon


class CollectorQuery:

  def __init__(self, queries:Iterable):
    self.queries = set(queries)

  def collect(self, taxids:AbstractSet[int], taxa:Mapping[int,Type[ncbi_taxonomist.taxon.Taxon]]):
    raise NotImplementedError
