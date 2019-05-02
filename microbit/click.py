import pyautogui
import microbit
import msvcrt
import time
#import sys

THRESHOLD=200.0
SENX=100.0
SENY=80.0

while True:
	print("Push H to help")
	time.sleep(0.5)
	if msvcrt.kbhit():
		tecla = msvcrt.getch()
		ayuda="""		AYUDA
		Pulsa A para manejar la cámara
		Pulsa B para manejar el movimiento		
		Pulsa AB a la vez para hacer click"""
		print (ayuda)
	
	if microbit.button_a.is_pressed() and microbit.button_b.is_pressed():
		print("Button AB pressed, click mode")
		pyautogui.click()
		
	elif microbit.button_a.is_pressed():
		print("Button A pressed, camera mode, press B to exit")
		screenWidth, screenHeight = pyautogui.size()
		#pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
		Factor = 1000*2 # Factor 2 porque la pantalla es 4k
		Width = screenWidth / Factor # Sacamos el multiplo para igualar a la resolución de la pantalla
		Height = screenHeight
		pyautogui.mouseDown()
		while True:
			x = microbit.accelerometer.get_x()
			y = microbit.accelerometer.get_y()
			
			if x > SENX:
				pyautogui.moveRel(x, None)
			elif x < -SENX:
				pyautogui.moveRel(x, None)
			
			if y > SENY:
				pyautogui.moveRel(None, -y*Width)
			elif y < -SENY:
				pyautogui.moveRel(None, -y*Width)
				
			if microbit.button_b.is_pressed():
				pyautogui.mouseUp()
				break
		
	elif microbit.button_b.is_pressed():
		while True:
			x = microbit.accelerometer.get_x()
			y = microbit.accelerometer.get_y()
			print("Button B pressed, movement mode, press A to exit")
			
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
				
			if microbit.button_a.is_pressed():
				break
	#print(microbit.accelerometer.get_values())
	microbit.sleep(500)