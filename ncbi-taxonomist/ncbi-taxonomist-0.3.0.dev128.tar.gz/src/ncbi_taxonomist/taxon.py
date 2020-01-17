#-------------------------------------------------------------------------------
#\author Jan P Buchmann <jan.buchmann@sydney.edu.au>
#\copyright 2019 The University of Sydney
#\description
#-------------------------------------------------------------------------------

import sys
import json

class Taxon:

  @classmethod
  def new(cls, attributes={}):
    return cls(attributes)

  @classmethod
  def new_from_json(cls, json_attributes):
    return Taxon.new(json.loads(json_attributes))

  def __init__(self, attributes={}):
    self.taxon_id = attributes.pop('taxon_id', None)
    self.parent_id = attributes.pop('parent_id', None)
    self.rank = attributes.pop('rank', None)
    self.names = attributes.pop('names', {})
    if self.rank == 'no rank':
      self.rank = None

  def update_names(self, names):
    self.names.update(names)

  def update(self, taxon):
    self.update_names(taxon.names)

  def get_attributes(self):
    return {'taxon_id':self.taxon_id,
            'parent_id':self.parent_id,
            'rank' : self.rank,
            'names':self.names}

  def get_names(self):
    return self.names

  def get_name_by_type(self, nametype='scientific_name'):
    for i in self.names:
      if self.names[i] == nametype:
        return i
