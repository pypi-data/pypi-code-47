import pkg_resources as _pkg_resources
import os as _os
import io as _io
import json as _json
import boto3 as _boto3
import glob as _glob
from lxml import etree as _etree
import time, re
from itertools import islice


ns = {'xs': 'http://www.w3.org/2001/XMLSchema', 'lx': 'lixi.org.au/schema/appinfo_elements', 'li': 'lixi.org.au/schema/appinfo_instructions'} 

if __name__ == '_LIXI':
    import _path_functions, _jsonschema_functions, _customise_schema, _xslt_transform 
else:    
    from lixi import _path_functions, _jsonschema_functions, _customise_schema, _xslt_transform 

class LIXI(object):
    """Represents a LIXI Instance.

    Args:
        schema_path (str): Path to a local copy of LIXI schema.
        
    The singleton class exists as a wrapper for all message manipulation functions the library is to provide.
    A LIXI schema is required because it is the underlying assumption that all LIXI members would 
    have a LIXI schema.
    """
    
    __instance = None
    
    @staticmethod 
    def getInstance():
        """ Static access method. """
        if LIXI.__instance == None:
            LIXI()
        return LIXI.__instance
    
    def __init__(self):
        """ Virtually private constructor. """      
        
        if LIXI.__instance != None:
            print("This should not have run")
        else:
            
            self.schema_folder_path = None#_pkg_resources.resource_filename(__name__, 'schema/schema')
            self.schema_index_dict = {}
            
            self.__S3_access = None
            self.__S3_secret = None
            
            self.current_transaction_type = None
            
            self.__schemas = {}
            self.__latest_versions = {}
            self.set_schema_latest_version()
            
            LIXI.__instance = self
    
    #Utility Functions
    def __write__(self, default_name, output_path, data):
        """Utility function to output a path.
        """        
        
        if _os.path.isdir(output_path):
            output_path = _os.path.join(output_path,default_name)
            
        try:
            with _io.open(output_path,'w+', encoding="utf-8") as out_file:
                out_file.write(data)            
        except Exception as e:
            raise LIXIResouceNotFoundError("Can not store at the specified path")  
        
    def set_schema_latest_version(self):
        """Utility function to get the latest version of the schema per transaction type
        """        
        
        for filename in _glob.glob(_os.path.join(_pkg_resources.resource_filename(__name__, 'xslts'),'*.zip')):
            if 'warnings' not in filename:
                filename = re.search('LIXI-([a-zA-Z0-9_-]*).zip', filename.replace('LIXI','',1)).group(1)
                
                split = filename.split('-')
                
                transaction_type = split[0]
                digit_1,digit_2,digit_3 = split[1].split('_')
                
                if transaction_type in self.__latest_versions:
                    old_version = self.__latest_versions[transaction_type]
                    olddigit_1,olddigit_2,olddigit_3 = old_version.split('_')
                    
                    if int(digit_1) > int(olddigit_1):
                        self.__latest_versions[transaction_type] = split[1]
                    elif int(digit_1) == int(olddigit_1):
                        if int(digit_2) > int(olddigit_2):
                            self.__latest_versions[transaction_type] = split[1]
                        elif int(digit_2) == int(olddigit_2):                        
                            if int(digit_3) > int(olddigit_3):
                                self.__latest_versions[transaction_type] = split[1]                            
                        
                    
                else:
                    self.__latest_versions[transaction_type] = split[1]
                
    
    def set_credentials(self, access, secret):
        """Sets the secret and access keys for a LIXI member. Provided by LIXI 
        
        Args:
            access (str): A members secret key.
            secret (str): A members secret key.

        Result:
            Sets self.__S3_access, self.__S3_secret.

        Raises:
            lixi2.LIXIInvalidSyntax: When the strings are not specified.
        """

        if access!=None and secret!=None:
            self.__S3_access = access
            self.__S3_secret = secret
        else:
            raise LIXIInvalidSyntax('Access/Secret not specified.') 
        
    def set_schema_path(self, schemapath, create_config=True):
        """Sets a default folder path to get the schemas. Usable in case Custom schemas are used
        
        Args:
            schemapath (str): An absolute folder path to schemas stored locally.

        Result:
            Sets self.__schemapath.

        Raises:
            lixi2.LIXIResouceNotFoundError: If the schema is not found at the schema path.
        """
        
        
        if schemapath!=None:
            if _os.path.exists(schemapath):
                self.schema_folder_path = str(schemapath)
                self.create_schema_index_from_folder(create_config = create_config)
            else:
                LIXIResouceNotFoundError('Schema folder path is incorrect.')
        else:
            raise LIXIResouceNotFoundError('Schema folder path not specified.')
        
    def create_schema_index_from_folder(self, reset=False, create_config=True):
        
        
        if _os.path.exists(self.schema_folder_path+'/config.json') and reset==False:
            with _io.open(self.schema_folder_path+'/config.json', encoding="utf-8") as json_index:
                self.schema_index_dict = _json.load(json_index)
        elif (create_config):
            
            #just xsd read but later on read jsons file
            
            ## ALL XSDs
            files = _glob.glob(_os.path.join(self.schema_folder_path,'*.xsd'))
            
            for filename in files:
                         
                filename = filename.replace('\\','/')
                f = _io.open(filename, mode="r", encoding="utf-8")               
                
                is_schema = False
                
                for line in islice(f,10):
                    
                    if 'lx:schemadetail' in line:
                        transactionschemasource = re.search('transactionschemasource="([A-Z0-9. ]*)"', line)
                        
                        if transactionschemasource!=None:
                            val = transactionschemasource.group(1)
                            schema_transaction_type = val.split(' ')[0]
                            self.current_transaction_type = schema_transaction_type
                            schema_version = val.split(' ')[1]
                            schema_custom_version = re.search('version="([a-zA-Z0-9_-]*)"', line).group(1)
                            schema_annotated = re.search('annotation="([a-zA-Z0-9_-]*)"', line).group(1)
                            is_schema = True
                        else:
                            schema_transaction_type = re.search('transaction="([A-Z]*)"', line).group(1)  
                            self.current_transaction_type = schema_transaction_type
                            schema_version = re.search('version="([0-9.]*)"', line).group(1)
                            schema_custom_version = None
                            schema_annotated = re.search('annotation="([a-zA-Z0-9_-]*)"', line).group(1)
                            is_schema = True
                            
                #schema_string =  f.read()
                #schema_output, schema_transaction_type, schema_version, schema_custom_version = self._parse_xml_schema(schema_string, 'xml')                
                f.close()
                
                if is_schema == True:
                    if schema_annotated == 'Full':
                        if schema_custom_version !=None:
                            self.schema_index_dict[schema_custom_version] = filename
                        else:
                            self.schema_index_dict['LIXI-'+schema_transaction_type+'-'+schema_version.replace('.','_')+'-Annotated'] = filename                  
                      

            ### ALL JSONs
            with _io.open(self.schema_folder_path+'/config.json','wb+') as outfile:
                s = _json.dumps (self.schema_index_dict, sort_keys=True, indent=4, ensure_ascii=False).encode('utf-8')
                outfile.write(s)
                              
                           
        else:
            raise LIXIResouceNotFoundError("Schema not available" + filename)
    
    def _parse_xml_schema(self, xsd_as_text, file_type, filepath):        
        
        passed = False
        schema_output = None
        
        if passed == False:
            try:
                parser = _etree.XMLParser(remove_blank_text=True)
                schema_output = _etree.fromstring(xsd_as_text, parser)
                passed = True
            except Exception as e:
                passed = False
                
        if passed == False:
            try:
                self.json_package = _json.loads(xsd_as_text)
                schema_output = _jsonschema_functions.convert_to_xml_schema(xsd_as_text)
                passed = True
            except Exception as e:
                passed = False        
        
        if passed == False:
            raise LIXIInvalidSyntax('The schema file is not well-formed\n' + str(filepath))                
        
        SchemaVersion = schema_output.xpath('./xs:element/xs:complexType/xs:sequence/xs:element[@name="SchemaVersion"]', namespaces=ns)[0]
        
        try:
            schema_transaction_type = SchemaVersion.xpath('./xs:complexType/xs:attribute[@name="LIXITransactionType"]', namespaces=ns)[0]
            schema_transaction_type = schema_transaction_type.attrib['fixed']
            self.current_transaction_type = schema_transaction_type
        except Exception as e:
            schema_transaction_type = None       
        
        try:
            schema_version = SchemaVersion.xpath('./xs:complexType/xs:attribute[@name="LIXIVersion"]', namespaces=ns)[0]
            schema_version = schema_version.attrib['fixed']
        except Exception as e:
            schema_version = None
            
        try:
            schema_custom_version = SchemaVersion.xpath('./xs:complexType/xs:attribute[@name="LIXICustomVersion"]', namespaces=ns)[0]
            schema_custom_version = schema_custom_version.attrib['fixed']            
        except Exception as e:
            schema_custom_version = None
         
        return schema_output, schema_transaction_type, schema_version, schema_custom_version                    
    
    def _read_path(self, filepath, filetype):

        cwd = _os.getcwd()
        filepath = _os.path.join(cwd, filepath)

        if _os.path.exists(filepath) == True:
            f = _io.open(filepath, mode="r", encoding="utf-8")
            schema_string =  f.read()
            f.close()
            schema_output, schema_transaction_type, schema_version, schema_custom_version = self._parse_xml_schema(schema_string, filetype, filepath)
            
            return schema_output, schema_transaction_type, schema_version, schema_custom_version
        else:
            dirlist = _os.listdir(cwd)
            raise LIXIResouceNotFoundError("Schema file not found at the specified path. | file path: " + filepath + " | file found: " + str(_os.path.exists(filepath)))    
     
    def load_schema(self, lixi_transaction_type=None, lixi_version=None, file_type="xml", custom_version=None, schema=None, schema_path=None, create_config=True):
        """Loads a LIXI schema.

        Args:
            lixi_transaction_type (str): Transaction type of the LIXI schema.
            lixi_version (str): Version of the LIXI schema.
            file_type (boolean): Indicates the type of LIXI schema provided.
            custom_version (str): Usually a complete file name of the custom schema.
            schema (str): LIXI schema as a String.
            schema_path (str): Absolute path to the LIXI schema.

        Result:
            Sets self.schema, self.annotated_schema.

        Raises:
            lixi2.LIXIResouceNotFoundError: If the schema is not found at the schema path.
            lixi2.LIXIInvalidSyntax: If the schema file is not well formed.
        """
        
        
        #Load all schemas from the folder 
        if len(self.schema_index_dict) <= 0 and self.schema_folder_path!=None and create_config:
            self.create_schema_index_from_folder(reset=False, create_config=create_config)
        
        #Read the schema into a string from the provided source. 
        if schema !=None:
            # can have json
            schema_output, schema_transaction_type, schema_version, schema_custom_version = self._parse_xml_schema(schema, file_type, 'text')
            return schema_output
            
        elif schema_path != None:
            schema_output, schema_transaction_type, schema_version, schema_custom_version = self._read_path(schema_path, file_type)
            if schema_custom_version != None:
                self.__schemas[schema_custom_version] = schema_output
                return self.__schemas[schema_custom_version]
            else:
                self.__schemas['LIXI-'+schema_transaction_type+'-'+schema_version.replace('.','_')+'-Annotated'] = schema_output
                return self.__schemas['LIXI-'+schema_transaction_type+'-'+schema_version.replace('.','_')+'-Annotated']                
            
        elif custom_version!=None:
            #best_case
            if custom_version in self.__schemas:
                return self.__schemas[custom_version]
            
            if self.schema_folder_path!=None:
                
                if custom_version not in self.schema_index_dict:
                    self.create_schema_index_from_folder(reset=True, create_config=create_config)
                
                if custom_version in self.schema_index_dict:
                    filepath = self.schema_index_dict[custom_version]
                    schema_output, schema_transaction_type, schema_version, schema_custom_version = self._read_path(filepath, file_type)
                    self.__schemas[schema_custom_version] = schema_output
                    return self.__schemas[schema_custom_version]                    
                else:
                    raise LIXIResouceNotFoundError('Custom schema '+custom_version+' not found. Please place the schema file in the specified folder.') 
            else:
                raise LIXIResouceNotFoundError('Schema folder not found. Please set a schema folder with lixi.set_schema_folder().') 

            
        elif lixi_transaction_type!=None and lixi_version!=None:
            #best_case
            schema_name = 'LIXI-'+lixi_transaction_type+'-'+lixi_version.replace('.','_')+'-Annotated'
            self.current_transaction_type = lixi_transaction_type
            
            if schema_name in self.__schemas:
                return self.__schemas[schema_name]
            
            if self.schema_folder_path!=None:
                
                if schema_name not in self.schema_index_dict and create_config:
                    self.create_schema_index_from_folder(reset=True, create_config=create_config)
                
                if schema_name in self.schema_index_dict and create_config:
                    filepath = self.schema_index_dict[schema_name]
                    schema_output, schema_transaction_type, schema_version, schema_custom_version = self._read_path(filepath, file_type)
                    self.__schemas[schema_name] = schema_output
                    return self.__schemas[schema_name]                    
                else:
                    raise Exception(lixi_transaction_type+' '+lixi_version+ ' Schema not found. Please place the schema file in the specified folder.') 
            
            
            if self.__S3_access!=None and self.__S3_secret!= None:
                session = _boto3.Session(
                    aws_access_key_id=self.__S3_access,
                    aws_secret_access_key=self.__S3_secret,
                )
                
                if file_type == 'xml':
                    schema_name2 = schema_name +'.xsd'
                elif file_type == 'json':
                    schema_name2 = schema_name.replace('-Annotated','_RFC-Annotated')
                    schema_name2 = schema_name2 + '.json'
                
                s3 = session.resource('s3')
                obj = s3.Object('lixi-schema', schema_name2)
                string_data = obj.get()['Body'].read().decode('utf-8')
                
                schema_output, schema_transaction_type, schema_version, schema_custom_version = self._parse_xml_schema(string_data, file_type, 'S3')
                self.__schemas[schema_name] = schema_output
                return self.__schemas[schema_name]                
            
            if self.__S3_access==None and self.__S3_secret== None and self.schema_folder_path==None:
                raise LIXIResouceNotFoundError('Schema folder not found. Please set a schema folder with lixi.set_schema_folder().')            
            
        else:
            raise LIXIResouceNotFoundError('Schema source not specified. Please specify a LIXI Schema as a string, Path to LIXI schema, Path to a folder that contains a LIXI schema or LIXI schema S3 credentials.')        


    def get_schema_paths(self, lixi_transaction_type = None, lixi_version=None, file_type="xml", custom_version=None, schema_string = None, schema_path=None ):
        """Get all the elements path of a LIXI schema.

        Args:
            lixi_transaction_type (str): Transaction type of the LIXI schema.
            lixi_version (str): Version of the LIXI schema.
            file_type (str): Indicates if JSON or XML LIXI schema is required.
            custom_version (str): Usually a complete file name of the custom schema.
            schema_string (str): LIXI schema as a String.
            schema_path (str): Absolute path to the LIXI schema.

        Result:
            a list of paths in the Schema 

        Raises:
            lixi2.LIXIInvalidSyntax: Validation errors for the lixi version or transaction type.
        """   
                
        schema = self.load_schema(lixi_transaction_type, lixi_version, file_type, custom_version, schema_string, schema_path)       
        
        return _path_functions.get_paths_for_schema_elements(schema)
    
    def get_schema_latest_version(self, transaction_type):
        """Gets the latest version of the schema per transaction type

        Args:
            transaction_type (str): Transaction type of the LIXI schema.

        Result:
            returns a string (X_X_X)

        Raises:
            lixi2.LIXIInvalidSyntax: Validation errors for the lixi version or transaction type.
        """  
        if transaction_type == "ACC": return self.__latest_versions['ACC']
        if transaction_type == "CAL": return self.__latest_versions['CAL']
        if transaction_type == "CDA": return self.__latest_versions['CDA']
        if transaction_type == "CNZ": return self.__latest_versions['CNZ']
        if transaction_type == "DAS": return self.__latest_versions['DAS']
        if transaction_type == "LMI": return self.__latest_versions['LMI']
        if transaction_type == "SVC": return self.__latest_versions['SVC']
        if transaction_type == "VAL": return self.__latest_versions['VAL']       
    
    
    
    #Entry Functions
    def fetch_json_schema(self,lixi_transaction_type=None, lixi_version=None, schema_string=None, schema_path=None, output_path=None): 
        """Fetches a JSON schema based on the info given.
    
        Args:
            lixi_transaction_type (str): Transaction type of the LIXI json schema to fetch.
            lixi_version (str): Version of the LIXI json schema to fetch.
            schema_string (str): LIXI schema as a String for conversion to JSON.
            schema_path (str): LIXI schema path as a String for conversion to JSON.
            output_path (str): A complete file path to store the output schema.
    
        Result:
            a customised schema as etree or saved to the output folder specified. 
    
        Raises:
            LIXIInvalidSyntax: Validation errors for the lixi version or transaction type.
            not found
        """ 
        
        output_schema = None
        
        if lixi_transaction_type==None and schema_string==None and schema_path==None :
            raise LIXIInvalidSyntax('Schema fetch parameters not specified.')
        
        if lixi_version!=None or lixi_transaction_type!=None:
            if lixi_transaction_type==None:
                raise LIXIInvalidSyntax('Schema Transaction type fetch parameter not specified.')
            
            if lixi_version==None:
                lixi_version = self.get_schema_latest_version(lixi_transaction_type)            
            
            output_xml_schema = self.load_schema(lixi_transaction_type=lixi_transaction_type, lixi_version=lixi_version)
            output_schema = _jsonschema_functions.convert_to_json_schema(output_xml_schema)               
        
        elif schema_string!=None or schema_path!=None:
            
            if schema_path!=None:
                output_xml_schema,a,b,c = self._read_path(schema_path, 'xml')
            else:
                output_xml_schema,a,b,c = self._parse_xml_schema(schema_string, 'xml', 'fetch_json_schema')
            
            output_schema = _jsonschema_functions.convert_to_json_schema(output_xml_schema)
            
        if output_path==None:
            return output_schema
        else:
            self.__write__('fetched_json_schema_output.json', output_path, str(_json.dumps(output_schema, sort_keys=True, indent=4, ensure_ascii=False)).strip())
    
    def fetch_xml_schema(self,lixi_transaction_type=None, lixi_version=None, schema_string=None, schema_path=None, output_path=None): 
        """Fetches a JSON schema based on the info given.
    
        Args:
            lixi_transaction_type (str): Transaction type of the LIXI xml schema to fetch.
            lixi_version (str): Version of the LIXI xml schema to fetch.
            schema_string (str): LIXI schema as a String for conversion to XML.
            schema_path (str): LIXI schema path as a String for conversion to XML.
            output_path (str): A complete file path to store the output schema.
    
        Result:
            a customised schema as etree or saved to the output folder specified. 
    
        Raises:
            LIXIInvalidSyntax: Validation errors for the lixi version or transaction type.
            not found
        """ 
        
        output_schema = None
        
        if lixi_transaction_type==None and schema_string==None and schema_path==None :
            raise LIXIInvalidSyntax('Schema fetch parameters not specified.')
        
        if lixi_version!=None or lixi_transaction_type!=None:
            if lixi_transaction_type==None:
                raise LIXIInvalidSyntax('Schema Transaction type fetch parameter not specified.')
            
            if lixi_version==None:
                lixi_version = self.get_schema_latest_version(lixi_transaction_type)            
            
            output_schema = self.load_schema(lixi_transaction_type=lixi_transaction_type, lixi_version=lixi_version)          
        
        elif schema_string!=None or schema_path!=None:
            
            if schema_path!=None:
                output_schema,a,b,c = self._read_path(schema_path, 'xml')
            else:
                output_schema,a,b,c = self._parse_xml_schema(schema_string, 'xml', 'fetch_xml_schema')
            
        if output_path==None:
            return output_schema
        else:
            self.__write__('fetched_xml_schema_output.xsd', output_path, str(_etree.tostring(output_schema, pretty_print=True).decode('utf-8')).strip() )    
        
    def generate_custom_schema(self, instructions=None, instructions_path=None, csv_text=None, csv_path=None, lixi_transaction_type=None, lixi_version=None, schema_string=None, schema_path=None, output_name=None, output_folder=None, output_type='xml'): 
        """Generates a custom schema based on the given customization instructions file.
    
        Args:
            instructions (str): Transaction type of the LIXI schema.
            instructions_file (str): Version of the LIXI schema.
            csv_text (str): Comma seperated list of all elements to include.
            csv_path (str): Path to a csv that contains a list of elements to include.
            lixi_transaction_type (str): Transaction type of the LIXI schema.
            lixi_version (str): Version of the LIXI schema.
            schema_string (str): LIXI schema as a String.
            schema_path (str): Absolute path to the LIXI schema.
            output_name (boolean): Name of the custom schema generated.
            output_folder (str): Usually a complete file name of the custom schema.
    
        Result:
            a customised schema as etree or saved to the output folder specified. 
    
        Raises:
            LIXIInvalidSyntax: Validation errors for the lixi version or transaction type.
        """
        
        
        #Read the instructions file
        if instructions!=None or instructions_path!=None:
        
            if instructions_path!=None :
                if _os.path.exists(instructions_path) == True:
                    instructions = _etree.parse(instructions_path)
                    instructions = instructions.getroot()
                    instructions = _etree.tostring(instructions).decode('utf-8')
                else:
                    raise LIXIResouceNotFoundError('Instructions file not found at the specified path.')
        
        
            if lixi_transaction_type==None and schema_string==None and schema_path==None:
                transactiontype = re.search('LIXITransactionType="([A-Z]*)"', instructions)
                if transactiontype!=None:
                    lixi_transaction_type = transactiontype.group(1)
                    lixi_version = str(self.get_schema_latest_version(lixi_transaction_type)).replace('_','.')
            
            schema = self.load_schema(lixi_transaction_type, lixi_version, 'xml' , None, schema_string, schema_path) # Has to be XML and has to be transaction hence custom is None
                                
            
        #Read the csv text/file. Assupmtion for csv text is 'Package,Package.Content,..........' 
        elif csv_text != None or csv_path != None:
            
            schema = self.load_schema(lixi_transaction_type, lixi_version, 'xml' , None, schema_string, schema_path) # Has to be XML and has to be transaction hence custom is None            
                
            include_elements_list = []
            
            if csv_path!=None:
                if _os.path.exists(csv_path) == True:
                    f = _io.open(csv_path, mode="r", encoding="utf-8")
                    csv_text =  f.read()
                    f.close()
                else:
                    raise LIXIResouceNotFoundError('CSV file not found at the specified path.')
            
            if len(csv_text.split(',')) > 0:
                temp_list = csv_text.replace('\n','').split(',')
            elif len(csv_text.split('\n')) > 0:   
                temp_list = csv_text.split('\n')
                
            include_elements_list = [elem.strip() for elem in temp_list]
            
            message_paths = _path_functions.get_paths_for_elements(paths_list=include_elements_list, schema=schema)    
            schema_paths = _path_functions.get_paths_for_schema_elements(schema)
            instructions = _path_functions.get_blacklist_paths_for_customization(self.current_transaction_type, message_paths, schema_paths)
            
        #Generate the customised schema as string
        customised_schema, output_name = _customise_schema.execute_customisation_instructions(schema, instructions, output_name)
        
        if output_type == 'xml':
            output = customised_schema ##xsd
        elif output_type == 'json':
            output = _jsonschema_functions.convert_to_json_schema(_etree.fromstring(customised_schema))
            output = _json.dumps(output, sort_keys=True, indent=4, ensure_ascii=False)
        
        #Output as required. 
        if output_folder==None:
            return output
        else:
            if output_type == 'xml':
                output_path = _os.path.join(output_folder,output_name+'.xsd')
            elif output_type == 'json':
                output_path = _os.path.join(output_folder,output_name+'.json')
            
            try:
                with _io.open(output_path,'w+', encoding="utf-8") as out_file:
                    out_file.write(output)                
            except Exception as e:
                raise LIXIResouceNotFoundError("Can not store at the specified folder "+e)




#Error Functions            
class LIXIResouceNotFoundError(Exception):
    pass


class LIXIInvalidSyntax(Exception):
    pass


class LIXIValidationError(Exception):
    
    def __init__(self, message=None, message_instance=None):
        
        if message is None:
            self.message = "The message is invalid."
        else:
            self.message = message
        
        self.message_instance = message_instance