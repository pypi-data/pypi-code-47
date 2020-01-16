from traverse_invoke import leaves
from traverse_invoke import entry_traverse as entry
import pprint as pp
pprint = pp.pprint

invocations = []

def earth(healthy):
    if healthy:
        print(f'earth is healthy')
    else:
        print(f'earth is NOT healthy')

def city(name, population=100, healthy=False):
    print(f'City {name} has {population} people. Healthy: {healthy}')

def building(name, address, floors=3):
    print(f'{name} Building {address} with {floors} floors')

def test_adapt():
    funcs = {
        'earth': earth,
        'city': city,
        'building': building
    }



    def gen_config():
        config = {
            'earth':{
                'healthy':True,
            },
            'city':{
                'healthy':False,
                'name':'Chicago',
            },
            'building':{
                'name':'Building 1',
            },
            'population':10000,
            'address':'Wacker Dr'
        }
        return config


    testpath = 'earth.city.building'

    entry(gen_config(), testpath.split('.'), funcs, leaf=leaves.adapt2)
    fnames = [i[0] for i in invocations]
    assert fnames == ['log_config', 'pre', 'basemod', 'sys', 'post']
    invocations.clear()

    return
