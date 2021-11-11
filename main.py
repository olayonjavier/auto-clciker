import pyautogui as pt
from time import sleep
from random import gauss

class Clicker:
    def __init__(self, target_png, speed):
        self.target_png = target_png
        self.speed = speed
        pt.FAILSAFE = True

    def nav_to_image(self):
        posVarianceX = abs(gauss(0, .001))
        posVarianceY = abs(gauss(0, .001))
        speedVariance = abs(gauss(self.speed, .000001))
        try:
            position = pt.locateCenterOnScreen(self.target_png, grayscale=True, confidence=.75)
            pt.moveTo(position[0] + posVarianceX, position[1] + posVarianceY, duration=speedVariance)
            print("Mouse moving: x: %f y: %f at speed: %f " %(position[0] + posVarianceX, position[1] + posVarianceY, speedVariance))
            pt.click()
        except:
            pt.hotkey('ctrl', 'r')
            sleep(2)
            print('Image not found...')
            return 0

class endImg:
    def __init__(self, img):
        self.img = img
    
    def isEndImg(self):
        try:
            position = pt.locateOnScreen(self.img, confidence=.6)
            pt.moveTo(position[0], position[0], duration=.000001)
        except:
            #print('end image not found...')
            return 0

if __name__ == '__main__':
    sleep(2)
    clicker = Clicker('images/target3.png', speed=0)
    endProg = endImg('images/endImg.png')
    clickCount = 0
    end = 0
    while True:
        if clicker.nav_to_image() == 0:
            end += 1
        #else: #for testing
            #end += 1
        else:
            clickCount += 1

        if endProg.isEndImg() != 0:
            print("Num of clicks: %d" %clickCount)
            print('End Image found. ending prog')
            break

        #if end > 10:
         #   print("Num of clicks: %d" %clickCount)
         #   print('Mine button not found')
         #   break


        