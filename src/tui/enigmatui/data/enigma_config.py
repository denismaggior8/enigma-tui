from enigmapython import Enigma
class EnigmaConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.enigma = None  
        return cls._instance
    
    def set_enigma(self, enigma):
        self.enigma = enigma