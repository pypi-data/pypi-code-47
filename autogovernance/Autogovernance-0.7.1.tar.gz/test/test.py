# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 11:32:19 2019

@author: LP885RH
"""
from os import path
import sys
import xlrd
#import autogovernance
from autogovernance import browser
#from autogovernance import tables
#import autogovernance.browser as browser
#import autogovernance.tables as tables



def get_dir(fn=''):
    """
    Get the current directory.
    
    Parameters:
        fn (str): (Optional) filename.
        
    Output:
        (str) Complete path of file.
    """

    try:
        if getattr(sys, 'frozen', False):
            application_path = path.dirname(sys.executable)
        elif __file__:
            application_path = path.dirname(__file__)
            
        filename = str(str(application_path)+"/"+str(fn))
        return filename
    except Exception as ex:
        print(ex)
        raise Exception('FATAL ERROR: No such file or directory.')

def read_dictionary(filename):
    """
    DOC String
    Parameters:
        filename (str): name of the excel file where the dictionary is contained.
        layer (str): name of the layer in which the dictionary is going to read.
        
    Outputs:
        (List) List of elements.
    """

    data_list = []
    direct = get_dir('_data/')
    if  path.isfile(direct + filename):
        try:
            doc = xlrd.open_workbook(direct + filename)
        except Exception as ex:
            print(ex)
            raise Exception("FATAL ERROR: No such file or directory.")

        sheets = doc.sheet_names()

            
            
        if 'dictionary' in sheets:
            dict_ = doc.sheet_by_name('dictionary')

        else:
            raise Exception("The sheet 'dictionary' doesn't exist in Excel file")

        
        for i in range(1, dict_.nrows):
            try:
                row = dict_.row_values(i)
                atr = Attributes(*[x for x in row[11:]])
                bt = BusinessTerm(*[x for x in row[8:11]])
                elem = Element(*[x for x in row[0:8]], bt, atr)
                data_list.append(elem)

            except:
                print("WARNING: " + str(i) + "th element has not be added")
                continue
                
        return data_list  
    
def read_qr(filename):
    data_list = []
    direct = get_dir('_data/')
    if  path.isfile(direct + filename):
        try:
            doc = xlrd.open_workbook(direct + filename)
        except Exception as ex:
            print(ex)
            raise Exception("FATAL ERROR: No such file or directory.")

        sheets = doc.sheet_names()

            
            
        if 'qr' in sheets:
            dict_ = doc.sheet_by_name('qr')

        else:
            raise Exception("The sheet 'dictionary' doesn't exist in Excel file")

        
        for i in range(1, dict_.nrows):
            
                row = dict_.row_values(i)
                qr_ = QR_object(*[x for x in row[0:14]])
                data_list.append(qr_)

                
        return data_list  

    
if __name__=='__main__':
    
    #PARAMETRIZACIONES
    #url de governance para el entorno
    URL = "https://admin.sgcto-int.stratio.com/service/governance-ui/"
    TENANT = 'gts'
    USER = 'stratio'
    PASSWORD = 'stratio'
    
    #BOOLEANOS 
    TABLAS = False
    QR = True #En desarrollo
    CAMPOS = False
    BORRADO_ATR_BT = False
    ATRIBUTOS = False
    GLOSARY = False #Temporalmente inutilizado por error en nueva versión Governance
    
    
    dict_data = read_dictionary('Dictionary_scripting.xlsx')
    driver = browser.init_autonav()
    driver.execute_script("document.body.style.zoom='67%'")
    browser.login(driver, URL, TENANT, USER, PASSWORD)

    
    if TABLAS:
        browser.fill_tables(driver, tables.get_tables(dict_data))

    if CAMPOS or ATRIBUTOS or BORRADO_ATR_BT or GLOSARY:
        browser.nav_fields(driver, dict_data, CAMPOS, ATRIBUTOS, BORRADO_ATR_BT, GLOSARY)
    
    if QR:
        qr_data = read_qr('Dictionary_scripting.xlsx')
        browser.fill_qr(driver, qr_data)
    
    driver.close()
