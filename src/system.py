from pigframe import *
from jaconv import alphabet2kana, kana2alphabet

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
        
        print(self.id_selected)
        for i, (ent, (playable)) in enumerate(self.world.get_component(Playable)):
            if i == self.id_selected:
                print("selected", ent)
                playable.selected = True
            else:
                playable.selected = False
                

class SysInputText(System):
    def process(self):
        for ent, (player, config) in self.world.get_components(Player, PlayerConfig):
            actions = self.world.actions
            text: str = config.name_alphabet

            if actions.backspace_p:
                print("backspace")
                if 0 < len(config.name):
                    print("erase")
                    config.name = config.name[:-1]
                    config.name_alphabet = kana2alphabet(config.name)
                    print(text, "->", config.name_alphabet)
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
                