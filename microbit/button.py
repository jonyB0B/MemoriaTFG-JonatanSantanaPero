import microbit
import pyautogui
while True:
	if microbit.button_a.was_pressed():
		microbit.display.show("A")
		screenWidth, screenHeight = pyautogui.size()
		pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
		pyautogui.dragTo(0, 0, 40, button='left')
		microbit.sleep(500)
		microbit.display.clear()