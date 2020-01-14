"""
A module for quickly reading data from files in the in CMC "standard" format.
Basically everything is done through the **getData** function.



"""


from typing import Callable, Iterator, Union, Optional, List, Iterable, MutableMapping
import datetime as DT


def getData( fileName:   Optional[str]=None,
             dirName:    Optional[str]=None,
             prefix:     Optional[str]='',
             suffix:     Optional[str]='',
             varName:    str=None, 
             datev:      Optional[Union[int,DT.datetime]]=None,
             ip1:        Optional[Union[List[int],int]]=None,
             ip2:        Optional[int]=None,
             ip3:        Optional[int]=None,
             ig1:        Optional[int]=None,
             ig2:        Optional[int]=None,
             ig3:        Optional[int]=None,
             typvar:     Optional[str]=None, 
             etiquette:  Optional[str]=None,
             latlon:     Optional[bool]=False,
             presFromVar:Optional[bool]=False,
             presLevels: Optional[Iterable[int]]=None,
             tmpDir:     Optional[str]=None) :


    """ Read data from CMC 'standard' files 

       - Entries with same validity date but different IP1s get sorted, concatenated and are output as a 3D array.
       - 2D latitudes and longitudes associated with the requested data are optionally outputted
       - Pressure values associated with requested data are optionally outputted
       - Vertical interpolation on pressure levels is supported 
       - Option to search valid entry in all standard files located within a directory 

    Args:
       fileName:    /path/to/fst/file.fst  
       dirName:     /path/to/a/directory/containing/fst/files/   
                    Search all standard files within a directory for a match 
                    with search criteria. 
                    Searching all files in large directories can take a while, 
                    use prefix and suffix to constrain search.
                    Note that fileName superseeds dirName
       prefix:      In combination with dirName; prefix of files to search
       suffix:      In combination with dirName; suffix of files to search
       varName:     Name of variable to read in fst file  eg:   UU, VV, TT, MPQC, etc.
       presFromVar: Flag to output pressure associated with returned data
       datev:       Cmc timestamp for validity date of retrieved data
       ip1:         Criterion for choosing what data will be read.
                    A list of ip1s can be provided to read a number of levels 
                    in one function call. 
       ip2:         Criterion for choosing what data will be read
       ip3:         Criterion for choosing what data will be read
       ig1:         Criterion for choosing what data will be read
       ig2:         Criterion for choosing what data will be read
       ig3:         Criterion for choosing what data will be read
       typvar:      Criterion for choosing what data will be read
       etiquette:   Criterion for choosing what data will be read
       latlon:      Flag to output 2D grids of latitude and longitudes associated with data
       presLevels:  List of pressure levels [hPa] onto which data is desired   eg [850,700,500]
       tmpDir:      /path/to/a/temporary/work/directory/   Only used for interpolation to pressure levels 
                    if None, $TMPDIR is used; may run out of space when large fields are interpolated

    Returns:
        {
            'values':    (ndarray) 2D or 3D array containing data  k=0 -> lowest level

            'meta':     (dict) meta data of the first matching entry in fst file

            'grid':     (dict) hgrid as returned by readGrid of rpn python

            'toctoc':   (dict) toctoc (!!) entry associated with data as returned by fstlir of rpn python

            'ip1List':  (list) ip1s for each level being returned

            'levList':  (list) levels corresponding to the ip1s in ip1List

            'lat':      (ndarray) 2D latitudes of data grid (conditional on latlon=True)

            'lon':      (ndarray) 2D longitudes of data grid (conditional on latlon=True)

            'pressure': (ndarray) 2D or 3D array of pressure (conditional on presLevels)

        }


    Examples:

       Get first matching entry of P0 as a 2D ndarray. 

       >>> import domcmc.fst_tools as fst_tools
       >>> fstFile = '/home/dja001/shared_stuff/files/python_test_data/2016081200_006_0001'
       >>> p0 = fst_tools.getData(fileName=fstFile, varName='P0')
       >>> print(p0.keys())
       dict_keys(['values', 'meta', 'grid', 'toctoc', 'ip1List', 'levList'])
       >>> print(p0['values'].shape)
       (328, 278)


       Get P0 at a different validity date:

       >>> import domcmc.fst_tools as fst_tools
       >>> import datetime as DT
       >>> fstFile = '/home/dja001/shared_stuff/files/python_test_data/2016081200_006_0001'
       >>> #
       >>> #directly with a datetime object
       >>> dt = DT.datetime(2016, 8, 12, 6, 10, 0, tzinfo=DT.timezone.utc)
       >>> p0 = fst_tools.getData(fileName=fstFile, varName='P0', datev=dt)
       >>> print(p0.keys())
       dict_keys(['values', 'meta', 'grid', 'toctoc', 'ip1List', 'levList'])
       >>> print(p0['values'].shape)
       (328, 278)
       >>> #
       >>> #with a CMC timestamp
       >>> p0 = fst_tools.getData(fileName=fstFile, varName='P0', datev=412062350)
       >>> print(p0.keys())
       dict_keys(['values', 'meta', 'grid', 'toctoc', 'ip1List', 'levList'])
       >>> print(p0['values'].shape)
       (328, 278)


       Get UU as a 3D ndarray. 
       Output 'lat' and 'lon' as 2D numpy arrays of latitudes and longitudes associated with the grid of UU

       >>> import domcmc.fst_tools as fst_tools
       >>> fstFile = '/home/dja001/shared_stuff/files/python_test_data/2016081200_006_0001'
       >>> uu = fst_tools.getData(fileName=fstFile, varName='UU', latlon=True)
       >>> print(uu.keys())
       dict_keys(['values', 'meta', 'grid', 'toctoc', 'ip1List', 'levList', 'lat', 'lon'])
       >>> print(uu['values'].shape)
       (328, 278, 81)
       >>> print(uu['lat'].shape, uu['lon'].shape)
       (328, 278) (328, 278)

       Get VV as a 3D ndarray given by the input of ip1 list. 
       Also output latitudes and longitudes associated with the grid of VV 

       >>> import domcmc.fst_tools as fst_tools
       >>> fstFile = '/home/dja001/shared_stuff/files/python_test_data/2016081200_006_0001'
       >>> ip1input = [75597472, 95258609, 95237745, 95011105, 94859092, 94831040]
       >>> vv = fst_tools.getData(fileName=fstFile, varName='VV', ip1=ip1input, latlon=True)
       >>> print(vv.keys())
       dict_keys(['values', 'meta', 'grid', 'toctoc', 'ip1List', 'levList', 'lat', 'lon'])
       >>> print(vv['values'].shape)
       (328, 278, 6)
       >>> print(vv['ip1List'])
       [75597472, 95258609, 95237745, 95011105, 94859092, 94831040]
       >>> print(vv['lat'].shape, vv['lon'].shape)
       (328, 278) (328, 278)
       >>>
       >>> #note that even with a list of ip1s, output levels get sorted 
       >>> #from lowest to highest
       >>> ip1input = [ 95258609, 94859092, 95011105, 95237745, 94831040, 75597472]
       >>> vv = fst_tools.getData(fileName=fstFile, varName='VV', ip1=ip1input, latlon=True)
       >>> print(vv['ip1List'])
       [75597472, 95258609, 95237745, 95011105, 94859092, 94831040]


       Get first matching entries of HU as 3D numpy array. 
       Output pressure associated with HU

       >>> import domcmc.fst_tools as fst_tools
       >>> fstFile = '/home/dja001/shared_stuff/files/python_test_data/2016081200_006_0001'
       >>> hu = fst_tools.getData(fileName=fstFile, varName='HU', presFromVar=True)
       >>> print(hu.keys())
       dict_keys(['values', 'meta', 'grid', 'toctoc', 'ip1List', 'levList', 'pressure'])
       >>> print(hu['values'].shape)
       (328, 278, 81)
       >>> print(hu['pressure'].shape)
       (328, 278, 81)


       Get TT field interpolated at 800, 500 and 200 hPa.
       returned 'values' is a 3D array where k=0 indicates the lowest level (here 800 hPa)
       pxs2pxt must be available in environment
       https://wiki.cmc.ec.gc.ca/wiki/Pxs2pxt

       >>> import domcmc.fst_tools as fst_tools
       >>> fstFile = '/home/dja001/shared_stuff/files/python_test_data/2016081200_006_0001'
       >>> # if the fst file is large, you may run out of space in $TMPDIR and 
       >>> # get weird errors. 
       >>> # In this case use tmpDir=/path/to/big/temporary/directory/ in your call to getData
       >>> tt = fst_tools.getData(fileName=fstFile, varName='TT', presLevels=[800,500,200])
       >>> print(tt.keys())
       dict_keys(['values', 'meta', 'grid', 'toctoc', 'ip1List', 'levList'])
       >>> print(tt['values'].shape)
       (328, 278, 3)

       It is often the case that a directory will contain many standard files, each containing entries
       at different validity times. Because of the different naming conventions found at the CMC, it
       then becomes cumbersome to figure out which file contains the desired entries at a given validity 
       time. To address this problem, use the dirName option. All standard files will be searched 
       for the desired entry. 

       >>> import domcmc.fst_tools as fst_tools
       >>> import datetime as DT
       >>> fstDir = '/home/dja001/shared_stuff/files/python_test_data/'
       >>> dt = DT.datetime(2016, 8, 12, 6, 20, 0, tzinfo=DT.timezone.utc)
       >>> pr = fst_tools.getData(dirName=fstDir, varName='PR', datev=dt)
       >>> print(pr.keys())
       dict_keys(['values', 'meta', 'grid', 'toctoc', 'ip1List', 'levList'])
       >>> print(pr['values'].shape)
       (324, 274)
       >>> # For large directories containing many standard files, use the prefix and/or suffix arguments to 
       >>> # restrict the search and speedup things
       >>> # in the following example, only files matching 2016081200*0001 will be searched.
       >>> pr2 = fst_tools.getData(dirName=fstDir, prefix='2016081200', suffix='0001', varName='PR', datev=dt)
       >>> print(pr2.keys())
       dict_keys(['values', 'meta', 'grid', 'toctoc', 'ip1List', 'levList'])
       >>> print(pr2['values'].shape)
       (324, 274)




    """

    import numpy as np
    import os
    import warnings
    import glob
    import subprocess
    import rpnpy.librmn.all as rmn
    import rpnpy.utils.fstd3d as fstd3d
    import rpnpy.vgd.all as vgd
    from rpnpy.rpndate import RPNDate
    import datetime as DT

    #was varname specified
    if varName is None :
        raise ValueError('varName: must be set to a fst variable name eg P0, UU, TT, etc')

    #get cmcTimestamp from datev
    if datev is None :
        cmcTimestamp=None
    else:
        if isinstance(datev, DT.datetime):
            dateObj = RPNDate(datev)
            cmcTimestamp = dateObj.datev
        else:
            #assume a cmc timestamp is passed
            try:
                cmcTimestamp=int(datev)
            except:
                raise ValueError('datev can only a datetime.datetime object OR a an integer representing a CMC timestamp')

    #use fileName or find file with matching entry
    if fileName is not None :
        #if fileName was provided use this
        if not os.path.isfile(fileName) :
            #files does not exist, throw a warning and return None
            warnings.warn('fileName: '+fileName+' does not exist')
            return None
        #by default input file is the file that will be read
        fileToRead = fileName
    else :
        if dirName is not None :
            #iterate over files in dirName and check which one match the search criterion
            #non FST files are skipped
            if not os.path.isdir(dirName) :
                raise ValueError('dirName: '+fileName+' is not a valid path')
            #get a list of files in there
            fileList = glob.glob(dirName+'/'+prefix+'*'+suffix)
            if len(fileList) == 0 :
                raise RuntimeError('no files in :'+dirName+'/'+prefix+'*'+suffix)
            fileToRead = None
            for thisFile in fileList :
                foundFile = None
                if presLevels is not None :
                    #entries necessary for vertical interpolation
                    p0 = _getVar(thisFile, 'P0',       
                                 datev=cmcTimestamp,   
                                 ip1=None, ip2=None, ip3=None,
                                 ig1=ig1,  ig2=ig2,  ig3=ig3,
                                 typvar=typvar, etiquette=etiquette,
                                 metaOnly=True, verbose=0,
                                 skipNonFst=True)
                    var = _getVar(thisFile, varName,       
                                 datev=p0['meta']['datev'],   
                                 ip1=None, ip2=None, ip3=None,
                                 ig1=ig1,  ig2=ig2,  ig3=ig3,
                                 typvar=typvar, etiquette=etiquette,
                                 metaOnly=True, verbose=0,
                                 skipNonFst=True)
                    if (p0 is not None) and (var is not None) :
                        #this file contains all necessary data
                        foundFile = thisFile
                else :
                    #entry necessary for normal retrieval
                    var = _getVar(thisFile, varName,       
                                  datev=cmcTimestamp,   
                                  ip1=ip1, ip2=ip2, ip3=ip3,
                                  ig1=ig1, ig2=ig2, ig3=ig3,
                                  typvar=typvar, etiquette=etiquette,
                                  metaOnly=True, verbose=0,
                                  skipNonFst=True)
                    if var is not None :
                        #this file contains all necessary data
                        foundFile = thisFile

                    #endif

                if foundFile is not None : 
                    if fileToRead is not None : 
                        raise RuntimeError('search criterion matched in two different files:'+fileToRead+'   '+thisFile)
                    else:
                        fileToRead = thisFile
            #endfor

            #if no match found after iterating over all files, return None
            if fileToRead is None :
                return None
    
        else :
            raise ValueError('Please provide one of fileName or dirName arguments')

    #a random number for temporary files
    rand = np.round(np.random.rand(1)*1e7).astype('int')
    randStr = '{:07d}'.format(rand[0])

    #temporary dir for this session
    if tmpDir is None :
        tmpDir = os.environ['TMPDIR']
    #valid dir
    if not os.path.exists(tmpDir) :
        raise ValueError('tmpDir: '+tmpDir+' is not a valid path ')

    #vertical interpolation  to pressure levels is desired
    if presLevels is not None :

        #comma separated string with list of levels [hPa]
        levelStr = ''
        for thisLevel in presLevels :
            levelStr += '{:07.2f}'.format(thisLevel)+','
        levelStr = levelStr.rstrip(',')

        #code for type of interpolation eg CUB_UU
        #CUB_    CUBIC   
        #CUBP_   CUBIC   Clip negative values
        #LIN_    LINEAR  
        #NOI_    NO INTERPOLATION    Use for surface or 2D  variables only 
        varStr= 'CUB_'+varName


        #get info on P0 and desired variable
        p0 = _getVar(fileName, 'P0',       
                     datev=cmcTimestamp,   
                     ip1=None, ip2=None, ip3=None,
                     ig1=ig1,  ig2=ig2,  ig3=ig3,
                     typvar=typvar, etiquette=etiquette)
        if p0 is None:
            raise ValueError('P0 is necessary for vertical interpolation')

        var = _getVar(fileName, varName,       
                     datev=p0['meta']['datev'],   
                     ip1=None, ip2=None, ip3=None,
                     ig1=ig1,  ig2=ig2,  ig3=ig3,
                     typvar=typvar, etiquette=etiquette,
                     metaOnly=True)
        if var is None:
            raise ValueError(varName+'not found in source fst file')
         
        #files necessary for vertical interpolation
        directives_file = tmpDir+'/'+randStr+'directives'
        src_p0_file     = tmpDir+'/'+randStr+'srcP0File.fst'
        pxsFile         = tmpDir+'/'+randStr+'tempPxsFile.fst'
        interpFile      = tmpDir+'/'+randStr+'interplated.fst'

        #check that variable and p0 are on same grid
        if (p0['meta']['ig1'] == var['meta']['ig1']) and (p0['meta']['ig2'] == var['meta']['ig2']) :
            #P0 and var are on the same grid

            #first step is to get P0 in the pxs file
            try:
               iunit = rmn.fstopenall(pxsFile,rmn.FST_RW)
            except:
               raise rmn.FSTDError("File not found/readable: %s" % pxsFile)
             
            try:
               # Write P0 record + grid identifiers
               p0Entry = p0['meta']
               p0Entry['d'] = np.asfortranarray(p0['values'],dtype='float32')
               rmn.fstecr(iunit, p0Entry)
               rmn.writeGrid(iunit, p0['grid'])
               rmn.fstecr(iunit, p0['toctoc'])
            except:
               raise RuntimeError('something went wrong writing P0 fst file')
            finally:
                # always close file
                rmn.fstcloseall(iunit)
        else:
            #p0 and variable are on the same grid
            #interpolate p0 to variable grid
            #   Not sure this is needed anymore.... 
            raise RuntimeError('hinterp with P0 on a different grid not yet implemented')
            #;P0 and var are NOT on the same grid, interpolate P0 to the variable grid
            #;copy p0 at desired time
            #;write directives file
            #OPENW,  lun, directives_file, /GET_LUN
            #PRINTF, lun, " desire(-1,['>>','^^','^>','!!'])"
            #PRINTF, lun, " desire(-1,['P0'],-1,"+STRING(datev,FORMAT='(i012)')+")"
            #FREE_LUN, lun
            #;copy necessary info in intermediate file
            #cmd='editfst -s '+origin_filename      + $
            #                ' -d '+src_p0_file     + $
            #                ' -i '+directives_file
            #print, cmd
            #SPAWN, cmd, output, errstat
            #print, output

            #;remove tmp files
            #SPAWN, 'rm -f '+directives_file      
            #;write pgsm directives file
            #OPENW,  lun, directives_file, /GET_LUN
            #PRINTF, lun, " sortie(STD,4000,A)"
            #PRINTF, lun, " grille(TAPE2,"+STRING(header_var.ig1,header_var.ig2,header_var.ig3,FORMAT='(i5,",",i5,",",i1)')+")"
            #PRINTF, lun, " setintx(LINEAIR)"
            #PRINTF, lun, " heure(TOUT)"
            #PRINTF, lun, " champ('P0')"
            #FREE_LUN, lun
            #cmd = 'pgsm    -iment '+src_p0_file     + $ 
            #      '        -ozsrt '+pxsFile        + $
            #      '        -i     '+directives_file
            #SPAWN, cmd, status, errstat
            #;if process was not sucessful stop
            #IF errstat NE 0 THEN BEGIN
            #    err_mes = 'Something went wrong with PGSM' +newline+$
            #              'CMD: '+cmd
            #    MESSAGE, err_mes, INFORMATIONAL=informational
            #ENDIF
            #;remove tmp files
            #SPAWN, 'rm -f '+directives_file      
            #SPAWN, 'rm -f '+src_p0_file      

        #Do the interpolation
        #make sure interpolation packsge is loaded
        try:
            path = subprocess.check_output(["which", "d.pxs2pxt"])
        except:
            raise RuntimeError('you must load pxs2pxt:   . ssmuse-sh -d eccc/cmd/cmdn/pxs2pxt/3.16.6/default')
        
        cmd= ['d.pxs2pxt', '-s'    , fileName,
                           '-datev', '{:07d}'.format(p0['meta']['datev']),
                           '-d'    , interpFile, 
                           '-pxs'  , pxsFile,
                           '-plevs', levelStr,
                           '-var'  , varStr ]
        try:
            subprocess.run(cmd)
        except:
            raise RuntimeError('Something went wrong with pxs2pxt')

        #cleanup
        os.remove(pxsFile)

        #change fileToRead to interpolated data file
        fileToRead = interpFile

    #END vertical interpolation if statement --------------------------------

    #get fst data for output
    var = _getVar(fileToRead, varName,       
                  datev=cmcTimestamp,   
                  ip1=ip1, ip2=ip2, ip3=ip3,
                  ig1=ig1, ig2=ig2, ig3=ig3,
                  typvar=typvar, etiquette=etiquette)

    #get 3D pressure if requested
    if (var is not None) and presFromVar :

        #error trapping done by _getVar above
        iunit = rmn.fstopenall(fileToRead,rmn.FST_RO)

        try:
            #linked ip1/ig1 ip2/ig2
            vgrid = vgd.vgd_read(iunit, ip1=var['meta']['ig1'], ip2=var['meta']['ig2'])
        except:
            rmn.fstcloseall(iunit)
            raise RuntimeError('something went wrong getting vertical grid descriptor')

        try:
            thisDatev = cmcTimestamp if cmcTimestamp is not None else -1
            press = fstd3d.get_levels_press(iunit, vgrid, var['values'].shape[0:2], var['ip1List'],
                                            datev=thisDatev)
        except:
            raise RuntimeError('something went wrong with pressure retrieval')
        finally:
            rmn.fstcloseall(iunit)

        #add pressure to output dictionary
        var['pressure'] = press['phPa']


    #get latitude and longitude if requested
    if (var is not None) and latlon == True :
        llDict = rmn.gdll(var['grid'])
        var['lat'] = llDict['lat']
        var['lon'] = llDict['lon']

    return var

