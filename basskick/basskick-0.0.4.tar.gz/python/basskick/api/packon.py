'''




'''


import logging
logger = logging.getLogger(__name__)

def create(name, benv=None):
    logger.info(
        'Creating Packons {}{}'.format(
            name,
            benv and ' in benv {}'.format(benv) or '',
        )
    )

def install(names, benv=None, upgrade=False, index_url=None):
    logger.info(
        '{} Packons {}{}{}'.format(
            upgrade and 'Upgrading' or 'Installing',
            names,
            benv and ' in benv {}'.format(benv) or '',
            index_url and ' from index {}'.format(index_url) or '',
        )
    )

def uninstall(names, benv=None):
    logger.info(
        'Uninstalling Packons {}{}'.format(
            names,
            benv and ' from benv {}'.format(benv) or '',
        )
    )

def list(benv, outdated, uptodate, editable):
    logger.info(
        'Listing Packons ({}){}'.format(
            'outdated={}, uptodate={}, editable={}'.format(
                outdated, uptodate, editable
            ),
            benv and ' in benv {}'.format(benv) or '',
        )
    )

def show(names, benv):
    logger.info(
        'Informations for Packons {}{}'.format(
            names,
            benv and ' in benv {}'.format(benv) or '',
        )
    )
