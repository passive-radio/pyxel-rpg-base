from dataclasses import dataclass
from pigframe import Component

@dataclass
class Position(Component):
    x: int
    y: int
    x_prev: int = None
    y_prev: int = None
    w: int = 16
    h: int = 16
    
@dataclass
class Velocity(Component):
    x: int
    y: int
    speed: float
    
@dataclass
class Movable(Component):
    pass

@dataclass
class Character(Component):
    name: str
    id: str
    
@dataclass
class PlayerConfig(Component):
    name_alphabet: str = ""
    name: str = ""
    
@dataclass
class CharacterStatus(Component):
    job: str
    hp: int
    mp: int
    melee: int
    magic: int
    ranged: int
    agility: int
    toughness: int
    hp_max: int
    mp_max: int
    
@dataclass
class Playable(Component):
    selected: bool = False

@dataclass
class Collidable(Component):
    pass

@dataclass
class Player(Character):
    pass

@dataclass
class NPC(Character):
    pass

@dataclass
class Interactable(Component):
    opponent: int | None = None # entity id, if None, not interacting
    status: int = 0 # 0: not interacted, 1: interacting, 2: fight, 3: talk