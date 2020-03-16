# micropySX126X
Micropython library for Semtech SX126X LoRa module.  
This micropython library is ported from [RadioLib](https://github.com/jgromes/RadioLib) by jgromes.  
This library is tested with Pycom WiPy 3.0 and SX1262DVK1PAS dev kit.

## Constructors(Similar for SX1261 and SX1268)  
***class*** **sx1262.SX1262(cs, irq, rst, gpio, clk='P10', mosi='P11', miso='P14')**  
Create and initialize SX1262 object.

The parameters are:  
- cs : NSS pin
- irq : DIO1 pin
- rst : RESET pin
- gpio : BUSY pin
- clk : SPI CLK pin
- mosi : SPI MOSI pin
- miso : SPI MISO pin

lora = sx1262.SX1262('P5','P6','P7','P8')

## Methods (Similar for SX1261 and SX1268)  
**lora.begin(freq=434.0, bw=125.0, sf=9, cr=7, syncWord=SX126X_SYNC_WORD_PRIVATE,  
power=14, currentLimit=60.0, preambleLength=8, tcxoVoltage=1.6, useRegulatorLDO=False)**  
This method is used to set LoRa configuration.

The parameters are:  
- freq : Frequency in KHz
- bw : Bandwidth in KHz
- sf : Spreading factor, 5 to 12
- cr : Coding rate, 5 to 8
- syncWord : Sync word, private = 0x12, public = 0x34
- power : TX power in dBm
- currentLimit : Current limit in mA
- preambleLength : Preamble length
- tcxoVoltage : TCXO input voltage in V
- useRegulatorLDO : Use LDO regulator = True, use DC-DC regulator = False

**lora.setBandwidth([bw])**  
Set LoRa bandwidth in KHz.
