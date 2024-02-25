import pyxel
from pigframe import *

from entity import *
from component import *
from system import *
from screen import *
from event import *
from triger import *
from actions import *

from font import BDFRenderer

class App(World):
    def __init__(self):
        super().__init__()
        self.init()
        
    def init(self):
        self.FPS = 60
        self.TITLE = "基本のRPG"
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
        self.process()
        
    def run(self):
        pyxel.run(self.update, self.draw)

if __name__ == "__main__":
    # App クラスのインスタンスを作成した
    app = App()
    
    # ユーザーアクションの定義を追加した
    app.set_user_actions_map(Actions())
    
    # シーンを追加した
    app.add_scenes(["start", "menu", "choose-player", "name-player", "play", "result", ])
    
    # エンティティーを追加した
    # プレイアブルキャラクター を追加する (プレイするキャラクター選択シーンで選べるキャラクター)
    create_playable(app, "剣士", 10, 10, 1, 100, 0, 10, 0, 0, 2)
    create_playable(app, "魔法使い", 10, 10, 1, 70, 30, 2, 10, 0, 1)
    create_playable(app, "狩人", 10, 10, 1, 80, 0, 5, 0, 10, 3)
    create_playable(app, "僧侶", 10, 10, 1, 80, 20, 5, 5, 0, 2)
    
    
    # システム処理を追加した
    app.add_system_to_scenes(SysChoosePlayer, "choose-player", priority = 0)
    app.add_system_to_scenes(SysInputText, "name-player", priority = 0)
    
    # スクリーン処理を追加した
    app.add_screen_to_scenes(ScLaunch, "start", priority = 0)
    app.add_screen_to_scenes(ScChoosePlayer, "choose-player", priority = 0)
    app.add_screen_to_scenes(ScNamePlayer, "name-player", priority = 0)
    app.add_screen_to_scenes(ScPlayerStatus, "play", priority = 0)
    
    # イベント処理を追加した
    app.add_event_to_scene(EvPlayerChoosed, "choose-player", lambda: app.actions.enter, priority = 0)
    app.add_event_to_scene(EvPlayBGM, "name-player", lambda: app.actions.enter_p, priority = 0)
    
    # シーン遷移処理を追加した
    app.add_scene_transition("start", "choose-player", lambda: app.actions.enter_p)
    app.add_scene_transition("choose-player", "name-player", lambda: app.actions.enter_p)
    app.add_scene_transition("name-player", "play", lambda: app.actions.enter_p)
    
    app.current_scene = "start"
    app.run()
    