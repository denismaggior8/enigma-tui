from textual.widgets import Input
from textual import events
from enigmatui.data.enigma_config import EnigmaConfig

class PlugboardInput(Input):

    async def on_input_changed(self, event: Input.Changed) -> None:
        event.value = event.value.lower()  # Convert input to lowercase
        """Sanitize input to allow only letters."""
        sanitized_value = "".join(c for c in event.value if c.isalpha() or c.isspace() or event.key == "backspace")
        if sanitized_value != event.value:
            event.input.value = sanitized_value  # Replace with sanitized input, lowercased


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _on_key(self,  event: events.Key):
        if event.key == "backspace" or event.key == "tab" or event.key == "shift+tab" or (event.key == "ctrl+s"):
            super()._on_key(event)
        elif (event.key == "left" or event.key == "space" or event.key == "ctrl-v") or (not event.is_printable):
            event.stop()
            event.prevent_default()
        else:
           super()._on_key(event)

    def on_focus(self, event: events.Focus) -> None:
        """Handle focus event to prevent full text selection."""
        # Use a small delay to ensure selection adjustments happen after focus logic
        self.call_later(self.clear_selection)
    
    def clear_selection(self) -> None:
        """Move cursor to the end and clear any selection."""
        self.cursor_position = len(self.value)  # Place the cursor at the end
        self.selection_range = None  # Clear selection
            