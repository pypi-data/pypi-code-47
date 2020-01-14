"""
indi game engine - input module
"""
from .event import EventType
from .keyboard import KeyEventCode, KeyCode, KeyModifier, Keyboard
from .touch import TouchEventCode, Touch

def getKeyboard():    
    return Keyboard.instance()

def getTouch():    
    return Touch.instance()
