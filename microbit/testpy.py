import microbit
import pyautogui
while True:
	if microbit.button_a.was_pressed():
		microbit.display.show("PULSA A")
		screenWidth, screenHeight = pyautogui.size()
		pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
		microbit.sleep(500)
		microbit.display.clear()