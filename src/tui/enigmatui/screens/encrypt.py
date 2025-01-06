from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Static, Header, Footer
from enigmapython.Utils import Utils
from textual.containers import Container, Horizontal, Vertical

from enigmatui.data.enigma_config import EnigmaConfig

class EncryptScreen(Screen):

    BINDINGS = [("escape", "exit", "Exit")]
    enigma_config = EnigmaConfig()


    def action_exit(self):
        self.app.pop_screen()    

    def compose(self) -> ComposeResult:
        yield Header()
        yield Horizontal(
            Vertical(
                Static("", id="enigma-diagram")
            )
        )
        yield Footer()

    def on_mount(self):
       self.query_one("#enigma-diagram").update(Utils.render_enigma_diagram(self.enigma_config.enigma))
       
            