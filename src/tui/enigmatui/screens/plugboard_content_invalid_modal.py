from textual.app import ComposeResult
from textual.screen import ModalScreen
from textual.widgets import Button, Label
from textual import on
from textual.containers import Container, Horizontal

class PlugboardContentInvalid(ModalScreen):
    """A modal exit screen."""

    def compose(self) -> ComposeResult:
        with Container():
            yield Label("Plugboard value is invalid, please make sure to input only letter pairs, not a single letter at the end")
            with Horizontal():
                yield Button("ok", id="ok")

    @on(Button.Pressed, "#ok")
    def back_to_app(self) -> None:
        self.app.pop_screen()