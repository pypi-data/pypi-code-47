#-------------------------------------------------------------------------------
#  \author Jan P Buchmann <jan.buchmann@sydney.edu.au>
#  \copyright 2019 The University of Sydney
#  \description
#-------------------------------------------------------------------------------


import json
from typing import Iterable


import ncbi_taxonomist.taxaquery.collector_query


class TaxidCollectorQuery(ncbi_taxonomist.taxaquery.collector_query.CollectorQuery):

  def __init__(self, queries:Iterable[int]):
    super().__init__(queries)

  def collect(self, taxon):
    self.queries.discard(taxon.taxon_id)
    print(json.dumps(taxon.get_attributes()))
