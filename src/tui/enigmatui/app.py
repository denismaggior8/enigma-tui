from enigmatui.screens.configuration import ConfigurationScreen
from enigmatui.screens.encryption import EncryptionScreen
from textual import App, Button, ComposeResult, Footer, Header, Vertical
class EnigmaApp(App):
    """Un'applicazione per simulare la macchina Enigma con sezioni separate."""

    CSS = """
    Screen {
        align: center middle;
    }
    Button {
        margin: 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header(title="Enigma Machine Simulator")
        yield Vertical(
            Button("Configure Machine", id="configure_button"),
            Button("Encrypt Message", id="encrypt_button"),
            id="menu",
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Gestisce la navigazione tra le sezioni."""
        button_id = event.button.id
        if button_id == "configure_button":
            self.push_screen(ConfigurationScreen())
        elif button_id == "encrypt_button":
            self.push_screen(EncryptionScreen())
