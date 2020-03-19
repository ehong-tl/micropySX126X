from sx1262 import SX1262
import time

def cb(events):
    if events & SX1262.RX_DONE:
        msg, err = lora.recv()
        error = SX1262.ERROR[err]
        print(msg)
        print(error)

lora = SX1262(cs='P5',irq='P6',rst='P7',gpio='P8')

lora.begin(freq=923, bw=500.0, sf=12, cr=8, syncWord=0x12,
           power=-5, currentLimit=60.0, preambleLength=8,
           implicit=False, implicitLen=0xFF,
           crcOn=True, txIq=False, rxIq=False,
           tcxoVoltage=1.7, useRegulatorLDO=False, blocking=True)

lora.setBlockingCallback(False, cb)
