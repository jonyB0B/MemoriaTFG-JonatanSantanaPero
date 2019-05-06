import pyautogui
import microbit
import msvcrt, sys

#Variables globales

THRESHOLD=200.0
SENX=180.0
SENY=280.0
AYUDA="""		AYUDA
	Pulsa A para manejar la cámara
	Pulsa B para manejar el movimiento		
	Pulsa AB a la vez para hacer click"""  
	
#FUNCIONES

def Help_Windows():
	ch = msvcrt.getwch()
	if ch == 'q':
		sys.exit()
	elif ch == 'h':
		print(AYUDA)
	else:
		print ("Wrong Key Pressed")
		print("Press H to help, Q to exit")
		
def Help_Linux():
	ch = input("Press H to help, Q to exit")
	if ch == 'q':
		sys.exit()
	elif ch == 'h':
		print(AYUDA)
	else:
		print ("Wrong Key Pressed")
		print("Press H to help, Q to exit")
		
def Camera(Width):
	while True:
		x = microbit.accelerometer.get_x()
		y = microbit.accelerometer.get_y()
			
		if x > SENX:
			pyautogui.moveRel(Height*x, None)
		elif x < -SENX:
			pyautogui.moveRel(Height*x, None)			
		if y > SENY:
			pyautogui.moveRel(None, y*Width)
		elif y < -SENY:
			pyautogui.moveRel(None, y*Width)
				
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
			pyautogui.keyDown("up")
		elif y < -THRESHOLD:
			pyautogui.keyDown("down")
		else:
			pyautogui.keyUp("down")
			pyautogui.keyUp("up")
			
		if microbit.button_a.is_pressed():
			break
			
def Center_Cam():
	screenWidth, screenHeight = pyautogui.size()
	pyautogui.mouseDown()
	pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
	pyautogui.mouseUp()
	
#MAIN
	
while True:

	if msvcrt.kbhit():
		Help_Windows()
		#Help_Linux()
			
	elif microbit.button_a.is_pressed() and microbit.button_b.is_pressed():
		print("Button AB pressed, click mode")
		pyautogui.click()
		
	elif microbit.button_a.is_pressed():
		print("Button A pressed, camera mode, press B to exit")
		screenWidth, screenHeight = pyautogui.size()
		Factor_y = 1920*6 # Factor 6 porque la pantalla es 4k
		Factor_x = 1080*6
		Width = screenWidth / Factor_y # Ajusto la sensibilidad
		Height = screenHeight/ Factor_x
		pyautogui.mouseDown()
		Camera(Width)
		
	elif microbit.button_b.is_pressed():
		print("Button B pressed, movement mode, press A to exit")
		#Centramos la poscion de la camara antes de movernos
		Center_Cam()
		Move()
		
	#print(microbit.accelerometer.get_values())
	microbit.sleep(500)