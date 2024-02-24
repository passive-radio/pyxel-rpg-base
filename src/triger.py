import pyxel

def triger_return():
    return pyxel.btn(pyxel.KEY_RETURN)

def triger_return_r():
    return pyxel.btnr(pyxel.KEY_RETURN)

def triger_return_p():
    return pyxel.btnp(pyxel.KEY_RETURN)

def triger_return_or_tap():
    return pyxel.btn(pyxel.KEY_RETURN) or pyxel.btn(pyxel.MOUSE_BUTTON_LEFT)

def triger_return_or_tap_p():
    return pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT)

def triger_return_or_tap_r():
    return pyxel.btnr(pyxel.KEY_RETURN) or pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT)