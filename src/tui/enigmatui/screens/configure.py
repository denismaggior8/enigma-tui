from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Static, Header, Footer, Select
from textual.containers import Container, Horizontal, Vertical
from enigmatui.data.enigma_config import EnigmaConfig
from enigmatui.screens.exit_configutation_without_saving_modal import ExitConfiguration
from enigmatui.screens.config_not_complete_modal import ConfigurationNotComplete

import enigmapython
# Enigma M3 components
from enigmapython.EnigmaM3 import EnigmaM3
from enigmapython.EnigmaM3RotorI import EnigmaM3RotorI
from enigmapython.EnigmaM3RotorII import EnigmaM3RotorII
from enigmapython.EnigmaM3RotorIII import EnigmaM3RotorIII
from enigmapython.EnigmaM3RotorIV import EnigmaM3RotorIV
from enigmapython.EnigmaM3RotorV import EnigmaM3RotorV
from enigmapython.EnigmaM3RotorVI import EnigmaM3RotorVI
from enigmapython.EnigmaM3RotorVII import EnigmaM3RotorVII
from enigmapython.EnigmaM3RotorVIII import EnigmaM3RotorVIII

from enigmapython.EtwPassthrough import EtwPassthrough

from enigmapython.ReflectorUKWB import ReflectorUKWB
from enigmapython.ReflectorUKWC import ReflectorUKWC

