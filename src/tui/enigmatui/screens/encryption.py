
from textual import ComposeResult, Static, Select, Button, Footer, Header, Vertical

class EncryptionScreen(App):
    """Schermata per la cifratura del messaggio."""

    def compose(self) -> ComposeResult:
        yield Header(title="Encrypt Message")
        yield Vertical(
            Static("Enter Message to Encrypt:"),
            TextInput(placeholder="Type your message here", id="message_input"),
            Button("Encrypt", id="encrypt_button"),
            Static("Encrypted Message:", id="output"),
            Button("Back to Menu", id="back_button"),
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Gestisce la cifratura e il ritorno al menu."""
        if event.button.id == "encrypt_button":
            # Per ora, restituiamo solo un messaggio simulato
            input_message = self.query_one("#message_input", TextInput).value
            encrypted_message = f"Encrypted({input_message})"  # Semplice placeholder
            self.query_one("#output", Static).update(encrypted_message)
        elif event.button.id == "back_button":
            self.pop_screen()