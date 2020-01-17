#-------------------------------------------------------------------------------
#  \author Jan P Buchmann <jan.buchmann@sydney.edu.au>
#  \copyright 2019 The University of Sydney
#  \description
#-------------------------------------------------------------------------------


from typing import Iterable, Type


import ncbi_taxonomist.taxon
import ncbi_taxonomist.utils
import ncbi_taxonomist.taxaquery.mapper_query


class NameMapperQuery(ncbi_taxonomist.taxaquery.mapper_query.MapperQuery):

  def __init__(self, queries:Iterable[str]):
    super().__init__(queries)

  def query_name(self, taxon:Type[ncbi_taxonomist.taxon.Taxon]) -> str:
    for i in taxon.get_names():
      if i in self.queries:
        self.queries.remove(i)
        return i
    return None


  def map_query(self, taxon:Type[ncbi_taxonomist.taxon.Taxon]):
    name = self.query_name(taxon)
    if name:
      ncbi_taxonomist.utils.json_stdout({'name':name, 'taxon':taxon.get_attributes()})
