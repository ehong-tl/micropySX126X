# micropySX126X
Semtech SX126X LoRa driver for Micropython.  
This micropython library is ported and modified from [RadioLib](https://github.com/jgromes/RadioLib) by jgromes.  
This micropython library supports generic and Pycom variant micropython.  
This micropython library was tested and working with Pycom WiPy 3.0 and SX1262DVK1PAS evaluation board.

## Constructors (Similar for SX1261 and SX1268)  
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
**lora.begin(freq=434.0, bw=125.0, sf=9, cr=7, syncWord=0x12, power=14, currentLimit=60.0  
preambleLength=8, implicit=False, implicitLen=0xFF, crcOn=True, txIq=False, rxIq=False,  
tcxoVoltage=1.6, useRegulatorLDO=False, blocking=True)**  
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
- implicit : Implicit or explicit header, implicit = True
- implicitLen : Implicit header payload length
- crcOn : CRC on or off
- txIq : TX invert IQ
- rxIq : RX invert IQ
- tcxoVoltage : TCXO input voltage in V
- useRegulatorLDO : Use LDO regulator = True, use DC-DC regulator = False
- blocking : Blocking TX/RX = True, non blocking TX/RX = False

Return: Error state (Refer to **Constants** LoRa error dictionary)

**lora.setBandwidth(bw)**  
Set LoRa bandwidth in KHz.  
Return: Error state

**lora.setFrequency(freq)**  
Set LoRa frequency in KHz.  
Return: Error state

**lora.setCodingRate(cr)**  
Set LoRa coding rate, 5 to 8.  
Return: Error state

**lora.setPreambleLength(preambleLength)**  
Set LoRa preamble length.  
Return: Error state

**lora.setSpreadingFactor(sf)**  
Set LoRa spreading factor, 5 to 12.  
Return: Error state

**lora.setOutputPower(power)**  
Set LoRa TX power in dBm.  
Return: Error state

**lora.setSyncWord(syncWord, [controlBits])**  
Set LoRa sync word, private = 0x12, public = 0x34.  
Optional parameter controlBits, default value is 0x44.  
e.g. syncWord = 0xAB, controlBits = 0xCD -> SX126x 2 bytes sync word = 0xACBD  
e.g. syncWord = 0x12, controlBits = 0x44 -> SX126x 2 bytes sync word = 0x1424  
Return: Error state

**lora.explicitHeader()**  
Enable LoRa explicit header mode.  
Return: Error state

**lora.implicitHeader(implicitLen)**  
Enable LoRa implicit header mode with implicit length parameter.  
Return: Error state

**lora.setCRC(crcOn)**  
Set CRC mode.  
Return: Error state

**lora.setTxIq(txIq)**  
Set TX invert IQ mode.  
Return: Error state

**lora.setRxIq(rxIq)**  
Set RX invert IQ mode.  
Return: Error state

**lora.setBlockingCallback(blocking, callback=None)**  
Set TX/RX blocking mode and interrupt callback.  
If blocking = True, TX/RX is set to blocking mode and callback function will be ignored.  
If blocking = False, TX/RX is set to non blocking mode and callback function will be triggered with events argument upon TX/RX events.  
If callback = None, events callback function will be disabled.

**lora.getRSSI()**  
Get LoRa RX RSSI.  
Return: RSSI value

**lora.getSNR()**  
Get LoRa RX SNR.  
Return: SNR value

**lora.getTimeOnAir(len)**  
Get RX time on air according to message length, len = message length.  
Return: Time on air value

**lora.send(data)**  
Send LoRa message, data type must be bytes or bytearray.  
Return: Payload length, error state

**lora.recv([len])**  
Read RX LoRa message, optional parameter len = message length.  
Return: Payload, error state

## Constants (Similar for SX1261 and SX1268)  
LoRa events: SX1262.TX_DONE, SX1262.RX_DONE  
LoRa error dictionary: SX1262.ERROR
