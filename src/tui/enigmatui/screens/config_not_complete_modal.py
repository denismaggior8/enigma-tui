from textual.app import ComposeResult
from textual.screen import ModalScreen
from textual.widgets import Button, Label
from textual import on
from textual.containers import Container, Horizontal

class ConfigurationNotComplete(ModalScreen):
    """A modal exit screen."""

    def compose(self) -> ComposeResult:
        with Container():
            yield Label("Enigma configuration is not yet complete, please fill the empty field before saving!")
            with Horizontal():
                yield Button("ok", id="ok")

    @on(Button.Pressed, "#ok")
    def back_to_app(self) -> None:
        self.app.pop_screen()