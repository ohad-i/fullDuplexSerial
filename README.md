# fullDuplexSerial

this repo is an example for full duplex serial implementation in python (is there anything else out there?).
it allows simultaneously read & write from the same serial device.

Just run serM.py twice, onece as sender and once as receiver simultaneously:  
writer:   
    python serM.py -p /dev/ttyUSB0 -b 57600 -w  
reader:   
    python serM.py -p /dev/ttyUSB0 -b 57600  
 
The magic that allows it is the serial port initialization with the flag "exclusive=False" like that:  
   
ser = Serial(port, baud, write_timeout=0, inter_byte_timeout=None, exclusive=False)  
   
thats it... have fun.    

