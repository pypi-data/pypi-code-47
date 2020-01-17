#  -------------------------------------------------------------------------------
#  \author Jan P Buchmann <jan.buchmann@sydney.edu.au>
#  \copyright 2019 The University of Sydney
#  \description
#  -------------------------------------------------------------------------------


from typing import Set, Type, Iterable, Mapping


from ncbi_taxonomist.db import sqlite_dbm
from ncbi_taxonomist.convert import taxon_converter
import ncbi_taxonomist.remote.query
import ncbi_taxonomist.taxaquery.name_resolver_query
import ncbi_taxonomist.taxaquery.taxid_resolver_query
import ncbi_taxonomist.taxaquery.accession_resolver_query
import ncbi_taxonomist.resolve.remote_resolver


class TaxaResolver:

  def __init__(self, db:Type[sqlite_dbm.TaxonomySqlite], email:str):
    self.db = db
    self.email = email

  def resolve_names(self,
                    names:Iterable[str],
                    converter:Type[taxon_converter.TaxonConverter]) -> Set[int]:
    nrq = ncbi_taxonomist.taxaquery.name_resolver_query.NameResolverQuery(names)
    taxids = [x for x in self.db.map_names_to_ids(names)]
    nrq.resolve(taxids, self.db.get_taxid_lineages(taxids, converter))
    return nrq.queries

  def resolve_taxids(self,
                     taxids:Iterable[int],
                     converter:Type[taxon_converter.TaxonConverter]) -> Set[int]:
    trq = ncbi_taxonomist.taxaquery.taxid_resolver_query.TaxidResolverQuery(taxids)
    self.db.get_taxid_lineages(taxids, converter)
    trq.resolve(taxids, self.db.get_taxid_lineages(taxids, converter))
    return trq.queries

  def resolve_names_remote(self,
                           names:Iterable[str],
                           converter:Type[taxon_converter.TaxonConverter]) -> Set[int]:
    nrq = ncbi_taxonomist.taxaquery.name_resolver_query.NameResolverQuery(names)
    rtq = ncbi_taxonomist.remote.query.RemoteTaxonomyQuery(self.email)
    rtq.query_names(names, ncbi_taxonomist.resolve.remote_resolver.RemoteResolver(nrq, converter))
    return nrq.queries

  def resolve_taxids_remote(self,
                            taxids:Iterable[int],
                            converter:Type[taxon_converter.TaxonConverter]) -> Set[int]:
    trq = ncbi_taxonomist.taxaquery.taxid_resolver_query.TaxidResolverQuery(taxids)
    rtq = ncbi_taxonomist.remote.query.RemoteTaxonomyQuery(self.email)
    rtq.query_taxids(taxids, ncbi_taxonomist.resolve.remote_resolver.RemoteResolver(trq, converter))
    return trq.queries


  def resolve_accession_mapping_remote(self,
                                       taxids:Iterable[int],
                                       accs_map:Mapping[int, Iterable[str]],
                                       converter:Type[taxon_converter.TaxonConverter]) -> Set[int]:
    arq = ncbi_taxonomist.taxaquery.accession_resolver_query.AccessionResolverQuery(accs_map)
    rtq = ncbi_taxonomist.remote.query.RemoteTaxonomyQuery(self.email)
    rtq.query_taxids(taxids, ncbi_taxonomist.resolve.remote_resolver.RemoteResolver(arq, converter))
    return arq.queries
