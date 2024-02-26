import pyxel
from pigframe import *

from component import *

class EvPlayerChoosed(Event):
    def __init__(self, world, priority: int = 0, **kwargs) -> None:
        super().__init__(world, priority, **kwargs)
        
    def _Event__process(self):
        for ent, (playable) in self.world.get_component(Playable):
            print(ent, playable.selected)
            if playable.selected:
                self.world.add_component_to_entity(ent, Player, name = "", id = ent)
                self.world.add_component_to_entity(ent, Movable)
                self.world.add_component_to_entity(ent, Collidable)
                self.world.add_component_to_entity(ent, Interactable)
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
        
class EvStartInteraction(Event):
    def __init__(self, world, priority: int = 0, **kwargs) -> None:
        super().__init__(world, priority, **kwargs)
        
    def _Event__process(self):
        for ent, (player, interactable) in self.world.get_components(Player, Interactable):
            if interactable.opponent is None:
                continue
            
            if interactable.status == 0:
                opponent = self.world.get_entity_object(interactable.opponent)
                opponent[Interactable].opponent = ent
                interactable.status = 1
                opponent[Interactable].status = 1
            else:
                opponent = self.world.get_entity_object(interactable.opponent)
                interactable.status = 0
                opponent[Interactable].status = 0

class EvStartFight(Event):
    def __init__(self, world, priority: int = 0, **kwargs) -> None:
        super().__init__(world, priority, **kwargs)
        
    def _Event__process(self):
        print("start fight")
        for ent, (player, interactable) in self.world.get_components(Player, Interactable):
            if interactable.opponent is None or interactable.status != 1:
                continue
            
            if interactable.status == 1:
                print("start fight")
                interactable.status = 2
                opponent = self.world.get_entity_object(interactable.opponent)
                opponent[Interactable].status = 2

class EvStartTalk(Event):
    def __init__(self, world, priority: int = 0, **kwargs) -> None:
        super().__init__(world, priority, **kwargs)
        
    def _Event__process(self):
        print("start talk")
        for ent, (player, interactable) in self.world.get_components(Player, Interactable):
            if interactable.opponent is None or interactable.status != 1:
                continue
            
            if interactable.status == 1:
                interactable.status = 3
                opponent = self.world.get_entity_object(interactable.opponent)
                opponent[Interactable].status = 3