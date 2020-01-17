#-------------------------------------------------------------------------------
#  \author Jan P Buchmann <jan.buchmann@sydney.edu.au>
#  \copyright 2019 The University of Sydney
#  \description
#-------------------------------------------------------------------------------


import os
import sys
import json
import logging
import resource
from typing import Mapping, Type, Iterable


#sys.path.insert(1, os.path.join(sys.path[0], '../include/taxonomy/src'))
import taxonompy
#sys.path.insert(1, os.path.join(sys.path[0], '../include/entrezpy/src'))
import entrezpy


from ncbi_taxonomist import utils
from ncbi_taxonomist import taxon
from ncbi_taxonomist import taxa_cache
from ncbi_taxonomist.convert import ncbi_converter
from ncbi_taxonomist.convert import db_converter
import ncbi_taxonomist.db.sqlite_dbm
import ncbi_taxonomist.db.importer
import ncbi_taxonomist.remote.query
import ncbi_taxonomist.mapping.taxa_mapper
import ncbi_taxonomist.resolve.taxa_resolver
import ncbi_taxonomist.collect.taxa_collector

logger = logging.getLogger('ncbi-taxonomist')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(ch)

class NcbiTaxonomist:

  cache = taxa_cache.TaxaCache()

  def __init__(self, dbpath:str=None, email:str=None):
    self.dbpath = dbpath
    self.email = email
    self.db = None
    if dbpath:
      self.db = ncbi_taxonomist.db.sqlite_dbm.TaxonomySqlite(dbpath)

  def cache_taxon(self, taxon:Type[taxon.Taxon]):
    NcbiTaxonomist.cache.cache_id(taxon.taxon_id)
    NcbiTaxonomist.cache.cache_names(taxon.get_names())

  def cache_taxa(self, taxa:Mapping[int,taxon.Taxon]):
    for i in taxa:
      self.cache_taxon(taxa[i])

  def map_taxa(self, taxids:Iterable[int]=None, names:Iterable[str]=None, remote:bool=False):
    """
      Map names to taxids and vice-versa. Print mappings as JSON to STDOUT.

      :param taxids: query taxids
      :param names: query names
      :param remote: query NCBI Entrez database
    """
    tm = ncbi_taxonomist.mapping.taxa_mapper.TaxaMapper(self.db, self.email)
    if self.db and names:
      nmap = tm.map_names(names, db_converter.DatabaseTaxonConverter(taxon.Taxon()))
    if self.db and taxids:
      tmap = tm.map_taxids(taxids, db_converter.DatabaseTaxonConverter(taxon.Taxon()))
    if remote and names:
      tm.map_names_remote(names, ncbi_converter.NcbiTaxonConverter(taxon.Taxon()))
    if remote and taxids:
      tm.map_taxids_remote(taxids, ncbi_converter.NcbiTaxonConverter(taxon.Taxon()))

  def map_accessions(self, accessions:Iterable[str], entrezdb:str, remote:bool=False):
    """
      Map accessions to taxids. Print mappings as JSON to STDOUT.

      :param accessions: query taxids
      :param entrezdb: accession origin Entrez database name
      :param remote: query NCBI Entrez database
    """
    tm = ncbi_taxonomist.mapping.taxa_mapper.TaxaMapper(self.db, self.email)
    if self.db:
      tm.map_accessions(accessions, entrezdb)
    if remote:
      if not entrezdb:
        entrezdb = 'nucleotide'
        logger.info("No entrez db given. Using nucleotide")
      tm.map_accessions_remote(accessions, entrezdb)

  def collect(self, taxids:Iterable[int]=None, names:Iterable[str]=None):
    """
      Collect taxa information remotely from Entrez.

      :param taxids: query taxids
      :param names: query names
    """
    tc = ncbi_taxonomist.collect.taxa_collector.TaxaCollector(self.email)
    if names:
      logger.debug("Collect names remotely: {}".format(names))
      tc.collect_names(names, ncbi_converter.NcbiTaxonConverter(taxon.Taxon()))
    if taxids:
      logger.debug("Collect taxids remotely: {}".format(names))
      tc.collect_taxids(taxids, ncbi_converter.NcbiTaxonConverter(taxon.Taxon()))

  def import_to_db(self, out_attrib:str, taxa:bool=False, lineage:bool=False, accessions:bool=False):
    """
      Import data to local taxonomy database. Attribute names can be passed to
      filter them for piped processing. Taxa, lineages and accessions require
      specific parser.

      :param out_attrib: attribute name to filter
      :param taxa: import taxa
      :param lineage: import lineage
      :param accession: import accession
    """
    if taxa:
      ncbi_taxonomist.db.importer.DatabaseImporter.import_taxa(self.db, db_converter.DatabaseTaxonConverter(taxon.Taxon()), out_attrib)
    if accessions:
      ncbi_taxonomist.db.importer.DatabaseImporter.import_accsessionmap(self.db, out_attrib)
    if lineage:
      ncbi_taxonomist.db.importer.DatabaseImporter.import_lineage(self.db, db_converter.DatabaseTaxonConverter(taxon.Taxon()), out_attrib)

  def resolve(self, taxids:Iterable[int]=None, names:Iterable[str]=None, remote:bool=False):
    """
    Resolve lineages for names and taxids. If a local database is given, it
    will be checked first, followed by checking Entrez remotely if requested.
    Lineagae are printed to STDOUT as JSON array.

    :param taxids: taxids
    :param names: taxa names
    :param remote: query NCBI Entrez database
    """
    logger.info("Resolving taxonomies")
    tr = ncbi_taxonomist.resolve.taxa_resolver.TaxaResolver(self.db, self.email)
    if self.db and names:
      logger.debug("Resolve {} name(s) locally: {}".format(len(names), names))
      tr.resolve_names(names, db_converter.DatabaseTaxonConverter(taxon.Taxon()))
    if self.db and taxids:
      logger.debug("Resolve {} taxid(s) locally: {}".format(len(taxids), taxids))
      tr.resolve_taxids(taxids, db_converter.DatabaseTaxonConverter(taxon.Taxon()))
    if remote and names:
      logger.debug("Resolve name(s) remotely : {}".format(names))
      tr.resolve_names_remote(names, ncbi_converter.NcbiTaxonConverter(taxon.Taxon()))
    if remote and taxids:
      logger.debug("Resolve id(s) remotely: {}".format(taxids))
      tr.resolve_taxids_remote(taxids, ncbi_converter.NcbiTaxonConverter(taxon.Taxon()))

  def resolve_accession_map(self, remote:bool=False):
    """
    Resolve lineages for accessions from STDIN. Lineagaes are printed to STDOUT
    as JSON array.

    :param remote: query NCBI Entrez database
    """
    accs_map = utils.parse_accession_map()
    tr = ncbi_taxonomist.resolve.taxa_resolver.TaxaResolver(self.db, self.email)
    if remote:
      logger.debug("Resolve accessions map remotely: {}".format(accs_map))
      tr.resolve_accession_mapping_remote([x for x in accs_map],
                                          accs_map,
                                          ncbi_converter.NcbiTaxonConverter(taxon.Taxon()))

  def get_subtree(self, taxa_ids:list=None, names:list=None, remote:bool=False):
    if self.db:
      dbc = db_converter.DatabaseTaxonConverter(taxon.Taxon())
      if taxa_ids:
        for i in self.db.collect_id_subtree(taxa_ids, dbc):
          self.cache_taxa(i.taxa)
          print(json.dumps(i.export_collection()))

    if remote:
      rtc = remote.RemoteTaxonomyCollector()
      nc = ncbi_converter.NcbiTaxonConverter(taxon.Taxon())
      taxa_ids = NcbiTaxonomist.cache.remove_cached_ids(taxa_ids)
      if taxa_ids:
        for i in taxa_ids:
          co.query(self.email, "txid{}[orgn]".format(i), nc)
