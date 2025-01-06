from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Static, Header, Footer, TextArea
from enigmapython.Utils import Utils
from textual.containers import Container, Horizontal, Vertical

from enigmatui.utility.observer import Observer
from enigmatui.data.enigma_config import EnigmaConfig

class EncryptScreen(Screen,Observer):

    BINDINGS = [("escape", "exit", "Exit")]
    enigma_config = EnigmaConfig()


    def action_exit(self):
        self.app.pop_screen()    

    def compose(self) -> ComposeResult:
        yield Header()
        yield Horizontal(
            Vertical(
                Static("", id="enigma-diagram")
            ),
            Vertical(
                Static("", id="enigma-wirings")
            )
        )
        yield Horizontal(
            
        )
        yield Horizontal(
                TextArea("", id="cleartext")
        )
        yield Horizontal(
                TextArea("", id="cyphertext")
        )
        yield Footer()

    def on_mount(self):
       self.enigma_config.add_observer(self)
       self.query_one("#enigma-diagram",Static).update(Utils.render_enigma_diagram(self.enigma_config.enigma))
       self.query_one("#enigma-wirings",Static).update("\n".join(["Rotor {} position:\n{}".format(i,self.enigma_config.enigma.rotors[i]) for i in range(len(self.enigma_config.enigma.rotors))]))


    def update(self, observable, *args, **kwargs):
       self.query_one("#enigma-diagram",Static).update(Utils.render_enigma_diagram(self.enigma_config.enigma))
       self.query_one("#enigma-wirings",Static).update("\n".join(["Rotor {} position:\n{}".format(i,self.enigma_config.enigma.rotors[i]) for i in range(len(self.enigma_config.enigma.rotors))]))
            