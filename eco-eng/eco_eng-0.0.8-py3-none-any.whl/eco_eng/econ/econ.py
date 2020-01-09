

def GetNPVTable(installCost,maintCost,disposalCost,annualRevenue,discountRate,lifetime):
    # determine annual net cash flow
    df = pd.DataFrame( index=np.arange(0, lifetime),
                  columns=["Year","Annual Cost","Annual Revenue","Net Cash Flow","Cumulative Cash Flow","Period NPV", "Cumulative NPV"])
    cumCashFlow = 0
    cumNPV = 0
    for year in range(0,lifetime):
        if year == 0:   # first year?
            annualCost = installCost
        elif year == lifetime-1:  # last year?
            annualCost = maintCost + disposalCost
        else:
            annualCost = maintCost
            
        netCashFlow = annualRevenue-annualCost
        cumCashFlow += netCashFlow
        npv = netCashFlow/((1+discountRate)**year)        
        cumNPV += npv
        df.iloc[year] = (year+1,annualCost,annualRevenue,netCashFlow,cumCashFlow,npv,cumNPV)
    return df


def GetNPV(i,R):
    npv = 0
    for p in range(0,len(R)):
        npv += R[p]/((1+i)**p)
    return npv