from textual.widgets import TextArea
from textual import events

class PlaceholderTextArea(TextArea):
    def __init__(self, placeholder, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = placeholder
        self.placeholder_active = True
        

    def _on_key(self,  event: events.Key):
        if self.placeholder_active:
            self.clear() 
            self.placeholder_active = False
            
        if event.key == "backspace":
            event.stop()
            event.prevent_default()
        else:
           super()._on_key(event)
            