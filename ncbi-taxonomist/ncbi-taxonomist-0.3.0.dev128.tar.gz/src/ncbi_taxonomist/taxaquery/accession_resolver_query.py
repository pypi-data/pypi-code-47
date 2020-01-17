#-------------------------------------------------------------------------------
#  \author Jan P Buchmann <jan.buchmann@sydney.edu.au>
#  \copyright 2019 The University of Sydney
#  \description
#-------------------------------------------------------------------------------


from typing import Type, Mapping, AbstractSet, Iterable

import ncbi_taxonomist.utils
from ncbi_taxonomist import taxon
from ncbi_taxonomist.resolve import lineage_resolver


class AccessionResolverQuery:

  @staticmethod
  def resolve_taxon(qry_taxid:int, taxa:Mapping[int,Type[taxon.Taxon]]) -> Iterable[Type[taxon.Taxon]]:
    return [x.get_attributes() for x in lineage_resolver.LineageResolver.resolve_lineage(qry_taxid, taxa)]

  def __init__(self, queries:Mapping[int, Iterable[str]]):
    self.queries = queries

  def resolve(self, taxids:AbstractSet[int], taxa:Mapping[int,Type[taxon.Taxon]]):
    for i in taxids:
      if i in self.queries:
        lin = AccessionResolverQuery.resolve_taxon(i, taxa)
        for j in self.queries.pop(i):
          ncbi_taxonomist.utils.json_stdout({'accs':j, 'lin':lin})
