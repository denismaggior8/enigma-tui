from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal
from textual.widgets import Header, Footer, Button, Select, Static, Header
from textual.events import Key
from enigmatui.screens.splash import SplashScreen
from enigmatui.screens.main import MainScreen
from enigmatui.screens.configure import ConfigureScreen
from enigmatui.screens.encrypt import EncryptScreen


class EnigmaApp(App[str]):
   
    CSS_PATH = "css/styles.css"
    TITLE = "Enigma TUI"
    SUB_TITLE = "A Terminal User Interface for Enigma machines by Denis Maggiorotto"

    def compose(self) -> ComposeResult:
        yield Header()

    def on_mount(self):
        self.install_screen(SplashScreen(), name="splash")
        self.install_screen(MainScreen(), name="main")
        self.push_screen("main") 
        self.push_screen("splash") 

   
        

    
