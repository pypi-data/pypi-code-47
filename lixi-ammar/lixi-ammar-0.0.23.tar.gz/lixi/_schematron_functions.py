from lxml import isoschematron
from lxml import etree


def validate(xml_etree, schematron_etree):
    """ Validates a LIXI message against a Schematron business rules file.
    
    Args:
        xml_etree (:obj:`lxml.etree`, required): message to check provided as a Python Etree.
        schematron_etree (:obj:`lxml.etree`, required): Schematron rules provided as a Python Etree.
    
    Result:
        result (:obj:`bool`): Indicates if validation was successfull.
        message (:obj:`str`): Validation message.
    
    Raises:
        LIXIResouceNotFoundError: If the schema is not found at the schema path.
        LIXIInvalidSyntax: If the schema file is not well formed.
    """

    schematron = isoschematron.Schematron(schematron_etree, store_report=True)
    validation_result = schematron.validate(xml_etree)

    report = schematron.validation_report

    if validation_result:
        return True, "No errors found."
    else:
        err_message = "Message schematron validation failed."
        err_message += "\nIncorrect Instructions:"

        for fail in report.xpath(
            "//svrl:failed-assert",
            namespaces={"svrl": "http://purl.oclc.org/dsdl/svrl"},
        ):
            err_message = (
                err_message
                + "\n    Error On Line "
                + str(fail.get("location"))
                + ": '"
                + fail.get("test")
                + "' test failed, "
                + fail.getchildren()[0].text
            )

        return False, err_message
