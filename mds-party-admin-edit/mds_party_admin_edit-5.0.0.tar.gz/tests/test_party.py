# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from datetime import timedelta
from trytond.tests.test_tryton import ModuleTestCase, with_transaction
from trytond.pool import Pool
from trytond.transaction import Transaction
from trytond.exceptions import UserError
from decimal import Decimal


def create_trytonuser(login, password, groupname=None):
    """ create Tryton user, add to group
    """
    pool = Pool()
    User = pool.get('res.user')
    Groups = pool.get('res.group')

    user, = User.create([{'name': login, 'login': login,}])
    User.write([user], {'password': password,})
    
    # add user to group
    if not isinstance(groupname, type(None)):
        gr1 = Groups.search(['name', '=', groupname])
        if len(gr1) == 1:
            l1 = list(gr1[0].users)
            l1.append(user)
            gr1[0].users = l1
            gr1[0].save()
        else :
            raise ValueError("Group '%s' not found" % groupname)

    return user
# end create_trytonuser


class PartyTestCase(ModuleTestCase):
    'Test party module'
    module = 'party_admin_edit'
    
    @with_transaction()
    def test_get_code_readonly(self):
        """ check results of funktion depends on group of user
        """
        transaction = Transaction()
        pool = Pool()
        Party = pool.get('party.party')
        Address = pool.get('party.address')
        Contact = pool.get('party.contact_mechanism')
        
        # user #1 - group 'Party Edit Fields'
        usr1 = create_trytonuser('frida', 'Test1234', 'Party Edit Fields')
        self.assertTrue(usr1)
        self.assertEqual(usr1.name, 'frida')
        self.assertEqual(len(usr1.groups), 1)
        self.assertEqual(usr1.groups[0].name, 'Party Edit Fields')

        # user #2 - no group
        usr2 = create_trytonuser('diego', 'Test1234', None)
        self.assertTrue(usr2)
        self.assertEqual(usr2.name, 'diego')
        self.assertEqual(len(usr2.groups), 0)
                
        # create party
        p1 = Party(
                name='Diego',
                code='1234',
                addresses=[
                        Address(
                            name='blng1',
                            street='Painter 1',
                        )
                    ],
                contact_mechanisms=[
                        Contact(
                            type = 'phone',
                            value = '0123456',
                            name = 'Phone',
                        ),
                    ],
            )
        p1.save()
        p_lst = Party.search([])
        self.assertEqual(len(p_lst), 1)
        self.assertEqual(p_lst[0].name, 'Diego')
        self.assertEqual(p_lst[0].addresses[0].name, 'blng1')
        self.assertEqual(p_lst[0].contact_mechanisms[0].value, '0123456')
        
        with transaction.set_user(usr1.id):
            with transaction.set_context({'groups': [x.id for x in usr1.groups]}):
                p2_lst1 = Party.search([])
                self.assertEqual(len(p2_lst1), 1)
                self.assertEqual(p2_lst1[0].get_code_readonly(''), False)
                self.assertEqual(p2_lst1[0].code_readonly, False)

        with transaction.set_user(usr2.id):
            with transaction.set_context({'groups': [x.id for x in usr2.groups]}):
                p2_lst2 = Party.search([])
                self.assertEqual(len(p2_lst2), 1)
                self.assertEqual(p2_lst2[0].get_code_readonly(''), True)
                self.assertEqual(p2_lst2[0].code_readonly, True)

# end ProductTestCase
