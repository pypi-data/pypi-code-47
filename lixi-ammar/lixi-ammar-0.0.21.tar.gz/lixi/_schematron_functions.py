from lxml import isoschematron
from lxml import etree


def validate(xml_etree, schematron_etree):
    
    schematron = isoschematron.Schematron(schematron_etree, store_report = True)
    validation_result = schematron.validate(xml_etree)
    
    report = schematron.validation_report
    
    if validation_result:
        return True, 'No errors found.'
    else:
        err_message = ''
        
        for fail in report.xpath('//svrl:failed-assert', namespaces={'svrl': 'http://purl.oclc.org/dsdl/svrl'}):
            err_message += '*********************************************\n'
            err_message += fail.getchildren()[0].text + '\n' 
            err_message += 'Failed Test: ' + fail.get('test') + '\n'
            err_message += 'Failed Test Location: ' + fail.get('location') + '\n'        
        
        return False, err_message

