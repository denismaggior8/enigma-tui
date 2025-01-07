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
        self.reset_enigma()
        self.notify_observers(self,None,None)

    def reset_enigma(self):
        self.enigma =  copy.deepcopy(self.configured_enigma) 
        self.notify_observers(self,None,None)
    
   
   