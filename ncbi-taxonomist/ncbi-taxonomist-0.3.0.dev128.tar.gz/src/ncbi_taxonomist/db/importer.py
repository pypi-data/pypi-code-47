#-------------------------------------------------------------------------------
#  \author Jan P Buchmann <jan.buchmann@sydney.edu.au>
#  \copyright 2019 The University of Sydney
#  \description
#-------------------------------------------------------------------------------

import sys
import json
import logging

import ncbi_taxonomist.utils

class DatabaseImporter:

  def __init__(self):
    pass

  @staticmethod
  def parse_taxa(taxon, taxa,  names):
    taxa.append(tuple([taxon.taxon_id, taxon.rank, taxon.parent_id]))
    if taxon.names:
      for j in taxon.names:
        names.append(tuple([taxon.taxon_id, j, taxon.names[j]]))

  @staticmethod
  def commit_taxa(db, taxa, names):
    db.add_taxa(taxa)
    db.add_names(names)
    taxa = []
    names = []

  @staticmethod
  def commit_accessions(db, taxids, accessions):
    db.add_taxids(taxids)
    db.add_accessions(accessions)
    taxids = []
    accessions = []

  @staticmethod
  def import_taxa(db, converter, out_attrib):
    taxa = []
    names = []
    for i in sys.stdin:
      attribs = DatabaseImporter.filter_attribute(i, out_attrib)
      DatabaseImporter.parse_taxa(converter.taxonmodel.new(attribs), taxa, names)
      if len(taxa) % 100000 == 0:
        DatabaseImporter.commit_taxa(db, taxa, names)
    if taxa:
      DatabaseImporter.commit_taxa(db, taxa, names)

  @staticmethod
  def import_accsessionmap(db, out_attrib):
    taxids = []
    accessions = []
    for i in sys.stdin:
      attribs = DatabaseImporter.filter_attribute(i, out_attrib)
      accessions.append((attribs.pop('accs'), attribs.pop('db'), attribs.get('type'), attribs.get('taxid')))
      taxids.append((attribs.pop('taxid'),))
      if len(accessions) % 100000 == 0:
        DatabaseImporter.commit_accessions(db, taxids, accessions)
    if accessions:
      DatabaseImporter.commit_accessions(db, taxids, accessions)

  @staticmethod
  def import_lineage(db, converter, out_attrib=None):
    taxa = []
    names = []
    for i in sys.stdin:
      attribs = DatabaseImporter.filter_attribute(i, out_attrib)
      for j in attribs.pop('lin'):
        DatabaseImporter.parse_taxa(converter.taxonmodel.new(j), taxa, names)
      if len(taxa) % 100000 == 0:
        DatabaseImporter.commit_taxa(db, taxa, names)
    if taxa:
      DatabaseImporter.commit_taxa(db, taxa, names)

  @staticmethod
  def filter_attribute(line, attrib):
    attribs = json.loads(line.strip())
    if attrib is None:
      sys.stdout.write(line)
      return attribs
    if attrib in attribs:
      sys.stdout.write(json.dumps(attribs[attrib])+'\n')
      return attribs
    #logger = logging.getLogger("{}.{}".format(ncbi_taxonomist.utils.resolve_log_nspace(DatabaseImporter), sys._getframe().f_code.co_name))
    #logger.debug("Attribute {} not found".format(attrib))
    logger = logging.getLogger('ncbi-taxonomist')
    logger.info("Attribute {} not found for filtering".format(attrib))
    return attribs
