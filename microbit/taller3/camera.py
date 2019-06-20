import pyautogui
import microbit
import msvcrt, sys

#Global variables
THRESHOLD=200.0
SENX=180.0
SENY=280.0

#Functions		
def Camera(Width, Height):
	while True:
		%% = microbit.accelerometer.get_%%()
		%%
			
		if %% > SENX:
			pyautogui.moveRel(%%*x, None)
		elif %% < -SENX:
			pyautogui.moveRel(%%*x, None)			
		if %% > SENY:
			pyautogui.moveRel(None, y*%%)
		elif %% < -SENY:
			pyautogui.moveRel(None, y*%%)
				
		if microbit.button_b.is_pressed():
			pyautogui.%%
			break
			
			
def Center_Cam():
	screenWidth, screenHeight = pyautogui.size()
	pyautogui.mouseDown()
	pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
	pyautogui.mouseUp()
	
#MAIN
while True:
	#Interaction
	if %% and %% :
		print("Buttons A & B pressed, click mode")		
	#Camera
	elif %% :
		print("Button A pressed")
		print("camera mode, press A again to exit")
		screenWidth, screenHeight = pyautogui.size()
		Factor_y = 1920
		Factor_x = 1080
		Width = screenWidth / Factor_y 
		Height = screenHeight/ Factor_x
		%%.mouseDown()
		Camera(Width,Height)
	#Movement
	elif %% :
		print("Button B pressed")
		print("movement mode, press B again to exit")
		Center_Cam()
		Move()
	microbit.sleep(500)