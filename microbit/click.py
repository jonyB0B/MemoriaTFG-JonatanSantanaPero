import pyautogui
import microbit
import msvcrt, sys, datetime
import time
#import sys

THRESHOLD=200.0
SENX=100.0
SENY=80.0

def Help_Windows():
	ayuda="""		AYUDA
	Pulsa A para manejar la cámara
	Pulsa B para manejar el movimiento		
	Pulsa AB a la vez para hacer click"""  
	ch = msvcrt.getwch()
	if ch == 'q':
		sys.exit()
	elif ch == 'h':
		print(ayuda)
	else:
		print ("Wrong Key Pressed")
		print("Press H to help, Q to exit")
		
def Help_Linux():
	ch = input("Press H to help, Q to exit")
	if ch == 'q':
		sys.exit()
	elif ch == 'h':
		print(ayuda)
	else:
		print ("Wrong Key Pressed")
		print("Press H to help, Q to exit")
		
def Camera(Width):
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
def Move():
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
			
		if microbit.button_a.is_pressed():
			break

while True:

	if msvcrt.kbhit():
		Help_Windows()
			
	if microbit.button_a.is_pressed() and microbit.button_b.is_pressed():
		print("Button AB pressed, click mode")
		pyautogui.click()
		
	elif microbit.button_a.is_pressed():
		print("Button A pressed, camera mode, press B to exit")
		screenWidth, screenHeight = pyautogui.size()
		Factor = 1000*2 # Factor 2 porque la pantalla es 4k, Full Hd sería 1
		Width = screenWidth / Factor # Sacamos el multiplo para igualar a la resolución de la pantalla
		Height = screenHeight
		pyautogui.mouseDown()
		Camera(Width)
		
	elif microbit.button_b.is_pressed():
		print("Button B pressed, movement mode, press A to exit")
		screenWidth, screenHeight = pyautogui.size()
		pyautogui.mouseDown()
		pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
		pyautogui.mouseUp()
		#Centramos la poscion de la camara antes de movernos
		Move()
		
	#print(microbit.accelerometer.get_values())
	microbit.sleep(500)