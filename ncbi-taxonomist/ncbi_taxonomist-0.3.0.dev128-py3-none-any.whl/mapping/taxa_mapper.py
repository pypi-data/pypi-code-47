#  -------------------------------------------------------------------------------
#  \author Jan P Buchmann <jan.buchmann@sydney.edu.au>
#  \copyright 2019 The University of Sydney
#  \description
#  -------------------------------------------------------------------------------

import json
from typing import Set, Type, Iterable


from ncbi_taxonomist.convert import taxon_converter
import ncbi_taxonomist.remote.query
import ncbi_taxonomist.mapping.remote_mapper
import ncbi_taxonomist.mapping.remote_accession_mapper
import ncbi_taxonomist.taxaquery.taxid_mapper_query
import ncbi_taxonomist.taxaquery.name_mapper_query
import ncbi_taxonomist.taxaquery.accession_mapper_query


class TaxaMapper:

  def __init__(self, db, email):
    self.db = db
    self.email = email

  def map_names(self, names:Iterable[str], converter:Type[taxon_converter.TaxonConverter]) -> Set[str]:
    amq = ncbi_taxonomist.taxaquery.name_mapper_query.NameMapperQuery(names)
    self.db.get_taxa_by_name(names, converter, amq)
    return amq.queries

  def map_taxids(self, taxids, converter):
    tmq = ncbi_taxonomist.taxaquery.taxid_mapper_query.TaxidMapperQuery(taxids)
    self.db.get_taxa_by_taxids(taxids, converter, tmq)
    return tmq.queries

  def map_accessions(self, accessions:Iterable[str], entrezdb:str) -> Set[str]:
    amq = ncbi_taxonomist.taxaquery.accession_mapper_query.AccessionMapperQuery(accessions)
    self.db.get_taxids_by_accessions(accessions, entrezdb, amq)
    return amq.queries

  def map_names_remote(self, names:Iterable[str], converter:Type[taxon_converter.TaxonConverter]) -> Set[str]:
    nmq = ncbi_taxonomist.taxaquery.name_mapper_query.NameMapperQuery(names)
    rtq = ncbi_taxonomist.remote.query.RemoteTaxonomyQuery(self.email)
    rtq.query_names(names, ncbi_taxonomist.mapping.remote_mapper.RemoteMapper(nmq, converter))
    return nmq.queries

  def map_taxids_remote(self, taxids:Iterable[int], converter:Type[taxon_converter.TaxonConverter]) -> Set[int]:
    tmq = ncbi_taxonomist.taxaquery.taxid_mapper_query.TaxidMapperQuery(taxids)
    rtq = ncbi_taxonomist.remote.query.RemoteTaxonomyQuery(self.email)
    rtq.query_taxids(taxids, ncbi_taxonomist.mapping.remote_mapper.RemoteMapper(tmq, converter))
    return tmq.queries

  def map_accessions_remote(self, accessions:Iterable[str], entrezdb:str) -> Set[str]:
    amq = ncbi_taxonomist.taxaquery.accession_mapper_query.AccessionMapperQuery(accessions)
    rtq = ncbi_taxonomist.remote.query.RemoteTaxonomyQuery(self.email)
    rtq.query_accessions(accessions,
                         entrezdb,
                         ncbi_taxonomist.mapping.remote_accession_mapper.RemoteAccessionMapper(amq))
    return amq.queries
