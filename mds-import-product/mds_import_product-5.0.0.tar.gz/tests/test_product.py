# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

from datetime import timedelta
from trytond.tests.test_tryton import ModuleTestCase, with_transaction
from trytond.pool import Pool
from trytond.transaction import Transaction
from trytond.exceptions import UserError
from decimal import Decimal



class ProductTestCase(ModuleTestCase):
    'Test product module'
    module = 'import_product'
    
    @with_transaction()
    def test_importwizard(self):
        """ run wizard to import some products
        """
        pool = Pool()
        Configuration = pool.get('import_product.configuration')
        ProdCategory = pool.get('product.category')
        ProdVar = pool.get('product.product')
        ImportWizard = pool.get('import_product.wizardcsvimport', type='wizard')
        CsvImportSchritt2 = pool.get('import_product.wizardcsvimport.schritt2')
        
        # create product-category
        prcat = ProdCategory(
                name = 'PrCat1',
                accounting = True,
            )
        prcat.save()
        # there should be 1x category
        prc_lst = ProdCategory.search([])
        self.assertEqual(len(prc_lst), 1)
        self.assertEqual(prc_lst[0].name, 'PrCat1')
        self.assertEqual(prc_lst[0].accounting, True)
        
        # store config
        cfg1 = Configuration(
                prodcat = prc_lst[0],
            )
        cfg1.save()
        cfg2 = Configuration.get_singleton()
        self.assertEqual(cfg2.prodcat.name, 'PrCat1')
        
        # start wizard
        (sess_id, start_state, end_state) = ImportWizard.create()
        w_obj = ImportWizard(sess_id)
        self.assertEqual(start_state, 'schritt1')

        # run start
        result = ImportWizard.execute(sess_id, {}, start_state)
        self.assertEqual(list(result.keys()), ['view'])
        self.assertTrue('csvtext' not in result['view']['defaults'].keys())
        self.assertTrue('attribute_set' not in result['view']['defaults'].keys())
        self.assertEqual(result['view']['defaults']['account_cat'], prc_lst[0].id)

        r1 = {}
        for i in result['view']['defaults'].keys():
            setattr(w_obj.schritt1, i, result['view']['defaults'][i])
            r1[i] = result['view']['defaults'][i]

        # insert csv-data
        t1 = '''"ProdName,C";"ProdNr,C";"ListPrice,N,10,2";"Unit,C"
"Product01";100;1.45;"kg"
"Product02";101;2;"l"'''
        r1['csvtext'] = t1
        self.assertEqual(r1['csvtext'], t1)
        self.assertTrue('attribute_set' not in r1.keys())
        self.assertEqual(r1['account_cat'], prc_lst[0].id)

        # run transition to selection of column
        result = ImportWizard.execute(sess_id,
                    {start_state: r1},
                    'selectcolumns')
        self.assertEqual(list(result.keys()), ['view'])
        self.assertEqual(result['view']['defaults']['sp01i'], 'ProdName,C')
        self.assertEqual(result['view']['defaults']['sp01t'], '0')
        self.assertEqual(result['view']['defaults']['sp02i'], 'ProdNr,C')
        self.assertEqual(result['view']['defaults']['sp02t'], '0')
        self.assertEqual(result['view']['defaults']['sp03i'], 'ListPrice,N,10,2')
        self.assertEqual(result['view']['defaults']['sp03t'], '0')
        self.assertEqual(result['view']['defaults']['sp04i'], 'Unit,C')
        self.assertEqual(result['view']['defaults']['sp04t'], '0')

        # fields of type Product should be in selection
        sel_list = CsvImportSchritt2.get_prodsel()
        sel_fields = []
        for i in sel_list:
            (fid, ftxt) = i
            sel_fields.append(fid)

        # check existence of fields
        self.assertEqual(sel_fields.count('0'), 1)
        self.assertEqual(sel_fields.count('account_category'), 1)
        self.assertEqual(sel_fields.count('code'), 1)
        self.assertEqual(sel_fields.count('consumable'), 1)
        self.assertEqual(sel_fields.count('cost_price'), 1)
        self.assertEqual(sel_fields.count('cost_price_method'), 1)
        self.assertEqual(sel_fields.count('default_uom'), 1)
        self.assertEqual(sel_fields.count('description'), 1)
        self.assertEqual(sel_fields.count('list_price'), 1)
        self.assertEqual(sel_fields.count('name'), 1)

        r1 = {}
        for i in result['view']['defaults'].keys():
            setattr(w_obj.schritt1, i, result['view']['defaults'][i])
            r1[i] = result['view']['defaults'][i]

        # select fields and columns
        r1['sp01t'] = 'name'
        r1['sp02t'] = 'code'
        r1['sp03t'] = 'list_price'
        r1['sp04t'] = 'default_uom'

        # run transition to create products
        result = ImportWizard.execute(sess_id,
                    {'schritt2': r1},
                    'importieren')
        self.assertEqual(result, {})    # 'end'
        ImportWizard.delete(sess_id)
        
        # we should have two products (+variants)
        pr_lst = ProdVar.search([])
        self.assertEqual(len(pr_lst), 2)
        
        # check product 1
        pr1 = ProdVar.search([('name', '=', 'Product01')])
        self.assertEqual(len(pr1), 1)
        self.assertEqual(pr1[0].name, 'Product01')
        self.assertEqual(pr1[0].code, '100')
        self.assertEqual(pr1[0].list_price, Decimal('1.45'))
        self.assertEqual(pr1[0].default_uom.symbol, 'kg')

        # check product 2
        pr2 = ProdVar.search([('name', '=', 'Product02')])
        self.assertEqual(len(pr2), 1)
        self.assertEqual(pr2[0].name, 'Product02')
        self.assertEqual(pr2[0].code, '101')
        self.assertEqual(pr2[0].list_price, Decimal('2.00'))
        self.assertEqual(pr2[0].default_uom.symbol, 'l')

    @with_transaction()
    def test_importwizard_attr(self):
        """ run wizard to import some products, with attributes
        """
        pool = Pool()
        Configuration = pool.get('import_product.configuration')
        ProdCategory = pool.get('product.category')
        ProdVar = pool.get('product.product')
        ImportWizard = pool.get('import_product.wizardcsvimport', type='wizard')
        CsvImportSchritt2 = pool.get('import_product.wizardcsvimport.schritt2')
        ProdAttrSet = pool.get('product.attribute.set')
        ProdAttr = pool.get('product.attribute')
        
        # create product-category
        prcat = ProdCategory(
                name = 'PrCat1',
                accounting = True,
            )
        prcat.save()
        # there should be 1x category
        prc_lst = ProdCategory.search([])
        self.assertEqual(len(prc_lst), 1)
        self.assertEqual(prc_lst[0].name, 'PrCat1')
        self.assertEqual(prc_lst[0].accounting, True)
        
        # create attribute set
        pattr_set = ProdAttrSet(
                name = 'Attr1',
                attributes = [
                        ProdAttr(
                                string = 'Txt1',
                                name = 'txt1',
                                type_ = 'char',
                            ),
                        ProdAttr(
                                string = 'Numbr1',
                                name = 'numbr1',
                                type_ = 'numeric',
                                digits = 2,
                            ),
                    ]
            )
        pattr_set.save()
        # check attribute set
        attr_lst = ProdAttrSet.search([])
        self.assertEqual(len(attr_lst), 1)
        self.assertEqual(attr_lst[0].name, 'Attr1')
        self.assertEqual(len(attr_lst[0].attributes), 2)

        attr_lst2 = ProdAttr.search([])
        self.assertEqual(len(attr_lst2), 2)
        
        # check attr 1
        attr_1 = ProdAttr.search([('name', '=', 'txt1')])
        self.assertEqual(len(attr_1), 1)
        self.assertEqual(attr_1[0].string, 'Txt1')
        self.assertEqual(attr_1[0].name, 'txt1')
        self.assertEqual(attr_1[0].type_, 'char')

        # check attr 2
        attr_2 = ProdAttr.search([('name', '=', 'numbr1')])
        self.assertEqual(len(attr_2), 1)
        self.assertEqual(attr_2[0].string, 'Numbr1')
        self.assertEqual(attr_2[0].name, 'numbr1')
        self.assertEqual(attr_2[0].type_, 'numeric')
        self.assertEqual(attr_2[0].digits, 2)
        
        # store config
        cfg1 = Configuration(
                prodcat = prc_lst[0],
                attribute_set = attr_lst[0],
            )
        cfg1.save()
        cfg2 = Configuration.get_singleton()
        self.assertEqual(cfg2.prodcat.name, 'PrCat1')
        self.assertEqual(cfg2.attribute_set.name, 'Attr1')
        
        # start wizard
        (sess_id, start_state, end_state) = ImportWizard.create()
        w_obj = ImportWizard(sess_id)
        self.assertEqual(start_state, 'schritt1')

        # run start
        result = ImportWizard.execute(sess_id, {}, start_state)
        self.assertEqual(list(result.keys()), ['view'])
        self.assertTrue('csvtext' not in result['view']['defaults'].keys())
        self.assertEqual(result['view']['defaults']['attribute_set'], attr_lst[0].id)
        self.assertEqual(result['view']['defaults']['account_cat'], prc_lst[0].id)

        r1 = {}
        for i in result['view']['defaults'].keys():
            setattr(w_obj.schritt1, i, result['view']['defaults'][i])
            r1[i] = result['view']['defaults'][i]

        # insert csv-data
        t1 = '''"ProdName,C";"ProdNr,C";"ListPrice,N,10,2";"Unit,C";"CostPrice,N,10,2";"Info2,C"
"Product01";100;1.45;"kg";1.10;"some info text"
"Product02";101;2;"l";1.21;"more text"'''
        r1['csvtext'] = t1
        self.assertEqual(r1['csvtext'], t1)
        self.assertEqual(r1['attribute_set'], attr_lst[0].id)
        self.assertEqual(r1['account_cat'], prc_lst[0].id)

        # run transition to selection of column
        result = ImportWizard.execute(sess_id,
                    {start_state: r1},
                    'selectcolumns')
        self.assertEqual(list(result.keys()), ['view'])
        self.assertEqual(result['view']['defaults']['sp01i'], 'ProdName,C')
        self.assertEqual(result['view']['defaults']['sp01t'], '0')
        self.assertEqual(result['view']['defaults']['sp02i'], 'ProdNr,C')
        self.assertEqual(result['view']['defaults']['sp02t'], '0')
        self.assertEqual(result['view']['defaults']['sp03i'], 'ListPrice,N,10,2')
        self.assertEqual(result['view']['defaults']['sp03t'], '0')
        self.assertEqual(result['view']['defaults']['sp04i'], 'Unit,C')
        self.assertEqual(result['view']['defaults']['sp04t'], '0')
        self.assertEqual(result['view']['defaults']['sp05i'], 'CostPrice,N,10,2')
        self.assertEqual(result['view']['defaults']['sp05t'], '0')
        self.assertEqual(result['view']['defaults']['sp06i'], 'Info2,C')
        self.assertEqual(result['view']['defaults']['sp06t'], '0')

        # fields of type Product should be in selection
        sel_list = CsvImportSchritt2.get_prodsel()
        sel_fields = []
        for i in sel_list:
            (fid, ftxt) = i
            sel_fields.append(fid)

        # check existence of fields
        # column-fields
        self.assertEqual(sel_fields.count('0'), 1)
        self.assertEqual(sel_fields.count('account_category'), 1)
        self.assertEqual(sel_fields.count('code'), 1)
        self.assertEqual(sel_fields.count('consumable'), 1)
        self.assertEqual(sel_fields.count('cost_price'), 1)
        self.assertEqual(sel_fields.count('cost_price_method'), 1)
        self.assertEqual(sel_fields.count('default_uom'), 1)
        self.assertEqual(sel_fields.count('description'), 1)
        self.assertEqual(sel_fields.count('list_price'), 1)
        self.assertEqual(sel_fields.count('name'), 1)
        # attribute-fields
        self.assertEqual(sel_fields.count('txt1'), 1)   
        self.assertEqual(sel_fields.count('numbr1'), 1)

        r1 = {}
        for i in result['view']['defaults'].keys():
            setattr(w_obj.schritt1, i, result['view']['defaults'][i])
            r1[i] = result['view']['defaults'][i]

        # select fields and columns
        r1['sp01t'] = 'name'
        r1['sp02t'] = 'code'
        r1['sp03t'] = 'list_price'
        r1['sp04t'] = 'default_uom'
        r1['sp05t'] = 'numbr1'
        r1['sp06t'] = 'txt1'

        # run transition to create products
        result = ImportWizard.execute(sess_id,
                    {'schritt2': r1},
                    'importieren')
        self.assertEqual(result, {})    # 'end'
        ImportWizard.delete(sess_id)
        
        # we should have two products (+variants)
        pr_lst = ProdVar.search([])
        self.assertEqual(len(pr_lst), 2)
        
        # check product 1
        pr1 = ProdVar.search([('name', '=', 'Product01')])
        self.assertEqual(len(pr1), 1)
        self.assertEqual(pr1[0].name, 'Product01')
        self.assertEqual(pr1[0].code, '100')
        self.assertEqual(pr1[0].list_price, Decimal('1.45'))
        self.assertEqual(pr1[0].default_uom.symbol, 'kg')
        self.assertEqual(pr1[0].attributes['numbr1'], Decimal('1.10'))
        self.assertEqual(pr1[0].attributes['txt1'], 'some info text')

        # check product 2
        pr2 = ProdVar.search([('name', '=', 'Product02')])
        self.assertEqual(len(pr2), 1)
        self.assertEqual(pr2[0].name, 'Product02')
        self.assertEqual(pr2[0].code, '101')
        self.assertEqual(pr2[0].list_price, Decimal('2.00'))
        self.assertEqual(pr2[0].default_uom.symbol, 'l')
        self.assertEqual(pr2[0].attributes['numbr1'], Decimal('1.21'))
        self.assertEqual(pr2[0].attributes['txt1'], 'more text')

# end ProductTestCase
