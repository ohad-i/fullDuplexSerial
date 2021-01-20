# fullDuplexSerial

this repo is an example for full duplex serial implementation in python (is there anything else out there?).
it allows simultaneously read & write from the same serial device.

Just run serM.py twice, onece as sender and once as receiver simultaneously:
writer: 
    python serM.py -p /dev/ttyUSB0 -b 57600 -w
reader: 
    python serM.py -p /dev/ttyUSB0 -b 57600
    
 
 thats it... have fun.
