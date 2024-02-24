from dataclasses import dataclass
from pigframe import Component

@dataclass
class Position(Component):
    x: int
    y: int
    
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
class CharacterStatus(Component):
    job: str
    hp: int
    mp: int
    melee: int
    magic: int
    ranged: int
    agility: int
    
@dataclass
class Playable(Component):
    selected: bool = False

@dataclass
class Player(Character):
    pass