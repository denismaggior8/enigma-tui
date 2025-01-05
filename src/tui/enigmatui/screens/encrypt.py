from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Static, Header, Footer

class EncryptScreen(Screen):

    BINDINGS = [("escape", "exit", "Exit")]

    def action_exit(self):
        self.app.pop_screen()

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("This is the de/encrypt screen.", id="main-text")
        yield Footer()