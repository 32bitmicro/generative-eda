import sys
 
# setting path
sys.path.append('../src')

from genEDA import *
from Devices.MCU.RP2040 import RP2040

# devices
RP2040 = RP2040('U1')

def showPins(pins):
    print('pins:')
    for p in pins:
        print(' ',p.idx,p.name)

def showDevice(dev):
    print()
    print('-------')
    print('device: ')
    print('refid:  ' + dev.refid)
    print('name:   ' + dev.name)
    print('type:   ' + dev.type)
    showPins(dev.pins)
    print('value:  ' + str(dev.value))
    print()

def unittestRP2040Device():
    global RP2040

    showDevice(RP2040)



if __name__ == '__main__':
    unittestRP2040Device()
