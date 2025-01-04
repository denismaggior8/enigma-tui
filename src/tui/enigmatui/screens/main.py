from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.containers import Horizontal, Vertical
from textual.widgets import Static, Header, Footer, Button
from enigmatui.screens.configure import ConfigureScreen
from enigmatui.screens.encrypt import EncryptScreen

class MainScreen(Screen):

    BINDINGS = [("c", "go_to_configure", "Configure"), ("e", "go_to_encrypt", "De/Encrypt")]

    def action_go_to_configure(self):
        self.app.push_screen("configure")

    def action_go_to_encrypt(self):
        self.app.push_screen("encrypt")

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("What do you want to do?", id="main-text")
        yield Footer()

    def on_mount(self):
        self.app.install_screen(ConfigureScreen(), name="configure")
        self.app.install_screen(EncryptScreen(), name="encrypt")