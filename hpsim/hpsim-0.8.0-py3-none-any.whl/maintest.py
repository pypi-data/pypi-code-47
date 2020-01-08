




import numpy as np

from . import acceleration
from . import force
from . import miscfuncs
from . import solver
from . import integrator
from . import ensgen
from . import timestep
from . import timegen
from . import visual
from . import energy

class hpsim:
    def __init__(cls, preload = True):
        
        cls.ensemble         = []
        cls._force_dict      = {}
        cls._iteration_steps = 0
        cls.mute             = False
        
        if preload:
            if not cls.mute:
                print('Preloading the Solar System.')
            cls.preload_solar_system()
            
            
            
            
    def _record_data(cls, var_key, save_key):
        """ 
        Method that records data. You're not supposed to use this, I will.
        """
        cls.ensemble[save_key] = np.append(cls.ensemble[save_key],
                                np.reshape(cls.ensemble[var_key],
                                          (cls.ensemble['number of objects'],
                                           3,1)), axis = 2)
    
    
    
    def _step(cls):
        """
        Method for taking a single time step. You're not supposed to use this,
        I will.
        """
        
        # First let the integrator make sure everything is in order
        cls._integration_method(cls.ensemble, *cls._integration_args)
        
        # Then make an empty force list
        cls.force = []
        # Iterate over all forces
        for k in np.arange(0, len(cls.force_dict_keys), 2):
            fargs = []
            # Get a tuple with all the variables needed for the forces
            for i in cls._force_dict[cls.force_dict_keys[k+1]]:
                fargs.append(cls.ensemble[i])
            fargs = tuple(fargs)
            force_func = cls._force_dict[cls.force_dict_keys[k]]
            cls.force.append(force_func(*fargs)) # FORCES
            
        # Calculate the acceleration
        cls.ensemble['acceleration'] = cls._acceleration(
                cls.ensemble['affectee mass'], *tuple(cls.force) +
                                                    cls._acceleration_args)
        
        # Then use the acceleration to iterate one step.
        cls._solver(cls.ensemble, *cls._solver_args)
        cls._iteration_steps += 1
        cls._time_now += cls.time_step
    
    
    
    def preload_solar_system(cls):
        """
        Method for preloading the solar system. Includes the following:
            TODO: write what it includes.
        """
        cls._wanted_forces = [force.gravity]
        cls.set_time(0, timestep.constant_dt(1e6), timegen.time_years(50))
        cls.set_acceleration_function(acceleration.classic_acceleration)
        cls.set_wanted_forces(cls._wanted_forces)
        cls.set_ensemble_generator(ensgen.solar_system)
        cls.set_integrator(integrator.n_body_nice)
        cls.set_solver(solver.sym1, (cls.time_step,))
        cls.set_ensemble()
        if not cls.mute:
            print('The Solar System has been preloaded. Please run the \
              appropriate preload-function to load something else instead.')
    
    
    def preload_random_solar_system(cls):
        cls._wanted_forces = [force.gravity]
        cls.set_time(0, timestep.constant_dt(1e6), timegen.time_years(50))
        cls.set_acceleration_function(acceleration.classic_acceleration)
        cls.set_wanted_forces(cls._wanted_forces)
        cls.set_ensemble_generator(ensgen.random_solar_system)
        cls.set_integrator(integrator.n_body_nice)
        cls.set_solver(solver.sym1, (cls.time_step,))
        cls.set_ensemble()
    
    
    def preload_n_body_nice(cls):
        cls._wanted_forces = [force.gravity]
        cls.set_time(0, timestep.constant_dt(1e6), timegen.time_years(50))
        cls.set_acceleration_function(acceleration.classic_acceleration)
        cls.set_wanted_forces(cls._wanted_forces)
        cls.set_ensemble_generator(ensgen.n_body_nice)
        cls.set_integrator(integrator.n_body_nice)
        cls.set_solver(solver.sym1, (cls.time_step,))
        cls.set_ensemble()
    
    
    
    
    def run(cls):
        """ Run it all. """
        if not cls._ready_to_go:
            pass #except("Something is missing and hpsim shouldn't run.")
            
        while cls._time_now < cls.time_end:
            cls.step()
            cls._record_data('affectee position', 'affectee position data')
        cls.set_plot_routine(visual.simple_3d_anim, (cls._iteration_steps,))
        print(cls._plot_args)
        print(type(cls._plot_args))
        cls.plot_output = cls._plot_func(cls.ensemble, *cls._plot_args)
    
    
    
    
    def set_acceleration_function(func, args = (), 
                               class_name = None, class_args = ()):
        """ Sets the acceleration function. """
        if class_name:
            cls._acceleration_object = class_name(*class_args)
            cls._acceleration        = cls._acceleration_object.func
        else:
            cls._acceleration = func
        
        cls._acceleration_args = args
    
    
    def set_ensemble(cls):
        """ This method runs the ensemble generator and sets the
        ensemble - and then checks it if it hasn't already been. """
        
        #print(cls._ensemble_generator_args)
        #print(type(cls._ensemble_generator_args))
        cls.ensemble = cls._ensemble_generator(*cls._ensemble_generator_args)
        if not cls._ensemble_is_ok:
            cls._ensemble_is_ok = miscfuncs.ensemble_checker(cls.ensemble,
                                                        cls._force_variables)
            
    
    def set_ensemble_generator(cls, func, args = (), check_now = True,
                               class_name = None, class_args = ()):
        """ This method sets the ensemble generator.
        Inputs:
        func:       
            A required input function taking any number of arguments.
            Should return the desired ensemble.
        fargs = None:
            A tuple containing all the arguments required by func.
            Can be left blank in case func takes no arguments.
        check_now = True:
            A boolean to tell if the program should test the ensem-
            ble generator now. Note that changing ensemble genera-
            tor will make the ensemble flagged as unchecked."""
        
        # If no fargs are present, the input args should be empty.
        if class_name:
            cls._ensemble_object    = class_name(*class_args)
            cls._ensemble_generator = cls._ensemble_object.func
        else:
            cls._ensemble_generator = func
        
        cls._ensemble_generator_args = args
        cls._ensemble_is_ok = False
        
        if check_now:
            cls._ensemble_is_ok = miscfuncs.ensemble_checker(
                    cls._ensemble_generator(*cls._ensemble_generator_args),
                    cls._force_variables)
        #print(cls._ensemble_generator_args)
        #print(type(cls._ensemble_generator_args))
        #cls.ensemble = cls._ensemble_generator(*cls._ensemble_generator_args)
        
    
    def set_force_dictionary(cls, func, keys, arg_keys):
        """ Sets the force dict. First key should be named "force <name>", 
        the second should be named "args <name>". It should throw an error,
        if they don't. """
        # TODO: MAKE FUNCTION THROW ERROR IF GIVEN KEYS DO NOT MATCH
        cls._force_dict[keys[0]] = func
        
        if arg_keys:
            cls._force_dict[keys[1]] = arg_keys
        else:
            cls._force_dict[keys[1]] = ()
        
        # A variable containing all keys in force_dict - for making use of it.
        cls.force_dict_keys = list(cls._force_dict.keys())
        
        # cls.force_dict_keys is supposed to contain
        # ['force force1', 'args force1'] etc
    
    
    def set_integration_method(cls, func, args = (), 
                               class_name = None, class_args = ()):
        """ 
        This method sets the integrator (name change pending).
        Inputs:
        func:
            A required input function taking any number of arguments.
            Should return the desired integration setup.
        args = ():
            A tuple containing all the arguments required by func.
            Can be left blank in case func takes no arguments. 
        class_name = None:
            In the case of func being a method in a class (for constructor
            purposes), the name of the class can be written here, or left 
            blank if fun is not a class method.
        class_args = ():
            A tuple containing all the arguments required by the class __init__
            function.
        """
        if class_name:
            cls._integration_object = class_name(*class_args)
            cls._integration_method = cls._integration_object.func
        else:
            cls._integration_method = func
        
        cls._integration_args = args
            
    
    def set_plot_routine(cls, func, args = (), 
                               class_name = None, class_args = ()):
        """ Sets the plotting routine. """
        if class_name:
            cls._plot_object = class_name(*class_args)
            cls._plot_func   = cls._plot_object.func
        else:
            cls._plot_func   = func
        
        cls._plot_args = args
    
    
    def set_solver(cls, func, args = (),
                   class_name = None, class_args = ()):
        """ Sets the solver. """
        if class_name:
            cls._solver_object = class_name(*class_args)
            cls._solver        = cls._solver_object.func
        else:
            cls._solver        = func
        
        cls._solver_args = args
        
    
    def set_time(cls, time_start, time_step, time_end):
        cls.time_start = time_start
        cls.time_step  = time_step
        cls.time_end   = time_end
        cls._time_now  = time_start
    
    
    def set_wanted_forces(cls, funcs):
        """ funcs should be a list with the wanted forces' functions, or
        the wanted forces one at a time. """
        for f in funcs:
            standard_force_params = force.check_force(f)
            #check_force returns a dict if the force is standard, else False
            if standard_force_params:
                cls.set_force_dictionary(f, **standard_force_params)
            else:
                Warning('The force' + f + 'is not in the standard library. \
                        you should call main.set_force_dict yourself.')
        cls._force_variables = miscfuncs.get_force_variables(cls.funcs)
        
    
    def switch_mute(cls):
        cls.mute *= -1
        