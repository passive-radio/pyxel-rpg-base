import pyxel

def triger_return():
    return pyxel.btnp(pyxel.KEY_RETURN)

def triger_return_or_tap():
    return pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)