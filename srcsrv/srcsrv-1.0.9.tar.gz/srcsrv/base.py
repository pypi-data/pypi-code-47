'''Program Database (PDB) parsing base class
'''
# Python modules
import logging


class Base(object):
    '''Base class for source indexing
    '''
    def __init__(self, args):
        self.args = args
        self.build_base = args.build_base
        # Make sure the path ends with '\\'
        if not self.build_base.endswith('\\'):
            self.build_base = self.build_base + '\\'

        self._sources = None
        logging.basicConfig(filename=self.args.log, level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger('Source_Indexing')


__all__ = ['Base']
