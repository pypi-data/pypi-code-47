#  -------------------------------------------------------------------------------
#  \author Jan P Buchmann <jan.buchmann@sydney.edu.au>
#  \copyright 2019 The University of Sydney
#  \description
#  -------------------------------------------------------------------------------

class TaxonConverter:

  def __init__(self, taxonmodel):
    self.taxonmodel = taxonmodel

  def convert_to_model(self, attributes):
    raise NotImplementedError

  def convert_from_model(self, taxonmodel, outdict=None):
    raise NotImplementedError
