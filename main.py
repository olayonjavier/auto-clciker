import pyautogui as pt
from time import sleep

class Clicker:
    def __init__(self, target_png, speed):
        self.target_png = target_png
        self.speed = speed
        pt.FAILSAFE = True

    def nav_to_image(self):
        try:
            position = pt.locateOnScreen(self.target_png, confidence=.8)
            pt.moveTo(position[0] + 15, position[1] + 15, duration=self.speed)
            pt.doubleClick()
        except:
            print('Image not found...')
            return 0


if __name__ == '__main__':
    sleep(2)
    clicker = Clicker('images/target.png', speed=.001)

    end = 0
    while True:
        if clicker.nav_to_image() == 0:
            end += 1

        if end > 20:
            break