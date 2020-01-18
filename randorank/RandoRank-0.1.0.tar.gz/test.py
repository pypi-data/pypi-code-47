import math
import pickle

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from randorank import MultiPeriod

test_constants = {'tau': .2,
                  'multi_slope': .008,
                  'multi_cutoff': 6,
                  'norm_factor': 1.3,
                  'initial_rating': 1500,
                  'initial_deviation': 50,
                  'initial_volatility': .01
                 }
test_players = {'etium': {'rating': 1550.0, 
                         'deviation': 32.0,
                         'volatility': 0.01002,
                         #'bolatility': 0.01002,
                         'variance': 20.0,
                         'delta': 3.0},
               'frostbite3030': {'rating': 1650.0, 
                                 'deviation': 24.0,
                                 'volatility': 0.009998,
                                 'variance': 15.0,
                                 'delta': 6.0}
               }
test_race = {'etium': 1768.0, 
             'frostbite3030': 1648.0, 
             'buane': 1598,
             'zelgadissan': 1597.0
             }
test_race2 = {'etium': 1768}

all_races = pickle.load(open("races.rr", "rb"))

period_rankings = []
period_sheets = []
for period in all_races:
    if len(period_rankings) == 0:
        test_period = MultiPeriod()
        test_period.set_constants(test_constants)
    else:
        test_period = MultiPeriod()
        test_period.set_constants(test_constants)
        test_period.add_players(period_rankings[-1])
    for race in period:
        if len(race) > 1 and len(list(filter(lambda x: math.isnan(x) is False, race.values()))) > 1:
            test_period.add_race(race)
    mid_rankings = test_period.rank()
    period_rankings.append(mid_rankings)

    test_df = pd.DataFrame.from_dict(mid_rankings, orient='index', columns=['rating', 'deviation', 'volatility', 'variance', 'delta', 'inactive_periods'])
    test_df = test_df.sort_values(by=['rating', 'deviation'], ascending=[False, True])
    test_df.insert(loc=0, column='Rank', value=np.arange(1, len(test_df) + 1))
    period_sheets.append(test_df)
    print(f'period done')

#final_rankings = period_rankings[-1]
#print(final_rankings)

with pd.ExcelWriter('scores.xlsx', engine='openpyxl') as writer:
        period_sheets[0].to_excel(writer, sheet_name='Period 1')
        period_sheets[1].to_excel(writer, sheet_name='Period 2')
        period_sheets[2].to_excel(writer, sheet_name='Period 3')
        period_sheets[3].to_excel(writer, sheet_name='Period 4')
        period_sheets[4].to_excel(writer, sheet_name='Period 5')
        period_sheets[5].to_excel(writer, sheet_name='Period 6')
        period_sheets[6].to_excel(writer, sheet_name='Period 7')
        period_sheets[7].to_excel(writer, sheet_name='Period 8')
        period_sheets[8].to_excel(writer, sheet_name='Period 9')
        period_sheets[9].to_excel(writer, sheet_name='Period 10')
        period_sheets[10].to_excel(writer, sheet_name='Period 11')
        period_sheets[11].to_excel(writer, sheet_name='Period 12')
        period_sheets[12].to_excel(writer, sheet_name='Period 13')

plt.hist(period_sheets[12]['rating'], 100)
plt.savefig('chart.png')
