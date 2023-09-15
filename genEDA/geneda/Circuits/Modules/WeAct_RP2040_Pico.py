from genEDA import *
from Devices.MCU.RP2040 import RP2040

# WeAct RP2040 Pico module RP2040 
class WeAct_RP2040_Pico(RP2040):
    def __init__(self,refid) -> None:
        U.__init__(self,refid)
        self.name = "RP2040"
        self.type = "MCU"
        self.value = ""
        self.pins = [
            Pin( 1,"GP0","I2C0_SDA/SPI0_RX/UART0_TX","IO"),
            Pin( 2,"GP1","I2C0_SCL/SPI0_CSn/UART0_RX","IO"),
            Pin( 3,"GND","GND","POWER"),
            Pin( 4,"GP2","I2C1_SDA/SPI0_SCK","IO"),
            Pin( 5,"GP3","I2C1_SCL/SPI0_TX","IO"),
            Pin( 6,"GP4","I2C0_SDA/SPI0_RX/UART1_TX","IO"),
            Pin( 7,"GP5","I2C0_SCL/SPI0_CSn/UART1_RX","IO"),
            Pin( 8,"GND","GND","POWER"),
            Pin( 9,"GP6","I2C1_SDA/SPI0_SCK","IO"),
            Pin(10,"GP7","I2C1_SCL/SPI0_TX","IO"),
            Pin(11,"GP8","I2C0_SDA/SPI1_RX/UART1_TX","IO"),
            Pin(12,"GP9","I2C0_SCL/SPI1_CSn/UART1_RX","IO"),
            Pin(13,"GND","GND","POWER"),
            Pin(14,"GP10","I2C1_SDA/SPI1_SCK","IO"),
            Pin(15,"GP11","I2C1_SCL/SPI1_TX","IO"),
            Pin(16,"GP12","I2C0_SDA/SPI1_RX/UART0_TX","IO"),
            Pin(17,"GP13","I2C0_SCL/SPI1_CSn/UART0_RX","IO"),
            Pin(18,"GND","GND","POWER"),
            Pin(19,"GP14","I2C1_SDA/SPI1_SCK","IO"),
            Pin(20,"GP15","I2C1_SCL/SPI1_TX","IO"),
            Pin(21,"GP16","I2C0_SDA/SPI0_RX/UART0_TX","IO"),
            Pin(22,"GP17","I2C0_SCL/SPI0_CSn/UART0_RX","IO"),
            Pin(23,"GND","GND","POWER"),
            Pin(24,"GP18","I2C1_SDA/SPI0_SCK","IO"),
            Pin(25,"GP19","I2C1_SCL/SPI0_TX","IO"),
            Pin(26,"GP20","I2C0_SDA","IO"),
            Pin(27,"GP21","I2C0_SCL","IO"),
            Pin(28,"GND","GND","POWER"),
            Pin(29,"GP22","?","IO"),
            Pin(30,"GP26","ADC0/I2C1_SDA","IO"),
            Pin(31,"GP27","ADC1/I2C1_SCL","IO"),
            Pin(32,"GP28","ADC2","IO"),
            Pin(33,"GND","GND","POWER"),
            Pin(34,"GP29","?","IO"),
            Pin(35,"GP35","ADC_VREF","IO"),
            Pin(36,"GP24","?","IO"),
            Pin(37,"3V3","3V3","POWER"),
            Pin(38,"GND","GND","POWER"),
            Pin(39,"VSYS","VSYS","POWER"),
            Pin(40,"VBUS","VBUS","POWER"),
            Pin(41,"GND","GND","POWER"),
            Pin(42,"SWDIO","SWDIO","IO"),
            Pin(43,"SWCLK","SWCLK","IO"),
            Pin(44,"3V3","3V3","POWER"),

        ]