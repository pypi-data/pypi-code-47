#  -------------------------------------------------------------------------------
#  \author Jan P Buchmann <jan.buchmann@sydney.edu.au>
#  \copyright 2019 The University of Sydney
#  \description
#  -------------------------------------------------------------------------------


from typing import Set, Type, Iterable, Mapping


import ncbi_taxonomist.remote.query
import ncbi_taxonomist.db.sqlite_dbm
import ncbi_taxonomist.collect.remote_collector
import ncbi_taxonomist.taxaquery.name_collector_query
import ncbi_taxonomist.taxaquery.taxid_collector_query
from ncbi_taxonomist.convert import taxon_converter

class TaxaCollector:

  def __init__(self, email:str):
    self.email = email

  def collect_names(self, names:Iterable[str], converter:Type[taxon_converter.TaxonConverter]) -> Set[int]:
    ncq = ncbi_taxonomist.taxaquery.name_collector_query.NameCollectorQuery(names)
    rtq = ncbi_taxonomist.remote.query.RemoteTaxonomyQuery(self.email)
    rtq.query_names(names, ncbi_taxonomist.collect.remote_collector.RemoteCollector(ncq, converter))
    return ncq.queries

  def collect_taxids(self, taxids:Iterable[int], converter:Type[taxon_converter.TaxonConverter]) -> Set[int]:
    tcq = ncbi_taxonomist.taxaquery.taxid_collector_query.TaxidCollectorQuery(taxids)
    rtq = ncbi_taxonomist.remote.query.RemoteTaxonomyQuery(self.email)
    rtq.query_taxids(taxids, ncbi_taxonomist.collect.remote_collector.RemoteCollector(tcq, converter))
    return tcq.queries
