#-------------------------------------------------------------------------------
#  \author Jan P Buchmann <jan.buchmann@sydney.edu.au>
#  \copyright 2019 The University of Sydney
#  \description
#-------------------------------------------------------------------------------

from typing import Iterable, Mapping


import ncbi_taxonomist.utils

class AccessionMapperQuery:

  def __init__(self, queries:Mapping[str, int]):
    self.queries = set(queries)

  def map_accession(self, summary:dict, srcdb:str) -> dict:
    accs = []
    if summary['caption'] in self.queries:
      self.collect_accessions(summary, accs, srcdb)
      return accs
    if summary['accessionversion'] in self.queries:
      self.collect_accessions(summary, accs, srcdb)
      return accs
    if summary['uid'] in self.queries:
      self.collect_accessions(summary, accs, srcdb)
      return accs
    if summary['extra'] in self.queries:
      self.collect_accessions(summary, accs, srcdb)
      return accs
    return None

  def collect_accessions(self, summary, accs, srcdb):
    taxid = summary.pop('taxid')
    if 'caption' in summary:
      self.queries.discard(summary['caption'])
      accs.append({'accs':summary.pop('caption'),
                   'taxid':taxid,
                   'type':'caption',
                   'db':srcdb})
      ncbi_taxonomist.utils.json_stdout(accs[-1])
    if 'accessionversion' in summary:
      self.queries.discard(summary['accessionversion'])
      accs.append({'accs':summary.pop('accessionversion'),
                   'taxid':taxid,
                   'type':'accessionversion',
                   'db':srcdb})
      ncbi_taxonomist.utils.json_stdout(accs[-1])
    if 'extra' in summary:
      self.queries.discard(summary['extra'])
      accs.append({'accs':summary.pop('extra'),
                   'taxid':taxid,
                   'type':'extra',
                   'db':srcdb})
      ncbi_taxonomist.utils.json_stdout(accs[-1])
    if 'uid' in summary:
      self.queries.discard(summary['uid'])
      accs.append({'accs':summary.pop('uid'),
                   'taxid':taxid,
                   'type':'uid',
                   'db':srcdb})
      ncbi_taxonomist.utils.json_stdout(accs[-1])

  def map_local_accession(self, accs_data:Mapping[str, str]):
    self.queries.discard(accs_data['accs'])
    ncbi_taxonomist.utils.json_stdout(accs_data)
