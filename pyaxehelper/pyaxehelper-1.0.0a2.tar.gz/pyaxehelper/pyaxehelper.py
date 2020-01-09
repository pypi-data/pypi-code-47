import copy
import pandas as pd
import numpy as np

def change_catalog_order(catalog):
    x = read_catalog(catalog)
    y = x.T.iloc[0:14].copy()
    z = y.copy()
    z1,z11 = z.iloc[11].name,z.iloc[12].name
    zz,zz2 = z1.split(),z11.split()
    zz[1],zz2[1] = '13','12'
    z2 = ' '.join(zz) + '\n'
    z22 = ' '.join(zz2) + '\n'
    z.rename(index={z1:z2,z11:z22}, inplace = True)
    tmp = z.iloc[0:11]
    tmp = tmp.append(z.iloc[12])
    tmp = tmp.append(z.iloc[11])
    tmp = tmp.append(z.iloc[13])
    tmpp = tmp.T.copy()
    write_catalog(catalog,tmpp)
    
def change_magiso2magwavelength(catalog,wavelength):
    x = read_catalog(catalog)
    y = x.columns[11].split()
    y[2] = 'MAG_F'+str(int(wavelength))
    z = ' '.join(y) + '\n'
    x.rename(columns={x.columns[11]:z},inplace=True)
    write_catalog(catalog,x)

def write_catalog(catalog,dataframe):
    x = open(catalog,'w')
    for i in dataframe.columns:
        x.writelines(i)
    for i in dataframe.values:
        string = ' '.join(i[0:2].astype(str))
        string = string + ' ' + str(i[2].astype(int))
        string = string + ' ' + ' '.join(i[3:].astype(str)) + '\n'
        x.writelines(string)
    x.close()
    
def read_catalog(catalog):
    x = open(catalog,'r')
    colname = []
    values = []
    for i in x.readlines():
        if i[0]=='#':
            colname.append(i)
        else:
            x2 = np.array(i.split(),dtype=np.double)
            values.append(x2)
    x.close()
    x3 = pd.DataFrame(values,columns=colname)
    x3 = x3.astype({colname[2]:'int64'})
    return copy.deepcopy(x3)

def select_source(v1,v2,catalog,method='RADEC'):
    CATALOG = read_catalog(catalog)
    x0 = CATALOG.iloc[:,3].values
    y0 = CATALOG.iloc[:,4].values
    dx,dy = x0-v1,y0-v2
    dd = np.sqrt(dx**2 + dy**2)
    index = np.argmin(dd)
    return CATALOG.iloc[:,index]
