from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Static, Header, Footer, Select
from textual.containers import Container, Horizontal, Vertical
from enigmatui.data.enigma_config import EnigmaConfig
from enigmatui.screens.confirmation_modal import ExitScreen
import enigmapython
# Enigma M3 components
from enigmapython.EnigmaM3 import EnigmaM3
from enigmapython.EnigmaM3RotorI import EnigmaM3RotorI
from enigmapython.EnigmaM3RotorII import EnigmaM3RotorII
from enigmapython.EnigmaM3RotorIII import EnigmaM3RotorIII

class ConfigureScreen(Screen):

    enigma_config = EnigmaConfig()


    BINDINGS = [("s", "save_and_exit", "Save and exit"),
                ("escape", "exit", "Exit")
               ]

    def action_exit(self):
        #self.app.pop_screen()
        self.app.push_screen(ExitScreen())

    def action_save_and_exit(self):
        #self.enigma_config.enigma = globals()[self.enigma_type.value]()
        self.app.pop_screen()

    def on_mount(self):
        self.enigma_type_select = self.query_one("#enigma_type", Select)
        self.etw_type_select = self.query_one("#etw_type", Select)
        self.rotor0_type_select = self.query_one("#rotor0_type", Select)
        self.rotor0_type_select = self.query_one("#rotor0_type", Select)
        self.rotor0_position_select = self.query_one("#rotor0_position", Select)
        self.rotor0_ring_select = self.query_one("#rotor0_ring", Select)
        self.rotor1_type_select = self.query_one("#rotor1_type", Select)
        self.rotor1_position_select = self.query_one("#rotor1_position", Select)
        self.rotor1_ring_select = self.query_one("#rotor1_ring", Select)
        self.rotor2_type_select = self.query_one("#rotor2_type", Select)
        self.rotor2_position_select = self.query_one("#rotor2_position", Select)
        self.rotor2_ring_select = self.query_one("#rotor2_ring", Select)
        

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("")
        yield Static("")
        yield Horizontal(
            Vertical(
                    Static("Select an Enigma machine model:"),
                    Select(options=[("Enigma M3", "EnigmaM3")],id="enigma_type")
                )
            
        )
        yield Vertical(
                    Static("Select ETW type:"),
                    Select(options=[],id="etw_type")
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
                    Select(options=[],id="reflector_type")
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
        if event.select.id == "enigma_type":
            if event.value == "EnigmaM3":

                self.etw_type_select.set_options([("Passthrough", "EtwPassthrough")]) 
                
                self.rotor0_type_select.set_options([("I ({})".format(EnigmaM3RotorI.wiring), "EnigmaM3RotorI"), 
                                                    ("II ({})".format(EnigmaM3RotorII.wiring), "EnigmaM3RotorII"), 
                                                    ("III ({})".format(EnigmaM3RotorIII.wiring), "EnigmaM3RotorIII")])
                self.rotor0_type_select.refresh()
                self.rotor0_position_select.set_options([(str(i), str(i)) for i in range(26)])
                self.rotor0_position_select.refresh()
                self.rotor0_ring_select.set_options([(str(i), str(i)) for i in range(26)])
                self.rotor0_ring_select.refresh()

                self.rotor1_type_select.set_options([("I ({})".format(EnigmaM3RotorI.wiring), "EnigmaM3RotorI"), 
                                                    ("II ({})".format(EnigmaM3RotorII.wiring), "EnigmaM3RotorII"), 
                                                    ("III ({})".format(EnigmaM3RotorIII.wiring), "EnigmaM3RotorIII")])
                self.rotor1_position_select.set_options([(str(i), str(i)) for i in range(26)])
                self.rotor1_position_select.refresh()
                self.rotor1_ring_select.set_options([(str(i), str(i)) for i in range(26)])
                self.rotor1_ring_select.refresh()

                self.rotor2_type_select.set_options([("I ({})".format(EnigmaM3RotorI.wiring), "EnigmaM3RotorI"), 
                                                    ("II ({})".format(EnigmaM3RotorII.wiring), "EnigmaM3RotorII"), 
                                                    ("III ({})".format(EnigmaM3RotorIII.wiring), "EnigmaM3RotorIII")])
                self.rotor2_position_select.set_options([(str(i), str(i)) for i in range(26)])
                self.rotor2_position_select.refresh()
                self.rotor2_ring_select.set_options([(str(i), str(i)) for i in range(26)])
                self.rotor2_ring_select.refresh()

            else:
                self.reset_form()
       
    def reset_form(self):
        self.etw_type_select.set_options([])
        self.rotor0_type_select.set_options([])
        self.rotor0_type_select.refresh()
        self.rotor0_position_select.set_options([])
        self.rotor0_position_select.refresh()
        self.rotor0_ring_select.set_options([])
        self.rotor0_ring_select.refresh()
        self.rotor1_type_select.set_options([])
        self.rotor1_type_select.refresh()
        self.rotor1_position_select.set_options([])
        self.rotor1_position_select.refresh()
        self.rotor1_ring_select.set_options([])
        self.rotor1_ring_select.refresh()
        self.rotor2_type_select.set_options([])
        self.rotor2_type_select.refresh()
        self.rotor2_position_select.set_options([])
        self.rotor2_position_select.refresh()
        self.rotor2_ring_select.set_options([])
        self.rotor2_ring_select.refresh()
            
                