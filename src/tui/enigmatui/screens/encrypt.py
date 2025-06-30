from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Static, Header, Footer, TextArea
from enigmapython.XRay import XRay
from textual.containers import Container, Horizontal, Vertical

from enigmatui.utility.observer import Observer
from enigmatui.widgets.undeletable_textarea import UndeletableTextArea
from enigmatui.data.enigma_config import EnigmaConfig

class EncryptScreen(Screen,Observer):

    BINDINGS = [("ctrl+r", "reset", "Reset Enigma"),
                ("escape", "back", "Back")]
    enigma_config = EnigmaConfig()

    def action_reset(self):
        self.enigma_config.reset_enigma()
        self.query_one("#cleartext", TextArea).clear()
        self.query_one("#ciphertext", TextArea).clear()
        self.update(None,None,None)

    def action_back(self):
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
                UndeletableTextArea(id="cleartext")
            ),
            Static(""),
            Static(""),
            Horizontal(
                Static("Ciphertext:", id="ciphertext-label"),
            ),
            Horizontal(
                UndeletableTextArea(id="ciphertext", read_only=True)
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
       self.query_one("#enigma-diagram",Static).update(XRay.render_enigma_xray(self.enigma_config.enigma))
       self.query_one("#enigma-wirings",Static).update("Plugboard ({}) wiring: \n{}\n\n".format(type(self.enigma_config.enigma.plugboard).__name__,self.enigma_config.enigma.plugboard)+"ETW ({}) wiring: \n{}\n\n".format(type(self.enigma_config.enigma.etw).__name__,self.enigma_config.enigma.etw)+"\n".join(["Rotor {} ({}) wiring:\n{}\n".format(i,type(self.enigma_config.enigma.rotors[i]).__name__,self.enigma_config.enigma.rotors[i]) for i in range(len(self.enigma_config.enigma.rotors))])+"\nReflector ({}) wiring: {}\n".format(type(self.enigma_config.enigma.reflector).__name__,self.enigma_config.enigma.reflector))


    def update(self, observable, *args, **kwargs):
        self.query_one("#enigma-diagram",Static).update(XRay.render_enigma_xray(self.enigma_config.enigma))
        self.query_one("#enigma-wirings",Static).update("Plugboard ({}) wiring: \n{}\n\n".format(type(self.enigma_config.enigma.plugboard).__name__,self.enigma_config.enigma.plugboard)+"ETW ({}) wiring: \n{}\n\n".format(type(self.enigma_config.enigma.etw).__name__,self.enigma_config.enigma.etw)+"\n".join(["Rotor {} ({}) wiring:\n{}\n".format(i,type(self.enigma_config.enigma.rotors[i]).__name__,self.enigma_config.enigma.rotors[i]) for i in range(len(self.enigma_config.enigma.rotors))])+"\nReflector ({}) wiring: {}\n".format(type(self.enigma_config.enigma.reflector).__name__,self.enigma_config.enigma.reflector))
    
    #def on_screen_resume(self) -> None:
    #    self.query_one("#ciphertext", TextArea).clear()
    #    self.query_one("#cleartext", TextArea).clear()
            