#-------------------------------------------------------------------------------
#\author Jan P Buchmann <jan.buchmann@sydney.edu.au>
#\copyright 2019 The University of Sydney
#\description
#-------------------------------------------------------------------------------

import json
from typing import Type

import entrezpy.base.analyzer
import taxonompy.parser.xmlparser

from ncbi_taxonomist.remote import taxonomy_result
from ncbi_taxonomist.convert import taxon_converter
from ncbi_taxonomist.taxaquery import resolver_query

class RemoteResolver(entrezpy.base.analyzer.EutilsAnalyzer):

  taxa = {}

  def __init__(self, query:Type[resolver_query.ResolverQuery], converter:Type[taxon_converter.TaxonConverter]):
    super().__init__()
    self.query = query
    self.converter = converter
    self.taxonomy_parser = taxonompy.parser.xmlparser.NcbiTaxoXmlParser(RemoteResolver.taxa)

  def init_result(self, response, request:object) -> bool:
    if not self.result:
      self.result = taxonomy_result.NcbiTaxonomyResult(request)
      return True
    return False

  def analyze_error(self, response, request:object):
    print (json.dumps({__name__:{'Response-Error':{
                                   'request-dump' : request.dump_internals(),
                                   'error' : response.getvalue()}}}))

  def analyze_result(self, response, request:object):
    self.init_result(request, request)
    results = self.taxonomy_parser.parse(response)
    self.result.add_queries(results.queries)
    for i in results.taxa:
      self.result.add_taxon(self.converter.convert_to_model(results.taxa[i].attribute_dict()))
    self.query.resolve(results.queries, self.result.taxa)
