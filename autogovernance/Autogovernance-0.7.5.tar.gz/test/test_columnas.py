# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 12:14:12 2019

@author: LP885RH
"""
"""
import pandas as pd

real = ['id', 'issueId', 'issueTransactionId', 'customerReference', 
                'product_id', 'product_name', 'refinance', 'relatedLoan', 
                'loansDataAmount', 'loansDataCurrency_code', 'loansDataTerm', 
                'event_id', 'eventName', 'statusName', 'approved', 'canceled', 
                'creationDate', 'valueDate', 'valueDateChanged', 
                'currency_code', 'applicant_id', 'applicant_name', 
                'beneficiary_id', 'beneficiary_name', 'riskType_id', 
                'riskType_name', 'riskAmount', 'totalPrepaidAmount', 
                'discrepanciesAffectRisk', 'credit_id', 'creditDate', 
                'creditorBank_bic', 'creditorBank_name', 
                'o32B_increaseCreditAmount', 'o33B_decreaseCreditAmount', 
                'creditCurrency_code', 'o39A_creditTolerance_id', 
                'o39A_creditTolerance_name', 'credit_tolerancePercentage', 
                'credit_toleranceAmount', 'credit_creditNegotiated', 
                'credit_creditPaid', 'credit_creditAccepted', 
                'credit_creditAvailableWithoutTolerance', 
                'credit_creditToBePaid', 'credit_realCreditAvailable', 
                'applicationId', 'loanType_id', 'loanType_name', 
                'associatedTransactionType_id', 
                'associatedTransactionType_name', 
                'associatedTransactionType_product', 
                'associatedTransactionReferenceNumber_id', 
                'associatedTransactionReferenceNumber_name', 
                'associatedSequenceNumber_id', 'associatedSequenceNumber_name', 
                'amortizationFrequency_id', 'amortizationFrequency_name', 
                'firstAmortizationDate', 'principalAmount', 'interest', 
                'interestRate', 'interestWaived_id', 'interestRateType_id', 
                'interestRateType_name', 'firstRateAdjustment', 
                'firstRateAdjustmentDate', 'currentInterestRate', 
                'defaultInterestRate', 'defaultInterestRatePayment', 
                'defaultInterestAmount', 'indexRate_id', 'indexRate_name', 
                'indexRate_basisPeriod_id', 'indexRate_basisPeriod_name', 
                'indexRateBank_bic', 'indexRateBank_name', 
                'indexRate_currency_code', 'indexRateValueDate', 
                'interestAccrue', 'interestAmount', 'interestCalculation', 
                'spread', 'interestPayment', 'interestPaymentFrequency', 
                'interestRatePayment', 'interestRateTypePayment_id', 
                'calendarTypeOfRate_id', 'calendarTypeOfRate_name', 
                'calendarInterestRate', 'calendarTotalInterest', 'rate', 
                'interestPaymentAmount', 'cancellationTransactionId', 
                'sequence', 'currencyAvailableAmount_code', 'amountToCancel', 
                'currencyAmountToCancel_code', 'interestWaived_name', 
                'interestRateTypePayment_name', 'riskCurrency', 
                'PrepaidAmount', 'credit_creditAvailable', 'credit_days', 
                'bankReference', 'transactionId', 'letterCreditType_id', 
                'letterCreditType_name', 'status_id', 'issueDate', 
                'expirationDate', 'collImpApprovalDateNoti', 'amount', 
                'credit_creditAmount', 'indexRateValue', 'cancellationDate', 
                'availableAmountCurrent', 'product_loansEnabled', 'indexName', 
                'ts', 'load_date']
 
excel = pd.read_excel('_data/Diccionario_scripting_00.xlsx', sheets='r1_core')

excel_columns = excel.field
real_columns = pd.DataFrame(columns=['field1'])
real_columns.field1 = pd.Series(real)

cruce = real_columns.merge(excel_columns, how='left', left_on='field1', right_on='field')
import numpy as np
print(cruce[cruce.field==np.nan])
"""
from autogovernance import browser
from autogovernance import tables
from autogovernance import element
from os import path
import sys
import xlrd

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
                atr = element.Attributes(*[x for x in row[11:]])
                bt = element.BusinessTerm(*[x for x in row[8:11]])
                elem = element.Element(*[x for x in row[0:8]], bt, atr)
                data_list.append(elem)

            except Exception as ex:
                print(ex)
                print("WARNING: " + str(i) + "th element has not been added")
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
                qr_ = element.QR_object(*[x for x in row[0:14]])
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
