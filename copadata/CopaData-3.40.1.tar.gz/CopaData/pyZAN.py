import pyodbc
import pandas as pd
from pandas.io.sql import DatabaseError
import datetime

class Server:
    """This class handles a connection to a zenon Analyzer metadata database and read or writes data."""

    def __init__(self, server:str, 
    metadb:str, 
    analyzer_major_version:int= 3, 
    use_integrated_security:bool = True, 
    user:str = None, 
    password:str = None):
        """Initializes a new connection to a zenon Analyzer metadata database.
        
        Parameters
        ----------
        server: `string`
            zenon Analyzer server computer name, e.g. 'localhost'

        metadb: `string`
            zenon Analyzer metadata database name, e.g. 'ZA_DATA'

        analyzer_major_version: `int`
            zenon Analyzer major version, e.g. 3 for 3.30, 3.40, ...

        use_integrated_security: `bool`
            Connect to the database using current windows credentials 

        user: `string`
            provided if use_integrated_security=False, sql user name 

        password: `string`
            provided if use_integrated_security=False, sql password   

        Examples
        --------   
        Connect to the local Analyzer metadata database 'REPORTING':

        >>> zan = Analyzer.Server( server='localhost', metadb='REPORTING')  
        """

        """The minimum zenon Analyzer version is 3.30."""
        if(analyzer_major_version >= 3):
            self._server = "{0}\ZA{1}".format(server, str(analyzer_major_version))
            self._metadb = metadb
            self._useIntegratedSecurity = use_integrated_security
            self._user = user
            self._password = password
            self._cnxn = None
            
            if self._useIntegratedSecurity : 
                self._cnxn = pyodbc.connect("DRIVER={SQL Server Native Client 11.0};Server="
                + self._server + "; Initial Catalog ="
                + self._metadb + "; Trusted_Connection=Yes")
            else:
                self._cnxn = pyodbc.connect("DRIVER={SQL Server Native Client 11.0};Server="
                + self._server + "; Initial Catalog ="
                + self._metadb + "; User = "
                + self._user + "; Password = " + self._password)

            #Check zenon Analyzer metadata database version. Must be at least version 7 for 3.30
            try:
                result = pd.read_sql(
                    f"SELECT [{self._metadb}].[dbo].[zrsGetDatabaseVersion]()", self._cnxn)
                self._version = result.iloc[0][0]
                if(self._version < 7):
                    raise RuntimeError(f"zenon Analyzer metadata database version {str(self._version)} ist not supported")
            except:
              raise RuntimeError("Unable to check zenon Analyzer metadata database version")              
        else:
           raise RuntimeError(f"Invalid zenon Analyzer major version {analyzer_major_version}! The major version must be 3 or higher.")    


    def read_MetaData_Archives(self)->pd.DataFrame:
        """Lists all archives from the connected zenon Analyzer metadata database

        Returns
        --------
        DataFrame: [ID, PROJECT_ID, REFERENCE, VISUALNAME, DESCRIPTION, CYCLETIME LOTARCHIV, PARENT_ID]
        """ 

        sqlCmd = f"SELECT [ID],[PROJECT_ID],[REFERENCE],[VISUALNAME],[DESCRIPTION],[CYCLETIME],[LOTARCHIV],[PARENT_ID] FROM [{self._metadb}].[dbo].[ARCHIV]"
        try:
            return pd.read_sql(sqlCmd, self._cnxn)
        except:
           raise RuntimeError("Unable to load archives from table")       


    def read_MetaData_Equipments(self)->pd.DataFrame:
        """Lists all equipment groups from the connected zenon Analyzer metadata database

        Returns
        --------
        DataFrame: [ID, REFERENCE, VISUALNAME, DESCRIPTION, NESTINGLEVEL, PARENT_ID, MODEL_ID]
        """   

        sqlCmd = f"SELECT [ID],[REFERENCE],[VISUALNAME],[DESCRIPTION],[NESTINGLEVEL],[PARENT_ID],[MODEL_ID] FROM [{self._metadb}].[dbo].[EQUIPMENT]"
        try:
            return pd.read_sql(sqlCmd, self._cnxn)
        except:
           raise RuntimeError("Unable to load equipment groups from table")     


    def read_MetaData_Projects(self)->pd.DataFrame:
        """Lists all projects from the connected zenon Analyzer metadata database

        Returns
        --------
        DataFrame: [ID, REFERENCE, VISUALNAME, DESCRIPTION]
        """  

        sqlCmd = f"SELECT [ID],[REFERENCE],[VISUALNAME],[DESCRIPTION] FROM [{self._metadb}].[dbo].[PROJECT]"
        try:
            return pd.read_sql(sqlCmd, self._cnxn)
        except:
           raise RuntimeError("Unable to load projects from table")


    def read_MetaData_Variables(self)->pd.DataFrame:
        """Lists all variables from the connected zenon Analyzer metadata database

        Returns
        --------
        DataFrame: [ID, PROJECT_ID, REFERENCE, VISUALNAME, DESCRIPTION, MEANINGS, UNIT]
        """  

        sqlCmd = f"SELECT [ID],[PROJECT_ID],[REFERENCE],[VISUALNAME],[DESCRIPTION],[MEANING],[UNIT] FROM [{self._metadb}].[dbo].[VARIABLE]"
        try:
            return pd.read_sql(sqlCmd, self._cnxn)
        except:
           raise RuntimeError("Unable to load variables from table")


    def read_Metadata_VariablesInArchives(self, archive_references:[]=None, project_references:[]=None)-> pd.DataFrame:
        """Lists archive variables filtered by archive and project references

        Parameters
        ----------
        archive_references: `list`
            Filter for archive references. 
            Only the variables from the archives filter will be returned. 
            If the list is empty variables for all archive will be returned. 

        project_reference: `list`
            Filter for project references. 
            Only the archive variables from the project filter will be returned. 
            If the list is empty archive variables from all projects will be returned. 

        Returns
        --------
        DataFrame: [ID, PROJECT_ID, REFERENCE, VISUALNAME, DESCRIPTION, MEANINGS, UNIT]
        """  
        variables = self.read_MetaData_Variables()
        archives = self.read_MetaData_Archives()

        if archive_references != None:
            archives = archives[archives.REFERENCE.isin(archive_references)]

        if project_references != None:
            projects = self.read_MetaData_Projects()
            archives = archives[archives.PROJECT_ID.isin(projects[projects.REFERENCE.isin(project_references)].ID)]
            
        result = self.read_MetaData_Variable_Archive_Relationship()
        ids = result[result.ARCHIV_ID.isin(archives.ID)].VARIABLE_ID
        return variables[variables.ID.isin(ids)]


    def read_Metadata_VariablesInEquipmentGroups(self, equipmentgroup_references:[]=None, project_references:[]=None)-> pd.DataFrame:
        """Lists variables which are linked to the equipment group filtered by equipment group and project references

        Parameters
        ----------
        equipmentgroup_references: `list`
            Filter for equipment group references. 
            Only the variables from the equipmentgroup filter will be returned. 
            If the list is empty variables for all equipment groups will be returned. 

        project_reference: `list`
            Filter for project references. 
            Only the equipment group variables from the project filter will be returned. 
            If the list is empty equipment group variables from all projects will be returned. 

        Returns
        --------
        DataFrame: [ID, PROJECT_ID, REFERENCE, VISUALNAME, DESCRIPTION, MEANINGS, UNIT]
        """  
        variables = self.read_MetaData_Variables()

        if project_references != None:
            projects = self.read_MetaData_Projects()
            variables = variables[variables.PROJECT_ID.isin(projects[projects.REFERENCE.isin(project_references)].ID)] 

        equipments = self.read_MetaData_Equipments()
        if equipmentgroup_references != None:
            equipments = equipments[equipments.REFERENCE.isin(equipmentgroup_references)]
        
        ev = self.read_MetaData_Variable_Equipment_Relationship()
        ids = ev[ev.EQUIPMENT_ID.isin(equipments.ID)].VARIABLE_ID
        return variables[variables.ID.isin(ids)]


    def read_Metadata_ArchivesInEquipmentGroups(self, equipmentgroup_references:[]=None, project_references:[]=None)-> pd.DataFrame:
        """Lists archives which are linked to the equipment group filtered by equipment group and project references

        Parameters
        ----------
        equipmentgroup_references: `list`
            Filter for equipment group references. 
            Only the archives from the equipment group filter will be returned. 
            If the list is empty archives for all equipment groups will be returned. 

        project_reference: `list`
            Filter for project references. 
            Only the equipment group archives from the project filter will be returned. 
            If the list is empty equipment group archives from all projects will be returned. 

        Returns
        --------
        DataFrame: [ID, PROJECT_ID, REFERENCE, VISUALNAME, DESCRIPTION, CYCLETIME, LOTARCHIV, PARENT_ID]
        """  
        archives = self.read_MetaData_Archives()
        equipments = self.read_MetaData_Equipments()

        if equipmentgroup_references != None:
            equipments = equipments[equipments.REFERENCE.isin(equipmentgroup_references)]
        
        av = self.read_MetaData_Archive_Equipment_Relationship()
        ids = av[av.EQUIPMENT_ID.isin(equipments.ID)].ARCHIV_ID
        archives = archives[archives.ID.isin(ids)]

        if project_references != None:
            projects = self.read_MetaData_Projects()
            archives = a[a.PROJECT_ID.isin(p[p.REFERENCE.isin(project_references)].ID)]

        return archives


    def read_Metadata_ArchivesInProjects(self, project_references:[]= None)-> pd.DataFrame:
        """Lists archives filtered by project references

        Parameters
        ----------
        project_reference: `list`
            Filter for project references. 
            Only the archives from the project filter will be returned. 
            If the list is empty archives from all projects will be returned. 

        Returns
        --------
        DataFrame: [ID, REFERENCE, VISUALNAME, DESCRIPTION, SERVER, STANDBY]
        """  
        projects = self.read_MetaData_Projects()

        if project_references != None:
            projects = projects[projects.REFERENCE.isin(project_references)]

        archives = self.read_MetaData_Archives()
        return archives[archives.PROJECT_ID.isin(projects.ID)]


    def read_MetaData_EventClasses(self)->pd.DataFrame:
        """Lists all alarm/event classes from the connected zenon Analyzer metadata database

        Returns
        --------
        DataFrame: [ID, REFERENCE, VISUALNAME, DESCRIPTION]
        """   

        sqlCmd = f"SELECT [ID],[REFERENCE],[VISUALNAME],[DESCRIPTION] FROM [{self._metadb}].[dbo].[EVENTCLASS]"
        try:
            return pd.read_sql(sqlCmd, self._cnxn)
        except:
           raise RuntimeError("Unable to load alarm/event classes from table")


    def read_MetaData_EventGroups(self)->pd.DataFrame:
        """Lists all alarm/event groups from the connected zenon Analyzer metadata database

        Returns
        --------
        DataFrame: [ID, REFERENCE, VISUALNAME, DESCRIPTION]
        """  

        sqlCmd = f"SELECT [ID],[REFERENCE],[VISUALNAME],[DESCRIPTION] FROM [{self._metadb }].[dbo].[EVENTGROUP]"
        try:
            return pd.read_sql(sqlCmd, self._cnxn)
        except:
           raise RuntimeError("Unable to load alarm/event groups from table")


    def read_MetaData_Archive_Equipment_Relationship(self)->pd.DataFrame:
        """Lists all archives assignments to equipment groups from the connected zenon Analyzer metadata database

        Returns
        --------
        DataFrame: [EQUIPMENT_ID, ARCHIV_ID]
        """  

        sqlCmd = f"SELECT [EQUIPMENT_ID],[ARCHIV_ID] FROM [{self._metadb}].[dbo].[ARCHIVEQUIPMENT]"
        try:
            return pd.read_sql(sqlCmd, self._cnxn)
        except:
           raise RuntimeError("Unable to load archives assignments to equipment groups from table")     


    def read_MetaData_Variable_Equipment_Relationship(self)->pd.DataFrame:
        """Lists all variables assignments to equipment groups from the connected zenon Analyzer metadata database

        Returns
        --------
        DataFrame: [EQUIPMENT_ID, VARIABLE_ID]
        """   

        sqlCmd = f"SELECT [EQUIPMENT_ID],[VARIABLE_ID] FROM [{self._metadb}].[dbo].[VARIABLEEQUIPMENT]"
        try:
            return pd.read_sql(sqlCmd, self._cnxn)
        except:
           raise RuntimeError("Unable to load variables assignments to equipment groups from table")     


    def read_MetaData_Variable_Archive_Relationship(self)->pd.DataFrame:
        """Lists all variables assignments to archives from the connected zenon Analyzer metadata database

        Returns
        --------
        DataFrame: [ARCHIV_ID, VARIABLE_ID, COMPRESSION]
        """  

        sqlCmd = f"SELECT [ARCHIV_ID],[VARIABLE_ID],[COMPRESSION] FROM [{self._metadb}].[dbo].[VARIABLEARCHIV]"
        try:
            return pd.read_sql(sqlCmd, self._cnxn)
        except:
           raise RuntimeError("Unable to load archives assignments to equipment groups from table") 
    

    def read_Online_Alarms(self, time_from:datetime, time_to:datetime, 
    project_reference:str = None, 
    connector:str ="zenonV6", 
    variable_references = [], 
    event_class_references = [],
    event_group_references = [],
    contextlist_ids  =[],
    show_visualnames:bool = False
    )->pd.DataFrame: 
        """Lists all active alarm items from the selected project. 
        
        'time_from', 'time_to' and 'project_reference' must be set.

        Possible filtering: variable names, alarm/event classes, alarm/event groups or alarm causes

        Parameters
        ----------
        time_from: `datetime`   
            Time filter begin in UTC.

        time_to: `datetime`
            Time filter end in UTC.

        project_reference: `string`
            Reference of the project from which the alarms should be read.
            To get the project reference use the function 'read_MetaData_Projects'.

        connector: `string`
            zenon Connectors: 'zenonV6' or 'zenonSQL'

        variable_references: `list`
            Filter for variable references. 
            Only the alarms of the list will be returned. 
            If the list is empty alarms for all variables will be returned. 
            To get the variable references use the function 'read_MetaData_Variables'.

        event_class_references: `list`
            Filter for alarm/event class references. 
            Only the alarms of the list will be returned.
            If the list is empty the filter will be inactive. 
            To get the alarm/event class references use the function 'read_MetaData_EventClasses'.
        
        event_group_references: `list`
            Filter for alarm/event group references. 
            Only the alarms of the list will be returned.
            If the list is empty the filter will be inactive. 
            To get the alarm/event group references use the function 'read_MetaData_EventGroup'.

        contextlist_ids: `list`       
            Filter for context list (alarm causes) IDs. 
            Only the alarms of the list will be returned.
            If the list is empty the filter will be inactive.  
            To get the context list IDs use the function 'read_Online_ContextList'.

        show_visualnames: 'bool'  
            'False' - Returns alarm information with internal database IDs.
            'True'  - Returns alarm information with visual names.

        Returns
        --------
        with show_visualnames = false

        DataFrame: [VARIABLE_ID, LIMIT, EVENTCLASS_ID, 
        EVENTGROUP_ID, TIMECOMES, TIMEGOES, 
        TIMEACKN, TIMEREACT, COUNTREACT, USER_ID, USER_NAME, 
        COMPUTER, VISUALTEXT, VALUES, STATUSFLAGS, COMMENT, ALARM_CAUSE]

        with show_visualnames = true

        DataFrame: [VARIABLE_NAME, LIMIT, EVENTCLASS_NAME, 
        EVENTGROUP_NAME, TIMECOMES, TIMEGOES, 
        TIMEACKN, TIMEREACT, COUNTREACT, USER_ID, USER_NAME, 
        COMPUTER, VISUALTEXT, VALUES, STATUSFLAGS, COMMENT, ALARM_CAUSE_NAME]
        
        Examples
        --------   
        Get all alarms from 2019-11-14 07:30 to 2019-11-14 10:30 of project ZAD_GBL:

        >>> time_to = datetime(year=2019, month=11, day=14, hour=10, minute=30)
        >>> time_from = time_to - timedelta(hours=3)
        >>> alarms = zan.read_Online_Alarms(time_from = time_from, time_to = time_to,project_reference='ZAD_GBL')
        """  

        variables = self._convert_list_To_String(variable_references)
        event_classes = self._convert_list_To_String(event_class_references)
        event_groups = self._convert_list_To_String(event_group_references)
        contextlist = self._convert_list_To_String(contextlist_ids)
        try:
            if not  show_visualnames:
                sqlCmd = f""""SELECT * FROM [{self._metadb}].[dbo].[zrsQueryAlarmEx2Function](
                        '{self._metadb}',
                        '{self.project_reference}',
                        '{self.connector}',
                        '{self.variables}',
                        '{self.event_classes}',
                        '{self.event_groups}',
                        '{self.contextlist}',
                        '{time_from.strftime('%Y-%m-%d %H:%M:%S')}',
                        '{time_from.strftime('%Y-%m-%d %H:%M:%S')})'"""
            else:
                sqlCmd=f"""SELECT va.[VISUALNAME] as VARIABLE_NAME, 
                            al.[LIMIT], 
                            cl.[VISUALNAME] as EVENTCLASS_NAME, 
                            gr.[VISUALNAME] as EVENTGROUP_NAME, 
                            al.[TIMECOMES], 
                            al.[TIMEGOES],
                            al.[TIMEACKN],
                            al.[TIMEREACT],
                            al.[COUNTREACT],
                            al.[USER_ID],
                            al.[USER_NAME],
                            al.[COMPUTER],
                            al.[VISUALTEXT],
                            al.[VALUE],
                            al.[STATUSFLAGS],
                            al.[COMMENT],
                            ac.[NAME] as ALARM_CAUSE_NAME
                            FROM [{self._metadb}].[dbo].[zrsQueryAlarmEx2Function](
                            '{self._metadb}'
                            ,'{project_reference}'
                            ,'{connector}'
                            ,'{variables}'
                            ,'{event_classes}'
                            ,'{event_groups}'
                            ,'{contextlist}'
                            ,'{time_from.strftime('%Y-%m-%d %H:%M:%S')}'
                            ,'{time_to.strftime('%Y-%m-%d %H:%M:%S')}') al
                            LEFT JOIN [{self._metadb}].[dbo].[VARIABLE] va ON va.[ID] = al.[VARIABLE_ID]
                            LEFT JOIN [{self._metadb}].[dbo].[EVENTCLASS] cl ON cl.[ID] = al.[EVENTCLASS_ID]
                            LEFT JOIN [{self._metadb}].[dbo].[EVENTGROUP] gr ON gr.[ID] = al.[EVENTGROUP_ID]
                            LEFT JOIN [{self._metadb}].[dbo].[zrsQueryTextListFunction]
                            ('{self._metadb}','{project_reference}','{connector}') ac ON 
                            ac.[ID] = al.[ALARM_CAUSE]
                            """
            return pd.read_sql(sqlCmd, self._cnxn)

        except DatabaseError as ex:
           raise RuntimeError(ex)
        except :
            raise RuntimeError("Unable to load active alarms")
    

    def read_Online_Archive(self, time_from:datetime, time_to:datetime, 
    project_reference:str = None, 
    archive_reference:str = None, 
    connector:str ="zenonV6", 
    variable_references = [], 
    archive_aggregation:int = 0,
    show_visualnames:bool = False
    )->pd.DataFrame: 
        """Lists archive data from the selected project and archive from Runtime. 
        
        'time_from', 'time_to', 'project_reference' and 'archive_reference' must be set.

        Filtering for variable names is possible.

        Parameters
        ----------
        time_from: `datetime`   
            Time filter begin in UTC.

        time_to: `datetime`
            Time filter end in UTC.

        project_reference: `string`
            Reference of the project from which the archive data should be read.
            To get the project reference use the function 'read_MetaData_Projects'.
        
        archive_reference: `string`
            Reference of the archive from which the archive data should be read.
            To get the archive reference use the function 'read_MetaData_Archives'.

        connector: `string`
            zenon connectors: 'zenonV6' or 'zenonSQL'

        variable_references: `list`
            Filter for variable references. 
            Only the archive value from the variables in the list will be returned. 
            If the list is empty will be returned. 
            To get the variable references use the function 'read_MetaData_Variables'.

        archive_aggregation: `int`
            For basic zenon archive this attribute must be set to '0' to return raw data (default).        
            If you want data from an aggregated archive the following aggregations are possible:

               -1 = get results for all aggregation types
               0 = Raw value
               1 = Sum
               2 = Average
               3 = Minimum
               4 = Maximum

        show_visualnames: 'bool'
            'False' - returns alarm information with internal database IDs.
            'True'  - returns alarm information with visual names.

        Returns
        --------
        with show_visualnames = false

        DataFrame: [VARIABLE_ID, CALCULATION, VALUE, STRVALUE, STATUSFLAGS, TIMESTAMP]

        with show_visualnames = true

        DataFrame: [VARIABLE_NAME, CALCULATION, VALUE, STRVALUE, STATUSFLAGS, TIMESTAMP]
        
        Examples
        --------   
        Get all archive entries from 2019-11-14 07:30 to 2019-11-14 10:30 of project 'ZAD_GBL' and archive '5A':

        >>> time_to = datetime(year=2019, month=11, day=14, hour=10, minute=30)
        >>> time_from = time_to - timedelta(hours=3)
        >>> archive_data = zan.read_Online_Archive(time_from = time_from, time_to = time_to,project_name='ZAD_GBL',archive_reference='5A')
        """

        if(archive_aggregation not in range(-1, 5)):
            raise RuntimeError(f"The archive_aggregation '{str(archive_aggregation)}' is out of range!")

        variables = self._convert_list_To_String(variable_references)
        try:
            if(self._version >= 8):
                if not  show_visualnames:
                    sqlCmd = f"""SELECT * FROM [{self._metadb}].[dbo].[zrsQueryArchiveExFunction](
                            '{self._metadb}'
                            ,'{project_reference}'
                            ,'{connector}'
                            ,'{archive_reference}'
                            ,'{variables}'
                            ,'{str(archive_aggregation)}'
                            ,'{time_from.strftime('%Y-%m-%d %H:%M:%S')}'
                            ,'{time_to.strftime('%Y-%m-%d %H:%M:%S')}')"""
                else:
                    sqlCmd=f"""SELECT va.[VISUALNAME] as VARIABLE_NAME, 
                                    ar.[CALCULATION],
                                    ar.[VALUE],
                                    ar.[STRVALUE],
                                    ar.[STATUSFLAGS],
                                    ar.[TIMESTAMP]
                                FROM [{self._metadb}].[dbo].[zrsQueryArchiveExFunction](
                                '{self._metadb}'
                                ,'{project_reference}'
                                ,'{connector}'
                                ,'{archive_reference}'
                                ,'{variables}'
                                ,'{str(archive_aggregation)}'
                                ,'{time_from.strftime('%Y-%m-%d %H:%M:%S')}'
                                ,'{time_to.strftime('%Y-%m-%d %H:%M:%S')}') ar
                                JOIN [{self._metadb}].[dbo].[VARIABLE] va ON va.[ID] = ar.[VARIABLE_ID]"""
            elif(self._version == 7):
                if not  show_visualnames:
                    if(archive_aggregation == -1):
                        sqlCmd = f"""SELECT * FROM [{self._metadb}].[dbo].[zrsQueryArchiveFunction](
                                '{self._metadb}'
                                ,'{project_reference}'
                                ,'{connector}'
                                ,'{archive_reference}'
                                ,'{variables}'
                                ,'{time_from.strftime('%Y-%m-%d %H:%M:%S')}'
                                ,'{time_to.strftime('%Y-%m-%d %H:%M:%S')}')"""
                    else:
                        sqlCmd = f"""SELECT * FROM [{self._metadb}].[dbo].[zrsQueryArchiveFunction](
                                '{self._metadb}'
                                ,'{project_reference}'
                                ,'{connector}'
                                ,'{archive_reference}'
                                ,'{variables}'
                                ,'{time_from.strftime('%Y-%m-%d %H:%M:%S')}'
                                ,'{time_to.strftime('%Y-%m-%d %H:%M:%S')}')
                                WHERE [CALCULATION] = {str(archive_aggregation)}"""
                else:
                    if(archive_aggregation == -1):
                        sqlCmd=f"""SELECT va.[VISUALNAME] as VARIABLE_NAME, 
                                        ar.[CALCULATION],
                                        ar.[VALUE],
                                        ar.[STRVALUE],
                                        ar.[STATUSFLAGS],
                                        ar.[TIMESTAMP]
                                    FROM [{self._metadb}].[dbo].[zrsQueryArchiveFunction](
                                    '{self._metadb}'
                                    ,'{project_reference}'
                                    ,'{connector}'
                                    ,'{archive_reference}'
                                    ,'{variables}'
                                    ,'{time_from.strftime('%Y-%m-%d %H:%M:%S')}'
                                    ,'{time_to.strftime('%Y-%m-%d %H:%M:%S')}') ar
                                    JOIN [{self._metadb}].[dbo].[VARIABLE] va ON va.[ID] = ar.[VARIABLE_ID]"""
                    else:
                      sqlCmd=f"""SELECT va.[VISUALNAME] as VARIABLE_NAME, 
                                        ar.[CALCULATION],
                                        ar.[VALUE],
                                        ar.[STRVALUE],
                                        ar.[STATUSFLAGS],
                                        ar.[TIMESTAMP]
                                    FROM [{self._metadb}].[dbo].[zrsQueryArchiveFunction](
                                    '{self._metadb}'
                                    ,'{project_reference}'
                                    ,'{connector}'
                                    ,'{archive_reference}'
                                    ,'{variables}'
                                    ,'{time_from.strftime('%Y-%m-%d %H:%M:%S')}'
                                    ,'{time_to.strftime('%Y-%m-%d %H:%M:%S')}') ar
                                    JOIN [{self._metadb}].[dbo].[VARIABLE] va ON va.[ID] = ar.[VARIABLE_ID]
                                    WHERE [CALCULATION] = {str(archive_aggregation)}"""               
            else:
                raise RuntimeError(f"Unsupported Analyzer metadata database version {str(self._version)}!")
                            
            return pd.read_sql(sqlCmd, self._cnxn)

        except DatabaseError as ex:
           raise RuntimeError(ex)
        except :
            raise RuntimeError("Unable to load archive data from Runtime")


    def read_Online_Current_Variables_Value(self, 
    project_reference:str = None, 
    connector:str ="zenonV6", 
    variable_references = [], 
    show_visualnames:bool = False
    )->pd.DataFrame: 
        """Lists the current values of the selected zenon variables from Runtime. 
        
        'project_reference' and at least one 'variable_references' must be set.

        Parameters
        ----------

        project_reference: `string`
            Reference of the project from which the variable values should be read.
            To get the project reference use the function 'read_MetaData_Projects'.
        
        connector: `string`
            zenon Connectors: 'zenonV6' or 'zenonSQL'

        variable_references: `list`
            Filter for variable references. 
            Only the variables value of the list will be returned. 
            If the list is empty no values will be returned. 
            To get the variable references use the function 'read_MetaData_Variables'.

        show_visualnames: 'bool'
            'False' - returns variable value information with internal database IDs.
            'True'  - returns variable value information with visual names.

        Returns
        --------
        with show_visualnames = false

        DataFrame: [VARIABLE_ID, VALUE, STRVALUE, STATUSFLAGS, TIMESTAMP]

        with show_visualnames = true

        DataFrame: [VARIABLE_NAME, VALUE, STRVALUE, STATUSFLAGS, TIMESTAMP]
        
        Examples
        --------   
        Get current values of variable references 'Test_1' and 'Test_2' of project 'ZAD_GBL':

        >>> archive_data = zan.read_Online_Current_Variables_Value(project_name='ZAD_GBL', variable_reference=['Test_1', 'Test_2'])
        """

        variables = self._convert_list_To_String(variable_references)
        try:
            if not  show_visualnames:
                sqlCmd = f"""SELECT * FROM [{self._metadb}].[dbo].[zrsQueryCurrentValueFunction](
                        '{self._metadb}'
                        ,'{project_reference}'
                        ,'{connector}'
                        ,'{variables}')"""
            else:
                sqlCmd=f"""SELECT va.[VISUALNAME] as VARIABLE_NAME, 
                                cu.[VALUE],
                                cu.[STRVALUE],
                                cu.[STATUSFLAGS],
                                cu.[TIMESTAMP]
                            FROM [{self._metadb}].[dbo].[zrsQueryCurrentValueFunction](
                            '{self._metadb}'
                            ,'{project_reference}'
                            ,'{connector}'
                            ,'{variables}') cu
                            JOIN [{self._metadb}].[dbo].[VARIABLE] va ON va.[ID] = cu.[VARIABLE_ID]"""

            return pd.read_sql(sqlCmd, self._cnxn)

        except DatabaseError as ex:
           raise RuntimeError(ex)
        except :
            raise RuntimeError("Unable to load current variable values from Runtime")


    def read_Online_Events(self, time_from:datetime, time_to:datetime, 
    project_reference:str = None, 
    connector:str ="zenonV6", 
    variable_references = [], 
    event_class_references = [],
    event_group_references = [],
    include_Fildered_Event:bool = True,
    include_Event_for_not_exported_variables:bool = False,
    include_System_Events:bool = False,
    show_visualnames:bool = False
    )->pd.DataFrame: 
        """Lists all events from the selected project from Runtime. 
        
        'time_from', 'time_to' and 'project_reference' must be set.

        Possible filtering: variable names, alarm/event classes, alarm/event groups and system events.

        Parameters
        ----------
        time_from: `datetime`   
            Time filter begin in UTC.

        time_to: `datetime`
            Time filter end in UTC.

        project_reference: `string`
            Reference of the project from which the events should be read.
            To get the project reference use the function 'read_MetaData_Projects'.

        connector: `string`
            zenon Connectors: 'zenonV6' or 'zenonSQL'

        variable_references: `list`
            Filter for variable references. 
            Only the events of the list will be returned. 
            If the list is empty all variables will be returned. 
            To get the variable references use the function 'read_MetaData_Variables'.

        event_class_references: `list`
            Filter for alarm/event class references. 
            Only the alarms/events from the list will be returned.
            If the list is empty the filter is inactive. 
            To get the alarm/event class references use the function 'read_MetaData_EventClasses'.
        
        event_group_references: `list`
            Filter for alarm/event group references. 
            Only the alarms/events of the list will be returned.
            If the list is empty the filter is inactive. 
            To get the alarm/event group references use the function 'read_MetaData_EventGroup'.

        include_Fildered_Event: `bool`
            Include events for exported variables as filtered in 'variable_references', 
            'event_class_references' and 'event_group_references'.

            'False' - Variables included in the metadata database are not considered
            'True'  - Variables included in the metadata database are considered

        include_Event_for_not_exported_variables: `bool`
            Include events for not exported variables as filtered by 'event_class_references' and 
            'event_group_references'.

            'False' - Variables not included in the metadata database are not considered
            'True'  - Variables not included in the metadata database are considered
        
        show_visualnames: 'bool'
            'False' - Returns event information with internal database IDs.
            'True'  - Returns event information with visual names.

        Returns
        --------
        with show_visualnames = false

        DataFrame: [VARIABLE_ID, LIMIT, EVENTCLASS_ID, 
        EVENTGROUP_ID, TIMECOMES, USER_ID, USER_NAME, 
        COMPUTER, VISUALTEXT, VALUES, COMMENT]

        with show_visualnames = true

        DataFrame: [VARIABLE_NAME, LIMIT, EVENTCLASS_NAME, 
        EVENTGROUP_NAME, TIMECOMES, USER_ID, USER_NAME, 
        COMPUTER, VISUALTEXT, VALUES, COMMENT]
        
        Examples
        --------   
        Get all events from 2019-11-14 07:30 to 2019-11-14 10:30 of project ZAD_GBL:

        >>> time_to = datetime(year=2019, month=11, day=14, hour=10, minute=30)
        >>> time_from = time_to - timedelta(hours=3)
        >>> alarms = zan.read_Online_Events(time_from = time_from, time_to = time_to,project_reference='ZAD_GBL', include_System_Events = True)
        """
        
        variables = self._convert_list_To_String(variable_references)
        event_classes = self._convert_list_To_String(event_class_references)
        event_groups = self._convert_list_To_String(event_group_references)
        has_fildered_Events = self._convert_bool_To_String(include_Fildered_Event)
        has_filder_for_not_exported_variables = self._convert_bool_To_String(include_Event_for_not_exported_variables)
        need_System_Events = self._convert_bool_To_String(include_System_Events)

        try:
            if not  show_visualnames:
                sqlCmd = f"""SELECT * FROM [{self._metadb}].[dbo].[zrsQueryEventEx2Function](
                        '{self._metadb}'
                        ,'{project_reference}'
                        ,'{connector}'
                        ,'{variables}'
                        ,'{event_classes}'
                        ,'{event_groups}'
                        ,'{time_from.strftime('%Y-%m-%d %H:%M:%S')}'
                        ,'{time_to.strftime('%Y-%m-%d %H:%M:%S')}'
                        ,'{has_fildered_Events}'
                        ,'{has_filder_for_not_exported_variables}'
                        ,'{need_System_Events}')"""
            else:
                sqlCmd=f"""SELECT va.[VISUALNAME] as VARIABLE_NAME, 
                            ev.[LIMIT], 
                            cl.[VISUALNAME] as EVENTCLASS_NAME, 
                            gr.[VISUALNAME] as EVENTGROUP_NAME, 
                            ev.[TIMECOMES], 
                            ev.[USER_ID],
                            ev.[USER_NAME],
                            ev.[COMPUTER],
                            ev.[VISUALTEXT],
                            ev.[VALUE],
                            ev.[STATUSFLAGS],
                            ev.[COMMENT]
                            FROM [{self._metadb}].[dbo].[zrsQueryEventEx2Function](
                            '{self._metadb}'
                            ,'{project_reference}'
                            ,'{connector}'
                            ,'{variables}'
                            ,'{event_classes}'
                            ,'{event_groups}'
                            ,'{time_from.strftime('%Y-%m-%d %H:%M:%S')}'
                            ,'{time_to.strftime('%Y-%m-%d %H:%M:%S')}'
                            ,'{has_fildered_Events}'
                            ,'{has_filder_for_not_exported_variables}'
                            ,'{need_System_Events}') ev
                            LEFT JOIN [{self._metadb}].[dbo].[VARIABLE] va ON va.[ID] = ev.[VARIABLE_ID]
                            LEFT JOIN [{self._metadb}].[dbo].[EVENTCLASS] cl ON cl.[ID] = ev.[EVENTCLASS_ID]
                            LEFT JOIN [{self._metadb}].[dbo].[EVENTGROUP] gr ON gr.[ID] = ev.[EVENTGROUP_ID]
                            """
            return pd.read_sql(sqlCmd, self._cnxn)

        except DatabaseError as ex:
           raise RuntimeError(ex)
        except :
            raise RuntimeError("Unable to load events from Runtime")


    def _read_Online_Lots(self, time_from:datetime, time_to:datetime,  
    project_reference:str, 
    connector:str = "zenonV6", 
    archive_reference:str = "")->pd.DataFrame:
        """Lists the lot information of the selected project.
        Parameters
        ---------
        time_from: `datetime`   
            Time filter begin in UTC.

        time_to: `datetime`
            Time filter end in UTC.

        project_reference: `string`
            Reference of the project from which the lot archive should be returned.
            To get the project reference use the function 'read_MetaData_Projects'.

        connector: `string`
            zenon Connectors: 'zenonV6' or 'zenonSQL'
        
        archive_reference: `string`
            Archive reference of the lot archive.
            To get the archive reference use the function 'read_MetaData_Archives'.

        Returns
        --------
        DataFrame: [LOT, START, END]
        """        
        
        sqlCmd = f"""SELECT *FROM [{self._metadb}].[dbo].[zrsQueryLotFunction](
                    '{self._metadb}'
                    ,'{project_reference}'
                    ,'{connector}'
                    ,'{archive_reference}'
                    ,'{time_from.strftime('%Y-%m-%d %H:%M:%S')}'
                    ,'{time_to.strftime('%Y-%m-%d %H:%M:%S')}')"""
        try:
            return pd.read_sql(sqlCmd, self._cnxn)
        except:
           raise RuntimeError("Unable to load lot information from table")


    def read_Online_Lots(self, time_from:datetime.datetime, 
    time_to:datetime.datetime, 
    project_reference:str, 
    archive_references:[]=None)-> pd.DataFrame:
        """Lists the lot information of the selected project and archives.
        Parameters
        ---------
        time_from: `datetime`   
            Time filter begin in UTC.

        time_to: `datetime`
            Time filter end in UTC.

        project_reference: `string`
            Reference of the project from which the lot archive should be returned.
            To get the project reference use the function 'read_MetaData_Projects'.

        archive_references: `list`
            Archive references of the lot archives.
            To get the archive references use the function 'read_MetaData_Archives'.

        Returns
        --------
        DataFrame: [LOT, START, END, ARCHIVE_REFERENCE, PROJECT_REFERENCE]
        """        

        if archive_references == None:
            archives = self.read_MetaData_Archives()
            refs = archives[archives.LOTARCHIV==True].REFERENCE
        else:
            refs = archive_references

        result=pd.DataFrame()
        for ref in refs:
            archiveLots = self._read_Online_Lots(time_from=time_from, time_to=time_to, project_reference=project_reference, archive_reference=ref)
            archiveLots["ARCHIVE_REFERENCE"]= ref
            archiveLots["PROJECT_REFERENCE"]= project_reference
            result=pd.concat([result,archiveLots],ignore_index=True)

        return result


    def read_Online_LotFilteredVariableValuesFromArchive(self, lot:pd.Series)-> pd.DataFrame:
        """Lists variable values from selected lot.
        Parameters
        ---------
        lot: `pandas.core.series.Series`   
            lot.START
            lot.END
            lot.ARCHIVE_REFERENCE
            lot.PROJECT_REFERENCE      

        Returns
        --------
        DataFrame: [VARIABLE_ID, CALCULATION, VALUE, STRVALUE, STATUSFLAG, TIMESTAMP]
        
        Examples
        --------   
        Using the result from read_Online_Lots:

        >>> l = zan.read_Online_Lots(time_from=datetime.datetime(2019,12,3,12,30,0),time_to=datetime.datetime(2019,12,3,13,30,0),project_reference="Project")
        >>> vals = zan.read_Online_LotFilteredVariableValuesFromArchive(l.loc[0])
        """    
        return self.read_Online_Archive(time_from=lot.START, time_to=lot.END, archive_reference=lot.ARCHIVE_REFERENCE, project_reference=lot.PROJECT_REFERENCE)


    def read_Online_Shift(self, time_from:datetime, time_to:datetime,  
    project_reference:str, 
    connector:str = "zenonSQL", 
    equipment_group_reference:str = "",
    include_Pause:bool = True
    )->pd.DataFrame:
        """Lists the shift information of the selected project.
        Parameters
        ---------
        time_from: `datetime`   
            Time filter begin in UTC.

        time_to: `datetime`
            Time filter end in UTC.

        project_reference: `string`
            Reference of the project from which the shift information should be read.
            To get the project reference use the function 'read_MetaData_Projects'.

        connector: `string`
            zenon Connectors: 'zenonV6' or 'zenonSQL'
        
        equipment_group_reference: `string`
            Equipment group reference of the shift.
            To get the equipment group reference use the function 'read_MetaData_Equipments'.

        include_Pause: `bool`

            'False' - Only shift without pause
            'True'  - Shift and pause

        Returns
        --------
        DataFrame: [ ID, SHIFT, START, END, BREAK, PAREND_ID]
        """       
        
        with_pause = self._convert_bool_To_String(include_Pause)

        sqlCmd = f"""SELECT *FROM [{self._metadb}].[dbo].[zrsQueryShiftFunction](
                    '{self._metadb}'
                    ,'{project_reference}'
                    ,'{connector}'
                    ,'{equipment_group_reference}'
                    ,'{with_pause}'
                    ,'{time_from.strftime('%Y-%m-%d %H:%M:%S')}'
                    ,'{time_to.strftime('%Y-%m-%d %H:%M:%S')}')"""
        try:
            return pd.read_sql(sqlCmd, self._cnxn)
        except:
           raise RuntimeError("Unable to load shift information from table")


    def read_Online_ContextList(self, project_reference:str, connector:str = "zenonV6")->pd.DataFrame:
        """Lists context list (Alarm causes) from selected project.
        Parameters
        ---------
        project_reference: `string`
            Reference of the project from which the context list should be read.
            To get the project reference use the function 'read_MetaData_Projects'.

        connector: `string`
            zenon Connectors: 'zenonV6' or 'zenonSQL'

        Returns
        --------
        DataFrame: [ID, NAME, DESCRIPTION, REMOVED, PARENT_ID]
        """        
        
        sqlCmd = f"""SELECT *FROM [{self._metadb}].[dbo].[zrsQueryTextListFunction](
                    '{self._metadb}'
                    ,'{project_reference}'
                    ,'{connector}')"""
        try:
            return pd.read_sql(sqlCmd, self._cnxn)
        except:
           raise RuntimeError("Unable to load context list information from table")


    def _convert_list_To_String(self, current_list:list):
        if not current_list:
            return ""
        else:
            return ",".join(map(str, current_list))


    def _convert_bool_To_String(self, value:bool):
        if not value:
            return "0"
        else:
            return "1"