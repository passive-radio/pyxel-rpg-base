from pigframe import *
from component import *

def create_playable(app: World, job: str, x: int, y: int, speed: int, hp: int, 
                mp: int, melee: int, magic: int, ranged: int, agility: int) -> int:
    """Create player entity and add components to it.

    Args:
        app (World): _description_
        name (_type_): _description_
        x (_type_): _description_
        y (_type_): _description_
        speed (_type_): _description_

    Returns:
        int: _description_
    """
    ent = app.create_entity()
    app.add_component_to_entity(ent, Position, x = x, y = y)
    app.add_component_to_entity(ent, Movable)
    app.add_component_to_entity(ent, Velocity, x = 0, y = 0, speed = speed)
    app.add_component_to_entity(ent, Playable)
    app.add_component_to_entity(ent, CharacterStatus, job = job, hp = hp, mp = mp, 
                                melee = melee, magic = magic, ranged = ranged, agility = agility)
    
    return ent