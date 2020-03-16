from sx1262 import SX1262
import time

lora = SX1262('P5','P6','P7','P8')

lora.begin()

while True:
    lora.send(b'Hello World!')
    time.sleep(10)
