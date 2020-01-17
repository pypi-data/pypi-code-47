#-------------------------------------------------------------------------------
#  \author Jan P Buchmann <jan.buchmann@sydney.edu.au>
#  \copyright 2019 The University of Sydney
#  \description
#-------------------------------------------------------------------------------


from typing import Iterable, Type


import ncbi_taxonomist.taxon
import ncbi_taxonomist.utils
import ncbi_taxonomist.taxaquery.resolver_query


class NameResolverQuery(ncbi_taxonomist.taxaquery.resolver_query.ResolverQuery):

  def __init__(self, queries:Iterable[str]):
    super().__init__(queries)

  def get_name(self, taxon:Type[ncbi_taxonomist.taxon.Taxon]) -> str:
    for i in taxon.get_names():
      if i in self.queries:
        self.queries.remove(i)
        return i
    return None

  def resolve(self, taxids:Iterable[int], taxa:Iterable[Type[ncbi_taxonomist.taxon.Taxon]]):
    for i in taxids:
      name = self.get_name(taxa[i])
      if name:
        ncbi_taxonomist.utils.json_stdout({'name':name,'lin':self.resolve_taxon(i, taxa)})
