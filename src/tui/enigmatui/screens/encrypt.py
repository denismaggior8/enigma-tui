from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Static, Header, Footer, TextArea
from enigmapython.Utils import Utils
from textual.containers import Container, Horizontal, Vertical

from enigmatui.utility.observer import Observer
from enigmatui.widgets.placeholder_textarea import PlaceholderTextArea
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
                Static("", id="enigma-diagram"),
                id="enigma-diagram-vertical"
            ),
            Vertical(
                Static("", id="enigma-wirings"),
                id="enigma-wirings-vertical"
            ),
            id="enigma-diagram-wirings-horizontal"
        )
        yield Vertical(
            Horizontal(
                Static("Cleartext:", id="cleartext-label"),
            ),
            Horizontal(
                TextArea(id="cleartext")
            ),
            Static(""),
            Static(""),
            Horizontal(
                Static("Ciphertext:", id="ciphertext-label"),
            ),
            Horizontal(
                TextArea(id="ciphertext", read_only=True)
            )
        )
        
        yield Footer()

    def on_text_area_changed(self, event: TextArea.Changed) -> None:
        if event.text_area.id == "cleartext" and event.text_area.text != 'Type your cleartext here...' and event.text_area.text != "":
            if self.query_one("#ciphertext", TextArea).text == "Read your ciphertext here...":
               self.query_one("#ciphertext", TextArea).clear()
            self.query_one("#ciphertext", TextArea).text = self.query_one("#ciphertext", TextArea).text + self.enigma_config.enigma.input_char(event.text_area.text[-1])
            self.update(self.enigma_config, None, None)

    def on_mount(self):
       self.enigma_config.add_observer(self)
       self.query_one("#enigma-diagram",Static).update(Utils.render_enigma_diagram(self.enigma_config.enigma))
       self.query_one("#enigma-wirings",Static).update("ETW wiring: \n{}\n\n".format(self.enigma_config.enigma.etw.wiring)+"\n".join(["Rotor {} wiring:\n{}\n".format(i,self.enigma_config.enigma.rotors[i]) for i in range(len(self.enigma_config.enigma.rotors))])+"\nReflector wiring: {}\n".format(self.enigma_config.enigma.reflector.wiring))


    def update(self, observable, *args, **kwargs):
       self.query_one("#enigma-diagram",Static).update(Utils.render_enigma_diagram(self.enigma_config.enigma))
       self.query_one("#enigma-wirings",Static).update("ETW wiring: \n{}\n\n".format(self.enigma_config.enigma.etw.wiring)+"\n".join(["Rotor {} wiring:\n{}\n".format(i,self.enigma_config.enigma.rotors[i]) for i in range(len(self.enigma_config.enigma.rotors))])+"\nReflector wiring: {}\n".format(self.enigma_config.enigma.reflector.wiring))
            