class ConfigureScreen(Screen):

    enigma_config = EnigmaConfig()


    BINDINGS = [("s", "save_and_exit", "Save and exit"),
                ("escape", "exit", "Exit")
               ]

    def action_exit(self):
        self.app.push_screen(ExitConfiguration())

    def action_save_and_exit(self):
        config_complete = True
        for select in self.query(".active"):
            if select.value  == Select.BLANK:
                config_complete = False
                break
        if config_complete == True:
            self.app.pop_screen()
        else:
            self.app.push_screen(ConfigurationNotComplete())
            
        

        #self.app.pop_screen()

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
        self.rotor3_type_select = self.query_one("#rotor3_type", Select)
        self.rotor3_position_select = self.query_one("#rotor3_position", Select)
        self.rotor3_ring_select = self.query_one("#rotor3_ring", Select)
        self.reflector_type_select = self.query_one("#reflector_type", Select)


    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("")
        yield Static("")
        yield Horizontal(
            Vertical(
                    Static("Select an Enigma machine model:"),
                    Select(options=[("Enigma M3", "EnigmaM3"),
                                    ("Enigma M4", "EnigmaM4")],id="enigma_type",
                                    allow_blank=False, 
                                    classes="active")
                )
            
        )
        yield Vertical(
                    Static("Select ETW type:"),
                    Select(options=[],
                           id="etw_type",
                           classes="active"
                           )
                )
        
        yield Horizontal(
                Vertical(
                    Static("Select rotor 3 type:"),
                    Select( id="rotor3_type", options=[]),
                    id="rotor3_type_vertical",
                    classes="invisible"
                ),
                Vertical(
                    Static("Select rotor 2 type:"),
                    Select( id="rotor2_type", options=[], classes="active")
                ),
                Vertical(
                    Static("Select rotor 1 type:"),
                    Select( id="rotor1_type", options=[], classes="active")
                ),
                Vertical(
                    Static("Select rotor 0 type:"),
                    Select( id="rotor0_type", options=[], classes="active")
                ),
                id="rotors_types_line"
        )

        yield Horizontal(
                Vertical(
                    Static("Select rotor 3 position:"),
                    Select( id="rotor3_position", options=[]),
                    id="rotor3_position_vertical",
                    classes="invisible"
                ),
                Vertical(
                    Static("Select rotor 2 position:"),
                    Select( id="rotor2_position", options=[], classes="active")
                ),
                Vertical(
                    Static("Select rotor 1 position:"),
                    Select( id="rotor1_position", options=[], classes="active")
                ),
                Vertical(
                    Static("Select rotor 0 position:"),
                    Select( id="rotor0_position", options=[], classes="active")
                ),
                id="rotors_position_line"
        )

        yield Horizontal(
                Vertical(
                    Static("Select rotor 3 ring:"),
                    Select( id="rotor3_ring", options=[]),
                    id="rotor3_ring_vertical",
                    classes="invisible"
                ),
                Vertical(
                    Static("Select rotor 2 ring:"),
                    Select( id="rotor2_ring", options=[], classes="active")
                ),
                Vertical(
                    Static("Select rotor 1 ring:"),
                    Select( id="rotor1_ring", options=[], classes="active")
                ),
                Vertical(
                    Static("Select rotor 0 ring:"),
                    Select( id="rotor0_ring", options=[], classes="active")
                ),
                id="rotors_rings_line"
        )

        yield Horizontal(
            Vertical(
                    Static("Select a reflector:"),
                    Select(options=[],id="reflector_type",classes="active")
                )
        )

        yield Footer()

    
    def on_select_changed(self, event: Select.Changed) -> None:
        if event.select.id == "enigma_type":
            
            self.query_one("#rotor3_type_vertical", Vertical).add_class("invisible")
            self.query_one("#rotor3_position_vertical", Vertical).add_class("invisible")
            self.query_one("#rotor3_ring_vertical", Vertical).add_class("invisible")

           
           
            
            if event.value == "EnigmaM3":

               

                self.etw_type_select.set_options([("Passthrough ({})".format(EtwPassthrough.wiring), "EtwPassthrough")]) 
                self.etw_type_select.value="EtwPassthrough"

                m3_rotors_options = [
                    ("I ({})".format(EnigmaM3RotorI.wiring), "EnigmaM3RotorI"), 
                    ("II ({})".format(EnigmaM3RotorII.wiring), "EnigmaM3RotorII"), 
                    ("III ({})".format(EnigmaM3RotorIII.wiring), "EnigmaM3RotorIII"),
                    ("IV ({})".format(EnigmaM3RotorIV.wiring), "EnigmaM3RotorIV"), 
                    ("V ({})".format(EnigmaM3RotorV.wiring), "EnigmaM3RotorV"), 
                    ("VI ({})".format(EnigmaM3RotorVI.wiring), "EnigmaM3RotorVI"),
                    ("VII ({})".format(EnigmaM3RotorVII.wiring), "EnigmaM3RotorVII"), 
                    ("VIII ({})".format(EnigmaM3RotorVIII.wiring), "EnigmaM3RotorVIII")]
                
                self.rotor0_type_select.set_options(m3_rotors_options)
                self.rotor0_position_select.set_options([(str(i), str(i)) for i in range(26)])
                self.rotor0_position_select.value = "0"
                self.rotor0_ring_select.set_options([(str(i), str(i)) for i in range(26)])
                self.rotor0_ring_select.value = "0"

                self.rotor1_type_select.set_options(m3_rotors_options)
                self.rotor1_position_select.set_options([(str(i), str(i)) for i in range(26)])
                self.rotor1_position_select.value = "0"
                self.rotor1_ring_select.set_options([(str(i), str(i)) for i in range(26)])
                self.rotor1_ring_select.value = "0"

                self.rotor2_type_select.set_options(m3_rotors_options)
                self.rotor2_position_select.set_options([(str(i), str(i)) for i in range(26)])
                self.rotor2_position_select.value = "0"
                self.rotor2_ring_select.set_options([(str(i), str(i)) for i in range(26)])
                self.rotor2_ring_select.value = "0"

                self.reflector_type_select.set_options([
                    ("UKW-B ({})".format(ReflectorUKWB.wiring), "ReflectorUKWB"), 
                    ("UKW-C ({})".format(ReflectorUKWC.wiring), "ReflectorUKWC")])
                self.reflector_type_select.value = "ReflectorUKWB"
                self.reflector_type_select.allow_blank=False


            elif event.value == "EnigmaM4":
                self.query_one("#rotor3_type_vertical", Vertical).remove_class("invisible")
                self.query_one("#rotor3_position_vertical", Vertical).remove_class("invisible")
                self.query_one("#rotor3_ring_vertical", Vertical).remove_class("invisible")

            else:
                self.reset_form_options()
       
    def reset_form_options(self):
        self.enigma_type_select.clear()
        self.etw_type_select.set_options([])
        self.rotor0_type_select.set_options([])
        self.rotor0_position_select.set_options([])
        self.rotor0_ring_select.set_options([])
        self.rotor1_type_select.set_options([])
        self.rotor1_position_select.set_options([])
        self.rotor1_ring_select.set_options([])
        self.rotor2_type_select.set_options([])
        self.rotor2_position_select.set_options([])
        self.rotor2_ring_select.set_options([])
        self.rotor3_type_select.set_options([])
        self.rotor3_position_select.set_options([])
        self.rotor3_ring_select.set_options([])
        self.reflector_type_select.set_options([])
            
                