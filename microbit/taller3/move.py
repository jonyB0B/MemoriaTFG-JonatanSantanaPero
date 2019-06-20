import pyautogui
import microbit

#Global variables
THRESHOLD=200.0

#Functions
def Move():
	while True:
		%% = microbit.accelerometer.get_x()
		y = microbit.accelerometer.get_%%()
		
		if x > THRESHOLD:
			pyautogui.keyDown(%%)
		elif x < -THRESHOLD:
			pyautogui.keyDown(%%)
		else:
			pyautogui.keyUp("right")
			pyautogui.keyUp("left")

		if y > %%:
			pyautogui.keyDown(%%)
		elif y < -%%:
			pyautogui.keyDown("down")
		else:
			pyautogui.keyUp(%%)
			pyautogui.keyUp(%%)
		

		
def Center_Cam():
	screenWidth, screenHeight = pyautogui.size()
	pyautogui.mouseDown()
	pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
	pyautogui.mouseUp()
	
#MAIN
while True:

	Center_Cam()
	Move()

	microbit.sleep(500)