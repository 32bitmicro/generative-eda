
from genEDA import *

# [Datasheet](https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf)

#1.4.3. GPIO Functions
#Each individual GPIO pin can be connected to an internal peripheral via the GPIO functions defined below. Some internal
#peripheral connections appear in multiple places to allow some system level flexibility. SIO, PIO0 and PIO1 can connect
#to all GPIO pins and are controlled by software (or software controlled state machines) so can be used to implement
# many functions.

#Table 2. General Purpose Input/Output (GPIO) Bank 0 Functions
GPIO_Functions="""
GPIO    F1          F2          F3          F4          F5          F6          F7          F8              F9
0       SPI0 RX     UART0 TX    I2C0 SDA    PWM0 A      SIO         PIO0        PIO1                        USB OVCUR DET
1       SPI0 CSn    UART0 RX    I2C0 SCL    PWM0 B      SIO         PIO0        PIO1                        USB VBUS DET
2       SPI0 SCK    UART0 CTS   I2C1 SDA    PWM1 A      SIO         PIO0        PIO1                        USB VBUS EN
3       SPI0 TX     UART0 RTS   I2C1 SCL    PWM1 B      SIO         PIO0        PIO1                        USB OVCUR DET
4       SPI0 RX     UART1 TX    I2C0 SDA    PWM2 A      SIO         PIO0        PIO1                        USB VBUS DET
5       SPI0 CSn    UART1 RX    I2C0 SCL    PWM2 B      SIO         PIO0        PIO1                        USB VBUS EN
6       SPI0 SCK    UART1 CTS   I2C1 SDA    PWM3 A      SIO         PIO0        PIO1                        USB OVCUR DET
7       SPI0 TX     UART1 RTS   I2C1 SCL    PWM3 B      SIO         PIO0        PIO1                        USB VBUS DET
8       SPI1 RX     UART1 TX    I2C0 SDA    PWM4 A      SIO         PIO0        PIO1                        USB VBUS EN
9       SPI1 CSn    UART1 RX    I2C0 SCL    PWM4 B      SIO         PIO0        PIO1                        USB OVCUR DET
10      SPI1 SCK    UART1 CTS   I2C1 SDA    PWM5 A      SIO         PIO0        PIO1                        USB VBUS DET
11      SPI1 TX     UART1 RTS   I2C1 SCL    PWM5 B      SIO         PIO0        PIO1                        USB VBUS EN
12      SPI1 RX     UART0 TX    I2C0 SDA    PWM6 A      SIO         PIO0        PIO1                        USB OVCUR DET
13      SPI1 CSn    UART0 RX    I2C0 SCL    PWM6 B      SIO         PIO0        PIO1                        USB VBUS DET
14      SPI1 SCK    UART0 CTS   I2C1 SDA    PWM7 A      SIO         PIO0        PIO1                        USB VBUS EN
15      SPI1 TX     UART0 RTS   I2C1 SCL    PWM7 B      SIO         PIO0        PIO1                        USB OVCUR DET
16      SPI0 RX     UART0 TX    I2C0 SDA    PWM0 A      SIO         PIO0        PIO1                        USB VBUS DET
17      SPI0 CSn    UART0 RX    I2C0 SCL    PWM0 B      SIO         PIO0        PIO1                        USB VBUS EN
18      SPI0 SCK    UART0 CTS   I2C1 SDA    PWM1 A      SIO         PIO0        PIO1                        USB OVCUR DET
19      SPI0 TX     UART0 RTS   I2C1 SCL    PWM1 B      SIO         PIO0        PIO1                        USB VBUS DET
20      SPI0 RX     UART1 TX    I2C0 SDA    PWM2 A      SIO         PIO0        PIO1        CLOCK GPIN0     USB VBUS EN
21      SPI0 CSn    UART1 RX    I2C0 SCL    PWM2 B      SIO         PIO0        PIO1        CLOCK GPOUT0    USB OVCUR DET
22      SPI0 SCK    UART1 CTS   I2C1 SDA    PWM3 A      SIO         PIO0        PIO1        CLOCK GPIN1     USB VBUS DET
23      SPI0 TX     UART1 RTS   I2C1 SCL    PWM3 B      SIO         PIO0        PIO1        CLOCK GPOUT1    USB VBUS EN
24      SPI1 RX     UART1 TX    I2C0 SDA    PWM4 A      SIO         PIO0        PIO1        CLOCK GPOUT2    USB OVCUR DET
25      SPI1 CSn    UART1 RX    I2C0 SCL    PWM4 B      SIO         PIO0        PIO1        CLOCK GPOUT3    USB VBUS DET
26      SPI1 SCK    UART1 CTS   I2C1 SDA    PWM5 A      SIO         PIO0        PIO1                        USB VBUS EN
27      SPI1 TX     UART1 RTS   I2C1 SCL    PWM5 B      SIO         PIO0        PIO1                        USB OVCUR DET
28      SPI1 RX     UART0 TX    I2C0 SDA    PWM6 A      SIO         PIO0        PIO1                        USB VBUS DET
29      SPI1 CSn    UART0 RX    I2C0 SCL    PWM6 B      SIO         PIO0        PIO1                        USB VBUS EN
"""

