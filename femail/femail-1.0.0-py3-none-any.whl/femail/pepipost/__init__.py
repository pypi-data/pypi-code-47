from jinja2 import Template
import requests
import json


class Client(object):
    """Pepipost: https://app.pepipost.com/"""
    def __init__(self, api_key: str = None, pepi_send_addr: str = None, pepi_username: str = None):
        if api_key is None: raise AttributeError("Please provide a api key obtained from app.pepipost.com.")

        if pepi_send_addr is None: raise AttributeError("Initialize the email adress provided by app.pepipost.com.")
        else: self.author_email = pepi_send_addr

        if pepi_username is None: raise AttributeError("Please provide your username provided by app.pepipost.com.")
        else: self.author_name = pepi_username

        self._endpoint = "https://api.pepipost.com/v2/sendEmail"

        self._headers = {
            'content-type': "application/json",
            'api_key': api_key
        }
    
    def send_mail(self, to: list = [], subject: str = None, body: str = None):
        """
        Send a email to a recipient or bulk send to multiple recipients.

        Parameters
        ----------
        to: list
            This argument is a LIST of EMAIL ADRESSES. Each email will recieve a new mail in their inbox.
        
        subject: str
            The subject of the email. This is a STRING.
        
        body: str
            The body of the email which is a STRING. U can use linebreaks \\n
        """
        data = json.dumps({
            'personalizations': [{'recipient': i} for i in to],
            'from': {
                'fromEmail': self.author_email, 'fromName': self.author_name
                },
            'subject': subject,
            'content': body
        })

        response = requests.post(url=self._endpoint, data=data, headers=self._headers)
        print(f"Mail(s) have been send to {len(to)} email(s).")

    def send_html_mail(self, to: list = [], subject: str = None, jinja_template_absolute_path: str = None, **kwargs):
        """
        This method renders a Jinja2 Template. Any kwargs will be passed through the render.

        Parameters
        ----------
        to: list
            This argument is a LIST of EMAIL ADRESSES, Each email will recieve a new mail in their inbox.

        subject: str
            The subject of the email. This is a STRING
        
        jinja_template_absolute_path: str
            The absolute path to the jinja2 template. This is also a STRING
        
        **kwargs
            any parameter passed in as a kwarg will be used in the render. This allows you to
            add parameters into your jinja2 template.
        """
        with open(jinja_template_absolute_path) as file_:
            template = Template(file_.read())
        template = template.render(**kwargs)
        self.send_mail(to, subject, template)
