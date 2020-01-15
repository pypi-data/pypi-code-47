# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 08:49:16 2019

@author: khaled.ghobashy
"""
# Standard library imports
import os

# 3rd party library imports
import cloudpickle
import sympy as sm

# Local applicataion imports
from ...symbolic.components import joints as joints
from ...symbolic.components import forces as forces
from ...symbolic.systems import topology_classes as topology_classes
from ...symbolic.systems import configuration_classes  as cfg_cls
from ...symbolic.components.matrices import vector
from ..serialization.structural.json.configuration_encoder import generator

###############################################################################

def get_file_name(script_path):
    name = os.path.basename(script_path).split('.')[0]
    return name

def load_pickled_data(file):
    with open(file, 'rb') as f:
        instance = cloudpickle.load(f)
    return instance


###############################################################################
###############################################################################

class config_node(object):

    def __init__(self, config_instance):
        self.config = config_instance
        self._decorate_items()
    
    @property
    def _items(self):
        members = {i:getattr(self,i) for i in dir(self) if not (i.startswith('_') and i.startswith("__"))}
        return members

    def _decorate_items(self):
        for attr,obj in self._items.items():
            setattr(self, attr, self._decorate(obj))
    
    def _decorate(self, edge_component):
        raise NotImplementedError


class geometries_nodes(object):

    def __init__(self, config_instance):
        self.Composite_Geometry = cfg_cls.Composite_Geometry
        self.Cylinder_Geometry = cfg_cls.Cylinder_Geometry
        self.Triangular_Prism = cfg_cls.Triangular_Prism
        self.Sphere_Geometry = cfg_cls.Sphere_Geometry

        super().__init__(config_instance)

    def _decorate(self, symbolic_type):
        def decorated(name, args, mirror=False):
            self.config.add_node(edge_component, *args, **kwargs)
        return decorated


class configuration(object):
    
    def __init__(self, name, model_instance):
        self.name = get_file_name(name)
        self.config = cfg_cls.abstract_configuration(self.name, model_instance.topology)
        self._decorate_methods()

    
    def add_node()
    
    @property
    def add_point(self):
        """
        Add a spatial point.

        Availabe Methods:
            'UserInput', 'Mirrored', 'Centered', 'Equal_to'
        """
        return self._point_methods
    
    @property
    def add_vector(self):
        return self._vector_methods
    
    @property
    def add_scalar(self):
        return self._scalar_methods
    
    @property
    def add_geometry(self):
        return self._geometry_methods
    
    @property
    def add_relation(self):
        return self._relation_methods
    
    def assign_geometry_to_body(self, body, geo, eval_inertia=True, mirror=False):
        self.config.assign_geometry_to_body(body, geo, eval_inertia, mirror)
    
    def assemble(self):
        self.config.assemble_equalities()


    def extract_inputs_to_csv(self, path):
        file_path = os.path.join(path, self.name)
        inputs_dataframe = self.config.create_inputs_dataframe()
        inputs_dataframe.to_csv('%s.csv'%file_path)
    
    def export_JSON_file(self, path=''):
        config_constructor = generator(self.config)
        config_constructor.write_JSON_file(path)
    
    def save(self):
        file = '%s.scfg'%self.name
        with open(file, 'wb') as f:
            cloudpickle.dump(self, f)
    
    def _decorate_methods(self):
        self._decorate_point_methods()
        self._decorate_vector_methods()
        self._decorate_scalar_methods()
        self._decorate_geometry_methods()
        self._decorate_relation_methods()

    def _decorate_point_methods(self):
        sym = 'hp'
        node_type = vector
        methods = ['Mirrored', 'Centered', 'Equal_to', 'UserInput']
        self._point_methods = self._decorate_components(node_type, sym, 
                                                        methods, cfg_cls.CR)
        
    def _decorate_vector_methods(self):
        sym = 'vc'
        node_type = vector
        methods = ['Mirrored', 'Oriented', 'Equal_to', 'UserInput']
        self._vector_methods = self._decorate_components(node_type, sym, 
                                                         methods, cfg_cls.CR)

    def _decorate_scalar_methods(self):
        sym = ''
        node_type = sm.symbols
        methods = ['Equal_to', 'UserInput']
        self._scalar_methods = self._decorate_components(node_type, sym, 
                                                         methods, cfg_cls.CR)
            
    def _decorate_geometry_methods(self):
        sym = 'gm'
        node_type = cfg_cls.Geometry
        methods = ['Composite_Geometry', 
                   'Cylinder_Geometry', 
                   'Triangular_Prism',
                   'Sphere_Geometry']
        self._geometry_methods = self._decorate_components(node_type, sym, 
                                                           methods, cfg_cls.Geometries)

    def _decorate_relation_methods(self):
        sym = None
        node_type = None
        methods = ['Mirrored', 'Centered', 'Equal_to', 'Oriented', 'UserInput']
        self._relation_methods = self._decorate_components(node_type, sym, 
                                                           methods, cfg_cls.CR)

    def _decorate_components(self, node_type, sym, methods_list, methods_class):   
        container_class = type('container', (object,), {})
        def dummy_init(dself): pass
        container_class.__init__ = dummy_init
        container_instance = container_class()

        for name in methods_list:
            method = getattr(methods_class, name)
            decorated_method = self._decorate_as_attr(node_type, sym, method)
            setattr(container_instance, name, decorated_method)
        
        return container_instance
    
    def _decorate_as_attr(self, symbolic_type, sym, construction_method):
        
        if construction_method is None:
            def decorated(*args, **kwargs):
                name = args[0]
                self._add_node(name, symbolic_type , sym=sym, **kwargs)
            decorated.__doc__ = ''
        
        elif symbolic_type is None:
            def decorated(*args, **kwargs):
                self._add_relation(construction_method, *args, **kwargs)
            decorated.__doc__ = construction_method.__doc__
       
        else:
            def decorated(*args, **kwargs):
                name = args[0]
                node = self._add_node(name, symbolic_type, sym=sym, **kwargs)
                self._add_relation(construction_method, node, *args[1:], **kwargs)
            decorated.__doc__ = construction_method.__doc__
        
        return decorated
    
    def _add_node(self, name, symbolic_type, **kwargs):
        return self.config.add_node(name, symbolic_type, **kwargs)

    def _add_relation(self, relation, node, arg_nodes, **kwargs):
        self.config.add_relation(relation, node, arg_nodes, **kwargs)


###############################################################################
###############################################################################

