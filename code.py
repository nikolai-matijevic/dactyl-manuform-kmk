import board
import busio

from digitalio import Direction

from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.matrix import DiodeOrientation # DonutCat Fork
# from kmk.scanners import DiodeOrientation # KMK

from adafruit_mcp230xx.mcp23017 import MCP23017


def MCP(i, k):
    pin = mcps[i].get_pin(int('{0}'.format(k)))
    pin.direction = Direction.OUTPUT
    # pin.pull = Pull.UP
    return pin


i2c = busio.I2C(scl=board.SCL, sda=board.SDA, frequency=100000)

mcps = [
    MCP23017(i2c, address=0x20),
    MCP23017(i2c, address=0x21),
    MCP23017(i2c, address=0x22),
    MCP23017(i2c, address=0x23),
]

pins = [
    MCP(1,14),
    MCP(1,13),
    MCP(1,12),
    MCP(1,11),
    MCP(1,10),
    MCP(1,9),
    MCP(1,8),
    MCP(0,7),
    MCP(0,6),
    MCP(0,5),
    MCP(0,4),
    MCP(0,10),
    MCP(0,9),
    MCP(0,8),
    MCP(0,11),
    MCP(0,12),
    MCP(0,13),
    MCP(0,3),
    MCP(0,0),
    MCP(0,14),
    MCP(0,2),
    MCP(0,15),
    MCP(0,1),
    MCP(2,12),
    MCP(2,3),
    MCP(2,13),
    MCP(2,2),
    MCP(2,1),
    MCP(2,5),
    MCP(2,15),
    MCP(2,0),
    MCP(2,14),
    MCP(2,11),
    MCP(2,4),
    MCP(2,10),
    MCP(2,9),
    MCP(2,6),
    MCP(2,8),
    MCP(2,7),
    MCP(3,7),
    MCP(3,6),
    MCP(3,5),
    MCP(3,4),
    MCP(3,3),
    MCP(3,2),
    MCP(3,1),
]

keyboard = KMKKeyboard()
keyboard.debug_enabled = True

keyboard.row_pins = (board.A0,)
keyboard.col_pins = tuple([p for p in pins],)
keyboard.diode_orientation = DiodeOrientation.COLUMNS

keyboard.keymap = [
    [
        KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Z, KC.U, KC.I, KC.O, KC.P, KC.NO,
        KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.NO, KC.NO,
        KC.Y, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.MINUS,
    ],
]

if __name__ == '__main__':
    keyboard.go()
