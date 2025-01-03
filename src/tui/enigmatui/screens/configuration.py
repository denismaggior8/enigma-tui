
from textual import ComposeResult, Static, Select, Button, Footer, Header, Vertical

class ConfigurationScreen(App):
    """Schermata per la configurazione della macchina Enigma."""

    def compose(self) -> ComposeResult:
        yield Header(title="Configure Enigma Machine")
        yield Vertical(
            Static("Select Rotor Configuration:"),
            Select(
                options=[
                    ("Rotor 0", "0"),
                    ("Rotor 1", "1"),
                    ("Rotor 2", "2"),
                    ("Rotor 3", "3"),
                ],
                id="rotor_select",
            ),
            Static("Set Reflector:"),
            Select(
                options=[
                    ("UKW A", "A"),
                    ("UKW B", "B"),
                    ("UKW C", "C"),
                ],
                id="reflector_select",
            ),
            Button("Back to Menu", id="back_button"),
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Gestisce il ritorno al menu principale."""
        if event.button.id == "back_button":
            self.pop_screen()