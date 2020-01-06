# System imports
import      os
import      getpass
import      argparse
import      json
import      pprint
import      subprocess
import      uuid
import      shutil
import      datetime
from        distutils.dir_util  import  copy_tree

# Project specific imports
import      pfmisc
from        pfmisc._colors      import  Colors
from        pfmisc              import  other
from        pfmisc              import  error

import      pudb
import      pftree
import      pfdicom
import      pfdicom_tagExtract

class pfdicom_agesort(pfdicom_tagExtract.pfdicom_tagExtract):
    """

    A class based on the 'pfdicom' infrastructure that processes a 
    regularly organized tree of MRI data into an explicitly constructed
    age-organized directory structure.

    This sub-class 

    """

    def externalExecutables_set(self):
        """
        A method to set the path/name of various executables.

        These results are obviously system specific, etc. 

        More sophisticated logic, if needed, should be added here.

        PRECONDITIONS:

            * None

        POSTCONIDTIONS:

            * Various names of executable helpers are set
        """
        self.exec_dcm2jpgConv           = '/usr/bin/dcmj2pnm'
        self.exec_jpgResize             = '/usr/bin/mogrify'
        self.exec_jpgPreview            = '/usr/bin/convert'
        self.exec_dcmAnon               = '/usr/bin/dcmodify'

    def sys_run(self, astr_cmd):
        """
        Simple method to run a command on the system.

        RETURN:

            * response from subprocess.run() call
        """

        pipe = subprocess.Popen(
            astr_cmd,
            stdout  = subprocess.PIPE,
            stderr  = subprocess.PIPE,
            shell   = True
        )
        bytes_stdout, bytes_stderr = pipe.communicate()
        if pipe.returncode:
            self.dp.qprint( "\n",
                            level   = 3,
                            syslog  = False)
            self.dp.qprint( "An error occured in calling \n%s\n" % pipe.args, 
                            comms   = 'error',
                            level   = 3)
            self.dp.qprint( "The error was:\n%s\n" % bytes_stderr.decode('utf-8'),
                            comms   = 'error',
                            level   = 3)
        return (bytes_stdout.decode('utf-8'), 
                bytes_stderr.decode('utf-8'), 
                pipe.returncode)

    def declare_selfvars(self):
        """
        A block to declare self variables
        """

        #
        # Object desc block
        #
        self.str_desc                   = ''
        self.__name__                   = "pfdicom_agesort"
        self.str_version                = "1.0.4"

        self.b_anonDo                   = False
        self.str_studyFileName          = 'study.json'
        self.str_DICOMthumbnail         = '300x300'
        self.b_symlinkDCMdata           = False
        self.b_doNotCleanUp             = False

        # Various executable helpers
        self.exec_dcm2jpgConv           = ''
        self.exec_jpgResize             = ''
        self.exec_jpgPreview            = ''
        self.exec_dcmAnon               = ''

        self.link                       = '.LINK'

        self.stage                      = 0

    def anonStruct_set(self):
        """
        Setup the anon struct
        """
        self.d_tagStruct = {
            "PatientName":      "anon",
            "PatientID":        "anon",
            "AccessionNumber":  "anon"
        }


    def __init__(self, *args, **kwargs):
        """
        Main constructor for object.
        """

        def tagStruct_process(str_tagStruct):
            self.str_tagStruct          = str_tagStruct
            if len(self.str_tagStruct):             
                self.d_tagStruct        = json.loads(str_tagStruct)
                self.b_anonDo           = True

        # pudb.set_trace()

        # Process some of the kwargs by the base class
        super().__init__(*args, **kwargs)

        pfdicom_agesort.declare_selfvars(self)
        pfdicom_agesort.externalExecutables_set(self)
        pfdicom_agesort.anonStruct_set(self)

        for key, value in kwargs.items():
            if key == 'tagStruct':          tagStruct_process(value)
            if key == 'verbosity':          self.verbosityLevel         = int(value)
            if key == 'studyJSON':          self.str_studyFileName      = value
            if key == 'DICOMthumbnail':     self.str_DICOMthumbnail     = value
            if key == 'symlinkDCMdata':     self.b_symlinkDCMdata       = value
            if key == 'doNotCleanUp':       self.b_doNotCleanUp         = value

        # Set logging
        self.dp                        = pfmisc.debug(    
                                            verbosity   = self.verbosityLevel,
                                            within      = self.__name__
                                            )
        self.log                       = pfmisc.Message()
        self.log.syslog(True)

    def inputReadCallback(self, *args, **kwargs):
        """
        Callback for reading files from specific directory.

        Here, we simply call the inputReadCallback of the 
        parent pfdicom_tagExtract method, which will return
        a single (middle) DCM file for tag extraction per
        series.

        """
        # pudb.set_trace()
        d_ret   = super().inputReadCallback(*args, **kwargs)

        return d_ret

    def inputReadCallbackSeries(self, *args, **kwargs):
        """
        Callback for reading files from specific directory.

        This method reads the (json) files and simply appends
        this json content into a list structure.
        """
        str_path            = ''
        l_file              = []
        b_status            = True
        l_JSONread          = []
        filesRead           = 0

        for k, v in kwargs.items():
            if k == 'l_file':   l_file      = v
            if k == 'path':     str_path    = v

        if len(args):
            at_data         = args[0]
            str_path        = at_data[0]
            l_file          = at_data[1]

        # pudb.set_trace()

        for f in l_file:
            self.dp.qprint("reading: %s/%s" % (str_path, f), level = 5)
            with open('%s/%s' % (str_path, f)) as fl:
                try:
                    d_json  = json.load(fl)
                    b_json  = True
                except:
                    b_json  = False
            b_status        = b_status and b_json
            l_JSONread.append(d_json)
            filesRead       += 1

        if not len(l_file): b_status = False

        return {
            'status':           b_status,
            'l_file':           l_file,
            'str_path':         str_path,
            'l_JSONread':       l_JSONread,
            'filesRead':        filesRead
        }

    def inputAnalyzeCallback(self, *args, **kwargs):
        """
        The initial analysis of a single DCM file is the _tagExtract()
        operation of the superclass.
        """
        # pudb.set_trace()
        d_ret   = super().inputAnalyzeCallback(*args, **kwargs)
        return d_ret

    def inputAnalyzeCallbackSeries(self, *args, **kwargs):
        """
        Callback for doing actual work on the Series data.

        Essentially, this method reads all the per-study json
        series files and creates a list of this content information.

        """
        d_JSONread          = {}
        b_status            = False
        l_json              = []
        l_file              = []
        filesAnalyzed       = 0

        # pudb.set_trace()

        for k, v in kwargs.items():
            if k == 'd_JSONread':   d_JSONread  = v
            if k == 'path':         str_path    = v

        if len(args):
            at_data         = args[0]
            str_path        = at_data[0]
            d_JSONread      = at_data[1]

        for d_JSONfileRead in d_JSONread['l_JSONread']:
            str_path    = d_JSONread['str_path']
            l_file      = d_JSONread['l_file']
            self.dp.qprint("analyzing: %s" % l_file[filesAnalyzed], level = 5)
            try:
                l_json.append(d_JSONfileRead['series']['data'][0])
            except:
                pass
            b_status    = True
            filesAnalyzed += 1

        return {
            'status':           b_status,
            'l_json':           l_json,
            'str_path':         str_path,
            'l_file':           l_file,
            'filesAnalyzed':    filesAnalyzed
        }

    def inputAnalyzeCallbackStudy(self, *args, **kwargs):
        """
        In this workflow, no "analysis" per se is performed 
        on the study.json content lists. This method is essentially
        a "nop".
        """
        d_JSONread          = {}
        b_status            = True
        filesAnalyzed       = 0

        # pudb.set_trace()

        for k, v in kwargs.items():
            if k == 'd_JSONread':   d_JSONread  = v
            if k == 'path':         str_path    = v

        if len(args):
            at_data         = args[0]
            str_path        = at_data[0]
            d_JSONread      = at_data[1]

        if not d_JSONread:  b_status    = False
        else: filesAnalyzed += 1

        return {
            'status':           b_status,
            'd_JSONread':       d_JSONread,
            'filesAnalyzed':    filesAnalyzed
        }

    @staticmethod
    def dateDiff_find(astr_date1, astr_date2):
        """
        Simply determine the date different between the
        two dates.

        Return:

            (totalDays, yearDiff, monthDiffGivenYearDiff, dayDiffGivenYearMonthDiff)

        Thus, 

            dateDiff_find('19740514', '20180821') 

        will return

            (16170, 44, 03, 07)

        or 16170 days | 44-yr/03-mo/07-da

        <astr_date1> and <astr_date2> do not have to be in chronological order.
        The function works on absolute date difference, not relative.

        Note that since months have varying length, and since this method
        uses average year and month lengths, there migth be minor day-resolution 
        rounding problems.

        For instance

            dateDiff_find( '20180101', '20190101')

        returns 11 months, 30 days; while

            dateDiff_find( '20180101', '20190102')

        returns 12 months, 00 days.


        """
        birthY, birthM, birthD  = int(astr_date1[0:4]), int(astr_date1[4:6]), int(astr_date1[6:8])
        scanY, scanM, scanD     = int(astr_date2[0:4]), int(astr_date2[4:6]), int(astr_date2[6:8])
        birthDate               = datetime.date(birthY, birthM, birthD)
        scanDate                = datetime.date(scanY, scanM, scanD)
        dateDiff                = abs(scanDate - birthDate)
                
        # How many years is this?
        YR                      = int(dateDiff.days / 365.2425)

        # How many months (after YR) is this?
        daysAfterYR             = int(dateDiff.days - (YR * 365.2425))
        MO                      = int(daysAfterYR / 30.44)

        # How many days (after YR/MO) is this?
        daysAfterYRMO           = int(daysAfterYR - (MO * 30.44))
        DA                      = daysAfterYRMO

        return (dateDiff.days, YR, MO, DA)

    def outputSaveCallback(self, at_data, **kwargs):
        """
        Callback for saving stage 1 output.

        In order to be thread-safe, all directory/file 
        descriptors must be *absolute* and no chdir()'s
        must ever be called!

        Outputs saved:
            * DICOM tag extract payload in each series dir
            * <series>-series.json with additional series info
        """
        path                = at_data[0]
        d_outputInfo        = at_data[1]

        d_ret               = super().outputSaveCallback(at_data, **kwargs)

        def jsonSeriesDescription_generate():

            def aquistionDate_determine(DCM, str_studyDate, str_seriesDate):
                """
                Try and "intelligently" determine the aquisitionDate
                given many weirdness.
                """
                str_aquisitionDate  = ""
                try:
                    str_aquisitionDate      = DCM.AcquistionDate
                except:
                    try:
                        if len(str_studyDate):
                            str_aquisitionDate  = str_studyDate
                        else:
                            str_aquisitionDate  = str_seriesDate
                    except:
                        try:
                            str_aquisitionDate  = str_seriesDate
                        except:
                            str_aquisitionDate  = ""
                if str_aquisitionDate == '19000101':
                    if str_studyDate != '19000101':
                        str_aquisitionDate  = str_studyDate
                    else:
                        str_aquisitionDate  = str_seriesDate
                return str_aquisitionDate

            def DICOMtag_lookup(DCM, str_tagName, str_notFound = ""):
                try:
                    str_tag             = getattr(DCM, str_tagName)
                except:
                    if len(str_notFound):
                        str_tag             = str_notFound
                    else:
                        str_tag             = "%s not found" % str_tagName
                return str_tag

            # pudb.set_trace()
            DCM                         = d_outputInfo['d_DCMfileRead']['d_DICOM']['dcm']
            str_jsonFileName            = '%s-series.json' % path
            str_seriesInstanceUID       = DICOMtag_lookup(DCM,  "SeriesInstanceUID")
            dcm_modalitiesInStudy       = DICOMtag_lookup(DCM,  "ModalitiesInStudy")
            str_seriesDescription       = DICOMtag_lookup(DCM,  "SeriesDescription")
            str_studyDescription        = DICOMtag_lookup(DCM,  "StudyDescription")
            str_patientID               = DICOMtag_lookup(DCM,  "PatientID")
            str_patientName             = DICOMtag_lookup(DCM,  "PatientName")
            str_seriesDate              = DICOMtag_lookup(DCM,  "SeriesDate",
                                                                "19000101")
            str_studyDate               = DICOMtag_lookup(DCM,  "StudyDate",
                                                                "19000101")
            str_patientBirthDate        = DICOMtag_lookup(DCM,  "PatientBirthDate",
                                                                "19000101")
            str_aquisitionDate          = aquistionDate_determine(  DCM,
                                                                    str_studyDate,
                                                                    str_seriesDate,)
            (days, yr, mo, da)          = pfdicom_agesort.dateDiff_find(
                                                str_patientBirthDate,
                                                str_aquisitionDate
                                        ) 
            json_obj = {
                "series": {
                    "data": [
                        {
                            "DCMinputPath" : {
                                "value":    d_outputInfo['d_DCMfileRead']['inputPath']
                            },
                            "AgeCalculated" : {
                                "value": {
                                    "daysTotal":    days,
                                    "yr":           yr,
                                    "mo":           mo,
                                    "da":           da
                                }
                            },
                        "SeriesInstanceUID": { "value": '%s' % str_seriesInstanceUID,},
                        "uid":               { "value": '%s' % str_seriesInstanceUID,},
                        "SeriesDescription": { "value": '%s' % str_seriesDescription,},
                        "StudyDescription":  { "value": '%s' % str_studyDescription,},
                        "ModalitiesInStudy": { "value": '%s' % dcm_modalitiesInStudy,},
                        "PatientID":         { "value": '%s' % str_patientID,},
                        "PatientName":       { "value": '%s' % str_patientName,},
                        "PatientBirthDate":  { "value": '%s' % str_patientBirthDate},
                        "AcquistionDate":    { "value": '%s' % str_aquisitionDate}
                        }
                    ],
                },
            }
            with open(str_jsonFileName, 'w') as f:
                json.dump(json_obj, f, indent = 4)

        jsonSeriesDescription_generate()

        return d_ret

    def outputSaveCallbackSeries(self, at_data, **kwags):
        """
        Callback for saving outputs.

        Outputs saved:
            * JSON study descriptor file. One file per study.
        """

        def age_lookup(dl_agePerStudy):
            """
            This method examines all the age-related dictionaries
            for this study and attempts to find the 'correct' age.

            Some DICOM studies contain report files which often have
            incomplete DICOM tag information. As a result, some age
            dictionaries can have incorrect age values, usually as the
            result of an AquisitionDate of 19000101 being used as a
            placeholder.

            This nested function attempts to mitigate against that
            by checking for 'daysTotal' field and ignoring that entry
            if the daysTotal exceeds 29200 (or 80 years).
            """
            for d_age in dl_agePerStudy:
                daysTotal   = d_age['AgeCalculated']['value']['daysTotal']
                if daysTotal > 29200:
                    continue
                else:
                    break
            return d_age['AgeCalculated']['value']

        path                = at_data[0]
        d_outputInfo        = at_data[1]
        other.mkdir(self.str_outputDir)
        other.mkdir(path)

        try:
            str_relPath     = path.split(self.str_outputDir+'/./')[1]
        except:
            str_relPath     = './'
        filesSaved          = 0

        d_age               = age_lookup(d_outputInfo['l_json'])
        str_studyDCMinputDir= os.path.dirname(d_outputInfo['l_json'][0]['DCMinputPath']['value'])
        str_leafNode        = '%s-%s' % (os.path.dirname(str_relPath), 
                                         os.path.basename(str_relPath).split('-')[-1])
        str_ageSortPath     = '%02d-yr/%02d-mo/%s-ex' % (d_age['yr'], d_age['mo'], str_leafNode)

        json_study          = {
            'sourcePathDCM':    str_studyDCMinputDir,    
            'sourcePathTag':    path,
            'ageSortPath':      str_ageSortPath,
            'data':             d_outputInfo['l_json']
        }

        with open('%s/%s' % (path, self.str_studyFileName), 'w') as f:
            json.dump(json_study, f, indent = 4)
            filesSaved += 1 
        f.close()

        return {
            'status':       True,
            'filesSaved':   filesSaved
        }

    def mklinks(self, oldtree, newtree):
        """
        This method (and 'linknames') is thinly adapted from:
        
        http://www.java2s.com/Code/Python/Utility/Makeacopyofadirectorytreewithsymboliclinkstoallfilesintheoriginaltree.htm

        with minor incorporation changes as well as updates to python3.
        """
        link_may_fail   = 0
        if not os.path.isdir(oldtree):
            self.dp.qprint(oldtree + ': not a directory', comms = 'error')
            return False
        try:
            other.mkdir(newtree)
        except os.error as msg:
            self.dp.qprint(newtree + ': cannot mkdir:' + msg, comms = 'error')
            return False
        linkname = os.path.join(newtree, self.link)
        try:
            os.symlink(os.path.join(os.pardir, oldtree), linkname)
        except os.error as msg:
            if not link_may_fail:
                self.dp.qprint(linkname + ': cannot symlink:' + msg, comms='error')
                return False
            else:
                self.dp.qprint(linkname + ': warning: cannot symlink:' + msg, comms='error')
        self.linknames(oldtree, newtree, self.link)
        return True

    @staticmethod
    def linknames(old, new, link):
        try:
            names = os.listdir(old)
        except os.error as msg:
            print(old + ': warning: cannot listdir:' + msg)
            return
        for name in names:
            if name not in (os.curdir, os.pardir):
                oldname = os.path.join(old, name)
                linkname = os.path.join(link, name)
                newname = os.path.join(new, name)
                if os.path.isdir(oldname) and \
                not os.path.islink(oldname):
                    try:
                        other.mkdir(newname)
                        ok = 1
                    except:
                        print(newname + \
                            ': warning: cannot mkdir:' + msg)
                        ok = 0
                    if ok:
                        linkname = os.path.join(os.pardir,
                                                linkname)
                        pfdicom_agesort.linknames(oldname, newname, linkname)
                else:
                    os.symlink(linkname, newname)

    def outputSaveCallbackStudy(self, at_data, **kwags):
        """
        Callback for saving outputs.

        This method "moves" the original study content to a new tree 
        structure based on the study patient age.

        First, this method needs to copytree the *original* image (DCM)
        tree to the new location, then it needs to copy the extracted 
        tags into that moved tree.

        It represents the terminal point of the processing stream.

        """

        path                = at_data[0]
        d_JSONStudy         = at_data[1]
        other.mkdir(self.str_outputDir)

        str_sourcePathTag   = path
        str_sourcePathDCM   = d_JSONStudy['d_JSONread']['l_JSONread'][0]['sourcePathDCM']
        str_destinationPath = '%s/%s' % (
            self.str_outputDir, 
            d_JSONStudy['d_JSONread']['l_JSONread'][0]['ageSortPath'])
        str_relPath         = './'
        try:
            str_relPath     = path.split(self.str_outputDir+'/./')[1]
        except:
            str_relPath     = './'

        # Process the orignal study tree over
        if not self.b_symlinkDCMdata:
            copy_tree(str_sourcePathDCM, str_destinationPath, preserve_symlinks = 1)
        else:
            self.mklinks(str_sourcePathDCM, str_destinationPath)

        # Now copy the tag data into this tree as well
        copy_tree(str_sourcePathTag, str_destinationPath, preserve_symlinks = 1)
        # shutil.copytree(str_sourcePathTag, str_destinationPath, symlinks = True)

        # and finally, clean up the original tag path if specified
        if not self.b_doNotCleanUp:
            # First, remove the sourcetagpath
            shutil.rmtree(str_sourcePathTag, ignore_errors = True)
            # Now we need to check if the parent is empty, and if so, 
            # remove the parent
            str_parentDir   = os.path.dirname(str_sourcePathTag)
            if not os.listdir(str_parentDir):
                shutil.rmtree(str_parentDir, ignore_errors = True)

        return {
            'status':       True,
            'filesSaved':   1
        }

    def processDCM(self, **kwargs):
        """
        The callback for the initial stage 1 process. Since stage 1 is
        really a call to the parent pfdicom_tagExtract, we shadow that
        machinery by calling the parent's callbacks here. 
        """
        d_process       = {}
        d_process       = self.pf_tree.tree_process(
                            inputReadCallback       = self.inputReadCallback,
                            analysisCallback        = self.inputAnalyzeCallback,
                            outputWriteCallback     = self.outputSaveCallback,
                            persistAnalysisResults  = False
        )
        return d_process

    def processSeries(self, **kwargs):
        """
        A simple "alias" for calling the pftree method.
        """
        # pudb.set_trace()
        d_process       = {}
        d_process       = self.pf_tree.tree_process(
                            inputReadCallback       = self.inputReadCallbackSeries,
                            analysisCallback        = self.inputAnalyzeCallbackSeries,
                            outputWriteCallback     = self.outputSaveCallbackSeries,
                            persistAnalysisResults  = False
        )
        return d_process

    def processStudy(self, **kwargs):
        """
        A simple "alias" for calling the pftree method.
        """
        d_process       = {}
        d_process       = self.pf_tree.tree_process(
                            inputReadCallback       = self.inputReadCallbackSeries,
                            analysisCallback        = self.inputAnalyzeCallbackStudy,
                            outputWriteCallback     = self.outputSaveCallbackStudy,
                            persistAnalysisResults  = False
        )
        return d_process        
    
    def processMAP(self, **kwargs):
        """
        A simple "alias" for calling the pftree method.
        """
        d_process       = {}
        d_process       = self.pf_tree.tree_process(
                            inputReadCallback       = self.inputReadCallbackMAP,
                            analysisCallback        = self.inputAnalyzeCallbackMAP,
                            outputWriteCallback     = self.outputSaveCallbackMAP,
                            persistAnalysisResults  = False
        )
        d_library = {
            "data": list(self.pf_tree.d_inputTree.keys())
            }
        self.dp.qprint("mapping: %s" % d_library, level = 1)
        with open("%s/map.json" % self.str_inputDir, 'w') as outfile:
            json.dump(d_library, outfile, indent = 4)
        
        return d_process        
    
    def filelist_prune(self, at_data, *args, **kwargs):
        """
        The filelist_prune behaves differently pending the processing stage.
        """

        # pudb.set_trace()
        if self.stage == 1:
            d_ret   = pfdicom_tagExtract.pfdicom_tagExtract.filelist_prune(self, at_data, *args, **kwargs)
        if self.stage == 2 or self.stage == 3:
            d_ret   = pfdicom.pfdicom.filelist_prune(self, at_data, *args, **kwargs)

        return d_ret

    def run(self, *args, **kwargs):
        """
        The run method calls the base class run() to 
        perform initial probe and analysis.

        Then, it effectively calls the method to perform
        the DICOM tag substitution.

        """
        b_status            = True
        d_process           = {}
        func_process        = self.processDCM
        self.str_analysis   = 'DICOM analysis'

        for k, v in kwargs.items():
            if k == 'func_process': func_process        = v
            if k == 'description':  self.str_analysis   = v
            if k == 'stage':        self.stage          = v          

        self.dp.qprint(
                "Starting pfdicom_agesort %s... (please be patient while running)" % \
                    self.str_analysis, 
                level = 1
                )

        # Run the base class, which probes the file tree
        # and does an initial analysis. Also suppress the
        # base class from printing JSON results since those 
        # will be printed by this class
        # pudb.set_trace()
        d_pfdicom       = pfdicom.pfdicom.run(
                                        self,
                                        JSONprint   = False,
                                        timerStart  = False
                                    )

        if d_pfdicom['status']:
            str_startDir    = os.getcwd()
            os.chdir(self.str_inputDir)
            if b_status:
                d_process   = func_process()
                b_status    = b_status and d_process['status']
            os.chdir(str_startDir)

        d_ret = {
            'status':       b_status,
            'd_pfdicom':    d_pfdicom,
            'd_process':    d_process,
            'runTime':      other.toc()
        }

        if self.b_json:
            self.ret_dump(d_ret, **kwargs)

        self.dp.qprint(
                'Returning from pfdicom_agesort %s...' % 
                self.str_analysis, level = 1
        )

        return d_ret
        