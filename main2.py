# importing time and threading
import time
import threading
from pynput.mouse import Button, Controller
import pyautogui as pt
from random import gauss


# pynput.keyboard is used to watch events of
# keyboard for start and stop of auto-clicker
from pynput.keyboard import Listener, KeyCode


# four variables are created to
# control the auto-clicker
delay = 0.001
button = Button.left
targetImg = 'images/target.png'
start_stop_key = KeyCode(char='a')
stop_key = KeyCode(char='b')

# threading.Thread is used
# to control clicks
class ClickMouse(threading.Thread):
	
# delay and button is passed in class
# to check execution of auto-clicker
	def __init__(self, target_png, speed, button):
		super(ClickMouse, self).__init__()
		self.speed = speed
		self.target_png = target_png
		self.button = button
		self.running = False
		self.program_running = True

	def start_clicking(self):
		self.running = True

	def stop_clicking(self):
		self.running = False

	def exit(self):
		self.stop_clicking()
		self.program_running = False

	def nav_to_image(self):
		posVarianceX = abs(gauss(30, .001))
		posVarianceY = abs(gauss(30, .001))
		speedVariance = abs(gauss(self.speed, .001))
		try:
			position = pt.locateOnScreen(self.target_png, confidence=.85)
			pt.moveTo(position[0] + posVarianceX, position[1] + posVarianceY, duration=speedVariance)
			print("Mouse moving: x: %f y: %f at speed: %f " %(position[0] + posVarianceX, position[1] + posVarianceY, speedVariance))
			mouse.click(self.button)
		except:
			print('Image not found...')
			return 0

	# method to check and run loop until
	# it is true another loop will check
	# if it is set to true or not,
	# for mouse click it set to button
	# and delay.
	def run(self):
		while self.program_running:
			while self.running:
				mouse.nav_to_image(self)
				mouse.click(self.button)
				time.sleep(self.delay)
			time.sleep(0.1)


# instance of mouse controller is created
mouse = Controller()
click_thread = ClickMouse(targetImg, delay, button)
click_thread.start()


# on_press method takes
# key as argument
def on_press(key):
	
# start_stop_key will stop clicking
# if running flag is set to true
	if key == start_stop_key:
		if click_thread.running:
			click_thread.stop_clicking()
		else:
			click_thread.start_clicking()
			
	# here exit method is called and when
	# key is pressed it terminates auto clicker
	elif key == stop_key:
		click_thread.exit()
		listener.stop()


with Listener(on_press=on_press) as listener:
	listener.join()
