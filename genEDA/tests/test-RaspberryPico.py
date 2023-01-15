import sys
 
# setting path
sys.path.append('../src')

from genEDA import *
from Devices.MCU.RP2040 import RP2040
from Circuits.Modules.RaspberryPico import RaspberryPico

# modules
RaspberryPico = RaspberryPico('U1')

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

def showDevices(mod):
    for d in mod.devices:
        showDevice(d)
    pass

def unittestRaspberryPicoModule():
    global RaspberryPico

    showDevices(RaspberryPico)



if __name__ == '__main__':
    unittestRaspberryPicoModule()
