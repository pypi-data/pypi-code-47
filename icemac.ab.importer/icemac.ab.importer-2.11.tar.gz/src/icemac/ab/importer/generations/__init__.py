"""Database initialisation and upgrading."""

import zope.generations.generations


GENERATION = 0


manager = zope.generations.generations.SchemaManager(
    minimum_generation=GENERATION,
    generation=GENERATION,
    package_name='icemac.ab.importer.generations')
