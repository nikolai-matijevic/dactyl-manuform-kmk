import board
import busio
import digitalio

from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.scanners.digitalio import MatrixScanner
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.extensions.media_keys import MediaKeys
from kmk.handlers.sequences import simple_key_sequence
from kmk.modules.mouse_keys import MouseKeys

from adafruit_mcp230xx.mcp23017 import MCP23017


class DactylManuform(KMKKeyboard):
    def __init__(self):
        self.matrix = MatrixScanner(
            cols=(board.A0,),
            rows=tuple([p for p in pins],),
            diode_orientation=DiodeOrientation.COLUMNS,
        )


def MCP(i, k):
    pin = mcps[i].get_pin(int('{0}'.format(k)))
    pin.direction = digitalio.Direction.INPUT
    pin.pull = digitalio.Pull.UP
    return pin


i2c = busio.I2C(scl=board.SCL, sda=board.SDA, frequency=100000)

mcps = [
    MCP23017(i2c, address=0x20),
    MCP23017(i2c, address=0x21),
    MCP23017(i2c, address=0x22),
    MCP23017(i2c, address=0x23),
]

# +----+----+----+----+----+        :        +----+----+----+----+----+
# |1,14|1,11|0,7 |0,10|0,11|        :        |2,15|2,11|2,9 |3,7 |3,3 |
# +----+----+----+----+----+        :        +----+----+----+----+----+
# |1,13|1,10|0,6 |0,9 |0,12|        :        |2,0 |2,11|2,9 |3,7 |3,3 |
# +----+----+----+----+----+        :        +----+----+----+----+----+
# |1,12|1,9 |0,5 |0,8 |0,13|        :        |2,14|2,10|2,8 |3,5 |3,1 |
# +----+----+----+----+----+        :        +----+----+----+----+----+
#      |1,8 |0,4 |                  :                  |2,7 |3,4 |
#      +----+----+----+----+        :        +----+----+----+----+
#                |0,3 |0,0 |        :        |2,1 |2,5 |
#                +----+----+----+   :   +----+----+----+
#                     |0,2 |0,14|   :   |2,13|2,2 |
#                     +----+----+   :   +----+----+
#                     |0,1 |0,15|   :   |2,12|2,3 |
#                     +----+----+   :   +----+----+

pins = [
    MCP(1, 14), MCP(1, 11), MCP(0, 7) , MCP(0, 10), MCP(0, 11),                                MCP(2, 15), MCP(2, 11), MCP(2, 9) , MCP(3, 7) , MCP(3, 3) ,
    MCP(1, 13), MCP(1, 10), MCP(0, 6) , MCP(0, 9) , MCP(0, 12),                                MCP(2, 0) , MCP(2, 4) , MCP(2, 6) , MCP(3, 6) , MCP(3, 2) ,
    MCP(1, 12), MCP(1, 9) , MCP(0, 5) , MCP(0, 8) , MCP(0, 13),                                MCP(2, 14), MCP(2, 10), MCP(2, 8) , MCP(3, 5) , MCP(3, 1) ,
                MCP(1, 8) , MCP(0, 4) ,                                                                                MCP(2, 7) , MCP(3, 4) ,
                                        MCP(0, 3) , MCP(0, 0) ,                                MCP(2, 1) , MCP(2, 5) ,
                                                    MCP(0, 2) , MCP(0, 14),        MCP(2, 13), MCP(2, 2) ,
                                                    MCP(0, 1) , MCP(0, 15),        MCP(2, 12), MCP(2, 3) ,
]

keyboard = DactylManuform()
keyboard.debug_enabled = True
keyboard.modules.append(ModTap())
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(MouseKeys())
keyboard.modules.append(Layers())

ESC = KC.MT(KC.ESC, KC.LSFT)
BSP = KC.MT(KC.BSPC, KC.LCTL)
SPC = KC.MT(KC.SPC, KC.LALT)
ENT = KC.MT(KC.ENT, KC.LSFT)

_______ = KC.TRNS

keyboard.keymap = [
    [
        KC.q,       KC.w,       KC.e,       KC.r,       KC.t,                                   KC.z,       KC.u,       KC.i,       KC.o,       KC.p,
        KC.a,       KC.s,       KC.d,       KC.f,       KC.g,                                   KC.h,       KC.j,       KC.k,       KC.l,       KC.SCLN,
        KC.y,       KC.x,       KC.c,       KC.v,       KC.b,                                   KC.n,       KC.m,       KC.COMM,    KC.DOT,     KC.QUOT,
                    KC.LBRC,    KC.RBRC,                                                                                KC.MINS,    KC.EQL,
                                            ESC,        BSP,                                    SPC,        ENT,
                                                        KC.TAB,   KC.HOME,          KC.END,     KC.DEL,
                                                        KC.MO(1), KC.GRAVE,         KC.LGUI,    KC.MO(2),
    ],
    [
        KC.MW_UP,   _______,    KC.MS_UP,   _______,    _______,                                KC.VOLU,    _______,    KC.UP,      _______,    KC.PGUP,
        KC.MW_DN,   KC.MS_LEFT, KC.MS_DOWN, KC.MS_RIGHT,_______,                                KC.MUTE,    KC.LEFT,    KC.DOWN,    KC.RIGHT,   KC.PGDN,
        _______,    _______,    _______,    _______,    _______,                                KC.VOLD,    KC.SLSH,    KC.BSLS,    KC.QUES,    KC.PIPE,
                    _______,    _______,                                                                                KC.MB_LMB,  KC.MB_RMB,
                                            _______,    _______,                                _______,    _______,
                                                        _______,  _______,          _______,    _______,
                                                        _______,  _______,          _______,    _______,
    ],
    [
        KC.F1,      KC.F2,      KC.F3,      KC.F4,      KC.F5,                                  KC.F6,      KC.F7,      KC.F8,      KC.F9,      KC.F10,
        KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5,                                  KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,
        KC.EXLM,    KC.AT,      KC.HASH,    KC.DOLLAR,  KC.PERCENT,                             KC.CIRC,    KC.AMPR,    KC.ASTR,    KC.LPRN,    KC.RPRN,
                    KC.F11,     KC.F12,                                                                                 _______,    _______,
                                            _______,    _______,                                _______,    _______,
                                                        _______,  _______,          _______,    _______,
                                                        _______,  _______,          _______,    _______,
    ],
]

if __name__ == '__main__':
    keyboard.go()
