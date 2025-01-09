from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Static, Header, Footer, Select
from textual.containers import Container, Horizontal, Vertical
from enigmatui.data.enigma_config import EnigmaConfig
from enigmatui.screens.exit_configutation_without_saving_modal import ExitConfiguration
from enigmatui.screens.config_not_complete_modal import ConfigurationNotComplete

from enigmapython.Enigma import Enigma

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

# Enigma M4 components
from enigmapython.EnigmaM4 import EnigmaM4
from enigmapython.EnigmaM4RotorI import EnigmaM4RotorI
from enigmapython.EnigmaM4RotorII import EnigmaM4RotorII
from enigmapython.EnigmaM4RotorIII import EnigmaM4RotorIII
from enigmapython.EnigmaM4RotorIV import EnigmaM4RotorIV
from enigmapython.EnigmaM4RotorV import EnigmaM4RotorV
from enigmapython.EnigmaM4RotorVI import EnigmaM4RotorVI
from enigmapython.EnigmaM4RotorVII import EnigmaM4RotorVII
from enigmapython.EnigmaM4RotorVIII import EnigmaM4RotorVIII
from enigmapython.EnigmaM4RotorBeta import EnigmaM4RotorBeta
from enigmapython.EnigmaM4RotorGamma import EnigmaM4RotorGamma

from enigmapython.EtwPassthrough import EtwPassthrough
from enigmapython.PlugboardPassthrough import PlugboardPassthrough

from enigmapython.ReflectorUKWB import ReflectorUKWB
from enigmapython.ReflectorUKWC import ReflectorUKWC

