from pynput.mouse import Button, Controller
import time
mouse = Controller()

# Read pointer position
print('The current pointer position is {0}'.format(
    mouse.position))
time.sleep(5)
# Set pointer position
mouse.position = (150, 95)
print('Now we have moved it to {0}'.format(
    mouse.position))
# Press and release
mouse.press(Button.left)
mouse.release(Button.left)
mouse.position = (1845, 266)
print('Now we have moved it to {0}'.format(
    mouse.position))
time.sleep(2)
# Press and release
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(2)
mouse.position = (829, 441)
print('Now we have moved it to {0}'.format(
    mouse.position))
time.sleep(5)
# Press and release
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(2)
mouse.position = (1191, 723)
print('Now we have moved it to {0}'.format(
    mouse.position))
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(5)
mouse.position = (1861, 403)
print('Now we have moved it to {0}'.format(
    mouse.position))
time.sleep(2)
# Press and release
mouse.press(Button.left)
mouse.release(Button.left)