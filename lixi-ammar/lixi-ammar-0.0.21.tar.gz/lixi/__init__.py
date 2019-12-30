__version__ = '0.0.21'
__all__ = [
    'set_credentials', 'set_schema_folder', 'get_schema_paths', 'get_custom_schema', 'get_json_schema', 'get_xml_schema','read_message' 
]

import os as _os

if __name__ == '__main__':
    from _LIXI import LIXI as _LIXI, LIXIValidationError, LIXIInvalidSyntax, LIXIResouceNotFoundError
    from _Message import Message as _Message
    import _path_functions, _jsonschema_functions, _customise_schema, _xslt_transform
else:    
    from lixi._LIXI import LIXI as _LIXI, LIXIValidationError, LIXIInvalidSyntax, LIXIResouceNotFoundError
    from lixi._Message import Message as _Message
    from lixi import _path_functions, _jsonschema_functions, _customise_schema, _xslt_transform

#import pkg_resources as _pkg_resources 
#import zipfile as _zipfile

# Unpacks and stores all the schemas if they exist in the library folder.
#if _os.path.exists(_pkg_resources.resource_filename(__name__, 'schema/schema/LIXI-CAL-2_6_19-Annotated.xsd')) == False:
#    zip_ref = zipfile.ZipFile(_pkg_resources.resource_filename(__name__, 'schema/schema.zip') , 'r')
#    zip_ref.extractall(_pkg_resources.resource_filename(__name__, 'schema'))
#    zip_ref.close()


isvalid = False

###################
## ENTRY POINTS 
###################

def set_credentials(access, secret):
    """Sets the secret and access keys for a LIXI member. Provided by LIXI 
    
    Args:
        access (str): A members secret key.
        secret (str): A members secret key.
    
    Result:
        Sets self.__S3_access, self.__S3_secret.
    
    Raises:
        LIXIInvalidSyntax: When the strings are not specified.
    """
    _LIXI.getInstance().set_credentials(access,secret)    
        
def set_schema_folder(schemapath, create_config=True):
    """Sets a default folder path to get the schemas. Usable in case Custom schemas are used
    
    Args:
        schemapath (str): An absolute folder path to schemas stored locally.

    Result:
        Sets self.__schemapath.

    Raises:
        LIXIResouceNotFoundError: If the schema is not found at the schema path.
    """
    _LIXI.getInstance().set_schema_path(schemapath, create_config)

   
