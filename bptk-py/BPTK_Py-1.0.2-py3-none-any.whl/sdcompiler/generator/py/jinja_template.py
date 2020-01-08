#                                                       /`-
# _                                  _   _             /####`-
# | |                                | | (_)           /########`-
# | |_ _ __ __ _ _ __  ___  ___ _ __ | |_ _ ___       /###########`-
# | __| '__/ _` | '_ \/ __|/ _ \ '_ \| __| / __|   ____ -###########/
# | |_| | | (_| | | | \__ \  __/ | | | |_| \__ \  |    | `-#######/
# \__|_|  \__,_|_| |_|___/\___|_| |_|\__|_|___/  |____|    `- # /
#
# Copyright (c) 2019 transentis labs GmbH
# MIT License

template = '''
#      _                   _ _
#  _____| |__ ___ _ __  _ __(_| |___ _ _
# (_-/ _` / _/ _ | '  \| '_ | | / -_| '_|
# /__\__,_\__\___|_|_|_| .__|_|_\___|_|
#                      |_|
# Copyright (c) 2013-2016 transentis management & consulting. All rights reserved.
#
try:
    from sdmodel import LERP, SDModel
except:
    from BPTK_Py.sdcompiler.sdmodel import LERP, SDModel
    
import numpy as np
from scipy.interpolate import interp1d
from scipy.special import gammaln
import math, statistics
import random, logging


def random_with_seed(seed):
    random.seed(seed)
    return random.random()

def beta_with_seed(a,b,seed):
    np.random.seed(seed)
    return np.random.beta(a,b)
    
def binomial_with_seed(n,p,seed):
    np.random.seed(seed)
    return np.random.binomial(n,p)
    
def gamma_with_seed(shape,scale,seed):
    np.random.seed(seed)
    return np.random.gamma(shape,scale)
    
def exprnd_with_seed(plambda,seed):
    np.random.seed(seed)
    return np.random.exponential(plambda)
    
def geometric_with_seed(p,seed):
    np.random.seed(seed)
    return np.random.geometric(p)
    
{{header}}

class simulation_model(SDModel):
    import logging
    def rank(self, lis, rank):
        rank = int(rank)
        sorted_list = sorted(lis)
        try:
            rankth_elem = sorted_list[rank-1]
        except IndexError as e:
            logging.error("RANK: Rank {} too high for array of size {}".format(rank,len(lis)))
        return lis.index(rankth_elem)+1
        
    def __init__(self):
        # Simulation Buildins
        self.dt = {{specs.dt}}
        self.starttime = {{specs.start}}
        self.stoptime = {{specs.stop}}
        self.units = '{{specs.units}}'
        self.method = '{{specs.method}}'
        self.equations = {

        # Stocks
        {% if 'labels' in stocks %}
        <p>Priority: {{ stocks.labels }}</p>
        {% endif %}
    
        {% for stock in stocks -%}
        '{{ stock.name }}{% if "labels" in stock.keys() %}[{{ stock.labels }}]{% endif %}'          : lambda t: {{ stock.expression}},
        {% endfor %}
    
        # Flows
        {% for flow in flows -%}
        '{{ flow.name }}{% if "labels" in flow.keys() %}[{{ flow.labels }}]{% endif %}'             : lambda t: {{ flow.expression}},
        {% endfor %}
    
        # converters
        {% for converter in converters -%}
        '{{ converter.name }}{% if "labels" in converter.keys() %}[{{ converter.labels }}]{% endif %}'      : lambda t: {{ converter.expression}},
        {% endfor %}
    
        # gf
        {% for gf in gfs -%}
        '{{ gf.name }}{% if "labels" in gf.keys() %}[{{ gf.labels }}]{% endif %}' : lambda t: LERP( {{ gf.expression}}, self.points['{{gf.name}}']),
        {% endfor %}
    
        #constants
        {% for constant in constants -%}
        '{{ constant.name }}{% if "labels" in constant.keys() %}[{{ constant.labels }}]{% endif %}' : lambda t: {{ constant.expression}},
        {% endfor %}
    
    
        }
    
        self.points = {
            {% for gf in gfs -%}
            '{{ gf.name }}' :  {{ gf.points}}  , {% endfor %}
        }
    
    
        self.dimensions = {
        {% for key, dimension in dimensions.items() %}	'{{dimension.name}}': {
                'labels': [ {% for label in dimension.labels -%} '{{label}}' {%- if not loop.last -%}, {% endif %} {% endfor%} ],
                'variables': [ {% for variable in dimension.variables -%} '{{variable.name}}'  {%- if not loop.last -%} , {% endif %} {% endfor%} ],
            },
        {% endfor %}}
                
        self.dimensions_order = {{dimensions.order}}     
    
        self.stocks = [{% for stock in stocks -%} '{{stock.name}}{% if "labels" in stock.keys() %}[{{ stock.labels }}]{% endif %}'   {%- if not loop.last -%} , {% endif %}  {% endfor%}]
        self.flows = [{% for flow in flows -%} '{{flow.name}}{% if "labels" in flow.keys() %}[{{ flow.labels }}]{% endif %}' {%- if not loop.last -%}, {% endif %}  {% endfor%}]
        self.converters = [{% for converter in converters -%} '{{converter.name}}{% if "labels" in converter.keys() %}[{{ converter.labels }}]{% endif %}' {%- if not loop.last -%}, {% endif %}  {% endfor%}]
        self.gf = [{% for gf in gfs -%} '{{gf.name}}{% if "labels" in gf.keys() %}[{{ gf.labels }}]{% endif %}' {%- if not loop.last -%}, {% endif %}  {% endfor%}]
        self.constants= [{% for constant in constants -%} '{{constant.name}}{% if "labels" in constant.keys() %}[{{ constant.labels }}]{% endif %}' {%- if not loop.last -%}, {% endif %}  {% endfor%}]
        self.events = [{% for event in events -%}
                { 'key':'{{event.entity}}',
                'threshold':{event.threshold}},
                'direction':'{{event.direction}}',
                'repeat':'{{event.repeat}}',
                'interval':{{event.interval}},
                'messages':[{% for message in event.messages -%}
                    { 'message':'{{message.message}}','action':'{{message.action}}'} {% endfor%}{% endfor%}
            ]
    
        self.memo = {}
        for key in list(self.equations.keys()):
          self.memo[key] = {}  # DICT OF DICTS!
    
    def specs(self):
        return self.starttime, self.stoptime, self.dt, '{{specs.units}}', '{{specs.method}}'
    
'''