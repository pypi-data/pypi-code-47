#-------------------------------------------------------------------------------
#  \author Jan P Buchmann <jan.buchmann@sydney.edu.au>
#  \copyright 2019 The University of Sydney
#  \description
#-------------------------------------------------------------------------------


import json
from typing import Iterable, Type


import ncbi_taxonomist.taxaquery.collector_query
import ncbi_taxonomist.taxon

class NameCollectorQuery(ncbi_taxonomist.taxaquery.collector_query.CollectorQuery):

  def __init__(self, queries:Iterable[str]):
    super().__init__(queries)

  def update_queries(self, taxon:Type[ncbi_taxonomist.taxon.Taxon]):
    for i in taxon.get_names():
      if i in self.queries:
        self.queries.remove(i)

  def collect(self, taxon):
    print(json.dumps(taxon.get_attributes()))
    self.update_queries(taxon)
