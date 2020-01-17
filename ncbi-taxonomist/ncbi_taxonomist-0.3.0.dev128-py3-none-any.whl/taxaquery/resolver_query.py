#-------------------------------------------------------------------------------
#  \author Jan P Buchmann <jan.buchmann@sydney.edu.au>
#  \copyright 2019 The University of Sydney
#  \description
#-------------------------------------------------------------------------------

from typing import Type, Mapping, List, AbstractSet, Iterable


from ncbi_taxonomist import taxon
from ncbi_taxonomist.resolve import lineage_resolver


class ResolverQuery:

  def __init__(self, queries:Iterable):
    self.queries = set(queries)

  def resolve_taxon(self, qry_taxid:int, taxa:Mapping[int,Type[taxon.Taxon]]) -> List[Type[taxon.Taxon]]:
    return [x.get_attributes() for x in lineage_resolver.LineageResolver.resolve_lineage(qry_taxid, taxa)]

  def resolve(self, taxids:AbstractSet[int], taxa:Mapping[int,Type[taxon.Taxon]]):
    raise NotImplementedError
