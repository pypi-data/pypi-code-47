from lino_book.projects.lydia.settings import *


class Site(Site):
    default_ui = 'lino_openui5.openui5'
    project_name = "openui5_lydia6"
    title = "Lydia Lino Open ui5 demo"
    languages = ['en', 'fr', 'de']
