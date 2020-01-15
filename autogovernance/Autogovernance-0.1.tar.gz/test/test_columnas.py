# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 12:14:12 2019

@author: LP885RH
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
