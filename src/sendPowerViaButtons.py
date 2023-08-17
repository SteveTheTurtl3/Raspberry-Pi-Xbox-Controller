
from evdev import InputDevice, categorize, ecodes, KeyEvent
import RPi.GPIO as GPIO
import time

gamepad = InputDevice('/dev/input/event4')
#print(gamepad)

# for event in gamepad.read_loop():
#print(categorize(event))

aBtn= 304
bBtn= 305
xBtn= 307
yBtn= 308
rbBtn= 311
lbBtn= 310


LED_PIN1 = 26
LED_PIN2 = 16
LED_PIN3 = 6
LED_PIN4 = 5
LED_PIN5 = 25
LED_PIN6 = 24
LED_PIN7 = 22
LED_PIN8 = 17


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(LED_PIN3, GPIO.OUT)
GPIO.setup(LED_PIN4, GPIO.OUT)
GPIO.setup(LED_PIN5, GPIO.OUT)
GPIO.setup(LED_PIN6, GPIO.OUT)
GPIO.setup(LED_PIN7, GPIO.OUT)
GPIO.setup(LED_PIN8, GPIO.OUT)

GPIO.output(LED_PIN2, GPIO.LOW)
GPIO.output(LED_PIN1, GPIO.LOW)
GPIO.output(LED_PIN3, GPIO.LOW)
GPIO.output(LED_PIN4, GPIO.LOW)
GPIO.output(LED_PIN5, GPIO.LOW)
GPIO.output(LED_PIN6, GPIO.LOW)
GPIO.output(LED_PIN7, GPIO.LOW)
GPIO.output(LED_PIN8, GPIO.LOW)

for event in gamepad.read_loop():
    if event.type == ecodes.EV_ABS:
        absevent = categorize(event)
        if ecodes.bytype[absevent.event.type][absevent.event.code] == 'ABS_RZ':
            if absevent.event.value > 128:
                GPIO.output(LED_PIN7, GPIO.HIGH)
            elif absevent.event.value <128:
                GPIO.output(LED_PIN7, GPIO.LOW)
        if ecodes.bytype[absevent.event.type][absevent.event.code] == 'ABS_Z':
            if absevent.event.value > 128:
                GPIO.output(LED_PIN8, GPIO.HIGH)
            elif absevent.event.value <128:
                GPIO.output(LED_PIN8, GPIO.LOW)
    if event.type == ecodes.EV_KEY:
        #if event.value == 1:
        #keyevent = categorize(event)
        #if keyevent.keystate == KeyEvent.key_down:
        if  event.code == aBtn and event.value == 1:
            GPIO.output(LED_PIN1, GPIO.HIGH)
        if event.code== aBtn and event.value == 0:
            GPIO.output(LED_PIN1, GPIO.LOW)
        if event.code == bBtn  and event.value == 1:
            GPIO.output(LED_PIN2, GPIO.HIGH)
        if event.code == bBtn and event.value == 0:
            GPIO.output(LED_PIN2, GPIO.LOW)
        if  event.code == xBtn and event.value == 1:
            GPIO.output(LED_PIN3, GPIO.HIGH)
        if event.code == xBtn and event.value == 0:
            GPIO.output(LED_PIN3, GPIO.LOW)
        if  event.code == yBtn and event.value == 1:
            GPIO.output(LED_PIN4, GPIO.HIGH)
        if event.code == yBtn and event.value == 0:
            GPIO.output(LED_PIN4, GPIO.LOW)
        if  event.code == rbBtn and event.value == 1:
            GPIO.output(LED_PIN5, GPIO.HIGH)
        if event.code== rbBtn and event.value == 0:
            GPIO.output(LED_PIN5, GPIO.LOW)
        if event.code == lbBtn  and event.value == 1:
            GPIO.output(LED_PIN6, GPIO.HIGH)
        if event.code == lbBtn and event.value == 0:
            GPIO.output(LED_PIN6, GPIO.LOW)