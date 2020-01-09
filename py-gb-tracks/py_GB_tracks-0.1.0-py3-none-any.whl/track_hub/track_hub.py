import os
from collections import defaultdict
from .hub_file import HubFile
from .genome_file import GenomeFile
from .. import tracks

tracks_types = {'bam': tracks.BamTrack,
                'bigBarChart': tracks.BigBarChartTrack,
                'bigBed': tracks.BigBedTrack,
                'bigChain': tracks.BigChainTrack,
                'bigGenePred': tracks.BigGenePredTrack,
                'bigInteract': tracks.BigInteractTrack,
                'bigMaf': tracks.BigMafTrack,
                'bigNarrowPeak': tracks.BigNarrowPeakTrack,
                'bigPsl': tracks.BigPslTrack,
                'bigWig': tracks.BigWigTrack}


class TrackHub:

    def __init__(self, root_dir, hub, shortLabel, longLabel, email,
                 genomesFile='genomes.txt', descriptionURL=None,
                 genomes=[], hub_file_path='hub.txt', genomes_file_path='genomes.txt'):
        '''
        '''
        self.root_dir = root_dir
        self.hub_file_path = os.path.join(root_dir, hub_file_path)
        self.genomes_file_path = os.path.join(root_dir, genomes_file_path)
        self.hub_file = HubFile(hub=hub, shortLabel=shortLabel, longLabel=longLabel,
                                genomesFile=genomesFile, email=email, descriptionURL=descriptionURL)
        self.genome_file = GenomeFile(genomes=genomes)
        self.tracks = defaultdict(list)
        self.subtracks = defaultdict(lambda: defaultdict(list))

    def create(self):
        '''
        '''
        if not os.path.isdir(self.root_dir):
            os.mkdir(self.root_dir)
        with open(self.hub_file_path, 'w') as hub_file:
            self.hub_file.write_to_file(hub_file)
        with open(self.genomes_file_path, 'w') as genome_file:
            self.genome_file.write_to_file(genome_file)
        for genome in self.genome_file.genomes:
            genome_dir_path = os.path.join(self.root_dir, genome.genome)
            if not os.path.isdir(genome_dir_path):
                os.mkdir(genome_dir_path)
            if genome.trackDb is not None:
                open(os.path.join(genome_dir_path, genome.trackDb), 'w')
            if genome.groups is not None:
                open(os.path.join(genome_dir_path, genome.groups), 'w')

    def add_track(self, genome, track_type, track_data=None):
        '''
        '''
        if genome not in self.genome_file:
            raise KeyError(f'{genome}')
        if track_type not in tracks_types:
            raise KeyError(f'{track_type}')
        if 'parent' in track_data and track_data['parent'] is not None:
            self.subtracks[genome][track_data['parent']].append(tracks_types[track_type](**track_data, data_type=track_type))
        else:
            self.tracks[genome].append(tracks_types[track_type](**track_data, data_type=track_type))

    def write_tracks(self):
        '''
        '''
        for genome, tracks in self.tracks.items():
            trackDb_file = open(os.path.join(self.root_dir, genome, self.genome_file[genome].trackDb), 'w')
            if genome in self.tracks:
                for i, track in enumerate(sorted(self.tracks[genome], key=lambda t: t.priority if t.priority is not None else 0)):
                    track.write_to_file(trackDb_file)
                    if i < len(self.tracks[genome]) - 1 or track.superTrack is not None:
                        trackDb_file.write('\n')
                    if track.superTrack is not None and genome in self.subtracks:
                        for j, subtrack in enumerate(sorted(self.subtracks[genome][track.track], key=lambda t: t.priority if t.priority is not None else 0)):
                            subtrack.write_to_file(trackDb_file, subtrack=True)
                            if i < len(self.tracks[genome]) - 1 or j < len(self.subtracks[genome][track.track]) - 1:
                                trackDb_file.write('\n')
