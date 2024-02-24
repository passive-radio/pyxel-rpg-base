from dataclasses import dataclass, asdict, make_dataclass, field
import pyxel
from pigframe import *

from component import *

@dataclass
class UserInputEvents:
    up: tuple = pyxel.btn, pyxel.KEY_UP, pyxel.KEY_W
    down: tuple = pyxel.btn, pyxel.KEY_DOWN, pyxel.KEY_S
    left: tuple = pyxel.btn, pyxel.KEY_LEFT, pyxel.KEY_A
    right: tuple = pyxel.btn, pyxel.KEY_RIGHT, pyxel.KEY_D
    enter: tuple = pyxel.btn, pyxel.KEY_RETURN, pyxel.KEY_RETURN2
    click: tuple = pyxel.btn, pyxel.MOUSE_BUTTON_LEFT
    click_p: tuple = pyxel.btnp, pyxel.MOUSE_BUTTON_LEFT
    enter_p: tuple = pyxel.btnp, pyxel.KEY_RETURN, pyxel.KEY_RETURN2
    enter_r: tuple = pyxel.btnr, pyxel.KEY_RETURN, pyxel.KEY_RETURN2
    backspace: tuple = pyxel.btn, pyxel.KEY_BACKSPACE, pyxel.KEY_KP_BACKSPACE
    backspace_p: tuple = pyxel.btnp, pyxel.KEY_BACKSPACE, pyxel.KEY_KP_BACKSPACE
    click_r: tuple = pyxel.btnr, pyxel.MOUSE_BUTTON_LEFT
    

pyxel.init(100, 100,)
user_input_events = UserInputEvents()
input_events = asdict(user_input_events)
print(input_events)
events = {}
for k, v in input_events.items():
    events[k] = False
    if isinstance(v, tuple) and callable(v[0]):
        happend = False
        for i in range(1, len(v)):
            if v[0](v[i]):
                happend = True
                break
        events[k] = happend

print(events)
fields = [(key, bool, field(default=val)) for key, val in events.items()]
print(fields)
EventResults = make_dataclass("EventResults", fields= fields)
print(EventResults, EventResults.up or EventResults.down)

class EvPlayerChoosed(Event):
    def __init__(self, world, priority: int = 0, **kwargs) -> None:
        super().__init__(world, priority, **kwargs)
        
    def _Event__process(self):
        for ent, (playable) in self.world.get_component(Playable):
            print("add Player", "to", ent)
            if playable.selected:
                self.world.add_component_to_entity(ent, Player, name = "", id = ent)
                playable.selected = False
            else:
                print("remove PlayerConfig", "from", ent)
                self.world.remove_component_from_entity(ent, PlayerConfig)
                self.world.remove_component_from_entity(ent, Playable)
                
class EvPlayBGM(Event):
    def __init__(self, world, priority: int = 0, **kwargs) -> None:
        super().__init__(world, priority, **kwargs)
        
    def _Event__process(self):
        pyxel.playm(0, loop=True)