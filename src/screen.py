import pyxel
from pigframe import Screen
from component import *
from font import BDFRenderer

class ScLaunch(Screen):
    def __init__(self, world, priority: int = 0, **kwargs) -> None:
        super().__init__(world, priority, **kwargs)
    
    def draw(self):
        screen_size = self.world.SCREEN_SIZE
        title = self.world.TITLE
        fps = self.world.FPS
        
        font_l: BDFRenderer = self.world.font_l
        font_m: BDFRenderer = self.world.font_m
        font_s: BDFRenderer = self.world.font_s
        
        font_l.draw_text(screen_size[0]//2 - len(title)*24//2, screen_size[1]//2 - 12, title, 0)
        
        text1 = "Press Enter to start"
        font_m.draw_text(screen_size[0]//2 - len(text1)*16//4, screen_size[1]//2 + 30, text1, 
                        int(pyxel.frame_count / fps * 5) % 15)

class ScChoosePlayer(Screen):
    def __init__(self, world, priority: int = 0, **kwargs) -> None:
        super().__init__(world, priority, **kwargs)
    
    def draw(self):
        screen_size = self.world.SCREEN_SIZE
        title = "Player Config"
        
        font_l: BDFRenderer = self.world.font_l
        font_m: BDFRenderer = self.world.font_m
        font_s: BDFRenderer = self.world.font_s
        
        pyxel.rect(100, 80, screen_size[0] - 200, 40, 1)
        pyxel.rectb(100, 80, screen_size[0] - 200, screen_size[1] - 160, 15)
        text = "Choose your character"
        font_l.draw_text(110, 90, text, 0)
        
        job_x = 110
        hp_x = 250
        mp_x = 250 + 64
        melee_x = 250 + 64 * 2
        magic_x = 250 + 64 * 3
        ranged_x = 250 + 64 * 4
        agility_x = 250 + 64 * 5
        
        font_l.draw_text(job_x, 140, "職業", 0)
        font_l.draw_text(hp_x, 140, "HP", 0)
        font_l.draw_text(mp_x, 140, "MP", 0)
        font_l.draw_text(melee_x, 140, "近接", 0)
        font_l.draw_text(magic_x, 140, "魔法", 0)
        font_l.draw_text(ranged_x, 140, "遠隔", 0)
        font_l.draw_text(agility_x, 140, "素早さ", 0)
        
        pyxel.rect(job_x, 172, 600, 2, 1)
        
        for i, (ent, (playable, status)) in enumerate(self.world.get_components(Playable, CharacterStatus)):
            
            text_color = 0
            bg_color = None
            if playable.selected:
                text_color = 0
                bg_color = 15
            
            if bg_color is not None:
                pyxel.rect(job_x, 190 + i * 24 * 2 - 4, 600, 32, bg_color)
                
            font_l.draw_text(job_x, 190 + i * 24 * 2, f"{status.job}", text_color)
            font_l.draw_text(hp_x, 190 + i * 24 * 2, f"{status.hp}", text_color)
            font_l.draw_text(mp_x, 190 + i * 24 * 2, f"{status.mp}", text_color)
            font_l.draw_text(melee_x, 190 + i * 24 * 2, f"{status.melee}", text_color)
            font_l.draw_text(magic_x, 190 + i * 24 * 2, f"{status.magic}", text_color)
            font_l.draw_text(ranged_x, 190 + i * 24 * 2, f"{status.ranged}", text_color)
            font_l.draw_text(agility_x, 190 + i * 24 * 2, f"{status.agility}", text_color)
            
        
        text2 = "Press Enter(Return) to start"
        font_l.draw_text(screen_size[0]//2 - len(text2)*24//4, screen_size[1] - 70, text2, 0)
        
class ScNamePlayer(Screen):
    def __init__(self, world, priority: int = 0, **kwargs) -> None:
        super().__init__(world, priority, **kwargs)
        
    def draw(self):
        for ent, (player, config) in self.world.get_components(Player, PlayerConfig):
            input_x = self.world.SCREEN_SIZE[0]//2 - len(config.name)*24//2
            input_y = self.world.SCREEN_SIZE[1]//2 - 12
            
            text1 = "Enter your name"
            self.world.font_l.draw_text(self.world.SCREEN_SIZE[0]//2 - len(text1)*24//4, input_y - 40, text1, 0)
            
            input_width = min(max(len(config.name) * 24 + 20, 200), 600)
            pyxel.rect(self.world.SCREEN_SIZE[0]//2 - input_width//2, input_y - 10, input_width, 40, 7)
            
            width = len(config.name) * 24
            text_render_x = self.world.SCREEN_SIZE[0]//2 - width//2
            self.world.font_l.draw_text(text_render_x, input_y, config.name, 0)
            
            text_bar_colors = [0, 7]
            pyxel.rect(text_render_x + width + 4, input_y, 2, 24, text_bar_colors[(pyxel.frame_count // (self.world.FPS//2)) % 2])
            
class ScPlayerStatus(Screen):
    def __init__(self, world, priority: int = 0, **kwargs) -> None:
        super().__init__(world, priority, **kwargs)
    
    def draw(self):
        for ent, (player, status) in self.world.get_components(Player, CharacterStatus):
            screen_size = self.world.SCREEN_SIZE
            x = 40
            y = screen_size[1] - 100
            hp_bar_y = y - 40
            pyxel.rect(x - 4, y - 4, 360, 84, 7)
            pyxel.rectb(x - 4, y - 4, 360, 84, 0)
            
            hp_max_x = 140
            hp_x = status.hp / status.hp_max * hp_max_x
            
            bar_height = 8
            
            self.world.font_s.draw_text(x, hp_bar_y - 2, "HP", 0)
            
            pyxel.rect(x + 20, hp_bar_y, hp_max_x, bar_height, 13)
            pyxel.rect(x + 20, hp_bar_y, hp_x, bar_height, 8)
            pyxel.rectb(x - 2 + 20, hp_bar_y - 2, hp_max_x + 4, bar_height + 4, 0)
            
            mp_bar_y = hp_bar_y + 16
            
            mp_max_x = 140
            if status.mp_max == 0:
                mp_x = 0
            else:
                mp_x = status.mp / status.mp_max * mp_max_x
                
            self.world.font_s.draw_text(x, mp_bar_y - 2, "MP", 0)
            pyxel.rect(x + 20, mp_bar_y, mp_max_x, bar_height, 13)
            pyxel.rect(x + 20, mp_bar_y, mp_x, bar_height, 5)
            pyxel.rectb(x - 2 + 20, mp_bar_y - 2, mp_max_x + 4, bar_height + 4, 0)
            
            text = f"{player.name}"
            self.world.font_l.draw_text(x, y, text, 0)
            hp = f"HP: {status.hp}"
            self.world.font_m.draw_text(x, y + 40, hp, 0)
            mp = f"MP: {status.mp}"
            self.world.font_m.draw_text(x, y + 60, mp, 0)
            melee = f"Melee: {status.melee}"
            self.world.font_m.draw_text(x + 70, y + 40, melee, 0)
            ranged = f"Ranged: {status.ranged}"
            self.world.font_m.draw_text(x + 70, y + 60, ranged, 0)
            magic = f"Magic: {status.magic}"
            self.world.font_m.draw_text(x + 150, y + 40, magic, 0)
            agility = f"Agility: {status.agility}"
            self.world.font_m.draw_text(x + 150, y + 60, agility, 0)
            toughness = f"Toughness: {status.toughness}"
            self.world.font_m.draw_text(x + 230, y + 40, toughness, 0)
            
class ScPlayerPawn(Screen):
    def __init__(self, world, priority: int = 0, **kwargs) -> None:
        super().__init__(world, priority, **kwargs)
    
    def draw(self):
        for ent, (player, position) in self.world.get_components(Player, Position):
            # pyxel.rect(position.x, position.y, 16, 16, 5)
            # pyxel.rectb(position.x, position.y, 16, 16, 0)
            pyxel.blt(position.x, position.y, 0, 0, 0, 23, 31, 7)
            # self.world.font_s.draw_text(position.x, position.y, player.name, 0)

class ScNPCPawn(Screen):
    def __init__(self, world, priority: int = 0, **kwargs) -> None:
        super().__init__(world, priority, **kwargs)
    
    def draw(self):
        for ent, (npc, position) in self.world.get_components(NPC, Position):
            # pyxel.rect(position.x, position.y, 16, 16, 3)
            # pyxel.rectb(position.x, position.y, 16, 16, 0)
            pyxel.blt(position.x, position.y, 0, 24, 0, 32, 31, 7)
            self.world.font_s.draw_text(position.x, position.y, npc.name, 0)
            
class ScInteraction(Screen):
    def draw(self):
        for ent, (player, interactable) in self.world.get_components(Player, Interactable):
            if interactable.opponent is None:
                continue
            opponent = self.world.get_entity_object(interactable.opponent)
            opponent_character = opponent[NPC]
            opponent_status = opponent[CharacterStatus]
            
            text = f"{opponent_character.name}"
            self.world.font_m.draw_text(10, 10, text, 0)
            
            if interactable.status == 0:
                message = f"Press Enter to interact."
                self.world.font_m.draw_text(10, 30, message, 0)
            
            if interactable.status == 1:
                message = f"Press Enter to end conversation."
                self.world.font_m.draw_text(10, 30, message, 0)
                text_fight = "Fight [F]"
                text_talk = "Talk [T]"
                self.world.font_m.draw_text(10, 50, text_fight, 0)
                self.world.font_m.draw_text(10, 70, text_talk, 0)
            
            if interactable.status == 2:
                message = f"Fighting {opponent_character.name}..."
                self.world.font_m.draw_text(10, 30, message, 0)
                
            if interactable.status == 3:
                message = f"Talking to {opponent_character.name}..."
                self.world.font_m.draw_text(10, 30, message, 0)
                
class ScOpponentStatus(Screen):
    def draw(self):
        for ent, (player, interactable) in self.world.get_components(Player, Interactable):
            if interactable.opponent is None or interactable.status != 2:
                print("no opponent or not fighting:", interactable.opponent, interactable.status)
                continue
            opponent = self.world.get_entity_object(interactable.opponent)
            character = opponent[NPC]
            status = opponent[CharacterStatus]
            
            text = f"{character.name}"
            self.world.font_m.draw_text(10, 10, text, 0)
            
            if interactable.status == 2:
                message = f"Fighting {character.name}..."
                self.world.font_m.draw_text(10, 30, message, 0)
                
            screen_size = self.world.SCREEN_SIZE
            x = screen_size[0] - 400
            y = 100
            
            hp_bar_y = y - 40
            pyxel.rect(x - 4, y - 4, 360, 84, 7)
            pyxel.rectb(x - 4, y - 4, 360, 84, 0)
            
            hp_max_x = 140
            hp_x = status.hp / status.hp_max * hp_max_x
            
            bar_height = 8
            
            self.world.font_s.draw_text(x, hp_bar_y - 2, "HP", 0)
            
            pyxel.rect(x + 20, hp_bar_y, hp_max_x, bar_height, 13)
            pyxel.rect(x + 20, hp_bar_y, hp_x, bar_height, 8)
            pyxel.rectb(x - 2 + 20, hp_bar_y - 2, hp_max_x + 4, bar_height + 4, 0)
            
            mp_bar_y = hp_bar_y + 16
            
            mp_max_x = 140
            if status.mp_max == 0:
                mp_x = 0
            else:
                mp_x = status.mp / status.mp_max * mp_max_x
                
            self.world.font_s.draw_text(x, mp_bar_y - 2, "MP", 0)
            pyxel.rect(x + 20, mp_bar_y, mp_max_x, bar_height, 13)
            pyxel.rect(x + 20, mp_bar_y, mp_x, bar_height, 5)
            pyxel.rectb(x - 2 + 20, mp_bar_y - 2, mp_max_x + 4, bar_height + 4, 0)
            pyxel.rect(x - 4, y - 4, 360, 84, 7)
            pyxel.rectb(x - 4, y - 4, 360, 84, 0)
            text = f"{character.name}"
            self.world.font_l.draw_text(x, y, text, 0)
            hp = f"HP: {status.hp}"
            self.world.font_m.draw_text(x, y + 40, hp, 0)
            mp = f"MP: {status.mp}"
            self.world.font_m.draw_text(x, y + 60, mp, 0)
            melee = f"Melee: {status.melee}"
            self.world.font_m.draw_text(x + 70, y + 40, melee, 0)
            ranged = f"Ranged: {status.ranged}"
            self.world.font_m.draw_text(x + 70, y + 60, ranged, 0)
            magic = f"Magic: {status.magic}"
            self.world.font_m.draw_text(x + 150, y + 40, magic, 0)
            agility = f"Agility: {status.agility}"
            self.world.font_m.draw_text(x + 150, y + 60, agility, 0)
            toughness = f"Toughness: {status.toughness}"
            self.world.font_m.draw_text(x + 230, y + 40, toughness, 0)
            
class ScPlayerFullImage(Screen):
    def draw(self):
        x = 300
        y = 300
        for ent, (player) in self.world.get_component(Player):
            pyxel.blt(x, y, 0, 0, 0, 23, 31, 7)
            
class ScOpponentFullImage(Screen):
    def draw(self):
        x = 600
        y = 300
        for ent, (player, interactable) in self.world.get_components(Player, Interactable):
            if interactable.opponent is None or interactable.status != 2:
                continue
            opponent = self.world.get_entity_object(interactable.opponent)
            pyxel.blt(x, y, 0, 24, 0, 32, 31, 7)