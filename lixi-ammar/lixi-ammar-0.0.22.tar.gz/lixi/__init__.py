__version__ = "0.0.22"
__all__ = [
    "set_credentials",
    "set_schema_folder",
    "get_schema_paths",
    "get_custom_schema",
    "get_json_schema",
    "get_xml_schema",
    "read_message",
]

import os as _os

if __name__ == "__main__":
    from _LIXI import (
        LIXI as _LIXI,
        LIXIValidationError,
        LIXIInvalidSyntax,
        LIXIResouceNotFoundError,
    )
    from _Message import Message as _Message
else:
    from lixi._LIXI import (
        LIXI as _LIXI,
        LIXIValidationError,
        LIXIInvalidSyntax,
        LIXIResouceNotFoundError,
    )
    from lixi._Message import Message as _Message


###################
## ENTRY POINTS
###################


def set_credentials(access, secret):
    """Sets the secret and access keys for a LIXI member, which would fetch a schema from the LIXI online repository. Used before doing any operations that require a schema. Both access key and secret key can be requested from LIXI admin. These are unique for an organization/member. 
    
    Args:
        access (:obj:`str`, required): A LIXI member's assigned access key.
        secret (:obj:`str`, required): A LIXI member's assigned secret key.
    
    Raises:
        LIXIInvalidSyntax: If 'access' is not specified or is not str.
        LIXIInvalidSyntax: If 'secret' is not specified or is not str.
    """

    _LIXI.getInstance().set_credentials(access, secret)


def set_schema_folder(folder_path, force_update=True):
    """Sets a directory path to fetch LIXI schemas from. Used before doing any operations that require a schema. Allows schema read from folder and a re-read of folder in case a file was added on runtime.  
    
    Args:
        folder_path (:obj:`str`, required): A path to a folder containing LIXI schema files.
        force_update (:obj:`bool`, optional): A flag to force update of the folder read. Defaults to True.

    Raises:
        LIXIInvalidSyntax: If folder_path is not specified.
        LIXIResouceNotFoundError: If folder_path provided does not exist.
    """
    _LIXI.getInstance().set_schema_path(folder_path, force_update)


def get_schema_paths(
    lixi_transaction_type=None,
    lixi_version=None,
    custom_version=None,
    schema_string=None,
    schema_path=None,
):
    """Fetches all of the elements paths of the LIXI schema provided as a Python List of paths. 

    Args:
        lixi_transaction_type (:obj:`str`, optional): The transaction type of the LIXI schema to be fetched. Should be one of 'ACC', 'CAL', 'CDA', 'CNZ', 'DAS', 'LMI', 'SVC', 'VAL'. Defaults to None.
        lixi_version (:obj:`str`, optional): The version of the LIXI schema to be fetched. Should be in the format of '2.6.24'. Defaults to None. Defaults to the latest version if only lixi_transaction_type is provided.
        custom_version (:obj:`str`, optional): The version of the LIXI custom schema to be fetched. Usually a complete file name of the custom schema. Defaults to None.
        schema_string (:obj:`str`, optional): LIXI schema provided as a string. Defaults to None.
        schema_path (:obj:`str`, optional): LIXI schema provided as a path. Defaults to None.

    Returns:
        A python list of all paths in the LIXI schema.

    Raises:
        LIXIInvalidSyntax: Validation errors for the lixi version or transaction type.
        LIXIResouceNotFoundError: If path provided does not exist.
        LIXIValidationError: If path provided does not exist.
    """
    return _LIXI.getInstance().get_schema_paths(
        lixi_transaction_type,
        lixi_version,
        'xml',
        custom_version,
        schema_string,
        schema_path,
    )


def get_custom_schema(
    instructions=None,
    instructions_path=None,
    csv_text=None,
    csv_path=None,
    lixi_transaction_type=None,
    lixi_version=None,
    schema=None,
    schema_path=None,
    output_name=None,
    output_folder=None,
):
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

    return _LIXI.getInstance().generate_custom_schema(
        instructions,
        instructions_path,
        csv_text,
        csv_path,
        lixi_transaction_type,
        lixi_version,
        schema,
        schema_path,
        output_name,
        output_folder,
    )


def get_json_schema(
    lixi_transaction_type=None,
    lixi_version=None,
    custom_version=None,
    schema_string=None,
    schema_path=None,
    output_path=None,
):
    """Fetches a JSON schema based on the info given.

    Args:
        lixi_transaction_type (str): Transaction type of the LIXI json schema to fetch.
        lixi_version (str): Version of the LIXI json schema to fetch.
        custom_version (str): Usually a complete file name of the custom schema.
        schema_string (str): LIXI schema as a String for conversion to JSON.
        schema_path (str): LIXI schema path as a String for conversion to JSON.
        output_path (str): Usually a complete file name of the custom schema.

    Result:
        a customised schema as etree or saved to the output folder specified. 

    Raises:
        LIXIInvalidSyntax: Validation errors for the lixi version or transaction type.
        not found
    """

    return _LIXI.getInstance().fetch_json_schema(
        lixi_transaction_type,
        lixi_version,
        custom_version,
        schema_string,
        schema_path,
        output_path,
    )


def get_xml_schema(
    lixi_transaction_type=None,
    lixi_version=None,
    custom_version=None,
    schema_string=None,
    schema_path=None,
    output_path=None,
):
    """Fetches a JSON schema based on the info given.

    Args:
        lixi_transaction_type (str): Transaction type of the LIXI json schema to fetch.
        lixi_version (str): Version of the LIXI json schema to fetch.
        custom_version (str): Usually a complete file name of the custom schema.
        schema_string (str): LIXI schema as a String for conversion to JSON.
        schema_path (str): LIXI schema path as a String for conversion to JSON.
        output_path (str): Usually a complete file name of the custom schema.

    Result:
        a customised schema as etree or saved to the output folder specified. 

    Raises:
        LIXIInvalidSyntax: Validation errors for the lixi version or transaction type.
        not found
    """

    return _LIXI.getInstance().fetch_xml_schema(
        lixi_transaction_type,
        lixi_version,
        custom_version,
        schema_string,
        schema_path,
        output_path,
    )


def read_message(
    message=None, message_path=None, file_type=None, schema_text=None, schema_path=None
):
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

    # Message Check
    if message_path != None:
        if _os.path.exists(message_path) == False:
            raise LIXIResouceNotFoundError(message_path)

    # Read the Message
    try:
        lixi_message = _Message(message, message_path, file_type)
    except Exception as e:
        raise LIXIInvalidSyntax("The file is not well-formed\n" + str(e))

    # Validate the Message
    isvalid, result = lixi_message.validate(schema=schema_text, schema_path=schema_path)

    if isvalid == False:
        raise LIXIValidationError(
            "Message is not valid against the LIXI schema\n" + result, lixi_message
        )

    return lixi_message


# Setting default schema folder as starting folder
# _cwd = _os.getcwd()
# set_schema_folder(_cwd)
# print(_cwd)

###################
## TEST CODE
###################

# la_schema = get_customized_schema(instructions_path='C:/Users/compb/Documents/Git/lixi-pypi/tests/Customisation_Instruction_CAL.xml', schema_path='C:/Users/compb/Documents/Git/lixi-pypi/tests/LIXI-CAL-2_6_19-Annotated.xsd', output_name='Ammar_CAL', output_folder='C:/Users/compb/Documents/Git/lixi-pypi/tests')
# print('hallelujah')
