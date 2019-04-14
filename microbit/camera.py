import microbit
import pyautogui
while True:
	if microbit.button_a.was_pressed():
		microbit.display.show("A")
		pyautogui.mouseDown();
		microbit.display.clear()
		microbit.sleep(50000)
	else:
		microbit.display.clear()
		pyautogui.mouseUp();
		microbit.sleep(500)