from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Static, Header, Footer

class ConfigureScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("This is the configuration screen.", id="main-text")
        yield Footer()