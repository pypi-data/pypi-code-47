#-------------------------------------------------------------------------------
#\author Jan P Buchmann <jan.buchmann@sydney.edu.au>
#\copyright 2019 The University of Sydney
#\description
#-------------------------------------------------------------------------------


import sys


import ncbi_taxonomist.convert.taxon_converter


class NcbiTaxonConverter(ncbi_taxonomist.convert.taxon_converter.TaxonConverter):

  attribute_mapper = {'taxid' : 'taxon_id', 'parent_taxid' : 'parent_id'}
  exclude = set(['misspelling', 'authority'])

  def __init__(self, taxonmodel):
    super().__init__(taxonmodel)

  def convert_to_model(self, attributes):
    for i in NcbiTaxonConverter.attribute_mapper:
      if i in attributes:
        attributes[NcbiTaxonConverter.attribute_mapper[i]] = attributes.pop(i)
    attributes['names'] = {attributes.pop('scientific_name'):'scientific_name'}
    attributes['names'].update(attributes['other_names'].pop('names', None))
    m = self.taxonmodel.new(attributes)
    if 'cde_names' in attributes['other_names']:
      for i in attributes['other_names'].pop('cde_names'):
        if i['cde'] not in NcbiTaxonConverter.exclude:
          m.names[i['name']] = 'cde'
          if i['uniqname']:
            m.names[i['uniqname']] = 'uniqname'
    return m
