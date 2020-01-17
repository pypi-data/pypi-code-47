#-------------------------------------------------------------------------------
#  \author Jan P Buchmann <jan.buchmann@sydney.edu.au>
#  \copyright 2019 The University of Sydney
#  \description
#-------------------------------------------------------------------------------


from typing import Iterable, Type


import ncbi_taxonomist.utils
import ncbi_taxonomist.taxon
import ncbi_taxonomist.taxaquery.mapper_query


class TaxidMapperQuery(ncbi_taxonomist.taxaquery.mapper_query.MapperQuery):

  def __init__(self, queries:Iterable[int]):
    super().__init__(queries)

  def taxidIsQuery(self, taxon:Type[ncbi_taxonomist.taxon.Taxon]) -> bool:
    if taxon.taxon_id in self.queries:
      self.queries.remove(taxon.taxon_id)
      return True
    return False

  def map_query(self, taxon:Type[ncbi_taxonomist.taxon.Taxon]):
    if self.taxidIsQuery(taxon):
      ncbi_taxonomist.utils.json_stdout({taxon.taxon_id:taxon.get_attributes()})
