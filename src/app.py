import pyxel
from pigframe import *

from entity import *
from component import *
from system import *
from screen import *
from event import *

from actions import *

from font import BDFRenderer
from characters import NPCS

class App(World):
    def __init__(self):
        super().__init__()
        self.init()
        
    def init(self):
        self.FPS = 60
        self.TITLE = "基本のＲＰＧ"
        self.SCREEN_SIZE = (960, 680)
        
        pyxel.init(self.SCREEN_SIZE[0], self.SCREEN_SIZE[1], title = self.TITLE, fps = self.FPS, )
        pyxel.load("assets/resource.pyxres")
        self.font_s = BDFRenderer("assets/b14.bdf")
        self.font_m = BDFRenderer("assets/b16.bdf")
        self.font_l = BDFRenderer("assets/b24.bdf")
        
        pyxel.mouse(True)
    
    def reset(self):
        pass
    
    def draw(self):
        pyxel.cls(13)
        self.process_screens()

    def update(self):
        self.scene_manager.update_scene()
        self.process_user_actions()
        self.scene_manager._SceneManager__process_events()
        self.process_events()
        self.process_systems()
        self.scene_manager._SceneManager__process_transitions()
        
    def run(self):
        pyxel.run(self.update, self.draw)

if __name__ == "__main__":
    # App クラスのインスタンスを作成した
    app = App()
    
    # ユーザーアクションの定義を追加した
    app.set_user_actions_map(Actions())
    
    # シーンを追加した
    app.add_scenes(["start", "menu", "choose-player", "name-player", "play", "fight", "result", ])
    
    # エンティティーを追加した
    # プレイアブルキャラクター を追加する (プレイするキャラクター選択シーンで選べるキャラクター)
    create_playable(app, "剣士", 40, 40, 1, 100, 0, 10, 0, 0, 2, 5)
    create_playable(app, "魔法使い", 40, 40, 1, 70, 30, 2, 10, 0, 1, 5)
    create_playable(app, "狩人", 40, 40, 1, 80, 0, 5, 0, 10, 3, 5)
    create_playable(app, "僧侶", 40, 40, 1, 80, 20, 5, 5, 0, 2, 5)
    
    # ボタンを追加した
    btn01 = create_button(app, (app.SCREEN_SIZE[0] - 120)//2, (app.SCREEN_SIZE[1] - 30)//2 + 40, 120, 30, "choose-player", "はじめる", 0, 7, 0)

    for npc in NPCS:
        create_npc(app, npc["name"], npc["job"], npc["x"], npc["y"], npc["speed"], npc["hp"], npc["mp"], 
                    npc["melee"], npc["magic"], npc["ranged"], npc["agility"], npc["toughness"])
    
    # システム処理を追加した
    app.add_system_to_scenes(SysChoosePlayer, "choose-player", priority = 0)
    app.add_system_to_scenes(SysInputText, "name-player", priority = 0)
    app.add_system_to_scenes(SysControlPlayer, "play", priority = 0)
    app.add_system_to_scenes(SysMoveByVelocity, "play", priority = 10)
    app.add_system_to_scenes(SysCollision, "play", priority = 20)
    app.add_system_to_scenes(SysUpdatePosition, "play", priority = 30)
    app.add_system_to_scenes(SysInteract, "play", priority = 40)
    app.add_system_to_scenes(SysButton, ["start", "menu", "choose-player", "name-player", "play", "fight"], priority = 50)
    app.add_system_to_scenes(SysButtonEvent, ["start", "menu", "choose-player", "name-player", "play", "fight"], priority = 60)
    
    # スクリーン処理を追加した
    app.add_screen_to_scenes(ScLaunch, "start", priority = 0)
    app.add_screen_to_scenes(ScChoosePlayer, "choose-player", priority = 0)
    app.add_screen_to_scenes(ScNamePlayer, "name-player", priority = 0)
    app.add_screen_to_scenes(ScPlayerStatus, ["play", "fight"], priority = 0)
    app.add_screen_to_scenes(ScPlayerPawn, "play", priority = 10)
    app.add_screen_to_scenes(ScNPCPawn, "play", priority = 20)
    app.add_screen_to_scenes(ScInteraction, "play", priority = 30)
    app.add_screen_to_scenes(ScOpponentStatus, "fight", priority = 40)
    app.add_screen_to_scenes(ScPlayerFullImage, "fight", priority = 50)
    app.add_screen_to_scenes(ScOpponentFullImage, "fight", priority = 60)
    app.add_screen_to_scenes(ScButton, ["start", "menu", "choose-player", "name-player", "play", "fight"], priority = 70)
    
    # イベント処理を追加した
    app.add_event_to_scene(EvStarted, "start", lambda: app.get_entity_object(btn01)[Button].clicked, priority = 0)
    # app.add_event_to_scene(EvPlayerChoosed, "choose-player", lambda: app.actions.enter_p, priority = 0)
    # app.add_event_to_scene(EvPlayBGM, "name-player", lambda: app.actions.enter_p, priority = 0)
    app.add_event_to_scene(EvStartInteraction, "play", lambda: app.actions.enter_p, priority = 30)
    app.add_event_to_scene(EvStartFight, "play", lambda: app.actions.f_p, priority = 20)
    app.add_event_to_scene(EvStartTalk, "play", lambda: app.actions.t_p, priority = 10)
    
    # シーン遷移処理を追加した
    # app.add_scene_transition("start", "choose-player", lambda: app.actions.enter_p)
    # app.add_scene_transition("choose-player", "name-player", lambda: app.actions.enter_p)
    # app.add_scene_transition("name-player", "play", lambda: app.actions.enter_p)
    app.add_scene_transition("play", "fight", lambda: app.actions.f_p)
    # app.add_scene_transition("start", "choose-player", lambda: app.get_entity_object(btn01)[Button].clicked)
    
    app.current_scene = "start"
    app.run()
    