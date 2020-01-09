# -*- coding: utf-8 -*-
# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.


from trytond.model import ModelView, ModelSQL, fields
from trytond.pool import Pool, PoolMeta
from trytond.wizard import Wizard, StateTransition, StateView, Button, StateAction
from trytond.transaction import Transaction
from trytond.pyson import Eval
from csv_reader import import_csv_file
from trytond.modules.product import TemplateFunction
from decimal import Decimal
from datetime import datetime

__all__ = ['CsvImportWizard']
__metaclass__ = PoolMeta


M2O_SEARCH = {
    'product.uom': 'symbol'
    }


def get_translation(msg_id, msg_type, msg_source):
    """ get translation in target-language
    """
    Translation = Pool().get('ir.translation')
    context = Transaction().context

    txt1 = msg_source
    tr_lst = Translation.search([
                ('name', '=', msg_id), 
                ('type', '=', msg_type),
                ('src', '=', msg_source),
                ('lang', '=', context.get('language', 'en')),
                ])
    if len(tr_lst) == 1:
        txt1 = tr_lst[0].value

    return txt1

# end get_translation


class CsvImportSchritt1(ModelView):
    'CSV-import - Schritt 1'
    __name__ = 'import_product.wizardcsvimport.schritt1'
    
    csvtext = fields.Binary(string=u'CSV-Datei', required=True)
    account_cat = fields.Many2One(model_name='product.category', string='Account Category',
        domain=[('accounting', '=', True)])
    attribute_set = fields.Many2One('product.attribute.set', 'Attribute Set',
        help="Select a set of attributes to apply on the variants.", readonly=True)

# end CsvImportSchritt1


SCHRITT2_NUM_COLS = 20
SEL_DONTUSED = '0'
TXT_DONTUSED = '-- / --'

