import pyxel
from pigframe import *

from component import *

class SysChoosePlayer(System):
    def __init__(self, world, priority: int = 0, **kwargs) -> None:
        super().__init__(world, priority, **kwargs)
        self.id_selected = 0
        
    def process(self):
        
        if pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.KEY_S):
            self.id_selected += 1
        elif pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.KEY_W):
            self.id_selected -= 1
        self.id_selected = max(0, min(self.id_selected, len(self.world.get_component(Playable)) - 1))
        
        for i, (ent, (playable)) in enumerate(self.world.get_component(Playable)):
            if i == self.id_selected:
                playable.selected = True
            else:
                playable.selected = False