#end of getData





def _getVar(fileName, varName,       
             datev=None,           #input
             ip1=None, ip2=None, ip3=None,
             ig1=None, ig2=None, ig3=None,
             typvar=None, etiquette=None,
             metaOnly=False, verbose=0, skipNonFst=False) :
    """
    get variable in fst file

        Search can be restricted to certain ip123, ig123, typvar and etiquette.

        It is also possible to obtain a subset of vertical levels by providing a 
        list of desired ip1s
        
        If the keyword **ip1** is not specified fst entries with the 
        the same meta but different ip1s will be concatenated into a 3d array for output

        The smallest k index will correspond to the lowest vertical level.

        if metaOnly=True the routine returns the meta data for the first entry and stops

    """
    import numpy as np
    import rpnpy.librmn.all as rmn
    import warnings

    if not rmn.isFST(fileName) :
        if skipNonFst == False :
            #default behaviour is to abort on non FST files
            raise rmn.FSTDError("Not an FSTD file: %s " % fileName)
        else :
            #with skipNonFst=True, None is returned without error
            return None
     
    # Open
    try:
        iunit = rmn.fstopenall(fileName,rmn.FST_RO)
    except:
        raise rmn.FSTDError("File not found/readable: %s" % fileName)
     
    #look for first entry matching search criteria 
    if type(ip1) is list :
        for myip1 in ip1 :
            keyDict = _myFstinf(iunit, datev=datev, etiket=etiquette, 
                                ip1=myip1, ip2=ip2, ip3=ip3, 
                                ig1=ig1, ig2=ig2, ig3=ig3, 
                                typvar=typvar, nomvar=varName)
            if keyDict is not None:
            # found at least one record
                break
    else:
        keyDict = _myFstinf(iunit, datev=datev, etiket=etiquette, 
                            ip1=ip1, ip2=ip2, ip3=ip3, 
                            ig1=ig1, ig2=ig2, ig3=ig3, 
                            typvar=typvar, nomvar=varName)

    if keyDict is None :
        nz = 0
        is_there = False
        rmn.fstcloseall(iunit)
        if verbose > 0 :
            print('Did not find anything in:')
            print(fileName)
            print('with:')
            print('varName='     , varName)
            print('datev='       , datev)
            if datev is not None:
                try:
                    (yyyymmdd, hhmmsshh) = rmn.newdate(rmn.NEWDATE_STAMP2PRINT, int(datev))
                except rmn.RMNBaseError:
                    print('Invalid CMC datestamp')
                print('       yyyymmdd hhmmss: ', yyyymmdd, hhmmsshh)
            print('ip1='         , ip1)
            print('ip2='         , ip2)
            print('ip3='         , ip3)
            print('ig1='         , ig1)
            print('ig2='         , ig2)
            print('ig3='         , ig3)
            print('typvar='      , typvar)
            print('etiquette='   , etiquette)

    else:
        #there is at least one good entry

        #get meta for this entry
        nz = 1
        refMeta = rmn.fstprm(keyDict['key'])
        grid    = rmn.readGrid(iunit, refMeta)
        toctoc  = rmn.fstlir(iunit,nomvar='!!',ip1=refMeta['ig1'],ip2=refMeta['ig2'])
        (rp1, rp2, rp3) = rmn.DecodeIp(refMeta['ip1'],refMeta['ip2'],refMeta['ip3'])

        if metaOnly :
            return {'meta':refMeta,'grid':grid,'toctoc':toctoc}

        if ip1 is None :
            #ip1 keyword not provided
            #try to find matching entries for 3D field
            #with same meta but different ip1

            #save ip1, and key for later
            keyList = [keyDict['key']]
            ip1List = [refMeta['ip1']]
            levList = [rp1.v1]

            keyDict, keepThisOne = _myFstinfx(keyDict, iunit, datev=refMeta['datev'], etiket=refMeta['etiket'], 
                                              ip1=None,           ip2=refMeta['ip2'], ip3=refMeta['ip3'], 
                                              ig1=refMeta['ig1'], ig2=refMeta['ig2'], ig3=refMeta['ig3'], 
                                              typvar=refMeta['typvar'], nomvar=refMeta['nomvar'])

            while (keyDict is not None) :

                if keepThisOne : 
                    #we have a valid entry save info for later
                    nz += 1
                    meta = rmn.fstprm(keyDict['key'])
                    (rp1, rp2, rp3) = rmn.DecodeIp(meta['ip1'],meta['ip2'],meta['ip3'])
                    #save ip1, and key for later
                    keyList.append(keyDict['key'])
                    ip1List.append(meta['ip1'])
                    levList.append(rp1.v1)

                #check if there are entries with same meta but different ip1
                keyDict, keepThisOne = _myFstinfx(keyDict, iunit, datev=refMeta['datev'], etiket=refMeta['etiket'], 
                                                  ip1=None,           ip2=refMeta['ip2'], ip3=refMeta['ip3'], 
                                                  ig1=refMeta['ig1'], ig2=refMeta['ig2'], ig3=refMeta['ig3'], 
                                                  typvar=refMeta['typvar'], nomvar=refMeta['nomvar'])
        elif type(ip1) is list :
            nz = 0
            keyList = []
            ip1List = []
            levList = []
            for myip1 in ip1:
                #check if there are entries with same meta 
                keyDict = _myFstinf(iunit, datev=refMeta['datev'], etiket=refMeta['etiket'], 
                                                 ip1=myip1,           ip2=refMeta['ip2'], ip3=refMeta['ip3'], 
                                                 ig1=refMeta['ig1'], ig2=refMeta['ig2'], ig3=refMeta['ig3'], 
                                                 typvar=refMeta['typvar'], nomvar=refMeta['nomvar'])

                if keyDict is not None : 
                    #we have a valid entry save info for later
                    nz += 1
                    meta = rmn.fstprm(keyDict['key'])
                    (rp1, rp2, rp3) = rmn.DecodeIp(meta['ip1'],meta['ip2'],meta['ip3'])
                    #save ip1, and key for later
                    keyList.append(keyDict['key'])
                    ip1List.append(meta['ip1'])
                    levList.append(rp1.v1)
                else:
                    raise ValueError('No entries in fst file with ip1: '+str(myip1))

    #read data 
    if nz == 0 :
        return None
    else:

        #desired output to numpy
        keyArr = np.array(keyList)
        ip1Arr = np.array(ip1List)
        levArr = np.array(levList)

        #sorted unique indices
        dum, inds = np.unique(levArr, return_index=True)
        #reverse order      hyb=1. is the lowest level
        revInds = np.flip(inds)

        #raise error if there are non-unique levels represented
        if ip1Arr.shape != revInds.shape:
            warnings.warn('Found more than one entry in fst file with same meta; this may or may not be bad... ; adjusting nz')
            nz = len(revInds)

        #sorted arrays
        keyArr = keyArr[revInds]
        ip1Arr = ip1Arr[revInds]
        levArr = levArr[revInds]

        #read output
        shape =  (refMeta['shape'][0],refMeta['shape'][1],nz)
        values = np.zeros(shape, order='F', dtype='float32')
        for kk in range(nz):
            dum = rmn.fstluk(keyArr[kk].item())
            values[:,:,kk] = dum['d']

    # Close file
    rmn.fstcloseall(iunit)

    return {'values':np.squeeze(values), 
            'meta':refMeta,
            'grid':grid,
            'toctoc':toctoc,
            'ip1List':ip1Arr.tolist(),
            'levList':levArr.tolist()}