class CsvImportSchritt2(ModelView):
    'CSV-import - Schritt 2'
    __name__ = 'import_product.wizardcsvimport.schritt2'
        
    sp01i = fields.Char(string=u'01', help=u'Content of column 1', readonly=True,
            states={'invisible': Eval('sp01i', '') == '',})
    sp01t = fields.Selection(string=u'Field Column 1', help=u'Field of column 1', selection='get_prodsel',
            states={
                'required': Eval('sp01i', '') != '',
                'invisible': Eval('sp01i', '') == '',
            }, depends=['sp01i'])

    sp02i = fields.Char(string=u'02', help=u'Content of column 2', readonly=True,
            states={'invisible': Eval('sp02i', '') == '',})
    sp02t = fields.Selection(string=u'Field Column 2', help=u'Field of column 2', selection='get_prodsel',
            states={
                'required': Eval('sp02i', '') != '',
                'invisible': Eval('sp02i', '') == '',
            }, depends=['sp02i'])

    sp03i = fields.Char(string=u'03', help=u'Content of column 3', readonly=True,
            states={'invisible': Eval('sp03i', '') == '',})
    sp03t = fields.Selection(string=u'Field Column 3', help=u'Field of column 3', selection='get_prodsel',
            states={
                'required': Eval('sp03i', '') != '',
                'invisible': Eval('sp03i', '') == '',
            }, depends=['sp03i'])


    sp04i = fields.Char(string=u'04', help=u'Content of column 4', readonly=True,
            states={'invisible': Eval('sp03i', '') == '',})
    sp04t = fields.Selection(string=u'Field Column 4', help=u'Field of column 4', selection='get_prodsel',
            states={
                'required': Eval('sp04i', '') != '',
                'invisible': Eval('sp04i', '') == '',
            }, depends=['sp04i'])

    sp05i = fields.Char(string=u'05', help=u'Content of column 5', readonly=True,
            states={'invisible': Eval('sp05i', '') == '',})
    sp05t = fields.Selection(string=u'Field Column 5', help=u'Field of column 5', selection='get_prodsel',
            states={
                'required': Eval('sp05i', '') != '',
                'invisible': Eval('sp05i', '') == '',
            }, depends=['sp05i'])

    sp06i = fields.Char(string=u'06', help=u'Content of column 6', readonly=True,
            states={'invisible': Eval('sp05i', '') == '',})
    sp06t = fields.Selection(string=u'Field Column 6', help=u'Field of column 6', selection='get_prodsel',
            states={
                'required': Eval('sp06i', '') != '',
                'invisible': Eval('sp06i', '') == '',
            }, depends=['sp06i'])

    sp07i = fields.Char(string=u'07', help=u'Content of column 7', readonly=True,
            states={'invisible': Eval('sp07i', '') == '',})
    sp07t = fields.Selection(string=u'Field Column 7', help=u'Field of column 7', selection='get_prodsel',
            states={
                'required': Eval('sp07i', '') != '',
                'invisible': Eval('sp07i', '') == '',
            }, depends=['sp07i'])

    sp08i = fields.Char(string=u'08', help=u'Content of column 8', readonly=True,
            states={'invisible': Eval('sp08i', '') == '',})
    sp08t = fields.Selection(string=u'Field Column 8', help=u'Field of column 8', selection='get_prodsel',
            states={
                'required': Eval('sp08i', '') != '',
                'invisible': Eval('sp08i', '') == '',
            }, depends=['sp08i'])

    sp09i = fields.Char(string=u'09', help=u'Content of column 9', readonly=True,
            states={'invisible': Eval('sp09i', '') == '',})
    sp09t = fields.Selection(string=u'Field Column 9', help=u'Field of column 9', selection='get_prodsel',
            states={
                'required': Eval('sp09i', '') != '',
                'invisible': Eval('sp09i', '') == '',
            }, depends=['sp09i'])

    sp10i = fields.Char(string=u'10', help=u'Content of column 10', readonly=True,
            states={'invisible': Eval('sp10i', '') == '',})
    sp10t = fields.Selection(string=u'Field Column 10', help=u'Field of column 10', selection='get_prodsel',
            states={
                'required': Eval('sp10i', '') != '',
                'invisible': Eval('sp10i', '') == '',
            }, depends=['sp10i'])

    sp11i = fields.Char(string=u'11', help=u'Content of column 11', readonly=True,
            states={'invisible': Eval('sp11i', '') == '',})
    sp11t = fields.Selection(string=u'Field Column 11', help=u'Field of column 11', selection='get_prodsel',
            states={
                'required': Eval('sp11i', '') != '',
                'invisible': Eval('sp11i', '') == '',
            }, depends=['sp11i'])

    sp12i = fields.Char(string=u'12', help=u'Content of column 12', readonly=True,
            states={'invisible': Eval('sp12i', '') == '',})
    sp12t = fields.Selection(string=u'Field Column 12', help=u'Field of column 12', selection='get_prodsel',
            states={
                'required': Eval('sp12i', '') != '',
                'invisible': Eval('sp12i', '') == '',
            }, depends=['sp12i'])

    sp13i = fields.Char(string=u'13', help=u'Content of column 13', readonly=True,
            states={'invisible': Eval('sp13i', '') == '',})
    sp13t = fields.Selection(string=u'Field Column 13', help=u'Field of column 13', selection='get_prodsel',
            states={
                'required': Eval('sp13i', '') != '',
                'invisible': Eval('sp13i', '') == '',
            }, depends=['sp13i'])

    sp14i = fields.Char(string=u'14', help=u'Content of column 14', readonly=True,
            states={'invisible': Eval('sp14i', '') == '',})
    sp14t = fields.Selection(string=u'Field Column 14', help=u'Field of column 14', selection='get_prodsel',
            states={
                'required': Eval('sp14i', '') != '',
                'invisible': Eval('sp14i', '') == '',
            }, depends=['sp14i'])

    sp15i = fields.Char(string=u'15', help=u'Content of column 15', readonly=True,
            states={'invisible': Eval('sp15i', '') == '',})
    sp15t = fields.Selection(string=u'Field Column 15', help=u'Field of column 15', selection='get_prodsel',
            states={
                'required': Eval('sp15i', '') != '',
                'invisible': Eval('sp15i', '') == '',
            }, depends=['sp15i'])

    sp16i = fields.Char(string=u'16', help=u'Content of column 16', readonly=True,
            states={'invisible': Eval('sp16i', '') == '',})
    sp16t = fields.Selection(string=u'Field Column 16', help=u'Field of column 16', selection='get_prodsel',
            states={
                'required': Eval('sp16i', '') != '',
                'invisible': Eval('sp16i', '') == '',
            }, depends=['sp16i'])

    sp17i = fields.Char(string=u'17', help=u'Content of column 17', readonly=True,
            states={'invisible': Eval('sp17i', '') == '',})
    sp17t = fields.Selection(string=u'Field Column 17', help=u'Field of column 17', selection='get_prodsel',
            states={
                'required': Eval('sp17i', '') != '',
                'invisible': Eval('sp17i', '') == '',
            }, depends=['sp17i'])

    sp18i = fields.Char(string=u'18', help=u'Content of column 18', readonly=True,
            states={'invisible': Eval('sp18i', '') == '',})
    sp18t = fields.Selection(string=u'Field Column 18', help=u'Field of column 18', selection='get_prodsel',
            states={
                'required': Eval('sp18i', '') != '',
                'invisible': Eval('sp18i', '') == '',
            }, depends=['sp18i'])

    sp19i = fields.Char(string=u'19', help=u'Content of column 19', readonly=True,
            states={'invisible': Eval('sp19i', '') == '',})
    sp19t = fields.Selection(string=u'Field Column 19', help=u'Field of column 19', selection='get_prodsel',
            states={
                'required': Eval('sp19i', '') != '',
                'invisible': Eval('sp19i', '') == '',
            }, depends=['sp19i'])

    sp20i = fields.Char(string=u'20', help=u'Content of column 20', readonly=True,
            states={'invisible': Eval('sp20i', '') == '',})
    sp20t = fields.Selection(string=u'Field Column 20', help=u'Field of column 20', selection='get_prodsel',
            states={
                'required': Eval('sp20i', '') != '',
                'invisible': Eval('sp20i', '') == '',
            }, depends=['sp20i'])

    @classmethod
    def get_prodsel(cls):
        """ get list of fields an string og type 'product.product'
        """
        pool = Pool()
        Product = pool.get('product.product')
        ProductAttr = pool.get('product.attribute')
        
        field_list = cls.get_product_fields()
        l1 = [(SEL_DONTUSED, TXT_DONTUSED)]
        usd1 = []
        for i in field_list:
            (fnam, ftyp, fmodl, fpar) = i
            
            use_name = '%s-%s' % (fnam, fmodl)
            if use_name in usd1:
                continue
            usd1.append(use_name)
            
            fdesc = fnam
            
            if fmodl == 'product.attribute':
                attrlst = ProductAttr.search([('name', '=', fnam), ('type_', '=', ftyp)])
                if len(attrlst) == 1:
                    fdesc = '%s [Attr]' % (attrlst[0].string)
            else :
                if fnam in Product._fields.keys():
                    fdesc = get_translation('product.product,%s' % fnam, 'field', \
                        Product._fields[fnam].string)

            l1.append((fnam, '%s [%s]' % (fdesc, ftyp)))
        return l1

    @classmethod
    def get_product_fields(cls):
        """ get list of fields in product-type
        """
        pool = Pool()
        ProdVar = pool.get('product.product')
        ProdTempl = pool.get('product.template')
        Config = pool.get('import_product.configuration')
        
        ignore_types = ['one2many', 'many2many']
        ignore_names = ['attribute_set', 'list_prices', 'active']
        incl_fields = ['account_category', 'default_uom']
        l1 = []
    
        for k in [(ProdTempl, 'product.template'), (ProdVar, 'product.product')]:
            (k1, k2) = k
            
            for i in k1._fields.keys():
                # ignore TemplateFunction
                if isinstance(k1._fields[i], TemplateFunction):
                    continue

                if not k1._fields[i].name in incl_fields:
                    # ignore Function-fields
                    if isinstance(k1._fields[i], fields.Function):
                        if not isinstance(k1._fields[i], TemplateFunction) and \
                            not isinstance(k1._fields[i], fields.MultiValue):
                            continue
                    # ignore some fields
                    if k1._fields[i]._type in ignore_types:
                        continue
                    if k1._fields[i].name in ignore_names:
                        continue
                    # ignore columns without field
                    if not isinstance(k1._fields[i], fields.Char) and \
                        not isinstance(k1._fields[i], fields.Boolean):
                        if not hasattr(k1._fields[i], '_field'):
                            continue
    
                modl_name = getattr(k1._fields[i], 'model_name', '-')
                l1.append((k1._fields[i].name, k1._fields[i]._type, modl_name, k2))
        
        # add fields from attribute-set
        cfg1 = Config.get_singleton()
        if hasattr(cfg1, 'attribute_set'):
            if not isinstance(cfg1.attribute_set, type(None)):
                for i in cfg1.attribute_set.attributes:
                    l1.append((i.name, i.type_, 'product.attribute', 'product.product'))
        return l1

