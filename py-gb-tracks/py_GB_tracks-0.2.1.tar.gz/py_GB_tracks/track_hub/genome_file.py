import os
from ..meta import FileWriter


class Genome(FileWriter):

    def __init__(self, genome, trackDb='trackDb.txt', metaDb=None, metaTab=None, twoBitPath=None,
                 groups=None, description=None, organism=None, defaultPos=None, orderKey=None,
                 htmlPath=None, scientificName=None):
        '''
        '''
        self.genome = genome
        self.trackDb = trackDb
        self.metaDb = metaDb
        self.metaTab = metaTab
        self.twoBitPath = twoBitPath
        self.groups = groups
        self.description = description
        self.organism = organism
        self.defaultPos = defaultPos
        self.orderKey = orderKey
        self.htmlPath = htmlPath
        self.scientificName = scientificName


class GenomeFile:

    def __init__(self, genomes=[]):
        '''
        '''
        self.genomes = []
        if len(genomes) > 0:
            for genome in genomes:
                self.genomes.append(Genome(**genome))

    def __contains__(self, item):
        '''
        '''
        for genome in self.genomes:
            if genome.genome == item:
                return True
        return False

    def __getitem__(self, key):
        '''
        '''
        for genome in self.genomes:
            if genome.genome == key:
                return genome
        raise KeyError(f'{key}')

    def write_to_file(self, output_file):
        '''
        '''
        for genome in self.genomes:
            genome.write_to_file(output_file)