#end _getVar---------------------------


def _myFstinf(iunit, datev=None, etiket=None, 
             ip1=None, ip2=None, ip3=None, 
             ig1=None, ig2=None, ig3=None, 
             typvar=None, nomvar=None):
    """
    Wrapper for fstinf that allow :
        - parameters to have the None value
        - filtering with the IGs
    """
    import rpnpy.librmn.all as rmn

    #defaults for fstinf
    if datev        is None : datev=-1
    if ip1          is None : ip1=-1
    if ip2          is None : ip2=-1
    if ip3          is None : ip3=-1
    if typvar       is None : typvar=' '
    if etiket       is None : etiket=' '

    keyDict = rmn.fstinf(iunit, datev=datev, etiket=etiket, 
                         ip1=ip1, ip2=ip2, ip3=ip3, 
                         typvar=typvar, nomvar=nomvar)

    if (keyDict is not None) and ( (ig1 is not None) or (ig2 is not None) or (ig3 is not None) ) :

        #get meta
        meta = rmn.fstprm(keyDict['key'])

        #extra filtering of the IGs
        #   key is set to None if no match
        if ig1 is not None:
            if ig1 != meta['ig1']:
                keyDict = None
        if ig2 is not None:
            if ig2 != meta['ig2']:
                keyDict = None
        if ig3 is not None:
            if ig3 != meta['ig3']:
                keyDict = None

    return keyDict


