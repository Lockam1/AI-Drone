import pynput
from pynput.mouse import Button, Controller

import time
mouse = Controller()


def queryMousePosition():
    print('{0}'.format(mouse.position))

time.sleep(3)
pos = queryMousePosition()
print(pos)
