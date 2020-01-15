import pandas as pd
import numpy as np

def GetNPVTable(installCost,maintCost,disposalCost,periodRevenue,discountRate,lifetime):
    """Calculates a table containing cost, revenue, and NPV values 
    for a specified number of periods. 

    Parameters
    ----------
    installCost : float
        installation cost ($), applied in the first period
        
    maintCost : float
        maintanence cost ($/period), applied each period
        
    disposalCost : float
        disposal cost ($), applied in the last period
        
    periodRevenue : float
        revenue ($/period), applied to each period
        
    discountRate : float
        period discount rate (decimal percent)
        
    lifetime : int
        number of periods to consider

    Returns
    -------
    DataFrame
        Pandas dataframe with row=periods, cols=costs/revenues/npvs
    """

    # determine annual net cash flow
    df = pd.DataFrame( index=np.arange(0, lifetime),
                  columns=["Year","Period Cost","Period Revenue","Net Cash Flow","Cumulative Cash Flow","Period NPV", "Cumulative NPV"])
    cumCashFlow = 0
    cumNPV = 0
    for year in range(1,lifetime+1):
        if year == 1:   # first year?
            periodCost = installCost
        elif year == lifetime:  # last year?
            periodCost = maintCost + disposalCost
        else:
            periodCost = maintCost
            
        netCashFlow = periodRevenue-periodCost
        cumCashFlow += netCashFlow
        npv = netCashFlow/((1+discountRate)**year)        
        cumNPV += npv
        df.iloc[year-1] = (year,periodCost,periodRevenue,netCashFlow,cumCashFlow,npv,cumNPV)
    return df


def GetNPV(discountRate,R):
    """Calculates NPV at the end of a period, based on net revenue flows.
    
    Parameters
    ----------
    discountRate : float
        Period discount rate (e.g. 0.05)
    R : list-like
        List or array of net revenue values for each period
        
    Returns
    -------
    float
        Net present value at the end of the perioeds represented in R
    """

    npv = 0
    for p in range(0,len(R)):
        npv += R[p]/((1+discountRate)**(p+1))  # (p+1) since p is 0-based
    return npv


def GetNPVs(discountRate,R):
    """Calculates NPV for a list of periods, based on net revenue flows.
    
    Parameters
    ----------
    i : float
        Period discount rate (e.g. 0.05)
    R : list-like
        List or array of net revenue values for each period
        
    Returns
    -------
    numpy array of floats
        Net present value at the end of each period represented in R
    """
    npv = np.zeros(len(R))
    npv[0] = R[0]/((1+discountRate)**(1))

    for p in range(1,len(R)):
        npv[p] = npv[p-1] + R[p]/((1+discountRate)**(p+1))
    return npv


def GetDiscountedPaybackPeriod(discountRate,R):
    """Calculates Discounted payback period based on a discount rate and array of revenue flows by period.
    
    Parameters
    ----------
    discountRate : float
        Period discount rate (e.g. 0.05)
    R : list-like
        List or array of net revenue values for each period
        
    Returns
    -------
    float
        discounted payback period        
    """

    # Step 1 - Discount cash flows
    Rd = GetNPVs(discountRate,R)

    if Rd[0] > 0:  # mus be negative -> positive
        return -1

    # find when rd crosses zero
    iLeft = 0
    iRight = 0

    for i in range(0,len(Rd)):
        if Rd[i] < 0:
            iLeft = i
        else:
            iRight = i
            break
    
    if iRight == 0: # no positives found?
        return -2

    # find where Rd crosses zero (R0)
    p0 = iRight - (Rd[iRight]/(Rd[iRight]-Rd[iLeft]))
    return p0+1  # to make period one-based