def _myFstinfx(key, iunit, datev=None, etiket=None, 
              ip1=None, ip2=None, ip3=None, 
              ig1=None, ig2=None, ig3=None, 
              typvar=None, nomvar=None):
    """
    Wrapper for fstinfx that allow :
        - parameters to have the None value
        - filtering with the IGs

    Returns
    key         as usual
    keepThisOne   a flag to indicate that a match was not found with the provided IGs
    """
    import rpnpy.librmn.all as rmn

    #defaults for fstinfx
    if datev        is None : datev=-1
    if ip1          is None : ip1=-1
    if ip2          is None : ip2=-1
    if ip3          is None : ip3=-1
    if typvar       is None : typvar=' '
    if etiket       is None : etiket=' '

    keepThisOne=True
    keyDict = rmn.fstinfx(key, iunit, datev=datev, etiket=etiket, 
                          ip1=ip1, ip2=ip2, ip3=ip3, 
                          typvar=typvar, nomvar=nomvar)

    if (keyDict is not None) and ( (ig1 is not None) or (ig2 is not None) or (ig3 is not None) ) :

        #get meta
        meta = rmn.fstprm(keyDict['key'])

        #extra filtering of the IGs
        #   key is set to None if no match
        if ig1 is not None:
            if ig1 != meta['ig1']:
                keepThisOne=False
        if ig2 is not None:
            if ig2 != meta['ig2']:
                keepThisOne=False
        if ig3 is not None:
            if ig3 != meta['ig3']:
                keepThisOne=False

    return keyDict, keepThisOne

if __name__ != '__main__' :

    import rpnpy.librmn.all as rmn
    #this is not a great option but it will only print
    # "c_fstopi option MSGLVL set to 6"
    #once

    #less verbose outputs on import
    rmn.fstopt(rmn.FSTOP_MSGLVL, rmn.FSTOPI_MSG_ERROR)


