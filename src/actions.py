from dataclasses import dataclass
from pigframe import ActionMap
import pyxel

@dataclass
class Actions(ActionMap):
    up: tuple = pyxel.btn, pyxel.KEY_UP, pyxel.KEY_W
    down: tuple = pyxel.btn, pyxel.KEY_DOWN, pyxel.KEY_S
    left: tuple = pyxel.btn, pyxel.KEY_LEFT, pyxel.KEY_A
    right: tuple = pyxel.btn, pyxel.KEY_RIGHT, pyxel.KEY_D
    up_p: tuple = pyxel.btnp, pyxel.KEY_UP, pyxel.KEY_W
    down_p: tuple = pyxel.btnp, pyxel.KEY_DOWN, pyxel.KEY_S
    left_p: tuple = pyxel.btnp, pyxel.KEY_LEFT, pyxel.KEY_A
    right_p: tuple = pyxel.btnp, pyxel.KEY_RIGHT, pyxel.KEY_D
    enter: tuple = pyxel.btn, pyxel.KEY_RETURN, pyxel.KEY_RETURN2
    click: tuple = pyxel.btn, pyxel.MOUSE_BUTTON_LEFT
    click_p: tuple = pyxel.btnp, pyxel.MOUSE_BUTTON_LEFT
    enter_p: tuple = pyxel.btnp, pyxel.KEY_RETURN, pyxel.KEY_RETURN2
    enter_r: tuple = pyxel.btnr, pyxel.KEY_RETURN, pyxel.KEY_RETURN2
    backspace: tuple = pyxel.btn, pyxel.KEY_BACKSPACE, pyxel.KEY_KP_BACKSPACE
    backspace_p: tuple = pyxel.btnp, pyxel.KEY_BACKSPACE, pyxel.KEY_KP_BACKSPACE
    click_r: tuple = pyxel.btnr, pyxel.MOUSE_BUTTON_LEFT
    escape: tuple = pyxel.btn, pyxel.KEY_ESCAPE
    space: tuple = pyxel.btn, pyxel.KEY_SPACE
    space_p: tuple = pyxel.btnp, pyxel.KEY_SPACE
    a_p: tuple = pyxel.btnp, pyxel.KEY_A
    b_p: tuple = pyxel.btnp, pyxel.KEY_B
    c_p: tuple = pyxel.btnp, pyxel.KEY_C
    d_p: tuple = pyxel.btnp, pyxel.KEY_D
    e_p: tuple = pyxel.btnp, pyxel.KEY_E
    f_p: tuple = pyxel.btnp, pyxel.KEY_F
    g_p: tuple = pyxel.btnp, pyxel.KEY_G
    h_p: tuple = pyxel.btnp, pyxel.KEY_H
    i_p: tuple = pyxel.btnp, pyxel.KEY_I
    j_p: tuple = pyxel.btnp, pyxel.KEY_J
    k_p: tuple = pyxel.btnp, pyxel.KEY_K
    l_p: tuple = pyxel.btnp, pyxel.KEY_L
    m_p: tuple = pyxel.btnp, pyxel.KEY_M
    n_p: tuple = pyxel.btnp, pyxel.KEY_N
    o_p: tuple = pyxel.btnp, pyxel.KEY_O
    p_p: tuple = pyxel.btnp, pyxel.KEY_P
    q_p: tuple = pyxel.btnp, pyxel.KEY_Q
    r_p: tuple = pyxel.btnp, pyxel.KEY_R
    s_p: tuple = pyxel.btnp, pyxel.KEY_S
    t_p: tuple = pyxel.btnp, pyxel.KEY_T
    u_p: tuple = pyxel.btnp, pyxel.KEY_U
    v_p: tuple = pyxel.btnp, pyxel.KEY_V
    w_p: tuple = pyxel.btnp, pyxel.KEY_W
    x_p: tuple = pyxel.btnp, pyxel.KEY_X
    y_p: tuple = pyxel.btnp, pyxel.KEY_Y
    z_p: tuple = pyxel.btnp, pyxel.KEY_Z
    a: tuple = pyxel.btn, pyxel.KEY_A
    b: tuple = pyxel.btn, pyxel.KEY_B
    c: tuple = pyxel.btn, pyxel.KEY_C
    d: tuple = pyxel.btn, pyxel.KEY_D
    e: tuple = pyxel.btn, pyxel.KEY_E
    f: tuple = pyxel.btn, pyxel.KEY_F
    g: tuple = pyxel.btn, pyxel.KEY_G
    h: tuple = pyxel.btn, pyxel.KEY_H
    i: tuple = pyxel.btn, pyxel.KEY_I
    j: tuple = pyxel.btn, pyxel.KEY_J
    k: tuple = pyxel.btn, pyxel.KEY_K
    l: tuple = pyxel.btn, pyxel.KEY_L
    m: tuple = pyxel.btn, pyxel.KEY_M
    n: tuple = pyxel.btn, pyxel.KEY_N
    o: tuple = pyxel.btn, pyxel.KEY_O
    p: tuple = pyxel.btn, pyxel.KEY_P
    q: tuple = pyxel.btn, pyxel.KEY_Q
    r: tuple = pyxel.btn, pyxel.KEY_R
    s: tuple = pyxel.btn, pyxel.KEY_S
    t: tuple = pyxel.btn, pyxel.KEY_T
    u: tuple = pyxel.btn, pyxel.KEY_U
    v: tuple = pyxel.btn, pyxel.KEY_V
    w: tuple = pyxel.btn, pyxel.KEY_W
    x: tuple = pyxel.btn, pyxel.KEY_X
    y: tuple = pyxel.btn, pyxel.KEY_Y
    z: tuple = pyxel.btn, pyxel.KEY_Z