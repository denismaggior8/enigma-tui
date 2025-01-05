from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Static, Header, Footer, Select
from textual.containers import Container, Horizontal, Vertical
from enigmatui.data.enigma_config import EnigmaConfig
from enigmatui.screens.confirmation_modal import ExitScreen

class ConfigureScreen(Screen):

    enigma_config = EnigmaConfig()
    enigma_selection = None

    BINDINGS = [("s", "save_and_exit", "Save and exit"),("escape", "exit", "Exit")]

    def action_exit(self):
        #self.app.pop_screen()
        self.app.push_screen(ExitScreen())

    def action_save_and_exit(self):
        #self.enigma_config.enigma = 
        self.app.pop_screen()
        

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("")
        yield Static("")
        yield Horizontal(
            Vertical(
                    Static("Select an Enigma machine model:"),
                    Select(options=[("Enigma M3", "EnigmaM3")],id="enigma_selection")
                )
        )
        
        yield Horizontal(
                Vertical(
                    Static("Select rotor 0 type:"),
                    Select( id="rotor0_type", options=[])
                ),
                Vertical(
                    Static("Select rotor 0 position:"),
                    Select( id="rotor0_position", options=[])
                ),
                Vertical(
                    Static("Select rotor 0 ring:"),
                    Select( id="rotor0_ring", options=[])
                )
        )

        yield Horizontal(
                Vertical(
                    Static("Select rotor 1 type:"),
                    Select( id="rotor1_type", options=[])
                ),
                Vertical(
                    Static("Select rotor 1 position:"),
                    Select( id="rotor1_position", options=[])
                ),
                Vertical(
                    Static("Select rotor 1 ring:"),
                    Select( id="rotor1_ring", options=[])
                )
        )

        yield Horizontal(
                Vertical(
                    Static("Select rotor 2 type:"),
                    Select( id="rotor2_type", options=[])
                ),
                Vertical(
                    Static("Select rotor 2 position:"),
                    Select( id="rotor2_position", options=[])
                ),
                Vertical(
                    Static("Select rotor 2 ring:"),
                    Select( id="rotor2_ring", options=[])
                )
        )

        yield Horizontal(
            Vertical(
                    Static("Select a reflector:"),
                    Select(options=[],id="reflector_selection")
                )
        )

        yield Footer()

    def action_leave_screen(self) -> None:
        def confirm_leave():
            self.pop_screen()
            self.dismiss_modal()

        def cancel_leave():
            self.dismiss_modal()

        self.push_modal(ConfirmationModal(on_confirm=confirm_leave, on_cancel=cancel_leave))
    
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