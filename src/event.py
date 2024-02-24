import pyxel
from pigframe import *

from component import *

class EvPlayerChoosed(Event):
    def __init__(self, world, priority: int = 0, **kwargs) -> None:
        super().__init__(world, priority, **kwargs)
        
    def _Event__process(self):
        for ent, (playable) in self.world.get_component(Playable):
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