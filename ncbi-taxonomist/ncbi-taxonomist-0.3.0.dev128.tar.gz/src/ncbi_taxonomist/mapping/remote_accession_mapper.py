#-------------------------------------------------------------------------------
#\author Jan P Buchmann <jan.buchmann@sydney.edu.au>
#\copyright 2019 The University of Sydney
#\description
#-------------------------------------------------------------------------------

import json
from typing import Type


import entrezpy.base.analyzer

import ncbi_taxonomist.taxaquery.resolver_query
import ncbi_taxonomist.remote.accession_result

class RemoteAccessionMapper(entrezpy.base.analyzer.EutilsAnalyzer):

  def __init__(self, query:Type[ncbi_taxonomist.taxaquery.resolver_query.ResolverQuery]):
    super().__init__()
    self.query = query

  def init_result(self, response:dict, request:object) -> bool:
    if not self.result:
      self.result = ncbi_taxonomist.remote.accession_result.NcbiAccessionResult(request)
      return True
    return False

  def analyze_error(self, response:dict, request:object):
    print (json.dumps({__name__:{'Response-Error':{
                                   'request-dump' : request.dump_internals(),
                                   'error' : response}}}))

  def analyze_result(self, response:dict, request:object):
    self.init_result(request, request)
    for i in response['result'].pop('uids', None):
      accs = self.query.map_accession(response['result'].pop(i), request.db)
      if accs:
        self.result.add_accessions(accs)
