from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Static, Header, Footer, Select
from enigmatui.data.enigma_config import EnigmaConfig

class ConfigureScreen(Screen):

    enigma_config = EnigmaConfig()
    enigma_selection = None

    BINDINGS = [("s", "save_and_exit", "Save and exit"),("escape", "exit", "Exit")]

    def action_exit(self):
        self.app.pop_screen()

    def action_save_and_exit(self):
        self.enigma_config.enigma = 
        self.app.pop_screen()

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("")
        yield Static("Select an Enigma machine model")
        yield Select(
            options=[("Enigma M3", "EnigmaM3")],
            id="enigma_selection"
        )
        if self.enigma_selection:
            yield Select( id="dropdown-2", options=[])
            yield Select( id="dropdown-3", options=[])
            yield Select( id="dropdown-4", options=[])

        yield Footer()
    
    def on_select_changed(self, event: Select.Changed) -> None:
        # Update dependent dropdowns based on first dropdown selection
        if event.select.id == "dropdown-1":
            if event.select.value == "choice1":
                self.query_one("#dropdown-2").options = [("Option A", "a"), ("Option B", "b")]
                self.query_one("#dropdown-3").options = [("Option C", "c"), ("Option D", "d")]
                self.query_one("#dropdown-4").options = [("Option E", "e"), ("Option F", "f")]
            elif event.select.value == "choice2":
                self.query_one("#dropdown-2").options = [("Option G", "g"), ("Option H", "h")]
                self.query_one("#dropdown-3").options = [("Option I", "i"), ("Option J", "j")]
                self.query_one("#dropdown-4").options = [("Option K", "k"), ("Option L", "l")]