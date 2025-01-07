from enigmatui.utility.observable import Observable
import copy
class EnigmaConfig(Observable):
    _instance = None
   
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(EnigmaConfig, cls).__new__(cls)
            cls._instance.configured_enigma = None  # valore predefinito
            cls._instance.enigma = None  # valore predefinito
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not self._initialized:
            super().__init__()  # Initialize the observer
    
    def set_configured_enigma(self, enigma):
        self.configured_enigma = enigma
        self.enigma = self.configured_enigma.clone()
        self.notify_observers(self,None,None)

    def reset_enigma(self):
        self.enigma = self.configured_enigma.clone()
        self.notify_observers(self,None,None)
    
   
   