class ConfigureScreen(Screen):

    enigma_config = EnigmaConfig()


    BINDINGS = [("s", "save_and_exit", "Save and exit")
                #,("escape", "exit", "Exit")
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
            etw = globals()[self.etw_type_select.value]()
            rotor0 =  globals()[self.rotor0_type_select.value](position=int(self.rotor0_position_select.value),ring=int(self.rotor0_ring_select.value))
            rotor1 =  globals()[self.rotor1_type_select.value](position=int(self.rotor1_position_select.value),ring=int(self.rotor1_ring_select.value))
            rotor2 =  globals()[self.rotor2_type_select.value](position=int(self.rotor2_position_select.value),ring=int(self.rotor2_ring_select.value))
            reflector = globals()[self.reflector_type_select.value]()

            if self.enigma_type_select.value == "EnigmaM3":
                self.enigma_config.set_configured_enigma(EnigmaM3(rotor1=rotor0, 
                                                     rotor2=rotor1, 
                                                     rotor3=rotor2, 
                                                     plugboard=PlugboardPassthrough(),
                                                     etw=etw, 
                                                     reflector=reflector,
                                                     auto_increment_rotors=True
                                                     )
                                            )
            elif self.enigma_type_select.value == "EnigmaM4":
                rotor3 =  globals()[self.rotor3_type_select.value](position=int(self.rotor3_position_select.value),ring=int(self.rotor3_ring_select.value))
                self.enigma_config.set_configured_enigma(EnigmaM4(rotor1=rotor0, 
                                                     rotor2=rotor1, 
                                                     rotor3=rotor2,
                                                     rotor4=rotor3, 
                                                     plugboard=PlugboardPassthrough(),
                                                     etw=etw, 
                                                     reflector=reflector,
                                                     auto_increment_rotors=True
                                                     )
                                            )
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
            

            self.enigma_config.unset_configured_enigma()

            self.query_one("#rotor3_type_vertical", Vertical).add_class("invisible")
            self.query_one("#rotor3_position_vertical", Vertical).add_class("invisible")
            self.query_one("#rotor3_ring_vertical", Vertical).add_class("invisible")

            self.rotor3_type_select.remove_class("active")
            self.rotor3_position_select.remove_class("active")
            self.rotor3_ring_select.remove_class("active")
            
            if event.value == "EnigmaM3":

               

                self.etw_type_select.set_options([("Passthrough\t({})".format(EtwPassthrough.wiring), "EtwPassthrough")]) 
                self.etw_type_select.value="EtwPassthrough"

                m3_rotors_options = [
                    ("I\t({})".format(EnigmaM3RotorI.wiring), "EnigmaM3RotorI"), 
                    ("II\t({})".format(EnigmaM3RotorII.wiring), "EnigmaM3RotorII"), 
                    ("III\t({})".format(EnigmaM3RotorIII.wiring), "EnigmaM3RotorIII"),
                    ("IV\t({})".format(EnigmaM3RotorIV.wiring), "EnigmaM3RotorIV"), 
                    ("V\t({})".format(EnigmaM3RotorV.wiring), "EnigmaM3RotorV"), 
                    ("VI\t({})".format(EnigmaM3RotorVI.wiring), "EnigmaM3RotorVI"),
                    ("VII\t({})".format(EnigmaM3RotorVII.wiring), "EnigmaM3RotorVII"), 
                    ("VIII\t({})".format(EnigmaM3RotorVIII.wiring), "EnigmaM3RotorVIII")]
                
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
                    ("UKW-B\t({})".format(ReflectorUKWB.wiring), "ReflectorUKWB"), 
                    ("UKW-C\t({})".format(ReflectorUKWC.wiring), "ReflectorUKWC")])
                self.reflector_type_select.value = "ReflectorUKWB"
                self.reflector_type_select.allow_blank=False


            elif event.value == "EnigmaM4":
                self.query_one("#rotor3_type_vertical", Vertical).remove_class("invisible")
                self.query_one("#rotor3_position_vertical", Vertical).remove_class("invisible")
                self.query_one("#rotor3_ring_vertical", Vertical).remove_class("invisible")

                self.rotor3_type_select.add_class("active")
                self.rotor3_position_select.add_class("active")
                self.rotor3_ring_select.add_class("active")

                self.etw_type_select.set_options([("Passthrough ({})".format(EtwPassthrough.wiring), "EtwPassthrough")]) 
                self.etw_type_select.value="EtwPassthrough"

                m4_rotors_options = [
                    ("I\t({})".format(EnigmaM4RotorI.wiring), "EnigmaM4RotorI"), 
                    ("II\t({})".format(EnigmaM4RotorII.wiring), "EnigmaM4RotorII"), 
                    ("III\t({})".format(EnigmaM4RotorIII.wiring), "EnigmaM4RotorIII"),
                    ("IV\t({})".format(EnigmaM4RotorIV.wiring), "EnigmaM4RotorIV"), 
                    ("V\t({})".format(EnigmaM4RotorV.wiring), "EnigmaM4RotorV"), 
                    ("VI\t({})".format(EnigmaM4RotorVI.wiring), "EnigmaM4RotorVI"),
                    ("VII\t({})".format(EnigmaM4RotorVII.wiring), "EnigmaM4RotorVII"), 
                    ("VIII\t({})".format(EnigmaM4RotorVIII.wiring), "EnigmaM4RotorVIII"),
                    ("Beta\t({})".format(EnigmaM4RotorBeta.wiring), "EnigmaM4RotorBeta"),
                    ("Gamma\t({})".format(EnigmaM4RotorGamma.wiring), "EnigmaM4RotorGamma")]
                
                self.rotor0_type_select.set_options(m4_rotors_options)
                self.rotor0_position_select.set_options([(str(i), str(i)) for i in range(26)])
                self.rotor0_position_select.value = "0"
                self.rotor0_ring_select.set_options([(str(i), str(i)) for i in range(26)])
                self.rotor0_ring_select.value = "0"

                self.rotor1_type_select.set_options(m4_rotors_options)
                self.rotor1_position_select.set_options([(str(i), str(i)) for i in range(26)])
                self.rotor1_position_select.value = "0"
                self.rotor1_ring_select.set_options([(str(i), str(i)) for i in range(26)])
                self.rotor1_ring_select.value = "0"

                self.rotor2_type_select.set_options(m4_rotors_options)
                self.rotor2_position_select.set_options([(str(i), str(i)) for i in range(26)])
                self.rotor2_position_select.value = "0"
                self.rotor2_ring_select.set_options([(str(i), str(i)) for i in range(26)])
                self.rotor2_ring_select.value = "0"

                self.rotor3_type_select.set_options(m4_rotors_options)
                self.rotor3_position_select.set_options([(str(i), str(i)) for i in range(26)])
                self.rotor3_position_select.value = "0"
                self.rotor3_ring_select.set_options([(str(i), str(i)) for i in range(26)])
                self.rotor3_ring_select.value = "0"

                self.reflector_type_select.set_options([
                    ("UKW-B\t({})".format(ReflectorUKWB.wiring), "ReflectorUKWB"), 
                    ("UKW-C\t({})".format(ReflectorUKWC.wiring), "ReflectorUKWC")])
                self.reflector_type_select.value = "ReflectorUKWB"
                self.reflector_type_select.allow_blank=False

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
            
                