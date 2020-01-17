#-------------------------------------------------------------------------------
#  \author Jan P Buchmann <jan.buchmann@sydney.edu.au>
#  \copyright 2019, 2020 The University of Sydney
#-------------------------------------------------------------------------------


import sys
import logging
import sqlite3
from typing import Iterable, Dict, List, Tuple, Type


import ncbi_taxonomist.utils
import ncbi_taxonomist.taxon
from ncbi_taxonomist.convert import db_converter
from ncbi_taxonomist.taxaquery import mapper_query
from ncbi_taxonomist.taxaquery import collector_query
from ncbi_taxonomist.taxaquery import resolver_query
from ncbi_taxonomist.taxaquery import accession_mapper_query
from ncbi_taxonomist.collection import subtree_collection
from ncbi_taxonomist.db.sqlite_table import taxa_table
from ncbi_taxonomist.db.sqlite_table import name_table
from ncbi_taxonomist.db.sqlite_table import alias_table
from ncbi_taxonomist.db.sqlite_table import accession_table


class TaxonomySqlite:

  def __init__(self, dbpath:str):
    self.logger = logging.getLogger(ncbi_taxonomist.utils.resolve_log_nspace(TaxonomySqlite))
    self.logger.debug("Create instance")
    self.path = dbpath
    self.connection = self.init_connection(dbpath)
    self.taxa = taxa_table.TaxaTable(dbpath).create(self.connection)
    self.names = name_table.NameTable(dbpath).create(self.connection)
    self.accessions = accession_table.AccessionTable(dbpath).create(self.connection)
    self.logger.info("Database initialized")

  def init_connection(self, dbpath:str) -> sqlite3.Connection:
    self.logger.debug("Connecting to: {}".format(dbpath))
    connection = sqlite3.connect(dbpath)
    connection.execute("PRAGMA foreign_keys=1")
    connection.row_factory = sqlite3.Row
    self.logger.info("Connected to: {}".format(dbpath))
    return connection

  def close_connection(self) -> None:
    self.connection.close()

  def connect(self) -> sqlite3.Connection:
    if self.connection is None:
      return self.init_connection(self.path)
    return self.connection

  def add_taxa(self, taxa:Iterable[Tuple[int,str,int]]) -> None:
    self.taxa.insert(self.connection, taxa)

  def add_taxids(self, taxids:Iterable[Tuple[int,]]) -> None:
    self.taxa.insert_taxids(self.connection, taxids)

  def add_names(self, names:Iterable[Tuple[int,str,str]]) -> None:
    self.names.insert(self.connection, names)

  def add_accessions(self, accessions:Iterable[Tuple[str, str, str, int]])  -> None:
    self.accessions.insert(self.connection, accessions)

  def collect_name_subtree(self, start_names, converter, torank=None):
    raise NotImplementedError

  def collect_id_subtree(self, root_ids:Iterable[int], converter) -> List:
    """
    Collect subtree for given taxon ids.
    """
    collections = []
    for i in root_ids:
      for j in self.taxa.get_subtree(self.connection, i):
        converter.convert_to_model({'taxon_id': j['taxon_id'],
                                    'parent_id':j['parent_id'],
                                    'rank':j['rank'],
                                    'name':j['name'], 'type':j['type']})
      collections.append(subtree_collection.SubtreeCollection(i, converter.taxa))
      converter.reset()
    return collections

  def get_taxa_by_name(self, names:Iterable[str], converter,
                       query:Type[mapper_query.MapperQuery]=None) -> Dict[str,int]:
    """
    Find taxa by name and use the converter to format into appropriate model.
    ToDo: Test if  n.name='man' OR n.name='Bacteria OR ...' is better approach

    :param names: taxonomy names to find
    :param converter: taxon database converter
    :return: name taxa id mapping
    """
    stmt = """SELECT n.name, n.type, t.taxon_id, t.rank, t.parent_id FROM taxa t
              JOIN names n on t.taxon_id=n.taxon_id WHERE n.name=?"""
    taxa = {}
    for i in names:
      for j in self.connection.cursor().execute(stmt, (i,)):
        if j['taxon_id'] not in taxa:
          taxa[j['taxon_id']] = converter.convert_to_model({'taxon_id': j['taxon_id'],
                                                            'parent_id':j['parent_id'],
                                                            'rank':j['rank']})
        taxa[j['taxon_id']].update_names({j['name']:j['type']})
        if query:
          query.map_query(taxa[j['taxon_id']])
    return taxa

  def get_taxids_by_accessions(self, accs:Iterable[str], db:str,
                               query:Type[accession_mapper_query.AccessionMapperQuery]=None) -> List[Dict]:
    """
    Find taxa by name and use the converter to format into appropriate model.

    :param accs: accessions
    :param db: Entrez db name
    :param query: search query
    """
    stmt = """SELECT a.accession, a.db, a.type, t.taxon_id FROM taxa t JOIN
              accessions a on t.taxon_id=a.taxon_id WHERE a.accession=? AND a.db=?"""
    if not db:
      db='%'
      stmt = """SELECT a.accession, a.db, a.type, t.taxon_id FROM taxa t JOIN
                accessions a on t.taxon_id=a.taxon_id WHERE a.accession=? AND a.db LIKE ?"""
    mappings = []
    for i in accs:
      for j in self.connection.cursor().execute(stmt, (i, db)):
        mappings.append({'accs':j['accession'], 'taxid':j['taxon_id'], 'type':j['type'], 'db':j['db']})
        if query:
          query.map_local_accession(mappings[-1])
    return mappings

  def get_taxa_by_taxids(self,
                         taxids:Iterable[int],
                         converter:Type[db_converter.DatabaseTaxonConverter],
                         query:Type[mapper_query.MapperQuery]=None) -> Dict[int, ncbi_taxonomist.taxon.Taxon]:
    """
    Find taxa by taxid and format into appropriate model.

    :param taxids: list of taxids
    :param converter: taxon database converter
    :return: taxa found in db
    """
    stmt = """SELECT t.taxon_id, t.rank, t.parent_id, n.name, n.type \
              FROM taxa t JOIN names n on t.taxon_id=n.taxon_id WHERE t.taxon_id=?"""
    taxa = {}
    for i in taxids:
      for j in self.connection.cursor().execute(stmt, (i,)):
        if j['taxon_id'] not in taxa:
          taxa[j['taxon_id']] = converter.convert_to_model({'taxon_id': j['taxon_id'],
                                                            'rank':j['rank'],
                                                            'parent_id':j['parent_id']})
        taxa[j['taxon_id']].update_names({j['name']:j['type']})
        if query:
          query.map_query(taxa[j['taxon_id']])
    return taxa

  def get_taxid_lineages(self,
                         taxids:Iterable[int],
                         converter:Type[db_converter.DatabaseTaxonConverter]) -> Dict[int, ncbi_taxonomist.taxon.Taxon]:
    """
    Find linegae for given taxon id. Found taxids are cached to avoid unnecessary
    lookups.
    ToDo: use converters own cache

    :param taxids: taxids to find lineage for
    :param converter: taxon converter to convert database rows into taxon models
    :return: converter
    """
    found_taxa = {}
    for i in taxids:
      if i not in found_taxa:
        for j in self.taxa.get_lineage(self.connection, i, self.names.name):
          if j['taxon_id'] not in found_taxa:
            found_taxa[j['taxon_id']] = converter.convert_to_model({'taxon_id': j['taxon_id'],
                                                                    'rank':j['rank'],
                                                                    'parent_id':j['parent_id']})
          found_taxa[j['taxon_id']].update_names({j['name']:j['type']})
    return found_taxa
