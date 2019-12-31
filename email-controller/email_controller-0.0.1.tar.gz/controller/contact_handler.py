""" Handler to get and log user's contact in database
> Checks to see if the user is violating the contact rules
> > If user is eligble for contact, set the email in the database
> > If the user has violated one of the contact rules:
> > > Give a status code and return the expected error messaging
> > > TODO LOG INSTANCE IN ERROR HANDLER
"""
from controller.record_validation import RecordValidation
from controller.smtp_controller import GMailController
from utils_package.data_controller.scripts.email_controller.email_audit_queries import AuditWriter
from utils_package.data_controller.pg_config import PGConfig
from datetime import datetime


class ContactHandler(object):
    """ Handles contact form entries """
    PRIMARY_ADDRESS = 'jamberin@gmail.com'

    def __init__(self):
        """ Initialize class variables """
        self.record_validation = RecordValidation()
        self.audit_writer = AuditWriter()
        self.gmail = GMailController()
        self.config = PGConfig()

    def contact_form_entry(self, name, email, message):
        """
        For contact form entries, validate the email, handle responses, and send the email
        :param name:
        :param email:
        :param message:
        :return: Status code, display message, display validation
        """
        # Validate that the email address associated is eligible for contact
        response = self.record_validation.validate_rule_for_contact(email)
        if response['validation']:
            error_message = self.__record_validation_error_handler(response)
            error_status = 429
            return error_status, error_message['display_message'], error_message
        else:
            if self.send_contact_form_email(name, email, message):
                record_dict = {
                    'strname': name,
                    'stremailaddress': email,
                    'strmessage': message
                }
                response = self.audit_writer.insert_new_record(record_dict)
                assert response[0] == 1, 'Record was not created, ensure database working: ' \
                                         '[name: %s, email: %s, message: %s]' % (name, email, message)
                response_status = 201
                response_message = {
                    'violation_code': [0],
                    'violation_reasons': [None],
                    'display_message': 'Your message has been sent! I will be in contact shortly.'
                }
            else:
                return Exception('Issues sending message')
            return response_status, response_message['display_message'], response_message

    def send_contact_form_email(self, name, email_address, message):
        """
        Sends a simple plaintext email regarding contact
        :param name: Name from contact
        :param email_address: Email address from contact
        :param message: Message that is to be sent
        :return: Success or failure message
        """
        contact_date = datetime.strftime(datetime.now(), '%x')
        email_message = """
        Timestamp: %s
        Name: %s
        eMail Address: %s
        Message: %s
        """ % (contact_date, name, email_address, message)
        subject = 'Contact from %s | %s' % (name, contact_date)
        login_dict = self.config.get_smtp_dict('primary_gmail')
        response = self.gmail.attempt_send_message(login_dict, email_message, self.PRIMARY_ADDRESS, subject)
        return response

    @staticmethod
    def __record_validation_error_handler(error_response):
        """
        Builds the error response to be sent back to the front end
        :param error_response: Depending on the error_response content, the appropriate error message is sent
        :return: Error response reason and message
        """
        # Build the error message and code to be sent to the front end
        message = {
            'violation_code': [],
            'violation_reasons': [],
            'display_message': 'It looks like you have tried to contact too many times. '
        }

        # For the given violation reasons
        if 'DAY' in error_response['val_reason']:
            message['violation_code'].append(1)
            message['violation_reasons'].append('Daily contact violation')
            message['display_message'].append('Over three times in the last day. ')
        if 'WEEK' in error_response['val_reason']:
            message['violation_code'].append(2)
            message['violation_reasons'].append('Weekly contact violation')
            message['display_message'].append('More than five times in the past week. ')
        if 'MONTH' in error_response['val_reason']:
            message['violation_code'].append(3)
            message['violation_reasons'].append('Monthly contact violation')
            message['display_message'].append('Over twenty times in the last month. ')
        if 'ANNUAL' in error_response['val_reason']:
            message['violation_code'].append(4)
            message['violation_reasons'].append('Annual contact violation')
            message['display_message'].append('More than forty times in the year month. ')

        return message
