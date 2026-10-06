# Note: This program was written based on the Lab 3 pin configuration
# and expected behavior, but was not hardware-tested because Pico access
# was unavailable.

from machine import Pin
import time

# Set up LED and button
led = Pin(18, Pin.OUT)
button = Pin(22, Pin.IN, Pin.PULL_DOWN)

# LED starts off
led_state = 0
led.value(led_state)

while True:
    if button.value() == 1:
        # Toggle the LED state
        led_state = not led_state
        led.value(led_state)

        # Simple debounce delay
        time.sleep_ms(200)

        # Wait until the button is released
        while button.value() == 1:
            pass

        # wSmall delay to avoid release bounce
        time.sleep_ms(50)
        