import pyxel
from pigframe import *
from jaconv import alphabet2kana, kana2alphabet

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
                # print("selected", ent)
                playable.selected = True
            else:
                playable.selected = False
                

class SysInputText(System):
    def process(self):
        for ent, (player, config) in self.world.get_components(Player, PlayerConfig):
            text: str = config.name_alphabet
            if pyxel.btnp(pyxel.KEY_BACKSPACE) or pyxel.btnp(pyxel.KEY_KP_BACKSPACE):
                print("backspace")
                if 0 < len(config.name):
                    print("erase")
                    config.name = config.name[:-1]
                    config.name_alphabet = kana2alphabet(config.name)
                    print(text, "->", config.name_alphabet)
                    return
                    
            if pyxel.btnp(pyxel.KEY_A):
                text += "a"
            if pyxel.btnp(pyxel.KEY_B):
                text += "b"
            if pyxel.btnp(pyxel.KEY_C):
                text += "c"
            if pyxel.btnp(pyxel.KEY_D):
                text += "d"
            if pyxel.btnp(pyxel.KEY_E):
                text += "e"
            if pyxel.btnp(pyxel.KEY_F):
                text += "f"
            if pyxel.btnp(pyxel.KEY_G):
                text += "g"
            if pyxel.btnp(pyxel.KEY_H):
                text += "h"
            if pyxel.btnp(pyxel.KEY_I):
                text += "i"
            if pyxel.btnp(pyxel.KEY_J):
                text += "j"
            if pyxel.btnp(pyxel.KEY_K):
                text += "k"
            if pyxel.btnp(pyxel.KEY_L):
                text += "l"
            if pyxel.btnp(pyxel.KEY_M):
                text += "m"
            if pyxel.btnp(pyxel.KEY_N):
                text += "n"
            if pyxel.btnp(pyxel.KEY_O):
                text += "o"
            if pyxel.btnp(pyxel.KEY_P):
                text += "p"
            if pyxel.btnp(pyxel.KEY_Q):
                text += "q"
            if pyxel.btnp(pyxel.KEY_R):
                text += "r"
            if pyxel.btnp(pyxel.KEY_S):
                text += "s"
            if pyxel.btnp(pyxel.KEY_T):
                text += "t"
            if pyxel.btnp(pyxel.KEY_U):
                text += "u"
            if pyxel.btnp(pyxel.KEY_V):
                text += "v"
            if pyxel.btnp(pyxel.KEY_W):
                text += "w"
            if pyxel.btnp(pyxel.KEY_X):
                text += "x"
            if pyxel.btnp(pyxel.KEY_Y):
                text += "y"
            if pyxel.btnp(pyxel.KEY_Z):
                text += "z"
            
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
                