__name__ = 'neumf'
major = 0
minor = 0
patch = 4
__version__ = '{}.{}.{}'.format(major, minor, patch)


__author__ = "Sumner Magruder"
__fname__, *_, __lname__ = __author__.lower().split(' ')

__university__ = 'uni-hamburg'
__institute__ = 'zmnh'
__domain__ = '{}{}{}.de'.format(__institute__, '.' if __university__ else '', __university__)
__author_email__ = '{}.{}@{}'.format(__fname__, __lname__, __domain__)
__description__ = ''
__url__ = 'https://pypi.org/project/{}/'.format(__name__)
