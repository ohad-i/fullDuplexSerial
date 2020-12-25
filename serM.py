import os
from serial import Serial
import argparse
from select import select
import time


parser = argparse.ArgumentParser(description='Config RFD modem')
parser.add_argument('-p', '--port', default='/dev/ttyUSB0', help='RFD modem port, default: /dev/ttyUSB0')
parser.add_argument('-b', '--baudRate', type=int, default=57600, help='Modem baud rate, default: 57600 ')

args = parser.parse_args()



def sendData(ser, data, chunckSize=200):
    # ChuckSize num of bytes to sen at onece
    # dt synced to baudrate 5[ms]*200[B]=7200[B]=57600[b]
    sent = 0
    while (sent < len(data)):
        sent +=  ser.write(data[sent:sent+chunckSize])
        time.sleep(0.0001)

    return sent





if __name__=='__main__':

    baud = args.baudRate
    port = args.port
    ser = Serial(port, baud, write_timeout=0, inter_byte_timeout=None, exclusive=False)#, timeout=1)
    ser1 = Serial(port, baud, write_timeout=0, inter_byte_timeout=None, exclusive=False)#, timeout=1)
    

    dataSum = int((0.75*baud)//8//2)
    oneSecData = b'ab'*dataSum

    
    tic = time.time()

    dataSum = 0.0
    tic = time.time()
    while True:
        time.sleep(0.0001)
        #dataSum += sendData(ser, oneSecData)
        dataSum += sendData(ser, b'00112233445566'*1)
        if time.time() - tic >= 5:
            bps = (dataSum*8)/(time.time() - tic)
            print('sent bps: %0.2f[bps] effective baud rate: %0.2f'%(bps, bps/baud) ) 
            tic = time.time()
            dataSum = 0.0

    



