from sx1262 import SX1262
import time

lora = SX1262('P5','P6','P7','P8')

lora.begin()

while True:
    msg, err = lora.recv()
    if len(msg) > 0:
        error = SX1262.ERROR[err]
        print(msg)
        print(error)