# end CsvImportSchritt2


class CsvImportWizard(Wizard):
    'Import CSV-File'
    __name__ = 'import_product.wizardcsvimport'
    
    start_state = 'schritt1'
    schritt1 = StateView(model_name='import_product.wizardcsvimport.schritt1', \
                        view='import_product.wizardcsvimport_schritt1_form', \
                        buttons=[Button(string=u'Abbruch', state='end', icon='tryton-cancel'), 
                                 Button(string=u'Select columns 1', 
                                        state='selectcolumns', icon='tryton-forward'),
                                ])
    schritt2 = StateView(model_name='import_product.wizardcsvimport.schritt2', \
                        view='import_product.wizardcsvimport_schritt2_form', \
                        buttons=[Button(string=u'Abbruch', state='end', icon='tryton-cancel'), 
                                 Button(string=u'Back', 
                                        state='schritt1', icon='tryton-back'),
                                 Button(string=u'Import products', 
                                        state='importieren', icon='tryton-forward'),
                                ])

    selectcolumns = StateTransition()
    importieren = StateTransition()

    @classmethod
    def __setup__(cls):
        super(CsvImportWizard, cls).__setup__()
        cls._error_messages.update({
            'wizimp_cfgprodcat': (u"Configuration: value 'Product Category' must be set"),
            'wizimp_toomanycolumn': (u"Import: too many columns in csv-file."),
            'wizimp_m2o_notmatch': (u"Import: value '%s' not exactly match to column '%s' in table '%s', found %s items"),
        })

    def default_schritt1(self, fields):
        """ fill fields in step 1
        """
        erg1 = {}

        pool = Pool()
        Config = pool.get('import_product.configuration')
        cfg1 = Config.get_singleton()
        
        if not hasattr(cfg1, 'prodcat'):
            self.raise_user_error('wizimp_cfgprodcat')
        if isinstance(cfg1.prodcat, type(None)):
            self.raise_user_error('wizimp_cfgprodcat')
        
        if not hasattr(self.schritt1, 'account_cat'):
            self.schritt1.account_cat = cfg1.prodcat
        if isinstance(self.schritt1.account_cat, type(None)):
            self.schritt1.account_cat = cfg1.prodcat

        if hasattr(cfg1, 'attribute_set'):
            self.schritt1.attribute_set = cfg1.attribute_set

        l1 = ['csvtext', 'account_cat', 'attribute_set']
        for i in l1:
            if hasattr(self.schritt1, i):
                v1 = getattr(self.schritt1, i)
                if not isinstance(v1, type(None)):
                    erg1[i] = v1
                    
            if i in ['account_cat', 'attribute_set']:
                if i in erg1.keys():
                    if not isinstance(erg1[i], type(1)):
                        erg1[i] = erg1[i].id

        return erg1

    def default_schritt2(self, fields):
        """ fill fields in step 2
        """
        erg1 = {}

        pool = Pool()
        ProdTempl = pool.get('product.template')
        
        l1 = []
        for i in range(SCHRITT2_NUM_COLS):
            l1.append('sp%02di' % (i + 1))
            l1.append('sp%02dt' % (i + 1))

        for i in l1:
            if hasattr(self.schritt2, i):
                v1 = getattr(self.schritt2, i)
                if not isinstance(v1, type(None)):
                    erg1[i] = v1
        return erg1

    def transition_selectcolumns(self):
        """ read csv-file, fill list of detected columns,
            step 1 --> step 2
        """
        (l1, fieldnames, infotxt) = import_csv_file(self.schritt1.csvtext, 
            firstline=True, decimalremove=[])

        # fill lines 
        used1 = []
        formvar = self.schritt2
        for i in range(SCHRITT2_NUM_COLS):
            if i < len(fieldnames):
                setattr(self.schritt2, 'sp%02dt' % (i + 1), SEL_DONTUSED)
                setattr(self.schritt2, 'sp%02di' % (i + 1), fieldnames[i])
            else :
                break
        return 'schritt2'

    def transition_importieren(self):
        """ read csv-file, add party-objects
        """
        pool = Pool()
        ProdTempl = pool.get('product.template')
        ProdVar = pool.get('product.product')
        Schritt2 = pool.get('import_product.wizardcsvimport.schritt2')

        # list of fields
        field_list = Schritt2.get_product_fields()
        fields_dict = {}
        for i in field_list:
            (fnam, ftyp, fmodl, fpar) = i
            if not fnam in fields_dict.keys():
                fields_dict[fnam] = {'typ': ftyp, 'modl': fmodl, 'fpar': fpar}
            
        def get_colname_wotype(colname):
            c1 = colname.split(',')
            return c1[0]

        def add_value_to_obj(linedata, obj1, obj_modl):
            for k in range(SCHRITT2_NUM_COLS):
                sp_prd = getattr(self.schritt2, 'sp%02dt' % (k + 1), SEL_DONTUSED)    # selection for product-field
                sp_csv = getattr(self.schritt2, 'sp%02di' % (k + 1), '')              # name of column in csv-file

                if (sp_prd == SEL_DONTUSED) or isinstance(sp_prd, type(None)):
                    continue

                sp2 = get_colname_wotype(sp_csv)

                # dont add value to wrong model
                if fields_dict[sp_prd]['fpar'] != obj_modl:
                    continue

                if fields_dict[sp_prd]['modl'] == 'product.attribute':
                    if isinstance(obj1.attributes, type(None)):
                        obj1.attributes = {}
                    if fields_dict[sp_prd]['typ'] == 'float':
                        obj1.attributes[sp_prd] = float(linedata[sp2])
                    elif fields_dict[sp_prd]['typ'] == 'integer':
                        obj1.attributes[sp_prd] = int(linedata[sp2])
                    elif fields_dict[sp_prd]['typ'] == 'numeric':
                        obj1.attributes[sp_prd] = Decimal(linedata[sp2])
                    elif fields_dict[sp_prd]['typ'] == 'char':
                        obj1.attributes[sp_prd] = linedata[sp2]
                    elif fields_dict[sp_prd]['typ'] == 'datetime':
                        obj1.attributes[sp_prd] = datetime.strptime(linedata[sp2], '%Y-%m-%d %H:%M:%S')
                    elif fields_dict[sp_prd]['typ'] == 'date':
                        obj1.attributes[sp_prd] = datetime.strptime(linedata[sp2], '%Y-%m-%d')
                    elif fields_dict[sp_prd]['typ'] == 'boolean':
                        obj1.attributes[sp_prd] = linedata[sp2]
                    else :
                        obj1.attributes[sp_prd] = linedata[sp2]
                else :
                    if fields_dict[sp_prd]['typ'] == 'many2one':
                        # link existing record to product
                        TabObj = pool.get(fields_dict[sp_prd]['modl'])
                        # search in table for value from csv-file
                        # prefer search-column from 'M2O_SEARCH'
                        qu_col = M2O_SEARCH.get(fields_dict[sp_prd]['modl'], 'name')
                        m2o = TabObj.search([(qu_col, '=', linedata[sp2])])
                        if len(m2o) != 1:
                            self.raise_user_error('wizimp_m2o_notmatch', \
                                (linedata[sp2], qu_col, fields_dict[sp_prd]['modl'], len(m2o)))
                        setattr(obj1, sp_prd, m2o[0])
                    else :
                        setattr(obj1, sp_prd, linedata[sp2])
            return obj1
            
        (l1, fieldnames, infotxt) = import_csv_file(self.schritt1.csvtext, 
            firstline=True, decimalremove=[])
            
        cnt1 = 0
        # import products
        for i in l1:
            p1 = ProdTempl()
            p2 = ProdVar()

            p1.account_category = self.schritt1.account_cat
            p1 = add_value_to_obj(i, p1, 'product.template')

            if not isinstance(self.schritt1.attribute_set, type(None)):
                p1.attribute_set = self.schritt1.attribute_set
            p1.products = [p2]
            p1.save()

            p2a = ProdVar.search([('template', '=', p1.id)])
            if len(p2a) == 1:
                p2a = p2a[0]
            else :
                raise ValueError('ProductVariant id=%s not fount' % (p1.id))

            p2a = add_value_to_obj(i, p2a, 'product.product')
            p2a.save()

        return 'end'

# end CsvImportWizard
