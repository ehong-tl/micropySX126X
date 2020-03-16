# micropySX126X
Micropython library for Semtech SX126X LoRa module.  
This micropython library is ported from [RadioLib](https://github.com/jgromes/RadioLib) by jgromes.  
This library is tested with Pycom WiPy 3.0 and SX1262DVK1PAS dev kit.

## Constructors
**class** sx1262.SX1262(cs, irq, rst, gpio, clk='P10', mosi='P11', miso='P14')  
Create and initialize SX1262 object.

The parameters are:  
- cs : NSS pin
- irq : DIO1 pin
- rst : RESET pin
- gpio : BUSY pin
- CLK : SPI CLK pin
- MOSI : SPI MOSI pin
- MISO : SPI MISO pin

