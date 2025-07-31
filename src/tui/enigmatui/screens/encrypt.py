from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Static, Header, Footer, TextArea, Button
from textual.events import Paste
from textual.containers import Container, Horizontal, Vertical

from enigmatui.utility.observer import Observer
from enigmatui.widgets.undeletable_textarea import UndeletableTextArea
from enigmatui.data.enigma_config import EnigmaConfig
from enigmapython.XRay import XRay
import pyperclip

import re

class EncryptScreen(Screen,Observer):

    _prev_cleartext_area_text = ""

    BINDINGS = [("ctrl+r", "reset", "Reset Enigma"),
                ("escape", "back", "Back")]
    enigma_config = EnigmaConfig()

    def action_reset(self):
        self.enigma_config.reset_enigma()
        self.query_one("#cleartext", TextArea).clear()
        self.query_one("#ciphertext", TextArea).clear()
        self.update(None,None,None)
        self._prev_cleartext_area_text = ""

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
                Static("Cleartext:", id="cleartext-label")
            ),
            Horizontal(
                UndeletableTextArea(id="cleartext"),
                Button("Copy", id="cleartext_copy"),
                Button("Paste", id="cleartext_paste")
            ),
            Static(""),
            Static(""),
            Horizontal(
                Static("Ciphertext:", id="ciphertext-label")
            ),
            Horizontal(
                UndeletableTextArea(id="ciphertext", read_only=True),
                Button("Copy", id="ciphertext_copy")
            )
        )
        
        yield Footer()

    def on_text_area_changed(self, event: TextArea.Changed) -> None:
        if event.text_area.id == "cleartext" and event.text_area.text != 'Type your cleartext here...' and event.text_area.text != "":
            # Save cleartext area (after the update)
            cleartext_area = event.text_area
            # Query the ciphertext area to update
            ciphertext_area = self.query_one("#ciphertext", TextArea)
            # Get the current cleartext area text (yet to be cleared)
            current_text = event.text_area.text
            # Get the previous cleartext area text (as it was before the update)
            prev_text = self._prev_cleartext_area_text
            # Remove from the cleartext area any character not in the alphabet list
            cleartext_area.text = re.sub(f"[^{''.join(self.enigma_config.enigma.alphabet_list)}]", "", current_text)
            # Update the _prev_cleartext_area_text with the update and cleared text
            self._prev_cleartext_area_text = cleartext_area.text
            # Set the cursor position to the end of the cleartext area
            cleartext_area.cursor_location = (len(cleartext_area.text.splitlines()) - 1, len(cleartext_area.text.splitlines()[-1]))
            # Append to the ciphertext area the just recently typed text (delta)
            ciphertext_area.text += self.enigma_config.enigma.input_string(cleartext_area.text[len(prev_text):])
            # Let the observers know that the enigma machine state has changed
            self.update(self.enigma_config, None, None)

        
    async def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "cleartext_copy":
            cleartext_area = self.query_one("#cleartext", TextArea)
            pyperclip.copy(cleartext_area.text)
        elif event.button.id == "cleartext_paste":
            paste_text =  pyperclip.paste()
            cleaned = re.sub(f"[^{''.join(self.enigma_config.enigma.alphabet_list)}]", "", paste_text)
            cleartext_area = self.query_one("#cleartext", TextArea)
            cleartext_area.text  += cleaned
        elif event.button.id == "ciphertext_copy":
            ciphertext_area = self.query_one("#ciphertext", TextArea)
            pyperclip.copy(ciphertext_area.text)


    def on_mount(self):
       self.enigma_config.add_observer(self)
       self.query_one("#enigma-diagram",Static).update(XRay.render_enigma_xray(self.enigma_config.enigma))
       self.query_one("#enigma-wirings",Static).update("Plugboard ({}) wiring: \n{}\n\n".format(type(self.enigma_config.enigma.plugboard).__name__,self.enigma_config.enigma.plugboard)+"ETW ({}) wiring: \n{}\n\n".format(type(self.enigma_config.enigma.etw).__name__,self.enigma_config.enigma.etw)+"\n".join(["Rotor {} ({}) wiring:\n{}\n".format(i,type(self.enigma_config.enigma.rotors[i]).__name__,self.enigma_config.enigma.rotors[i]) for i in range(len(self.enigma_config.enigma.rotors))])+"\nReflector ({}) wiring:\n{}\n".format(type(self.enigma_config.enigma.reflector).__name__,self.enigma_config.enigma.reflector))


    def update(self, observable, *args, **kwargs):
        self.query_one("#enigma-diagram",Static).update(XRay.render_enigma_xray(self.enigma_config.enigma))
        self.query_one("#enigma-wirings",Static).update("Plugboard ({}) wiring: \n{}\n\n".format(type(self.enigma_config.enigma.plugboard).__name__,self.enigma_config.enigma.plugboard)+"ETW ({}) wiring: \n{}\n\n".format(type(self.enigma_config.enigma.etw).__name__,self.enigma_config.enigma.etw)+"\n".join(["Rotor {} ({}) wiring:\n{}\n".format(i,type(self.enigma_config.enigma.rotors[i]).__name__,self.enigma_config.enigma.rotors[i]) for i in range(len(self.enigma_config.enigma.rotors))])+"\nReflector ({}) wiring:\n{}\n".format(type(self.enigma_config.enigma.reflector).__name__,self.enigma_config.enigma.reflector))
    
    #def on_screen_resume(self) -> None:
    #    self.query_one("#ciphertext", TextArea).clear()
    #    self.query_one("#cleartext", TextArea).clear()
            