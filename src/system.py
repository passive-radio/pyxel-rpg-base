from pigframe import *
from jaconv import alphabet2kana, kana2alphabet
import pyxel

from component import *

class SysChoosePlayer(System):
    def __init__(self, world, priority: int = 0, **kwargs) -> None:
        super().__init__(world, priority, **kwargs)
        self.id_selected = 0
        
    def process(self):
        actions = self.world.actions
        
        if actions.down_p:
            self.id_selected += 1
        elif actions.up_p:
            self.id_selected -= 1
        self.id_selected = max(0, min(self.id_selected, len(self.world.get_component(Playable)) - 1))
        
        for i, (ent, (playable)) in enumerate(self.world.get_component(Playable)):
            if i == self.id_selected:
                playable.selected = True
            else:
                playable.selected = False
                

class SysInputText(System):
    def process(self):
        for ent, (player, config) in self.world.get_components(Player, PlayerConfig):
            actions = self.world.actions
            text: str = config.name_alphabet

            if actions.backspace_p:
                if 0 < len(config.name):
                    config.name = config.name[:-1]
                    config.name_alphabet = kana2alphabet(config.name)
                    return
                    
            if actions.a_p:
                text += "a"
            if actions.b_p:
                text += "b"
            if actions.c_p:
                text += "c"
            if actions.d_p:
                text += "d"
            if actions.e_p:
                text += "e"
            if actions.f_p:
                text += "f"
            if actions.g_p:
                text += "g"
            if actions.h_p:
                text += "h"
            if actions.i_p:
                text += "i"
            if actions.j_p:
                text += "j"
            if actions.k_p:
                text += "k"
            if actions.l_p:
                text += "l"
            if actions.m_p:
                text += "m"
            if actions.n_p:
                text += "n"
            if actions.o_p:
                text += "o"
            if actions.p_p:
                text += "p"
            if actions.q_p:
                text += "q"
            if actions.r_p:
                text += "r"
            if actions.s_p:
                text += "s"
            if actions.t_p:
                text += "t"
            if actions.u_p:
                text += "u"
            if actions.v_p:
                text += "v"
            if actions.w_p:
                text += "w"
            if actions.x_p:
                text += "x"
            if actions.y_p:
                text += "y"
            if actions.z_p:
                text += "z"
            if actions.space_p:
                text += " "
            if actions.bar_p:
                text += "-"
            
            if text[-2:] == "si":
                text = text[:-2] + "shi"
            if text[-2:] == "ti":
                text = text[:-2] + "chi"
            if text[-2:] == "tu":
                text = text[:-2] + "tsu"
            text_jp: str = alphabet2kana(text)
            if (text_jp != "") and (0 < len(text_jp)):
                config.name = text_jp
                config.name_alphabet = text
                player.name = text_jp
                
class SysControlPlayer(System):
    def __init__(self, world, priority: int = 0, **kwargs) -> None:
        super().__init__(world, priority, **kwargs)
        
    def process(self):
        for ent, (player, vel) in self.world.get_components(Player, Velocity):
            actions = self.world.actions
            vel.x = 0
            vel.y = 0
            if actions.up:
                vel.y = -1
            if actions.down:
                vel.y = 1
            if actions.left:
                vel.x = -1
            if actions.right:
                vel.x = 1
                
class SysMoveByVelocity(System):
    def __init__(self, world, priority: int = 0, **kwargs) -> None:
        super().__init__(world, priority, **kwargs)
    
    def process(self):
        for ent, (pos, vel) in self.world.get_components(Position, Velocity):
            pos.x += vel.x * vel.speed
            pos.y += vel.y * vel.speed
            pos.x = int(pos.x)
            pos.y = int(pos.y)
            
