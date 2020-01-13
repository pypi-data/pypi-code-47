from nexoclom import Input
from MESSENGERuvvs import MESSENGERdata
import cProfile
import pstats
from pstats import SortKey


data = MESSENGERdata('Ca', 'Orbit = 36')
data = data[0:20]
inputs = Input('inputfiles/Ca.isotropic.maxwellian.50000.input')

#inputs.run(1e5, overwrite=True)
#cProfile.run("inputs.line_of_sight(data.data, 'radiance')",
#             'LOSstats.dat')
inputs.line_of_sight(data.data, 'radiance')

# p = pstats.Stats('LOSstats.dat')
# p.strip_dirs().sort_stats(SortKey.TIME).print_stats()

