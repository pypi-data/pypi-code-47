#-------------------------------------------------------------------------------
#  \author Jan P Buchmann <jan.buchmann@sydney.edu.au>
#  \copyright 2019 The University of Sydney
#  \description
#-------------------------------------------------------------------------------


from typing import Iterable


import ncbi_taxonomist.utils
import ncbi_taxonomist.taxaquery.resolver_query


class TaxidResolverQuery(ncbi_taxonomist.taxaquery.resolver_query.ResolverQuery):

  def __init__(self, queries:Iterable[int]):
    super().__init__(queries)

  def get_taxid(self, taxid:[int]) -> int:
    if taxid in self.queries:
      self.queries.remove(taxid)
      return taxid
    return None

  def resolve(self, taxids, taxa):
    for i in taxids:
      if self.get_taxid(i):
        ncbi_taxonomist.utils.json_stdout({'taxid':i, 'lin':self.resolve_taxon(i, taxa)})