"""
1.4.2. Pin Descriptions Table 1. The function of each pin is briefly described here. 
Fullelectricalspecifications can be found in Chapter 5. Name Description

GPIOx       General-purpose digital input and output. RP2040 can connect one of a number of internal
            peripherals to each GPIO, or control GPIOs directly from software.

GPIOx/ADCy  General-purpose digital input and output, with analogue-to-digital converter function. The RP2040
            ADC has an analogue multiplexer which can select any one of these pins, and sample the voltage.

QSPIx       Interface to a SPI, Dual-SPI or Quad-SPI flash device, with execute-in-place support. These pins can
            also be used as software-controlled GPIOs, if they are not required for flash access.

USB_DM      and
USB_DP
            USB controller, supporting Full Speed device and Full/Low Speed host. A 27Ω series termination
            resistor is required on each pin, but bus pullups and pulldowns are provided internally.

XIN and XOUT 
            Connect a crystal to RP2040’s crystal oscillator. XIN can also be used as a single-ended CMOS
            clock input, with XOUT disconnected. The USB bootloader requires a 12MHz crystal or 12MHz
            clock input.

RUN         Global asynchronous reset pin. Reset when driven low, run when driven high. If no external reset is
            required, this pin can be tied directly to IOVDD.

SWCLK and
SWDIO
            Access to the internal Serial Wire Debug multi-drop bus. Provides debug access to both
            processors, and can be used to download code.

TESTEN      Factory test mode pin. Tie to GND.

GND         Single external ground connection, bonded to a number of internal ground pads on the RP2040 die.

IOVDD       Power supply for digital GPIOs, nominal voltage 1.8V to 3.3V
"""

class RP2040(U):
    def __init__(self,refid) -> None:
        U.__init__(self,refid)
        self.name = "RP2040"
        self.type = "MCU"
        self.value = ""
        self.pins = [
            Pin( 1,"IOVDD","","POWER"),
            Pin( 2,"GPIO0","","IO"),
            Pin( 3,"GPIO1","","IO"),
            Pin( 4,"GPIO2","","IO"),
            Pin( 5,"GPIO3","","IO"),
            Pin( 6,"GPIO4","","IO"),
            Pin( 7,"GPIO5","","IO"),
            Pin( 8,"GPIO6","","IO"),
            Pin( 9,"GPIO7","","IO"),
            Pin(10,"IOVDD","","POWER"),
            Pin(11,"GPIO8","","IO"),
            Pin(12,"GPIO9","","IO"),
            Pin(13,"GPIO10","","IO"),
            Pin(14,"GPIO11","","IO"),
            Pin(15,"GPIO12","","IO"),
            Pin(16,"GPIO13","","IO"),
            Pin(17,"GPIO14","","IO"),
            Pin(18,"GPIO15","","IO"),
            Pin(19,"TESTEN","","SYSTEM"),
            Pin(20,"XIN","","SYSTEM"),
            Pin(21,"XOUT","","SYSTEM"),
            Pin(22,"IOVDD","","POWER"),
            Pin(23,"DVDD","","POWER"),
            Pin(24,"SWCLK","","IO/SWD"),
            Pin(25,"SWDIO","","IO/SWD"),
            Pin(26,"RUN","","SYSTEM"),
            Pin(27,"GPIO16","","IO"),
            Pin(28,"GPIO17","","IO"),
            Pin(29,"GPIO18","","IO"),
            Pin(30,"GPIO19","","IO"),
            Pin(31,"GPIO20","","IO"),
            Pin(32,"GPIO21","","IO"),
            Pin(33,"IOVDD","","POWER"),
            Pin(34,"GPIO22","","IO"),
            Pin(35,"GPIO23","","IO"),
            Pin(36,"GPIO24","","IO"),
            Pin(37,"GPIO25","","IO"),
            Pin(38,"GPIO26/ADC0","","IO/AIO"),
            Pin(39,"GPIO27/ADC1","","IO/AIO"),
            Pin(40,"GPIO28/ADC2","","IO/AIO"),
            Pin(41,"GPIO29/ADC3","","IO/AIO"),
            Pin(42,"IOVDD","","POWER"),
            Pin(43,"ADC_AVDD","","POWER"),
            Pin(44,"VREG_VIN","","POWER"),
            Pin(45,"VREG_VOUT","","POWER"),
            Pin(46,"USB_DM","","USB"),
            Pin(47,"USB_DP","","USB"),
            Pin(48,"USB_VDD","","POWER"),
            Pin(49,"IOVDD","","POWER"),
            Pin(50,"DVDD","","POWER"),
            Pin(51,"QSPI_SD3","","SPI"),
            Pin(52,"QSPI_SCLK","","SPI"),
            Pin(53,"QSPI_SD0","","SPI"),
            Pin(54,"QSPI_SD2","","SPI"),
            Pin(55,"QSPI_SD1","","SPI"),
            Pin(56,"QSPI_SS_N","","SPI"),
        ]
