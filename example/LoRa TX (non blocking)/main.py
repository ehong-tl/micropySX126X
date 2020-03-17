from sx1262 import SX1262
import time

def cb(events):
    if events & SX1262.TX_DONE:
        print('TX done.')

lora = SX1262('P5','P6','P7','P8')

lora.begin()

lora.setTrigger(True, cb)

while True:
    lora.send(b'Hello World!')
    time.sleep(10)
