import RPi.GPIO as GPIO
import time

# Set up the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set GPIO pin 17 as output
LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)

# Blink the LED
try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)  # Turn LED on
        time.sleep(1)                    # Wait for 1 second
        GPIO.output(LED_PIN, GPIO.LOW)   # Turn LED off
        time.sleep(1)                    # Wait for 1 second
except KeyboardInterrupt:
    # Clean up GPIO settings on exit
    GPIO.cleanup()
    print("Program exited safely.")
