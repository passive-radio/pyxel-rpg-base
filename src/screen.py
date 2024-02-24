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
            text = f"{player.name} {status.job} {status.hp} {status.mp} {status.melee} {status.magic} {status.ranged} {status.agility}"
            self.world.font_l.draw_text(10, 10, text, 0)