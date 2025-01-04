from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Static, Header, Footer
import asyncio

SPLASH_TEXT = """Enigma TUI is a Terminal User Interface for Enigma machines, 
allowing you to simulate different Enigma machine models from the terminal."""


class SplashScreen(Screen):

    BINDINGS = [("enter", "app.pop_screen", "Go to app")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static(" Welcome! ", id="welcome")
        yield Static(SPLASH_TEXT, id="splash-text")
        yield Static("Press enter to continue [blink]_[/]", id="any-key")
        yield Footer()
    
 
