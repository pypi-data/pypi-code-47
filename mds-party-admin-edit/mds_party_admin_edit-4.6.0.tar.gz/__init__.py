from trytond.pool import Pool
from .party import Party


def register():
    Pool.register(
        Party,
        module='party_admin_edit', type_='model')
