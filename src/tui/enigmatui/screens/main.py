from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Static, Header, Footer

class MainScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("This is the main application screen.", id="main-text")