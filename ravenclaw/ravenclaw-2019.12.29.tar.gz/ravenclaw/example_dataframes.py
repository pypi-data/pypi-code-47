from collections import OrderedDict
import pandas as pd


lotr = pd.DataFrame(OrderedDict({
    'number': range(11),
    'firstname': [
        'Frodo', 'Aragorn', 'Gandalf', 'Legolas', 'Saruman', 
        'Bilbo', 'Gollum', 'Arwen', 'Galadriel', 'Boromir', 'other'],
    'lastname': [
        'Baggins', 'Gorn', None, None, None,
        'Baggins', None, None, None, None, 'Other'
    ],
    'date': pd.Series(pd.date_range(start = pd.datetime.today(), periods = 11)).dt.date
}))

