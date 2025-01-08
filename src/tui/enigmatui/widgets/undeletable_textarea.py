from textual.widgets import TextArea
from textual import events
from enigmatui.data.enigma_config import EnigmaConfig

class UndeletableTextArea(TextArea):

    enigma_config = EnigmaConfig()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _on_key(self,  event: events.Key):
        #if event.key == "backspace" or event.key == "enter" :
        if (event.key == "enter" or event.key == "space" or event.key == "backspace" or event.key == "ctrl+d") or (event.is_printable and event.key not in self.enigma_config.enigma.alphabet_list):
            event.stop()
            event.prevent_default()
        else:
           super()._on_key(event)
            