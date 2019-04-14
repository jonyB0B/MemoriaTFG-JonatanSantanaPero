import pyautogui
import microbit

while True:

	x = button_a.is_pressed()
	if x:
		pyautogui.click()
	else:
		display.show(Image.SAD)