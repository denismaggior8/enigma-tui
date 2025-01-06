from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Static, Header, Footer
import asyncio

SPLASH_TEXT = """Enigma TUI is a Terminal User Interface for Enigma machines, 
allowing you to simulate different Enigma machine models from the terminal."""



ENIGMA_DIAG = """
                UKW        Rotor       Rotor       Rotor        ETW      PLUGBOARD
                             2           1           0      
              +-----+     +-----+     +-----+     +-----+     +-----+     +-----+
              |     |     |     |     |     |     |     |     |     |     |     |
              |  +--|--<--|-----|--<--|-----|--<--|-----|--<--|-----|--<--|-----|----< d <-- Key
              |  |  |  w  |     |  n  |     |  l  |     |  d  |     |  d  |     |
              |  |  |     |     |     |     |     |     |     |     |     |     |
              |  |  |     |     |     |     |     |     |     |     |     |     |
              |  |  |  v  |     |  i  |     |  v  |     |  n  |     |  m  |     |     
              |  +--|-->--|-----|-->--|-----|-->--|-----|-->--|-----|-->--|-----|----> n --> Lamp
              |     |     |     |     |     |     |     |     |     |     |     |
              +-----+     +-----+     +-----+     +-----+     +-----+     +-----+

        Pos.:                00          00          01    
        Ring:                00          00          00
"""
class SplashScreen(Screen):

    BINDINGS = [("enter", "app.pop_screen", "Go to app")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static(" Welcome! ", id="welcome")
        yield Static(SPLASH_TEXT, id="splash-text")
        yield Static(ENIGMA_DIAG, id="enigma-diagram")
        yield Static("On every screen, ⬇️  see in the bar at the bottom ⬇️  the possible options. Now press enter to continue.", id="any-key")
        yield Footer()
    
 
