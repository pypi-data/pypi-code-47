import copy,os,glob
import pandas as pd
import numpy as np
from astropy.io import fits

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
    return CATALOG.iloc[index,:]

def make_meta(FILES):
    GID,DID = {},{}
    for i,ii in enumerate(FILES):
        hdr = fits.open(ii)['PRIMARY'].header
        xx = hdr['FILTER']
        if xx[0]=='G':
            GID[i] = {}
            GID[i]['FILE_ORIG'] = ii
            GID[i]['FILTER'] = xx
            GID[i]['EXPSTART'] = hdr['EXPSTART']
            GID[i]['POSTARG1'] = hdr['POSTARG1']
            GID[i]['POSTARG2'] = hdr['POSTARG2']
        elif xx[0]=='F':
            DID[i] = {}
            DID[i]['FILE_ORIG'] = ii
            DID[i]['FILTER'] = xx
            DID[i]['EXPSTART'] = hdr['EXPSTART']
            DID[i]['POSTARG1'] = hdr['POSTARG1']
            DID[i]['POSTARG2'] = hdr['POSTARG2']
    GID = _make_pairs(GID,DID)
    return GID,DID

def _make_pairs(GID,DID):
    x = pd.DataFrame(DID).T
    x.reset_index(drop=False, inplace=True)
    x.rename(columns={"index": "ID"}, inplace=True)
    for i in GID:
        x2 = GID[i]['EXPSTART']
        x3 = x['EXPSTART'].values
        x4 = np.abs(x3-x2)
        index = np.argmin(x4)
        GID[i]['DIRECT'] = x.iloc[index].to_dict()   
    return GID

def prepare_folders(GID):
    # GRISM/
    x = glob.glob('*')
    if 'GRISM' not in x:
        os.mkdir('GRISM')
    for i in GID:
        x1 = GID[i]['FILE_ORIG']
        x2 = 'GRISM/'+x1.split('/')[-1]
        os.system("cp {0} {1}".format(x1,x2))
        GID[i]['FILE_NEW'] = x2.split('/')[-1:]
    x = open("GRISM/GRISM.lis","w") 
    for i in GID:
        x.writelines(GID[i]['FILE_NEW'])
        x.write('\n')
    x.close()
    # DIRECT/
    x = glob.glob('*')
    if 'DIRECT' not in x:
        os.mkdir('DIRECT')
    for i in GID:
        x1 = GID[i]['DIRECT']['FILE_ORIG']
        x2 = 'DIRECT/'+x1.split('/')[-1]
        os.system("cp {0} {1}".format(x1,x2))
        GID[i]['DIRECT']['FILE_NEW'] = x2.split('/')[-1]
    x = open("DIRECT/DIRECT.lis","w") 
    for i in GID:
        x.writelines(GID[i]['DIRECT']['FILE_NEW'])
        x.write('\n')
    x.close()

def make_axelis(GID):
    x = open("aXe.lis","w") 
    for i in GID:
        x1 = GID[i]['FILE_ORIG'].split('/')[-1]
        x2 = GID[i]['DIRECT']['FILE_ORIG'].split('/')[-1].split('.')[0]+'_1.cat'
        x3 = GID[i]['DIRECT']['FILE_ORIG'].split('/')[-1]
        x.writelines('{0} {1} {2}'.format(x1,x2,x3))
        x.write('\n')
    x.close()
    