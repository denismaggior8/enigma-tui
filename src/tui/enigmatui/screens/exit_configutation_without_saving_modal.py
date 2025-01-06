from textual.app import ComposeResult
from textual.screen import ModalScreen
from textual.widgets import Button, Label
from textual import on
from textual.containers import Container, Horizontal

class ExitConfiguration(ModalScreen):
    """A modal exit screen."""

    def compose(self) -> ComposeResult:
        with Container():
            yield Label("Are you sure you want to exit configuration screen without saving?")
            with Horizontal():
                yield Button("no", id="no")
                yield Button("yes", id="yes")
    
    @on(Button.Pressed, "#yes")
    def exit_app(self) -> None:
        self.app.pop_screen()
        self.app.pop_screen()

    @on(Button.Pressed, "#no")
    def back_to_app(self) -> None:
        self.app.pop_screen()