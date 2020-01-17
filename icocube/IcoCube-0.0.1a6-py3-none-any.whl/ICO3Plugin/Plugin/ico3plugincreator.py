#  Copyright (c) $Gille PREVOT, Guillaume PREVOT, Anne-Delphine PREVOT
import importlib
import inspect
from ICO3PluginCollection.MessageView.MessageFramePlugin import MessageFramePlugin

class ICO3PluginCreator:

    @staticmethod
    def instanciatePlugin(module_name, class_name, xMainFrame, xPosition = None):
        instance = None

        #AAAAA = MessageFramePlugin(xMainFrame, xPosition)

        try:
            module = importlib.import_module(module_name)
            xx = inspect.getmembers(module, inspect.isclass)
            class_ = getattr(module, class_name)
            # if issubclass(class_, ICO3FramePlugin) :
            instance = class_(xMainFrame, xPosition)
            # else :
            #     instance = class_()
            return instance
        except Exception as e:
            print("***ERROR****  " +module_name+" "+  class_name + " "+ str(e) )
        return None


