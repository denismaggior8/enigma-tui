from textual.widgets import TextArea
from textual import events

class UndeletableTextArea(TextArea):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _on_key(self,  event: events.Key):
        if event.key == "backspace":
            event.stop()
            event.prevent_default()
        else:
           super()._on_key(event)
            