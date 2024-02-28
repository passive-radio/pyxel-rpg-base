"""Component module"""

from dataclasses import dataclass
from pigframe import Component

@dataclass
class Position(Component):
    """Position component
    """
    x: int
    y: int
    x_prev: int = None
    y_prev: int = None
    w: int = 16
    h: int = 16
    
@dataclass
class Velocity(Component):
    """Velocity component
    """
    x: int
    y: int
    speed: float
    
@dataclass
class Movable(Component):
    """Movable component
    If this component is attached to an entity, the entity can be moved by some systems.
    """
    pass

@dataclass
class Character(Component):
    """Character component
    If this component is attached to an entity, the entity is a character."""
    name: str
    id: str
    
@dataclass
class PlayerConfig(Component):
    """PlayerConfig component
    If this component is attached to an entity, the entity is a candidate of player."""
    name_alphabet: str = ""
    name: str = ""
    
@dataclass
class CharacterStatus(Component):
    """CharacterStatus component
    If this component is attached to an entity, the entity has some status of character 
    (e.g. Player, NPC).
    """
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
    """Playable component
    If this component is attached to an entity, the entity is playable."""
    selected: bool = False

@dataclass
class Collidable(Component):
    """Collidable component
    If this component is attached to an entity, the entity is collidable."""
    pass

@dataclass
class Player(Character):
    """Player component
    If this component is attached to an entity, the entity is a player."""
    pass

@dataclass
class NPC(Character):
    """NPC component
    If this component is attached to an entity, the entity is a NPC."""
    pass

@dataclass
class Interactable(Component):
    """Interactable component
    If this component is attached to an entity, the entity is interactable."""
    opponent: int | None = None # entity id, if None, not interacting
    status: int = 0 # 0: not interacted, 1: interacting, 2: fight, 3: talk

@dataclass
class Button(Component):
    """Button component
    If this component is attached to an entity, the entity is a button."""
    x: int
    y: int
    w: int
    h: int
    text: str | None
    to: str | None
    hover: bool = False
    clicked: bool = False
    clicking: bool = False
    color: int = 0
    bg_color: int = 7
    border_color: int | None = 0