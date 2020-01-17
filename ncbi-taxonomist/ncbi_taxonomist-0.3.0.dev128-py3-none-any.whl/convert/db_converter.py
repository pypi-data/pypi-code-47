#  -------------------------------------------------------------------------------
#  \author Jan P Buchmann <jan.buchmann@sydney.edu.au>
#  \copyright 2019 The University of Sydney
#  \description
#  -------------------------------------------------------------------------------


from typing import Dict, Type, Mapping


import ncbi_taxonomist.taxon
import ncbi_taxonomist.convert.taxon_converter

class DatabaseTaxonConverter(ncbi_taxonomist.convert.taxon_converter.TaxonConverter):

  def __init__(self, taxonmodel:Type[ncbi_taxonomist.taxon.Taxon]):
    super().__init__(taxonmodel)

  def convert_to_model(self, dbentry:Mapping) -> Type[ncbi_taxonomist.taxon.Taxon]:
    dbentry['names'] = {}
    if 'name' in dbentry:
      dbentry['names'].update({dbentry['name']:dbentry['type']})
    return self.taxonmodel.new(dbentry)

  def convert_from_model(self, taxonmodel:Type[ncbi_taxonomist.taxon.Taxon]) -> Dict[str, str]:
    return model.get_attribues()
