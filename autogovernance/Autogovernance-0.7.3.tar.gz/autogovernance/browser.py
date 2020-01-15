# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 16:25:41 2019

@author: LP885RH
"""

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.action_chains import ActionChains
from element import Element
from element import QR_object
from element import Attribute
from element import BusinessTerm
import sys
import tables
import logging

def init_autonav():
    #Iniciar driver de Chrome para la navegación
    options = Options() 
    options.add_argument("--start-maximized")
    try:
        return webdriver.Chrome(options=options)
    except:
        print("There is a driver error")
        sys.exit()



def wait(driver):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "progress-bar")))
        WebDriverWait(driver, 10).until_not(EC.presence_of_element_located((By.CLASS_NAME, "progress-bar")))
    except:
        pass

def check_changes(driver, table, field):
    try:
        cont = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "foreground-notification__content")))
        span = cont.find_element_by_tag_name("span")
        print('Status: ' + span.text)
        print(str(table) + ' : '+ str(field))
        """if span.text=="The asset has been successfully updated ":
            print('OK')
        else:
            print('KO')"""
    except:
        print('Status: There is a problem to update')
        print(str(table) + ' : '+ str(field))

        
def login(driver, url, tenant, user, password):
    """
    DOC String

    """
    t = tenant
    u = user
    p = password
    try:
        driver.get(url)
        tenant = driver.find_element_by_id("tenant")
        user = driver.find_element_by_id("username")
        passw = driver.find_element_by_id("password")
        button = driver.find_element_by_id("login-button")

        tenant.send_keys(t)
        user.send_keys(u)
        passw.send_keys(p)
        button.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='sth-header-logo']")))
        
    except:
        print('There is a login error.')
        sys.exit()

def nav_fields(driver, fields, b_fields, b_attrib, b_erase_attrib, b_busi_terms):
    #LOGGING CAMPOS
    #logging.basicConfig(filename="field_log.log", level=logging.INFO)
    formatter = logging.Formatter('%(levelname)s %(message)s %(asctime)s')
    field_log = logging.getLogger('field')
    fh = logging.FileHandler('log_fields.log', mode='w+')
    fh.setFormatter(formatter)
    field_log.addHandler(fh)
    erase_log = logging.getLogger('erase')
    eh = logging.FileHandler('log_erase.log', mode='w')
    eh.setFormatter(formatter)
    erase_log.addHandler(eh)
    attr_log = logging.getLogger('attr')
    ah = logging.FileHandler('log_attr.log', mode='w')
    ah.setFormatter(formatter)
    attr_log.addHandler(ah)
    bt_log = logging.getLogger('bt')
    bh = logging.FileHandler('log_bt.log', mode='w')
    bh.setFormatter(formatter)
    bt_log.addHandler(bh)
    
    for field in fields:
        try:
            driver.get(build_route_field(field.route, field.table, field.field, 
                                         field.source))
            WebDriverWait(driver, 
                                  12).until(EC.presence_of_element_located((By.XPATH, 
                                    "//button[text()=' Edit ']"))).click()
        except:
            print("WARNING: the field '" + field.field + "' in table '" + field.table + "' doesn't exist or can't be accessed.")
            field_log.warning("Field '" + field.field + "' in table '" + field.table + "' doesn't exist or can't be accessed.")
            erase_log.warning("Field '" + field.field + "' in table '" + field.table + "' doesn't exist or can't be accessed.")
            attr_log.warning("Field '" + field.field + "' in table '" + field.table + "' doesn't exist or can't be accessed.")
            bt_log.warning("Field '" + field.field + "' in table '" + field.table + "' doesn't exist or can't be accessed.")
            continue
        
        if b_fields:
            try:
                fill_fields(driver, field)
            except:
                print("WARNING: the field '" + field.field + "' in table '" + field.table + "' couldn't be updated.")
                field_log.warning("Field '" + field.field + "' in table '" + field.table + "' couldn't be updated.")
            
        if b_erase_attrib:
            try:
                rm_atr(driver)
            except:
                print("WARNING: the attributes of field '" + field.field + "' in table '" + field.table + "' couldn't be erased.")
                erase_log.warning("Attributes of field '" + field.field + "' in table '" + field.table + "' couldn't be erased.")
            
        if b_attrib:
            try:
                fill_attributes(driver, field)
            except:
                print("WARNING: the attributes of field '" + field.field + "' in table '" + field.table + "' couldn't be updated.")
                attr_log.warning("Attributes of field '" + field.field + "' in table '" + field.table + "' couldn't be updated.")
            
        if b_busi_terms:
            try:
                fill_business_terms(driver, field)
            except:
                print("WARNING: the business terms of field '" + field.field + "' in table '" + field.table + "' couldn't be updated.")
                bt_log.warning("Business terms of field '" + field.field + "' in table '" + field.table + "' couldn't be updated.")
                              
            
        #Guardar
        try:

            save = WebDriverWait(driver, 
                                 7).until(EC.element_to_be_clickable((By.XPATH, 
                                                                "//button[@id='save-button']")))
            save.click()

            check_changes(driver, field.table, field.field)
            wait(driver)
        except:
            field_log.warning("Field '" + field.field + "' in table '" + field.table + "' can't be updated.")
            erase_log.warning("Field '" + field.field + "' in table '" + field.table + "' can't be updated.")
            attr_log.warning("Field '" + field.field + "' in table '" + field.table + "' can't be updated.")
            bt_log.warning("Field '" + field.field + "' in table '" + field.table + "' can't be updated.")
            
            
            cancel = WebDriverWait(driver, 
                                 7).until(EC.element_to_be_clickable((By.XPATH, 
                                                                "//button[@id='cancel-button']")))
            ActionChains(driver).move_to_element(cancel)
            cancel.click()
            


def build_route_table(route, table_name, system):
    try:
        directories = route.split("/")
    except Exception as ex:
        print(ex)
        return []
    o_route = ''
    static = 'https://admin.sgcto-int.stratio.com/service/governance-ui/datastores/'
    
    #TODO: ESTO HABRÍA QUE HACERLO GENÉRICO Y PARA ELLO HABRÍA QUE INDICAR LA FUENTE EN EL EXCEL

    if system=='hdfs':
        inter = '%2F'
        o_route = static + 'hdfs?assetMetadataPath=gts-hdfs:%2F'
        for d in directories:
            o_route = o_route + inter + d
        o_route1 = o_route + '%3E%2F' + table_name + ':'
        o_route2 = o_route + '%2F' + table_name + '%3E%2F:'+ table_name + ':'
        return [o_route1, o_route2]
    elif '.' in directories[0]: #system=='postgre'
        inter = '%2F'
        o_route = static + directories[0] + '?assetMetadataPath='+ directories[0] +':%2F%2F'+ directories[1] +'%3E%2F:'
        o_route1 = o_route + table_name + ':'
        return [o_route1]
    
    
        
    else:
        print('ERROR: Sistema no previsto:', system)
        
def build_route_field(route, table_name, field, source):
    try:
        directories = route.split("/")
    except Exception as ex:
        print(ex)
        return []
    o_route = ''
    static = 'https://admin.sgcto-int.stratio.com/service/governance-ui/datastores/'
    
    if source=='hdfs':
        inter = '%2F'
        o_route = static + source + '?assetMetadataPath=gts-hdfs:%2F'
        for i, d in enumerate(directories):
            o_route = o_route + inter + d
        o_route = o_route + inter + table_name + '%3E%2F:'+table_name+':'+field+':'
   
    
    elif '.' in source:
        inter = '%2F'
        o_route = static + source + '?assetMetadataPath='+ source + ':%2F%2Fgts-oneview%3E%2F:'
        o_route = o_route + table_name + ':'+field+':'
    
    
    else:
        
        print('ERROR: Sistema fuente no previsto: ', source)
    return o_route
            
#%%

def fill_tables(driver, table_list):
    """
    Doc string
    """
    #LOGGING TABLAS
    formatter = logging.Formatter('%(levelname)s %(message)s %(asctime)s')
    table_log = logging.getLogger('tables')
    th = logging.FileHandler('log_tables.log', mode='w+')
    th.setFormatter(formatter)
    table_log.addHandler(th)
    #logging.basicConfig(filename="tables_log.log", level=logging.INFO)

    for table in table_list:
        
    
        rutas = build_route_table(table.route, table.table, table.source)
        for i, elem in enumerate(rutas):
            try:
                driver.get(elem)
                
                
                if i==0 and len(rutas)>1:
                    WebDriverWait(driver, 
                                  30).until(EC.presence_of_element_located((By.XPATH, 
                                    "//button[text()=' Edit ']"))).click()
                else:
                    WebDriverWait(driver, 
                                  30).until(EC.presence_of_element_located((By.XPATH, 
                                    "//span[text()='Actions']"))).click()
                    WebDriverWait(driver, 
                                  10).until(EC.presence_of_element_located((By.XPATH, 
                                    "//span[text()='Edit']"))).click()
                
            except Exception as ex:
                print(ex)
                print("WARNING: tabla '" + str(table.table) + "' no existe o no se puede modificar")
                table_log.warning("Tabla '" + str(table.table) + "' no existe o no se puede modificar")
                continue
                
            try:
                alias = WebDriverWait(driver, 
                                      30).until(EC.presence_of_element_located((By.XPATH, 
                                        "//input[@placeholder='Type an alias']")))
                alias.clear()
                alias.send_keys(table.table_alias)
                description = WebDriverWait(driver, 
                                            30).until(EC.presence_of_element_located((By.XPATH, 
                                              "//textarea[@placeholder='Enter description']")))
                description.clear()
                description.send_keys(table.table_description)
                WebDriverWait(driver, 
                              30).until(EC.presence_of_element_located((By.XPATH, 
                                "//button[@id='save-button']"))).click()
            except Exception as ex:
                print(ex)
                print("WARNING: The table "+ table + "could not be updated.")
                table_log.warning("The table "+ table + "could not be updated.")
                
                continue
    table_log.warning("FINISHED: Tables information updated.")
    print("FINISHED: Tables information updated.")


#%% BUSINESS TERMS
def add_business_term(driver, community, domain, data_point):
    WebDriverWait(driver, 
                  30).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 
                                                                "editable-section-header")))[0].click()
    
    #VIA DROPDOWN
    """
    c = WebDriverWait(driver, 
                      10).until(EC.presence_of_element_located((By.CLASS_NAME, 
                                                            "community-selector")))
    WebDriverWait(c, 
                  10).until(EC.presence_of_element_located((By.TAG_NAME, "span"))).click()
    
    
    WebDriverWait(driver, 
                  10).until(EC.presence_of_element_located((By.XPATH, 
                                                           "//span[text()='"+community+"')]"))).click()
    """
    """
    #driver.execute_script("document.body.style.zoom='50%'")
    try:
        html = driver.find_element_by_tag_name("html")
        html.send_keys(Keys.CONTROL, Keys.SUBTRACT)
    except Exception as ex:
        print(ex)
    """
    
    search = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
    search.send_keys(data_point)
    
    tab = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "table")))
    tbody = tab.find_element_by_tag_name('tbody')
    rows = WebDriverWait(tbody, 30).until(EC.presence_of_all_elements_located((By.TAG_NAME, "tr")))
    #tbody.find_elements_by_tag_name('tr')
    
    for row in rows:
        tags = row.find_elements_by_tag_name('label')
        fc = False
        fd = False
        for tag in tags:
            if community==tag.text:
                fc = True
            if domain==tag.text and fc:
                fd = True
            if fc and fd:
                selects = row.find_elements_by_class_name('clickable')
                select = selects[0].find_element_by_tag_name('div')
                ActionChains(driver).move_to_element(select).click(select).perform()
                break
    try:
        #driver.execute_script("document.body.style.zoom='50%'")
        footer = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "footer")))

        
        save = WebDriverWait(footer, 30).until(EC.presence_of_element_located((By.TAG_NAME, "button")))
        ActionChains(driver).move_to_element(save).click().perform()
        #save.click()

    except Exception as ex:
        print(ex)
        #TODO: buscar casuiustica que hace que esto pete
        return None
        """
        cross = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "icon-cross close-button")))
        cross.click()
        """
   
def fill_business_terms(driver, field):
    """Doc str"""
    community = field.BusinessTerm.community
    domain = field.BusinessTerm.domain
    data_point = field.BusinessTerm.data_point
    
    if not community=='' or not domain=='' or not data_point=='':
    
        add_business_term(driver, community, domain, data_point)  


#%% ATRIBUTOS
def rm_atr(driver):
        try:
            tags = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class='icon-cross filter-tag__remove-button']")))

            for tag in tags:
                tag.click()
        except:
             pass


def add_attribute(driver, attr):
    "Doc String"
    
    try:
        WebDriverWait(driver, 
                      30).until(EC.element_to_be_clickable((By.ID, 
                                                            "add-attributes-button"))).click()
        WebDriverWait(driver, 
                      30).until(EC.element_to_be_clickable((By.XPATH, 
                                                            "//input[@placeholder='Select an attribute']"))).click()
        search = WebDriverWait(driver, 
                               30).until(EC.presence_of_element_located((By.XPATH, 
        
                                                                         "//input[@placeholder='Search...']")))
    except:
        pass
    
    try:    
        ActionChains(driver).move_to_element(search)
        search.clear()
        
        ActionChains(driver).move_to_element(search)
        search.send_keys(attr[0]) 

        try:
            lista = WebDriverWait(driver, 
                                  2).until(EC.presence_of_element_located((By.XPATH, 
            
                                                                             "//ul[@aria-label='submenu']")))
            touch = WebDriverWait(lista, 
                                  1).until(EC.presence_of_element_located((By.XPATH, 
            
                                                                             "//span[text()='"+attr[0]+"']")))
            touch.click()
        except:
            
            search.clear()
            return None
            #TODO: 
            
            
        
    
        while True:
            if check_exists_by_xpath(driver,
                                     "//input[@placeholder='Type a value']"):
                atrf = WebDriverWait(driver, 
                                     30).until(EC.presence_of_element_located((By.XPATH, 
                                                                                      "//input[@placeholder='Type a value']")))
                ActionChains(driver).move_to_element(atrf)
                atrf.send_keys(attr[1])
                
                break
            elif check_exists_by_xpath(driver, "//div[@class='value-layout']"):
                if bool(attr[1]):
                    rb = WebDriverWait(driver, 
                                         30).until(EC.element_to_be_clickable((By.XPATH, 
                                                                                   "//label[text()='true']")))
                    ActionChains(driver).move_to_element(rb).click(rb).perform()
                    rb.click()
                    break
                elif not bool(attr[1]):
                    rb = WebDriverWait(driver, 
                                         30).until(EC.presence_of_element_located((By.XPATH, 
                                                                                           "//label[text()='false']")))
                    ActionChains(driver).move_to_element(rb).click(rb).perform()
                    
                    rb.click()
                    break
                #TODO: contemplar que haya un dropdown
    except:
        pass            
            
            
    save_button = WebDriverWait(driver, 
                                30).until(EC.element_to_be_clickable((By.XPATH, 
                                  "//button[@class='button button-primary small']")))
    ActionChains(driver).move_to_element(save_button).click(save_button).perform()

    save_button.click()
            
                     
def fill_attributes(driver, field):
    """Doc str"""
    a_dict = field.Attributes.__dict__
    for key in a_dict:
        if not tables.isnan(a_dict[key]):
            add_attribute(driver, a_dict[key])
        

        
#%% CAMPOS
def fill_fields(driver, field):

    """Doc string"""
    
    #Introducir alias
    alias = WebDriverWait(driver, 
                          30).until(EC.presence_of_element_located((By.XPATH, 
                            "//input[@placeholder='Type an alias']")))
    alias.clear()
    alias.send_keys(field.alias)
    #Introducir descripcion
    description = WebDriverWait(driver, 
                                30).until(EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Enter description']")))
    description.clear()
    description.send_keys(field.description)            


#%% FUNCIONES UTILES  
def check_exists_by_xpath(driver, xpath):
    """Doc str"""
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

#%% QUALITY RULES
#Solo funciona en el caso de reglas proactivas
def fill_qr(driver, data):
    formatter = logging.Formatter('%(levelname)s %(message)s %(asctime)s')
    qr_log = logging.getLogger('qr')
    qh = logging.FileHandler('log_qr.log', mode='w+')
    qh.setFormatter(formatter)
    qr_log.addHandler(qh)
    for i, rule in enumerate(data):
        try:
            rutas = build_route_table(rule.route, rule.table, rule.source)
            if len(rutas)>1:
                driver.get(rutas[1])
    
            else:
                driver.get(rutas)
            qr_nav = WebDriverWait(driver, 
                                   30).until(EC.presence_of_element_located((By.XPATH, 
                                     "//a[@id='data-horizontal-tabs-tab-1']")))
            ActionChains(driver).move_to_element(qr_nav).click(qr_nav).perform()    
            
            wait(driver)
            
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//button[@id='quality-rule-list-creation-button']"))).click()
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//span[@class='label']"))).click()
            wait(driver)
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//button[@id='st-modal-button-Create_new']"))).click()
            
            wait(driver)
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//input[@id='st-input-quality-rule-name']"))).send_keys(rule.name)
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Enter a description']"))).send_keys(rule.description)
                      
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//input[@id='st-input-quality-rule-attribute-input']"))).click()
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//span[text()='"+rule.column+"']"))).click()
           
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//input[@id='st-input-quality-rule-operation-input']"))).click()
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//span[text()='"+rule.condition+"']"))).click()
           
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//input[@id='st-input-quality-rule-value']"))).click()
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//input[@id='st-input-quality-rule-value']"))).send_keys(str(rule.value))
            
            if rule.check_type=="AV":
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//input[@id='st-input-quality-rule-check-type-input']"))).click()
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//span[text()='by Absolute value']"))).click()
           
            else:
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//input[@id='st-input-quality-rule-check-type-input']"))).click()
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//span[text()='by Threshold (%)']"))).click()
           
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//input[@id='st-input-quality-rule-check-operator-input']"))).click()
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//span[text()='"+rule.check_op+"']"))).click()
               
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//st-input[@id='action-input-quality-rule-check-value']//div[@class='input-container']//input[contains(@class, 'st-input')]"))).click()
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//st-input[@id='action-input-quality-rule-check-value']//div[@class='input-container']//input[contains(@class, 'st-input')]"))).send_keys(str(rule.check_val))
            
            if rule.action=="MF":
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//input[@id='st-input-quality-rule-action-input']"))).click()
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Move failed to path']"))).click()
            else:
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//input[@id='st-input-quality-rule-action-input']"))).click()
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Pass through']"))).click()
               
            
            st = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//input[@id='st-input-quality-rule-status-input']")))
            ActionChains(driver).move_to_element(st).click(st).perform()
            if int(rule.status)==0:         
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Inactive']"))).click()
            else:
                WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Active']"))).click()
           
            #TODO: de momento estoy pulsando el boton cancelar porque si pulso save se guardaría y no se podría borrar.
            #Unicamente hay que cambiar el id por: quality-rule-save-button
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//button[@id='quality-rule-cancel-button']"))).click()
        except:
            print('WARNING: no se ha podido generar la regla número' + str(i+1))
            qr_log.warning("QR No. " + str(i+1))
            #LOG DE REGLAS DE CALIDAD
            continue               
        
      
    qr_log.warning("FINISHED: QR information updated.")    
    print("FINISHED: QR information updated.")