class SysCollision(System):
    def __init__(self, world, priority: int = 0, **kwargs) -> None:
        super().__init__(world, priority, **kwargs)
    
    def process(self):
        margin = 2
        for ent1, (_, pos1, vel1, _) in self.world.get_components(Player, Position, Velocity, Collidable):
            for ent2, (pos2, vel2, _) in self.world.get_components(Position, Velocity, Collidable):
                if ent1 != ent2:
                    if (pos2.x - margin <= pos1.x + pos1.w <= pos2.x + pos2.w + margin and pos2.y - margin <= pos1.y + pos1.h <= pos2.y + pos2.h + margin) \
                        or (pos2.x - margin <= pos1.x <= pos2.x + pos2.w + margin and pos2.y - margin <= pos1.y + pos1.h <= pos2.y + pos2.h + margin) \
                        or (pos2.x - margin <= pos1.x <= pos2.x + pos2.w + margin and pos2.y - margin <= pos1.y <= pos2.y + pos2.h + margin) \
                        or (pos2.x - margin <= pos1.x + pos1.w <= pos2.x + pos2.w + margin and pos2.y - margin <= pos1.y <= pos2.y + pos2.h + margin):
                        pos1.x = pos1.x_prev
                        pos1.y = pos1.y_prev

class SysUpdatePosition(System):
    def __init__(self, world, priority: int = 0, **kwargs) -> None:
        super().__init__(world, priority, **kwargs)
    
    def process(self):
        for ent, (pos) in self.world.get_component(Position):
            pos.x_prev = pos.x
            pos.y_prev = pos.y

class SysInteract(System):
    def process(self):
        margin = 4
        for ent, (pos, player, status) in self.world.get_components(Position, Player, CharacterStatus):
            for ent2, (pos2, npc, status2) in self.world.get_components(Position, NPC, CharacterStatus):
                if (pos2.x - margin <= pos.x + pos.w <= pos2.x + pos2.w + margin and pos2.y - margin <= pos.y + pos.h <= pos2.y + pos2.h + margin) \
                    or (pos2.x - margin <= pos.x <= pos2.x + pos2.w + margin and pos2.y - margin <= pos.y + pos.h <= pos2.y + pos2.h + margin) \
                    or (pos2.x - margin <= pos.x <= pos2.x + pos2.w + margin and pos2.y - margin <= pos.y <= pos2.y + pos2.h + margin) \
                    or (pos2.x - margin <= pos.x + pos.w <= pos2.x + pos2.w + margin and pos2.y - margin <= pos.y <= pos2.y + pos2.h + margin):
                    # print("interacted:", ent, ent2)
                    interactable = self.world.get_entity_object(ent)[Interactable]
                    interactable.opponent = ent2
                    # print("player:", player.name, status.hp, status.mp, status.melee, status.magic, status.ranged, status.agility, status.toughness)
                    # print("npc:", npc.name, status2.hp, status2.mp, status2.melee, status2.magic, status2.ranged, status2.agility, status2.toughness)
                    return
                else:
                    opponent_interactable = self.world.get_entity_object(ent2)[Interactable]
                    opponent_interactable.opponent = None
                    opponent_interactable.status = 0
                    
            interactable = self.world.get_entity_object(ent)[Interactable]
            interactable.opponent = None
            interactable.status = 0
            
class SysButton(System):
    """System for button component
    """
    def process(self):
        for ent, (button) in self.world.get_component(Button):
            hover_cond = button.x <= pyxel.mouse_x <= button.x + button.w and \
                button.y <= pyxel.mouse_y <= button.y + button.h
            clicked_cond = self.world.actions.mouse_left_p
            clicking_cond = self.world.actions.mouse_left
            if hover_cond:
                button.hover = True
                if clicked_cond:
                    button.clicked = True
                    print(f"Button (ent:{ent}) clicked!")
                elif clicking_cond:
                    button.clicking = True
                else:
                    button.clicking = False
                    button.clicked = False
            else:
                button.hover = False
                button.clicked = False
                button.clicking = False
                
class SysButtonEvent(System):
    """System for button component. If button is clicked, linked event is processed.
    """
    def process(self):
        for ent, (button) in self.world.get_component(Button):
            if button.clicked:
                next_scene = button.to
                # self.world.scene_manager.next_scene = next_scene
                # button.clicked = False
                