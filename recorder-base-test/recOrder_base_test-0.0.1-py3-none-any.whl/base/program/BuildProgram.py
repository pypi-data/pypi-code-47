# bchhun, {2019-07-25}

from ..acquisition import AcquisitionBase
from ..analysis import AnalyzeBase
from ..visualization import VisualizeBase
from ..utils import ProcessRunnable


class Program:
    """
    Connects module signals and slots.  Then runs any annotated runnables
    """

    # enable us to inspect all registered modules without this Program instance
    static_acq = []
    static_proc = []
    static_vis = []

    def __init__(self, acquire=None, analyze=None, visualize=None):

        # register lists of all modules in this application
        self.acq = []
        self.proc = []
        self.vis = []
        self.runnables = []

        self._assignments = set()

        # 'register' supplied modules in a list
        if issubclass(acquire.__class__, AcquisitionBase):
            self.acq.append(acquire)
            Program.static_acq.append(acquire)
            print("registering "+str(acquire))
        if issubclass(analyze.__class__, AnalyzeBase):
            self.proc.append(analyze)
            Program.static_proc.append(analyze)
            print("registering "+str(analyze))
        if issubclass(visualize.__class__, VisualizeBase):
            self.vis.append(visualize)
            Program.static_vis.append(visualize)
            print("registering "+str(visualize))

    def add_module(self, module):
        # add more modules to registry
        if issubclass(module.__class__, AcquisitionBase):
            self.acq.append(module)
            Program.static_acq.append(module)
        if issubclass(module.__class__, AnalyzeBase):
            self.proc.append(module)
            Program.static_proc.append(module)
        if issubclass(module.__class__, VisualizeBase):
            self.vis.append(module)
            Program.static_vis.append(module)

    def build(self):
        self._connect_signals()
        self._assign_runnables()

    def _connect_signals(self):
        """
        for all registered modules, assigns all signals to all slots between and within modules based on channels
        """
        for acq in self.acq:
            [self._assign_signal_slot(acq, acq2) for acq2 in self.acq]
            [self._assign_signal_slot(acq, proc) for proc in self.proc]
            [self._assign_signal_slot(acq, vis) for vis in self.vis]

        for proc in self.proc:
            [self._assign_signal_slot(proc, acq) for acq in self.acq]
            [self._assign_signal_slot(proc, proc2) for proc2 in self.proc]
            [self._assign_signal_slot(proc, vis) for vis in self.vis]

        for vis in self.vis:
            [self._assign_signal_slot(vis, acq) for acq in self.acq]
            [self._assign_signal_slot(vis, proc2) for proc2 in self.proc]
            [self._assign_signal_slot(vis, vis2) for vis2 in self.vis]

    def _assign_signal_slot(self, sig, slt):
        """
        Inspects provided classes for "emitter", "receiver", and "bidirectional" function decorations
        then, inspects those functions for matching channel assignments
        finally, connects the signals
        :param sig: Class that inherits one of the above three base classes, may contain pyqtSignals
        :param slt: Class that inherits one of the above three base classes, may contain pyqtSlots
        :return: None
        """

        sig_dict = self._retrieve_emitter_receiver_attribute(sig, 'emitter')
        slt_dict = self._retrieve_emitter_receiver_attribute(slt, 'receiver')

        # find all functions in sig that are decorated, and their corresponding channels
        for value, key in sig_dict.items():
            emitter_func = getattr(sig, key)

            # find all functions in slt that are decorated, and their corresponding channels
            for value2, key2 in slt_dict.items():
                receiver_func = getattr(slt, key2)

                # check matching channels and connect
                if emitter_func.emitter_channel == receiver_func.receiver_channel:
                    #todo: the problem is that some sigal/slots are double connected.  This is a workaround but
                    # does not identify the underlying problem.
                    if (str(emitter_func)+str(receiver_func)) in self._assignments:
                        print("connection exists, skipping: %s\t to %s\t" % (str(emitter_func), str(receiver_func)))
                        return
                    else:
                        sig.get_QChannel(emitter_func.emitter_channel).QChannel.connect(receiver_func)
                        self._assignments.add((str(emitter_func)+str(receiver_func)))
                        print("connecting %s\t to \t%s " % (str(emitter_func), str(receiver_func)))

    @staticmethod
    def _retrieve_emitter_receiver_attribute(module, socket_type):
        """
        identifies all functions annotated with 'emitter' and 'receiver' and puts these functions in a dictionary

        this dictionary is in {value: key} order to prevent collisions
            values = attributes or function identifier
            key = corresponding attribute or function name

        dictionary is a concatenated group of both __class__ and instance attributes

        * assumption is that there will be collisions if {key:value} is concatenated.
        *   so instead we reverse the dictionary order.
        """
        output_dict = {}
        # this function returns a concatenated dictionary of only those emitter/receiver functions
        if socket_type == 'emitter':

            # find methods with static decoration
            static_dict = {value: key for key, value in module.__class__.__dict__.items() if
                           "staticmethod" in str(value)}
            static_inspect = {value: key for value, key in static_dict.items() if
                              ".emitter" in str(module.__getattribute__(key)) or
                              '.bidirectional' in str(module.__getattribute__(key))}
            output_dict.update(static_inspect)

            # find methods with class decoration
            class_dict = {value: key for key, value in module.__class__.__dict__.items() if
                          ".emitter" in str(value) or ".bidirectional" in str(value)}
            output_dict.update(class_dict)

            # find instance methods
            inst_dict = {value: key for key, value in module.__dict__.items() if
                         ".emitter" in str(value) or ".bidirectional" in str(value)}
            output_dict.update(inst_dict)
            return output_dict

        elif socket_type == 'receiver':

            # find methods with static decoration
            static_dict = {value: key for key, value in module.__class__.__dict__.items() if
                           "staticmethod" in str(value)}
            static_inspect = {value: key for value, key in static_dict.items() if
                              ".receiver" in str(module.__getattribute__(key)) or
                              '.bidirectional' in str(module.__getattribute__(key))}
            output_dict.update(static_inspect)

            # find methods with class decoration
            class_dict = {value: key for key, value in module.__class__.__dict__.items() if
                          ".receiver" in str(value) or ".bidirectional" in str(value)}
            output_dict.update(class_dict)

            # find instance methods
            inst_dict = {value: key for key, value in module.__dict__.items() if
                         ".receiver" in str(value) or ".bidirectional" in str(value)}
            output_dict.update(inst_dict)
            return output_dict
        else:
            raise ValueError("must supply 'emitter' or 'receiver' as parameter")

    def _assign_runnables(self):
        for acq in self.acq:
            acq_dict = self._retrieve_runnables(acq)
            for value, key in acq_dict.items():
                runnable = getattr(acq, key)
                self.runnables.append(runnable)
        for proc in self.proc:
            proc_dict = self._retrieve_runnables(proc)
            for value, key in proc_dict.items():
                runnable = getattr(proc, key)
                self.runnables.append(runnable)
        for vis in self.vis:
            vis_dict = self._retrieve_runnables(vis)
            for value, key in vis_dict.items():
                runnable = getattr(vis, key)
                self.runnables.append(runnable)

    @staticmethod
    def _retrieve_runnables(module):
        """
        identifies all functions annotated with 'runnable' and puts these functions in a dictionary

        this dictionary is in {value: key} order to prevent collisions
            values = attributes or function identifier
            key = corresponding attribute or function name

        dictionary is a concatenated group of both __class__ and instance attributes

        * assumption is that there will be collisions if {key:value} is concatenated.
        *   so instead we reverse the dictionary order.
        """
        # this function returns a concatenated dictionary of only those runnable functions
        class_dict = {value: key for key, value in module.__class__.__dict__.items() if
                      ".runnable" in str(value)}
        inst_dict = {value: key for key, value in module.__dict__.items() if
                     ".runnable" in str(value)}
        class_dict.update(inst_dict)
        return class_dict

    def run(self):
        """
        for any runnables declared, launch them in a new pyqtThread
        :return: None
        """
        for runnable in self.runnables:
            process = ProcessRunnable(target=runnable, args=())
            process.start()