def get_schema_paths(lixi_transaction_type, lixi_version, file_type="xml", custom_version=None): 
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
        LIXIInvalidSyntax: Validation errors for the lixi version or transaction type.
    """
    return _LIXI.getInstance().get_schema_paths(lixi_transaction_type,lixi_version, file_type,custom_version)

def get_custom_schema(instructions=None, instructions_path=None, csv_text=None, csv_path=None, lixi_transaction_type=None, lixi_version=None, schema=None, schema_path=None, output_name=None, output_folder=None): 
    """Generates a custom schema based on the given customization instructions file.

    Args:
        instructions (str): Transaction type of the LIXI schema.
        instructions_file (str): Version of the LIXI schema.
        csv_text (str): Transaction type of the LIXI schema.
        csv_path (str): Transaction type of the LIXI schema.
        lixi_transaction_type (str): Transaction type of the LIXI schema.
        lixi_version (str): Version of the LIXI schema.
        schema_string (str): LIXI schema as a String.
        schema_path (str): Absolute path to the LIXI schema.
        output_name (boolean): Indicates if JSON or XML LIXI schema is required.
        output_folder (str): Usually a complete file name of the custom schema.

    Result:
        a customised schema as etree or saved to the output folder specified. 

    Raises:
        LIXIInvalidSyntax: Validation errors for the lixi version or transaction type.
    """

    if output_folder == None: 
        return _LIXI.getInstance().generate_custom_schema(instructions, instructions_path, csv_text, csv_path, lixi_transaction_type, lixi_version, schema, schema_path, output_name, output_folder)
    else:
        _LIXI.getInstance().generate_custom_schema(instructions, instructions_path, csv_text, csv_path, lixi_transaction_type, lixi_version, schema, schema_path, output_name, output_folder)

def get_json_schema(lixi_transaction_type=None, lixi_version=None, schema_string=None, schema_path=None, output_path=None): 
    """Fetches a JSON schema based on the info given.

    Args:
        lixi_transaction_type (str): Transaction type of the LIXI json schema to fetch.
        lixi_version (str): Version of the LIXI json schema to fetch.
        schema_string (str): LIXI schema as a String for conversion to JSON.
        schema_path (str): LIXI schema path as a String for conversion to JSON.
        output_path (str): Usually a complete file name of the custom schema.

    Result:
        a customised schema as etree or saved to the output folder specified. 

    Raises:
        LIXIInvalidSyntax: Validation errors for the lixi version or transaction type.
        not found
    """

    if output_path == None: 
        return _LIXI.getInstance().fetch_json_schema(lixi_transaction_type, lixi_version, schema_string, schema_path, output_path)
    else:
        _LIXI.getInstance().fetch_json_schema(lixi_transaction_type, lixi_version, schema_string, schema_path, output_path)

def get_xml_schema(lixi_transaction_type=None, lixi_version=None, schema_string=None, schema_path=None, output_path=None): 
    """Fetches a JSON schema based on the info given.

    Args:
        lixi_transaction_type (str): Transaction type of the LIXI json schema to fetch.
        lixi_version (str): Version of the LIXI json schema to fetch.
        schema_string (str): LIXI schema as a String for conversion to JSON.
        schema_path (str): LIXI schema path as a String for conversion to JSON.
        output_path (str): Usually a complete file name of the custom schema.

    Result:
        a customised schema as etree or saved to the output folder specified. 

    Raises:
        LIXIInvalidSyntax: Validation errors for the lixi version or transaction type.
        not found
    """

    if output_path == None: 
        return _LIXI.getInstance().fetch_xml_schema(lixi_transaction_type, lixi_version, schema_string, schema_path, output_path)
    else:
        _LIXI.getInstance().fetch_xml_schema(lixi_transaction_type, lixi_version, schema_string, schema_path, output_path)
    
def read_message(message=None, message_path=None, file_type=None, schema_text=None, schema_path=None):
    """Reads a LIXI message XML.

    Args:
        message (string): A LIXI message file in XML.
        message_path (string) : The absolute path to a LIXI message file in XML.
        file_type (string): The type of input type.
        schema_text (string): Schema provided as a text.
        schema_path (string): The absolute path to a schema.

    Result:
        lixi_message: A LIXI message instance or a list of LIXI message instances.

    Raises:
        LIXIResouceNotFoundError: If the schema is not found at the schema path.
        LIXIInvalidSyntax: If the schema file is not well formed.
    """
    
    #Message Check
    if message_path != None:
        if _os.path.exists(message_path) == False:
            raise LIXIResouceNotFoundError(message_path) 
    
    #Read the Message
    try:
        lixi_message = _Message(message, message_path, file_type)
    except Exception as e:
        raise LIXIInvalidSyntax('The file is not well-formed\n'+ str(e))

    ## check whether the schema for this message is available
    #schema_index_dict = _LIXI.getInstance().schema_index_dict
    #lixi_transaction_type = lixi_message.lixi_transaction_type
    #lixi_version = lixi_message.lixi_version.replace(".","_")
    #schema_index_key = "LIXI-" + lixi_transaction_type + "-" + lixi_version + "-Annotated"

    #if not schema_index_key in schema_index_dict:
        #raise Exception("Schema not available")
    
    #Validate the Message
    isvalid, result = lixi_message.validate(schema=schema_text, schema_path=schema_path)
    
    if isvalid == False:
        raise LIXIValidationError('Message is not valid against the LIXI schema\n'+ result, lixi_message)

    return lixi_message




#Setting default schema folder as starting folder
#_cwd = _os.getcwd()
#set_schema_folder(_cwd)
#print(_cwd)

###################
## TEST CODE
###################

#la_schema = get_customized_schema(instructions_path='C:/Users/compb/Documents/Git/lixi-pypi/tests/Customisation_Instruction_CAL.xml', schema_path='C:/Users/compb/Documents/Git/lixi-pypi/tests/LIXI-CAL-2_6_19-Annotated.xsd', output_name='Ammar_CAL', output_folder='C:/Users/compb/Documents/Git/lixi-pypi/tests')
#print('hallelujah')