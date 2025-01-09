from enigmatui.utility.observable import Observable
import copy
class EnigmaConfig(Observable):
    _instance = None
   
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(EnigmaConfig, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not self._initialized:
            super().__init__()  # Initialize the observer
            self.configured_enigma = None  # 
            self.enigma = None 
            self._initialized = True
    
    def set_configured_enigma(self, enigma):
        self.configured_enigma = enigma
        self.enigma = self.configured_enigma.clone()
        self.notify_observers(self,None,None)
    
    def unset_configured_enigma(self):
        self.configured_enigma = None
        self.enigma = None

    def reset_enigma(self):
        self.enigma = self.configured_enigma.clone()
        self.notify_observers(self,None,None)
    
    
   
   