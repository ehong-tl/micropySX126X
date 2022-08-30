# micropySX126X
Semtech SX126X LoRa driver for Micropython and CircuitPython.  
This library is ported and modified from [RadioLib](https://github.com/jgromes/RadioLib) by jgromes.  
This library supports generic and Pycom variant micropython as well as CircuitPython.  
Tested with:
1. WiPy3.0 + Semtech SX1262MB1PAS shield (LoRa)
2. WiPy3.0 + Ebyte E22-400M22S (LoRa)
3. WiPy3.0 + Ebyte E22-400M30S (LoRa) - Built-in 10dB amplifier, eg. SX1268.setOutputPower(20) = 30dBm output, SX1268.setOutputPower(0) = 10 dBm output
4. [LilyGO&#174; T-Echo](https://github.com/lyusupov/POST_TEcho)
5. Raspberry Pi Pico + [Waveshare SX126x Pico LoRa HAT](https://www.waveshare.com/pico-lora-sx1262-868m.htm)

## Constructors (Similar for SX1261 and SX1268)  
***class*** **sx1262.SX1262(spi_bus, clk, mosi, miso, cs, irq, rst, gpio)**  
Create and initialize SX1262 object.

The parameters are:  
- spi_bus : SPI bus ID
- clk : SPI CLK pin
- mosi : SPI MOSI pin
- miso : SPI MISO pin
- cs : NSS pin
- irq : DIO1 pin
- rst : RESET pin
- gpio : BUSY pin

## Methods (Similar for SX1261 and SX1268)  

### General  
**SX1262.setFrequency(freq)**  
Set frequency in MHz.  
Return: Status (Refer to **Constants** Status dictionary)

**SX1262.setOutputPower(power)**  
Set TX power in dBm.  
Return: Status

**SX1262.setBlockingCallback(blocking, callback=None)**  
Set TX/RX blocking mode and interrupt callback.  
If blocking = True, TX/RX is set to blocking mode and callback function will be ignored.  
If blocking = False, TX/RX is set to non blocking mode and callback function will be triggered with events argument upon TX/RX events.  
If callback = None, events callback function will be disabled.

**SX1262.getRSSI()**  
Get RX RSSI in dBm.  
Return: RSSI value

**SX1262.getTimeOnAir(len)**  
Get RX time on air according to message length, len = message length.  
Return: Time on air value

**SX1262.send(data)**  
Send message, data type must be bytes or bytearray.  
Return: Payload length, status

**SX1262.recv(len=0, timeout_en=False, timeout_ms=0)**  
Read RX message.  
len = Message length, if 0, default to SX126X_MAX_PACKET_LENGTH  
timeout_en = Enable RX timeout, if False, function blocking indefinitely until message received (Only in blocking mode)  
timeout_ms = RX timeout in ms, 0 means timeout = 100 LoRa symbols length for LoRa or timeout = 500% expected time-on-air for FSK  (Only in blocking mode)  
Return: Payload, status

### LoRa  
**SX1262.begin(freq=434.0, bw=125.0, sf=9, cr=7, syncWord=0x12, power=14, currentLimit=60.0  
preambleLength=8, implicit=False, implicitLen=0xFF, crcOn=True, txIq=False, rxIq=False,  
tcxoVoltage=1.6, useRegulatorLDO=False, blocking=True)**  
This method is used to set LoRa configuration.

The parameters are:  
- freq : Frequency in MHz
- bw : Bandwidth in kHz
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

Return: Status

**SX1262.setBandwidth(bw)**  
Set LoRa bandwidth in kHz.  
Return: Status

**SX1262.setCodingRate(cr)**  
Set LoRa coding rate, 5 to 8.  
Return: Status

**SX1262.setPreambleLength(preambleLength)**  
Set LoRa preamble length.  
Return: Status

**SX1262.setSpreadingFactor(sf)**  
Set LoRa spreading factor, 5 to 12.  
Return: Status

**SX1262.setSyncWord(syncWord, [controlBits])**  
Set LoRa sync word, private = 0x12, public = 0x34.  
Optional parameter controlBits, default value is 0x44.  
e.g. syncWord = 0xAB, controlBits = 0xCD -> SX126x 2 bytes sync word = 0xACBD  
e.g. syncWord = 0x12, controlBits = 0x44 -> SX126x 2 bytes sync word = 0x1424  
Return: Status

**SX1262.explicitHeader()**  
Enable LoRa explicit header mode.  
Return: Status

**SX1262.implicitHeader(implicitLen)**  
Enable LoRa implicit header mode with implicit length parameter.  
Return: Status

**SX1262.forceLDRO(enable)**  
Force enable Low Data Rate Optimization.  
Return: Status

**SX1262.autoLDRO()**  
Enable auto Low Data Rate Optimization.  
Return: Status

**SX1262.setCRC(crcOn)**  
Set LoRa CRC mode.  
Return: Status

**SX1262.setTxIq(txIq)**  
Set LoRa TX invert IQ mode.

**SX1262.setRxIq(rxIq)**  
Set LoRa RX invert IQ mode.

**SX1262.getSNR()**  
Get LoRa RX SNR in dB.  
Return: SNR value

### FSK  
**SX1262.beginFSK(freq=434.0, br=48.0, freqDev=50.0, rxBw=156.2, power=14, currentLimit=60.0,  
preambleLength=16, dataShaping=0.5, syncWord=[0x2D, 0x01], syncBitsLength=16,  
addrFilter=SX1262.ADDR_FILT_OFF, addr=0x00, crcLength=2, crcInitial=0x1D0F, crcPolynomial=0x1021,  
crcInverted=True, whiteningOn=True, whiteningInitial=0x0100,  
fixedPacketLength=False, packetLength=0xFF, preambleDetectorLength=SX1262.PREAMBLE_DETECT_16,  
tcxoVoltage=1.6, useRegulatorLDO=False,  
blocking=True)**  
This method is used to set FSK configuration.

The parameters are:  
- freq : Frequency in MHz
- br : Bit rate in kbps
- freqDev : Frequency deviation in kHz
- rxBW : RX bandwidth in kHz
- power : TX power in dBm
- currentLimit : Current limit in mA
- preambleLength : Preamble length
- dataShaping : Time-bandwidth product of the Gaussian filter to be used for shaping
- syncWord : Sync word
- syncBitsLength : Sync word length in bit
- addrFilter : Address filtering, refer to **Constants** FSK address filtering
- addr : Address for address filtering
- crcLength : CRC length, 0, 1 or 2
- crcInitial: CRC initial value
- crcPolynomial : Polynomial for CRC calculation
- crcInverted : Invert CRC bytes
- whiteningOn : Enable whitening
- whiteningInitial : Initial value used for whitening LFSR
- fixedPacketLength : Enable fixed packet length mode
- packetLength : Packet length in bytes (fixed packet length mode) or maximum packet length in bytes (variable packet length mode)
- preambleDetectorLength : Minimum preamble detection length, refer to **Constants** FSK preamble detector length
- tcxoVoltage : TCXO input voltage in V
- useRegulatorLDO : Use LDO regulator = True, use DC-DC regulator = False
- blocking : Blocking TX/RX = True, non blocking TX/RX = False

Return: Status

**SX1262.setBitRate(br)**  
Set FSK bit rate in kbps.  
Return: Status

**SX1262.setFrequencyDeviation(freqDev)**  
Set FSK frequency deviation in kHz.  
Return: Status

**SX1262.setRxBandwidth(rxBw)**  
Set FSK RX bandwidth in kHz.  
Return: Status

**SX1262.setDataShaping(dataShaping)**  
Set FSK time-bandwidth product of the Gaussian filter to be used for shaping.  
Return: Status

**SX1262.setSyncBits(syncWord, bitsLen)**  
Set FSK sync word and sync bits length.  
syncWord = Sync word in list  
bitsLen = Sync word bit length  
Return: Status

**SX1262.setPreambleLength(preambleLength)**  
Set FSK preamble length.  
Return: Status

**SX1262.setPreambleDetectorLength(preambleDetectorLength)**  
Set minimum preamble detection length, refer to **Constants** FSK preamble detector length.  

**SX1262.setNodeAddress(addr)**  
Activate address filtering on node address addr.  
Return: Status

**SX1262.setBroadcastAddress(addr)**  
Activate address filtering on node and broadcast address addr.  
Return: Status

**SX1262.disableAddressFiltering()**  
Disable address filtering.  
Return: Status

**SX1262.setCRC(len, initial=0x1D0F, polynomial=0x1021, inverted=True)**  
Set FSK CRC.  
len = CRC length, 0, 1 or 2  
initial = CRC initial  
polynomial = Polynomial used for CRC calculation  
inverted = Enable CRC bytes inversion  
Return: Status

**SX1262.setWhitening(enabled, initial=0x0100)**  
Set FSK whitening.  
initial = Initial value for whitening LFSR  
Return: Status

**SX1262.fixedPacketLengthMode(len)**  
Set FSK fixed packet length mode.  
len = Packet length in bytes  
Return: Status

**SX1262.variablePacketLengthMode(maxLen)**  
Set FSK variable packet length mode.  
maxLen = Max packet length in bytes  
Return: Status

## Constants (Similar for SX1261 and SX1268)  
Events: SX1262.TX_DONE, SX1262.RX_DONE  
FSK address filter: SX1262.ADDR_FILT_OFF, SX1262.ADDR_FILT_NODE, SX1262.ADDR_FILT_NODE_BROAD  
FSK preamble detector length: SX1262.PREAMBLE_DETECT_OFF, SX1262.PREAMBLE_DETECT_X -> X = 8, 16, 24, 32  
Status dictionary: SX1262.STATUS
