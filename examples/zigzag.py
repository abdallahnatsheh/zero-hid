from zero_hid import Mouse
import time


m = Mouse()
while True:
    m.move_relative(5,5)
    m.move_relative(-5,-5)
    time.sleep(10)
m.close()
