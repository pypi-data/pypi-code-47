import os
from ..track_hub import TrackHub


def create_default_hub(root_dir, hub_name, email, shortLabel=None, longLabel=None,
                       genomesFile='genomes.txt', descriptionURL=None,
                       genomes=[], hub_file_path='hub.txt', genomes_file_path='genomes.txt',
                       groups_file_path='groups.txt'):
    '''
    '''
    hub = TrackHub(root_dir=root_dir, hub=hub_name, shortLabel=shortLabel, longLabel=longLabel,
                   genomesFile=genomesFile, email=email, descriptionURL=descriptionURL,
                   genomes=genomes, hub_file_path=hub_file_path, genomes_file_path=genomes_file_path)

    # Set short and long labels to the name of the hub
    if not hub.hub_file.shortLabel:
        hub.hub_file.shortLabel = hub.hub_file.hub
    if not hub.hub_file.longLabel:
        hub.hub_file.longLabel = hub.hub_file.hub

    order = 0
    for genome in hub.genome_file.genomes:
        # Set 2bit file name to the name of the genome
        if not genome.twoBitPath:
            genome.twoBitPath = os.path.join(genome.genome, f'{genome.genome}.2bit')
        # Set groups file to default groups file ('groups.txt' if not specified)
        if not genome.groups:
            genome.groups = groups_file_path
        # Set genome description to the name of the genome
        if not genome.description:
            genome.description = genome.genome
        # Automatically increment and set genome order key
        if not genome.orderKey:
            genome.orderKey = order
        order += 1

    hub.create()
    return hub
