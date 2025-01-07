from textual.widgets import TextArea
from textual import events

class PlaceholderTextArea(TextArea):
    def __init__(self, placeholder, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.placeholder = placeholder
        self.text = placeholder
        self.placeholder_active = True
        

    def _on_key(self,  event: events.Key):
        print(f"Key pressed: {event.key}")
        if self.placeholder_active:
            self.clear()  # Clear the placeholder
            self.placeholder_active = False
        if event.key == "r":
            event.prevent_default()
        else:
            super()._on_key(event)