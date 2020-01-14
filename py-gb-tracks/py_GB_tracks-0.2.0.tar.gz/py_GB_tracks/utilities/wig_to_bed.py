import logging
from collections import defaultdict
from .color_scale import ColorScale
from .logging import Logger


class WigToBed:

    def __init__(self, log_level=logging.INFO, colors=((255, 0, 0), (0, 0, 255)), n_bins=100):
        self.logger = Logger(log_level=log_level)
        self.colors = colors
        self.n_bins = n_bins
        self.data = None
        self.features = defaultdict(lambda: defaultdict(lambda: {'start': None, 'end': None, 'strand': None, 'score': 0}))
        self.cds_positions = defaultdict(lambda: defaultdict(list))
        self.color_scale = None
        self.min_value = None
        self.max_value = None
        logging.info('Initialized WigToBed instance')

    def load_gtf_file(self, gtf_file_path):
        '''
        Load features from a GTF file.
        Output:
        - features: {scaffold: {CDS_name: {start: cds_start, end: cds_end, strand: feature_strand, score: cds_score}}}
        - cds_positions: {scaffold: {position: [CDS_names]}}
        '''
        logging.info('Loading features from GTF file')
        gtf_file = open(gtf_file_path)
        n_features, n_bp = 0, 0
        for line in gtf_file:
            if not line.startswith('#'):
                fields = line.split('\t')
                if fields[2] == 'CDS':
                    if not fields[0][:3] == 'chr':
                        scaffold = 'chr{}'.format(fields[0])  # Genome browsers require chromosome names to start with chr
                    start = int(fields[3])
                    end = int(fields[4])
                    attributes = dict([x.lstrip(' ').replace('"', '').split(' ') for x in fields[8][:-1].split(';') if x])
                    CDS_name = '{}_{}'.format(attributes['transcript_id'], attributes['exon_number'])
                    self.features[scaffold][CDS_name]['scaffold'] = scaffold
                    self.features[scaffold][CDS_name]['start'] = start
                    self.features[scaffold][CDS_name]['end'] = end
                    self.features[scaffold][CDS_name]['strand'] = fields[6]
                    self.features[scaffold][CDS_name]['CDS_name'] = CDS_name
                    for i in range(start, end):
                        self.cds_positions[scaffold][i].append(CDS_name)
                    n_features += 1
                    n_bp += abs(end - start)
        logging.info('Loaded <{:,}> CDS spanning <{:,}> bp'.format(n_features, n_bp))
        logging.info('GTF file loaded successfully'.format(n_features, n_bp))

    def load_wig_file(self, wig_file_path):
        '''
        Load scores from a wig file for a set of features.
        Positions within CDS are given by cds_positions.
        Scores are summed in features[scaffold][CDS]['score'].
        '''
        logging.info('Loading wig file <{}>'.format(wig_file_path))
        wig_file = open(wig_file_path)
        line_n = 0
        scaffold = None
        position = None
        for line in wig_file:
            if line.startswith('fixedStep'):
                fields = line.split()
                scaffold = fields[1].split('=')[-1]
                position = int(fields[2].split('=')[-1])
            else:
                if scaffold in self.cds_positions and position in self.cds_positions[scaffold]:
                    for transcript in self.cds_positions[scaffold][position]:
                        CDS = self.features[scaffold][transcript]
                        self.features[scaffold][CDS['CDS_name']]['score'] += float(line[:-1])
                position += 1
                if line_n % 25000000 == 0 and line_n != 0:
                    logging.info(' - Processed {} M. lines'.format(int(line_n / 1000000)))
                line_n += 1
        for scaffold, scaffold_features in self.features.items():
            for cds_name, cds_data in sorted(scaffold_features.items(), key=lambda x: x[1]['start']):
                average_score = round(cds_data['score'] / (int(cds_data['end']) - int(cds_data['start']) + 1), 5)
                self.features[scaffold][cds_name]['score'] = average_score
                if not self.min_value or average_score < self.min_value:
                    self.min_value = average_score
                elif not self.max_value or average_score > self.max_value:
                    self.max_value = average_score
        logging.info('Min score: <{}>, max score: <{}>'.format(self.min_value, self.max_value))
        logging.info('Wig file loaded successfully')

    def generate_color_scale(self):
        '''
        Wrapper to generate color scale.
        '''
        self.color_scale = ColorScale(min_value=self.min_value, max_value=self.max_value, n_bins=self.n_bins, colors=self.colors)
        logging.debug('Color scale info: ')
        logging.debug(' - min value <{}>, max value <{}>, number of bins: <{}>'.format(self.color_scale.min_value, self.color_scale.max_value, self.color_scale.n_bins))
        logging.debug(' - colors <{}>'.format(self.color_scale.colors))
        logging.debug(' - bins: {}'.format(self.color_scale.bins))
        logging.debug(' - scale: {}'.format(self.color_scale.color_scale))

    def features_to_bed(self, bed_file_path):
        '''
        Export features loaded from a GTF file and scored to a BED file.
        '''
        bed_file = None
        if bed_file_path:
            bed_file = open(bed_file_path, 'w')
        else:
            logging.info('No output file specified, output to stdout')
        for scaffold, scaffold_features in self.features.items():
            for cds_name, cds_data in sorted(scaffold_features.items(), key=lambda x: x[1]['start']):
                if cds_data['score'] > 1:
                    logging.warning('Feature score > 1: {}, {}, {}, {}'.format(cds_name, cds_data['score'], cds_data['start'], cds_data['end']))
                else:
                    color = self.color_scale.assign_color(cds_data['score'])
                    line = '\t'.join((scaffold, str(cds_data['start']), str(cds_data['end']),
                                      '{}_{}'.format(cds_data['CDS_name'], round(cds_data['score'], 3)),
                                      '0', cds_data['strand'], str(cds_data['start']), str(cds_data['end']),
                                      '{},{},{}'.format(*color)))
                    if bed_file:
                        bed_file.write('{}\n'.format(line))
                    else:
                        print(line)

    def wig_to_bed(self, wig_file_path, gtf_file_path, bed_file_path=None, colors=None, n_bins=None):
        '''
        Create a bed file with average score per CDS for all features in the provided gtf.
        Scores are computed from the wig file.
        If no bed file is specified, output to stdout.
        Colors and number of bins can be specified in this method.
        '''
        if colors:
            self.colors = colors
        if n_bins:
            self.n_bins = n_bins
        logging.info('Convert started')
        self.load_gtf_file(gtf_file_path)
        self.load_wig_file(wig_file_path)
        self.generate_color_scale()
        self.features_to_bed(bed_file_path)
        logging.info('Convert ended successfully')
