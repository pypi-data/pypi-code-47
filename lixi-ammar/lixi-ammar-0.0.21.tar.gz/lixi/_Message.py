import json as _json
from lxml import etree as _etree
import re, io, os

ns = {'xs': 'http://www.w3.org/2001/XMLSchema', 'lx': 'lixi.org.au/schema/appinfo_elements', 'li': 'lixi.org.au/schema/appinfo_instructions'} 

if __name__ == '__main__':
    import _xml_to_json, _path_functions, _jsonschema_functions, _xslt_transform, _schematron_functions
    from _LIXI import LIXI as _LIXI, LIXIValidationError, LIXIInvalidSyntax, LIXIResouceNotFoundError
else:    
    from lixi import _xml_to_json, _path_functions, _jsonschema_functions, _xslt_transform, _schematron_functions
    from lixi._LIXI import LIXI as _LIXI, LIXIValidationError, LIXIInvalidSyntax, LIXIResouceNotFoundError  

class Message():
    """Represents a LIXI message that conforms to a LIXI2 standard..

    Args:
        data (str): A LIXI message file in XML or JSON.
        is_json (boolean): 
        
    The class exists as a wrapper for all internal message functions the library is to provide.
    """

    def __init__(self, data, message_path, file_type):
        
        self.xml_package = None
        self.json_package = None
        
        self.json_string = None
        self.file_type = None
        
        self.schema_name = None
        self.is_valid = None
        self.validation_message = None
        
        ## If data specified
        if data!=None and message_path==None:
            passed = False
            if passed == False:
                try:
                    parser = _etree.XMLParser(remove_blank_text=True)
                    self.xml_package = _etree.fromstring(data, parser)
                    passed = True
                    self.file_type = 'xml'
                except Exception as e:
                    passed = False
                    
            if passed == False:
                try:
                    self.json_string = str(data)
                    self.json_package = _json.loads(data)                
                    
                    passed = True
                    self.file_type = 'json'
                except Exception as e:
                    passed = False
                
         ## If path specified
        elif data==None and message_path!=None:
            passed = False
            if passed == False:
                try:
                    self.xml_package = _etree.parse(message_path)
                    self.xml_package = self.xml_package.getroot()
                    passed = True
                    self.file_type = 'xml'
                except Exception as e:
                    passed = False
                    
            if passed == False:
                try:
                    
                    with io.open(message_path, "r", encoding="utf-8") as json_file:
                        self.json_string = str(json_file.read())
                        self.json_package = _json.loads(str(self.json_string))
                        
                    passed = True
                    self.file_type = 'json'
                except Exception as e:
                    passed = False                

        ##TODO:: if file_type specified then select type 
                
        if self.file_type == 'xml':
            
            self.is_json = False
    
            try:
                self.lixi_transaction_type = self.xml_package.xpath("/Package/SchemaVersion/@LIXITransactionType")[0]
            except IndexError:
                self.lixi_transaction_type = None      
    
            try:
                self.lixi_version = self.xml_package.xpath("/Package/SchemaVersion/@LIXIVersion")[0]
            except IndexError:
                self.lixi_version = None 
    
            try:
                self.lixi_custom_version = self.xml_package.xpath("/Package/SchemaVersion/@LIXICustomVersion")[0]
            except IndexError:
                self.lixi_custom_version = None
        
        elif self.file_type == 'json':
            
            self.is_json = True
            
            try:
                self.lixi_transaction_type = str(self.json_package['Package']['SchemaVersion']['@LIXITransactionType'])
            except Exception:
                self.lixi_transaction_type = None      
    
            try:
                self.lixi_version = str(self.json_package['Package']['SchemaVersion']['@LIXIVersion'])
            except Exception:
                self.lixi_version = None 
    
            try:
                self.lixi_custom_version = str(self.json_package['Package']['SchemaVersion']['@LIXICustomVersion'])
            except Exception:
                self.lixi_custom_version = None
                              
        else: # everything failed now we need better error messages 
            ##Better error messages
            error_message = ''
            
            if data==None and message_path!=None:
                with io.open(message_path, "r", encoding="utf-8") as file:
                    data = str(file.read())
                        
            if '"Package"' in data: ## is json
                try:
                    _json.loads(str(data))
                except Exception as e:
                    error_message = e
            elif '<Package>' in data:
                try:
                    doc = etree.parse(filename_xml)
                except Exception as e:
                    error_message = e
        
            raise LIXIInvalidSyntax('Message can not be read or type is not supported.\n'+ error_message)
    
    def __write__(self, default_name, output_path, data):
        """Utility function to output a path.
        """        
        
        if os.path.isdir(output_path):
            output_path = os.path.join(output_path,default_name)
            
        try:
            with io.open(output_path,'w+', encoding="utf-8") as out_file:
                out_file.write(data)            
        except Exception as e:
            raise LIXIResouceNotFoundError("Can not store at the specified path")        
            
    def to_json(self, to_return=False):
        """Validates a LIXI JSON message to XML message.

        Args:
            self: A LIXI message instance.

        Result:
            Equivalent LIXI JSON message instance. 

        Raises:
            lixi2._LIXIInvalidSyntax: Validation errors for the xml file.
        """         
        
        # for converstion an xsd is required hence setting it to be false
        schema_etree = _LIXI.getInstance().load_schema(self.lixi_transaction_type, self.lixi_version)       
        
        if self.json_package == None:
            self.json_package =  _xml_to_json.to_json(self.xml_package, schema_etree)
        
        if to_return == True:
            return Message(_json.dumps(self.json_package, sort_keys=True, indent=4, ensure_ascii=False) , None, 'json')
        else:
            self.file_type="json"
            self.is_json=True
    
    def to_xml(self, to_return=False):
        """Converts a LIXI XML message to JSON.

        Args:
            self: A LIXI message instance.
            to_return (bool): A check to indicate if the result needs to be 

        Result:
            Equivalent LIXI XML message instance.

        Raises:
            lixi2._LIXIInvalidSyntax: Validation errors for the xml file.
        """
        
        
        # for converstion an xsd is required hence setting it to be false
        schema_etree = _LIXI.getInstance().load_schema(self.lixi_transaction_type,self.lixi_version)
        
        if self.xml_package == None: 
            self.xml_package =  _xml_to_json.to_xml(self.json_package, schema_etree)
        
        if to_return == True:
            return Message(_etree.tostring(self.xml_package, pretty_print=True).decode('utf-8'), None, 'xml')
        else:
            self.file_type="xml"
            self.is_json=False
        
    def get_message_paths(self, output_path=None):
        """Get all the elements path of a LIXI Message.

        Args:
            self: A LIXI Message Instance
            output_path (str): An absolute path to store the output.

        Result:
            a list of paths in the Message 

        Raises:
            lixi2._LIXIInvalidSyntax: Validation errors for the lixi version or transaction type.
            lixi2._LIXIResouceNotFoundError: If the output path provided is not correct.
        """   

        schema = _LIXI.getInstance().load_schema(self.lixi_transaction_type,self.lixi_version, 'xml', self.lixi_custom_version)  
        
        if self.xml_package == None:
            self.xml_package =  _xml_to_json.to_xml(self.json_package, schema)            
        
        message_paths_list = _path_functions.get_paths_for_elements(message=self, schema=schema)
        
        if output_path==None:
            return message_paths_list
        else:        
            self.__write__('message_paths_output.txt', output_path, ",\n".join(message_paths_list))
    
    def get_schema_paths(self, output_path=None):
        """Get all the elements path of a LIXI Message.

        Args:
            self: A LIXI Message Instance
            output_path (str): An absolute path to store the output.

        Result:
            a list of paths in the Message 

        Raises:
            lixi2._LIXIInvalidSyntax: Validation errors for the lixi version or transaction type.
            lixi2._LIXIResouceNotFoundError: If the output path provided is not correct.
        """       
        
        schema_paths_list = _LIXI.getInstance().get_schema_paths(self.lixi_transaction_type, self.lixi_version, 'xml', self.lixi_custom_version)  
        
        if output_path==None:
            return schema_paths_list
        else:        
            self.__write__('schema_paths_output.txt', output_path, ",".join(schema_paths_list))
    
    def get_restriction_paths_for_schema(self, output_path=None):
        """Generates blacklist restriction paths to be used for a generating a smaller customised schema.

        Args:
            self: A LIXI Message Instance
            output_path (str): An absolute path to store the output.

        Result:
            customization_instructions (list): a str of blacklist customization restrictions.

        Raises:
            lixi2._LIXIInvalidSyntax: Validation errors for the lixi version or transaction type.
            lixi2._LIXIResouceNotFoundError: If the output path provided is not correct.
        """        
        
        message_paths = self.get_message_paths()
        schema_paths = self.get_schema_paths()
        
        customization_instructions = _path_functions.get_blacklist_paths_for_customization(self.lixi_transaction_type, message_paths, schema_paths)
        
        if output_path==None:
            return customization_instructions
        else:
            self.__write__('customization_instructions_output.xml', output_path, customization_instructions)
    
    def get_custom_schema(self, output_path=None): 
        """Generates a custom schema based on the element paths derived from a message.
    
        Args:
            output_path (str): An absolute path to store the output.
    
        Result:
            a customised schema as etree or saved to the output folder specified. 
    
        Raises:
            LIXIInvalidSyntax: Validation errors for the lixi version or transaction type.
            lixi2._LIXIResouceNotFoundError: If the output path provided is not correct.
        """       
        
        #Read the instructions file
        restriction_paths = self.get_restriction_paths_for_schema(output_path=None)
        
        #Generate the customised schema as string      
        if output_path==None:
            return _LIXI.getInstance().generate_custom_schema(instructions=restriction_paths, lixi_transaction_type=self.lixi_transaction_type, lixi_version=self.lixi_version, output_name=None, output_folder = None, output_type=self.file_type)
        else:
            
            basename = os.path.basename(output_path)
            dirname = os.path.dirname(output_path)
            
            if os.path.isdir(output_path):
                output_folder = output_path
                output_name = None
            elif os.path.isfile(output_path):
                output_folder = dirname
                output_name = str(basename).replace('.xsd','').replace('.json','').replace('.txt','')
            elif '.json' in basename or '.xsd' in basename or '.xml' in basename or '.txt' in basename:
                output_folder = dirname
                output_name = str(basename).replace('.xsd','').replace('.json','').replace('.txt','')                
            else:
                output_folder = None
                output_name = None                
            
            _LIXI.getInstance().generate_custom_schema(instructions=restriction_paths, lixi_transaction_type=self.lixi_transaction_type, lixi_version=self.lixi_version, output_name=output_name, output_folder = output_folder, output_type=self.file_type)
    
    def transform_message(self, to_version=None, to_return=False):
        """transforms a LIXI message to an older/newer version of LIXI.
    
        Args:
            to_version (string): The absolute path to a schema.
    
        Result:
            lixi_message: A LIXI message instance or a list of LIXI message instances.
    
        Raises:
            LIXIResouceNotFoundError: If the schema is not found at the schema path.
            LIXIInvalidSyntax: If the schema file is not well formed.
        """                
        if self.xml_package == None:
            self.xml_package =  _xml_to_json.to_xml(self.json_package, schema)
            
        from_version_str = self.lixi_version
        transaction_type = self.lixi_transaction_type
        
        if to_version == None: 
            to_version_str = str(_LIXI.getInstance().get_schema_latest_version(transaction_type)).replace('_','.')
        else:
            to_version_str = to_version
        
        result, all_warnings = _xslt_transform.transform_xslt(self.xml_package, transaction_type, from_version_str, to_version_str)
        
        self.xml_package = result
        
        if to_return == True:
            return self.xml_package
    
    def get_transform_warnings(self, to_version=None, output_path=None):
        """transforms a LIXI message to an older/newer version of LIXI.
    
        Args:
            to_version (string): The absolute path to a schema.
            output_path (str): An absolute path to store the output.
    
        Result:
            lixi_message: A LIXI message instance or a list of LIXI message instances.
    
        Raises:
            LIXIResouceNotFoundError: If the schema is not found at the schema path.
            LIXIInvalidSyntax: If the schema file is not well formed.
        """                
        if self.xml_package == None:
            self.xml_package =  _xml_to_json.to_xml(self.json_package, schema)
            
        from_version_str = self.lixi_version
        transaction_type = self.lixi_transaction_type
        
        if to_version == None: 
            to_version_str = str(_LIXI.getInstance().get_schema_latest_version(transaction_type)).replace('_','.')
        else:
            to_version_str = to_version
        
        result, all_warnings = _xslt_transform.transform_xslt(self.xml_package, transaction_type, from_version_str, to_version_str)
        
        if output_path==None:
            return all_warnings
        else:        
            self.__write__('transform_warnings_output.xml', output_path, all_warnings)        
    
    
    def validate_schematron(self, schematron_schema_text=None, schematron_schema_path=None):
        """Reads a LIXI message XML.
    
        Args:
            schematron_schema_text (string): Schematron rules schema provided as a text.
            schematron_schema_path (string): The absolute path to a schematron rules schema.
    
        Result:
            lixi_message: A LIXI message instance or a list of LIXI message instances.
    
        Raises:
            LIXIResouceNotFoundError: If the schema is not found at the schema path.
            LIXIInvalidSyntax: If the schema file is not well formed.
        """
        
        if self.xml_package == None:
            self.xml_package =  _xml_to_json.to_xml(self.json_package, schema)            
        
        if schematron_schema_path != None:
            if os.path.exists(schematron_schema_path) == True:
                f = io.open(schematron_schema_path, mode="r", encoding="utf-8")
                schematron_schema_text =  f.read()
            else:
                raise LIXIResouceNotFoundError("Schematron rules schema file not found at the specified path.")        
        
        try:
            parser = _etree.XMLParser(remove_blank_text=True)
            schematron_schema_etree = _etree.fromstring(schematron_schema_text, parser)
        except Exception as e:
            raise LIXIInvalidSyntax('The schematron schema is not well-formed.\n'+e)
            
        result, message = _schematron_functions.validate(self.xml_package, schematron_schema_etree)
        
        return result, message
    
    def validate(self, schema=None, schema_path=None, create_config=True):
        """Validates a LIXI message.

        Args:
            schema_string (str): A schema in string format  
            schema_path (str):

        Result:
            is_valid: True or False.
            validation_message: A short description of the validation message.

        Raises:
            lixi2._LIXIValidationError: Validation errors for the xml file.
        """       
        
        schema = _LIXI.getInstance().load_schema(self.lixi_transaction_type, self.lixi_version, 'xml', self.lixi_custom_version, schema, schema_path, create_config)                          
        
        validated_with = None
        if self.lixi_custom_version!=None:
            schema_custom_version = schema.xpath('./xs:element[@name="Package"]/xs:complexType/xs:sequence/xs:element[@name="SchemaVersion"]/xs:complexType/xs:attribute[@name="LIXICustomVersion"]', namespaces=ns)[0]
            schema_custom_version = schema_custom_version.attrib['fixed']
            
            validated_with = ", validated with '"+schema_custom_version+"'."
        else:
            validated_with = ", validated with '"+self.lixi_transaction_type+" "+self.lixi_version+"'."
     
               
        if self.file_type == 'xml':
            schema_validation = _etree.XMLSchema(schema)
            result = schema_validation.validate(self.xml_package)
            
            if result:
                self.is_valid = True
                self.validation_message = "Message is Valid"+validated_with
                return True, "Message is Valid"+validated_with
            else:
                error = "Message is invalid"+validated_with
                for scerror in schema_validation.error_log:
                    error = error + "\nError On Line "+str(scerror.line)+": "+scerror.message
                
                self.is_valid = False
                self.validation_message = error                
                return False, error    
            
        elif self.file_type == 'json':
            
            #XML provides a better check especially around dates and checking cross references. 
            #Methods for json validation which are close to xml validation exist but up to user's discretion.
            if self.xml_package == None:
                self.xml_package =  _xml_to_json.to_xml(self.json_package, schema)           
            
            
            schema_validation = _etree.XMLSchema(schema)
            result = schema_validation.validate(self.xml_package)
            
            if result:
                self.is_valid = True
                self.validation_message = "Message is Valid"+validated_with
                return True, "Message is Valid"+validated_with
            else:
                xml_errors = "Message is invalid"+validated_with
                for scerror in schema_validation.error_log:
                    xml_errors = xml_errors + "\nError On Line JSONX: "+scerror.message
         
                json_error_string = ''
                errors = str(xml_errors).split('\n')
                
                json_msg = self.json_string.split('\n')
                
                json_error_string = ''
                
                for error in errors:
                    
                    element = re.search("Element '([a-zA-Z. ]*)'", error)
                    attribute = re.search("attribute '([a-zA-Z. ]*)'", error)
                    
                    if attribute != None:
                        attribute_check = attribute.group(1)
                    else:
                        attribute_check = None
                        
                    
                    if element != None:
                        element_check = element.group(1)
                    else:
                        element_check = None                        
                    
                    line_no = 1
                    for line in json_msg:
                        if attribute_check != None:
                            if attribute_check in line:
                                json_error_string += error.replace("JSONX",str(line_no)) + '\n'
                                break
                        
                        elif element_check != None:
                            if element_check in line:
                                json_error_string += error.replace("JSONX",str(line_no)) + '\n'
                                break
                
                        line_no = line_no + 1
                
                self.is_valid = False
                self.validation_message = json_error_string
                return False, json_error_string                    
            
    def to_string(self):
        """Prints a LIXI message.

        Args:
            None

        Result:
            Pretty print LIXI Message

        """       
        
        if self.file_type == 'xml':
            return str(_etree.tostring(self.xml_package, pretty_print=True).decode('utf-8')).strip() 
        elif self.file_type == 'json':
            return str(_json.dumps(self.json_package, sort_keys=True, indent=4, ensure_ascii=False)).strip()
            
    def pretty_print(self):
        """Prints a LIXI message.

        Args:
            None

        Result:
            Pretty print LIXI Message

        """       
        print(self.to_string())
            
    def save(self, output_path=None):
        """saves a LIXI message to the path provided.

        Args:
            output_path (str): An absolute path to store the  file along with file anem and extension

        Result:
            Saves the LIXI Message to the path provided
        Raises:
            LIXIResouceNotFoundError: If the path provided is not valid.    
        """       
        
        string = self.to_string()
        
        if output_path ==None:
            if self.file_type == 'xml':
                output_path = 'message_output.xml'
            elif self.file_type == 'json':
                output_path = 'message_output.json'
        
        self.__write__('message_output.txt', output_path, string)