import pyautogui
import microbit

THRESHOLD=200.0

while True:
    x = microbit.accelerometer.get_x()
    y = microbit.accelerometer.get_y()

    if x > THRESHOLD:
        pyautogui.keyDown("right")
    elif x < -THRESHOLD: 
        pyautogui.keyDown("left")
    else:
        pyautogui.keyUp("right")
        pyautogui.keyUp("left")
	

    if y > THRESHOLD:
        pyautogui.keyDown("down")
    elif y < -THRESHOLD: 
        pyautogui.keyDown("up")
    else:
        pyautogui.keyUp("down")
        pyautogui.keyUp("up")
        

