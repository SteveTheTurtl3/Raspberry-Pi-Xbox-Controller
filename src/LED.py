#sets up the LEDs and tests them
import RPi.GPIO as GPIO
import time
LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN, GPIO.OUT)
try:
	while True:
		GPIO.output(LED_PIN, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(LED_PIN, GPIO.LOW)
		time.sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()
