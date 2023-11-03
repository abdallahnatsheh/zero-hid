from zero_hid import Keyboard, KeyCodes
from zero_hid.hid import keycodes
from zero_hid import Mouse
from time import sleep

k = Keyboard()
m = Mouse()
sleep(1.0)
k.press([KeyCodes.MOD_LEFT_GUI], KeyCodes.KEY_R)
sleep(0.5)
k.type('chrome', 0.02)
sleep(0.5)
k.press([], KeyCodes.KEY_ENTER)
sleep(3.0)
k.type('https://www.youtube.com/watch?v=dQw4w9WgXcQ', 0.02)
sleep(0.5)
k.press([], KeyCodes.KEY_ENTER)
sleep(3.0)
k.press([KeyCodes.MOD_LEFT_ALT], KeyCodes.KEY_SPACE)
k.type('x', 0.02)
