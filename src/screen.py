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

class ScPlayerConfig(Screen):
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