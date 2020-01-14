# -*- coding: utf-8 -*-

from trytond.model import ModelView, ModelSQL, fields
from trytond.pool import Pool, PoolMeta
from trytond.transaction import Transaction
from trytond.pyson import Id


# objektklassen auflisten
__all__ = ['Party']
__metaclass__ = PoolMeta


class Party(ModelSQL, ModelView):
    'Party'
    __name__ = 'party.party'

    def get_code_readonly(self, name):
        """ check if current user has permission to edit
        """
        pool = Pool()
        ModelData = pool.get('ir.model.data')
        Group = pool.get('res.group')
        context = Transaction().context
        
        id1 = Group(ModelData.get_id('party_admin_edit', 'group_party_edit_fields')).id
        if id1 in context.get('groups', []):
            return False
        else :
            return True

# ende Party
