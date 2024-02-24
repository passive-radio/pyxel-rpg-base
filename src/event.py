import pyxel
from pigframe import *

from component import *

class EvPlayerChoosed(Event):
    def __init__(self, world, priority: int = 0, **kwargs) -> None:
        super().__init__(world, priority, **kwargs)
        
    def _Event__process(self):
        for ent, (playable) in self.world.get_component(Playable):
            if playable.selected:
                self.world.add_component_to_entity(ent, Player, "", ent)
                playable.selected = False