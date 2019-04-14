import microbit
while True:
		print(microbit.accelerometer.get_values())
		microbit.sleep(250)