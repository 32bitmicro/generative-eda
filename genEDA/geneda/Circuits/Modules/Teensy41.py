from genEDA import *
from Devices.MCU.MIMXRT1062 import MIMXRT1062

#Pin	Name	    GPIO	Serial	        I2C	        SPI	            PWM	        CAN	    Audio	XBAR	FlexIO	Analog	SD/CSI/LCD
# 1	    AD_B0_02	1.02	Serial1(6) TX		        SPI1(3) MISO	PWM1_X0	    2_TX		    IO-16			
# 0	    AD_B0_03	1.03	Serial1(6) RX		        SPI1(3) CS0	    PWM1_X1	    2_RX		    IO-17			
#24/A10	AD_B0_12	1.12	Serial6(1) TX	Wire2(4) SCL		        PWM1_X2					                    A1:1  	
#25/A11	AD_B0_13	1.13	Serial6(1) RX	Wire2(4) SDA		        PWM1_X3	    GPT1_CLK				        A1:2	
#19/A5	AD_B1_00	1.16	Serial3(2) CTS	Wire(1) SCL		            QT3_0				                3:0	    A1:5, A2:5	
#18/A4	AD_B1_01	1.17	Serial3(2) RTS	Wire(1) SDA		            QT3_1				                3:1	    A1:6, A2:6	
#14/A0	AD_B1_02	1.18	Serial3(2) TX			                    QT3_2		        SPDIF_OUT		3:2	    A1:7, A2:7	
#15/A1	AD_B1_03	1.19	Serial3(2) RX			                    QT3_3		        SPDIF_IN		3:3	    A1:8, A2:8	
#40/A16	AD_B1_04 	1.20								3:4	A1:9,A2:9	USDHC2_DATA0
#41/A17	AD_B1_05 	1.21				GPT2_1				3:5	A1:10,A2:10	USDHC2_DATA1
#17/A3	AD_B1_06	1.22	Serial4(3) TX	Wire1(3) SDA				SPDIF_LOCK		3:6	A1:11, A2:11	USDHC2_DATA2
#16/A2	AD_B1_07	1.23	Serial4(3) RX	Wire1(3) SCL				SPDIF_EXTCLK		3:7	A1:12, A2:12	USDHC2_DATA3
#22/A8	AD_B1_08	1.24				PWM4_A0	1_TX			3:8	A1:13, A2:13	USDHC2_CMD
#23/A9	AD_B1_09	1.25				PWM4_A1	1_RX	1:MCLK		3:9	A1:14, A2:14	USDHC2_CLK
#20/A6	AD_B1_10	1.26	Serial5(8) TX					1:RX_SYNC		3:10	A1:15, A2:15	
#21/A7	AD_B1_11	1.27	Serial5(8) RX					1:RX_BCLK		3:11	A1:0, A2:0	
#38/A14	AD_B1_12 	1.28			SPI1(3) CS0 			1:rx_data 		3:12	A2:1	
#39/A5	AD_B1_13 	1.29			SPI1(3) MISO			1:tx_data 		3:13	A2:2	
#26/A12	AD_B1_14	1.30			SPI1(3) MOSI			1:TX_BCLK		3:14	A2:3  	
#27/A13	AD_B1_15	1.31			SPI1(3) SCK			1:TX_SYNC		3:15	A2:4  	
#10	    B0_00	    2.00			SPI(4) CS0	QT1_0		MQS_RIGHT		2:0     		
#12	    B0_01	    2.01			SPI(4) MISO	QT1_1		MQS_LEFT		2:1     		
#11	    B0_02	    2.02			SPI(4) MOSI	QT1_2	1_TX			2:2		
#13	    B0_03	    2.03			SPI(4) SCK	QT2_0	1_RX			2:3		
# 6	    B0_10	    2.10				PWM2_A2, QT4_1		1:TX3_RX1		2:10		
# 9	    B0_11	    2.11				PWM2_B2,QT4_2		1:TX2_RX2		2:11		
#32	    B0_12	    2.12						1:TX1_RX3	IO-10	2:12		
# 8	    B1_00	    2.16	Serial2(4) TX			PWM1_A3		1:RX_DATA	IO-14	2:16, 3:16		
# 7	    B1_01	    2.17	Serial2(4) RX			PWM1_B3		1:TX_DATA	IO-15	2:17, 3:17		
#36	    B1_02    	2.18			SPI(4) CS2 	PWM2_A3		1:TX_BCLK 	IO-16	2:18,3:18		
#37	    B1_03    	2.19			SPI(4) CS1 	PWM2_B3		1:TX_SYNC 	IO-17	2:19,3:19		
#35	    B1_12    	2.28	Serial8(5) TX							2:28,3:28		
#34	    B1_13    	2.29	Serial8(5) RX							2:29,3:29		
#45	    SD_B0_00	3.12		Wire1(3) SCL	SPI2(1) SCK	PWM1_A0			IO-04			CMD
#44	    SD_B0_01	3.13		Wire1(3) SDA	SPI2(1) CS0	PWM1_B0			IO-05			CLK
#43	    SD_B0_02	3.14	Serial5(8) CTS		SPI2(1) MOSI	PWM1_A1			IO-06			DATA0
#42	    SD_B0_03	3.15	Serial5(8) RTS		SPI2(1) MISO	PWM1_B1			IO-07			DATA1
#47	    SD_B0_04	3.16	Serial5(8) TX		FLEXSPI B_SSO_B	PWM1_A2			IO-08			DATA2
#46	    SD_B0_05	3.17	Serial5(8) RX		FLEXSPI B_DQS	PWM1_B2			IO-09			DATA3
#28	    EMC_32	    3.18	Serial7(7) RX			PWM3_B1						
#31	    EMC_36	    3.22				GPT1_2	3_TX	3:TX_DATA	IO-22			
#30	    EMC_37	    3.23				GPT1_3 	3_RX	3:MCLK	IO-23			
# 2	    EMC_04	    4.04				PWM4_A2		2:TX_DATA	IO-06	1:4		
# 3	    EMC_05	    4.05				PWM4_B2		2:TX_SYNC	IO-07	1:5		
# 4	    EMC_06	    4.06				PWM2_A0		2:TX_BCLK	IO-08	1:6		
#33	    EMC_07	    4.07				PWM2_B0		2:MCLK	IO-09	1:7		
#5	    EMC_08	    4.08				PWM2_A1		2:RX_DATA	IO-17	1:8		
#51	    EMC_22	    4.22		Wire1(3) SCL	FLEXSPI2_A_SS1_B	PWM3_B3, QT2_3						
#48	    EMC_24	    4.24	Serial8(5) RX 		FLEXSPI2_A_SS0_B	PWM1_B0						
#53	    EMC_25	    4.25	Serial1(6) TX 		FLEXSPI2_A_SCLK	PWM1_A1						
#52	    EMC_26	    4.26	Serial1(6) RX 		FLEXSPI2_A_DATA00	PWM1_B1				1:12		
#49	    EMC_27	    4.27	Serial8(5) RTS		FLEXSPI2_A_DATA01, SPI2(1) SCK  	PWM1_A2				1:13		
#50	    EMC_28	    4.28	Serial8(5) CTS		FLEXSPI2_A_DATA02, SPI2(1) MOSI	PWM1_B2				1:14		
#54	    EMC_29	    4.29	Serial1(6) RTS		FLEXSPI2_A_DATA03, SPI2(1) MISO	PWM3_A0				1:15		
#29	    EMC_31	    4.31	Serial7(7) TX		SPI2(1) CS1	PWM3_A1						

# Sorted
# Pin	Name	    GPIO	Serial	        I2C	        SPI	            PWM	        CAN	    Audio	XBAR	FlexIO	Analog	SD/CSI/LCD
# 0	    AD_B0_03	1.03	Serial1(6) RX		        SPI1(3) CS0	    PWM1_X1	    2_RX		    IO-17			
# 1	    AD_B0_02	1.02	Serial1(6) TX		        SPI1(3) MISO	PWM1_X0	    2_TX		    IO-16			
# 2	    EMC_04	    4.04				PWM4_A2		2:TX_DATA	IO-06	1:4		
# 3	    EMC_05	    4.05				PWM4_B2		2:TX_SYNC	IO-07	1:5		
# 4	    EMC_06	    4.06				PWM2_A0		2:TX_BCLK	IO-08	1:6		
# 5	    EMC_08	    4.08				PWM2_A1		2:RX_DATA	IO-17	1:8		
# 6	    B0_10	    2.10				PWM2_A2, QT4_1		1:TX3_RX1		2:10		
# 7	    B1_01	    2.17	Serial2(4) RX			PWM1_B3		1:TX_DATA	IO-15	2:17, 3:17		
# 8	    B1_00	    2.16	Serial2(4) TX			PWM1_A3		1:RX_DATA	IO-14	2:16, 3:16		
# 9	    B0_11	    2.11				PWM2_B2, QT4_2		1:TX2_RX2		2:11		
# 10	B0_00	    2.00			SPI(4) CS0	QT1_0		MQS_RIGHT		2:0     		
# 11	B0_02	    2.02			SPI(4) MOSI	QT1_2	1_TX			2:2		
# 12	B0_01	    2.01			SPI(4) MISO	QT1_1		MQS_LEFT		2:1     		
# 13	B0_03	    2.03			SPI(4) SCK	QT2_0	1_RX			2:3		
# 14/A0	AD_B1_02	1.18	Serial3(2) TX			                    QT3_2		        SPDIF_OUT		3:2	    A1:7, A2:7	
# 15/A1	AD_B1_03	1.19	Serial3(2) RX			                    QT3_3		        SPDIF_IN		3:3	    A1:8, A2:8	
# 16/A2	AD_B1_07	1.23	Serial4(3) RX	Wire1(3) SCL				SPDIF_EXTCLK		3:7	A1:12, A2:12	USDHC2_DATA3
# 17/A3	AD_B1_06	1.22	Serial4(3) TX	Wire1(3) SDA				SPDIF_LOCK		3:6	A1:11, A2:11	USDHC2_DATA2
# 18/A4	AD_B1_01	1.17	Serial3(2) RTS	Wire(1) SDA		            QT3_1				                3:1	    A1:6, A2:6	
# 19/A5	AD_B1_00	1.16	Serial3(2) CTS	Wire(1) SCL		            QT3_0				                3:0	    A1:5, A2:5	
# 20/A6	AD_B1_10	1.26	Serial5(8) TX					1:RX_SYNC		3:10	A1:15, A2:15	
# 21/A7	AD_B1_11	1.27	Serial5(8) RX					1:RX_BCLK		3:11	A1:0, A2:0	
# 22/A8	AD_B1_08	1.24				PWM4_A0	1_TX			3:8	A1:13, A2:13	USDHC2_CMD
# 23/A9	AD_B1_09	1.25				PWM4_A1	1_RX	1:MCLK		3:9	A1:14, A2:14	USDHC2_CLK
#24/A10	AD_B0_12	1.12	Serial6(1) TX	Wire2(4) SCL		        PWM1_X2					                    A1:1  	
#25/A11	AD_B0_13	1.13	Serial6(1) RX	Wire2(4) SDA		        PWM1_X3	    GPT1_CLK				        A1:2	
#26/A12	AD_B1_14	1.30			SPI1(3) MOSI			1:TX_BCLK		3:14	A2:3  	
#27/A13	AD_B1_15	1.31			SPI1(3) SCK			1:TX_SYNC		3:15	A2:4  	
#28	    EMC_32	    3.18	Serial7(7) RX			PWM3_B1						
#29	    EMC_31	    4.31	Serial7(7) TX		SPI2(1) CS1	PWM3_A1						
#30	    EMC_37	    3.23				GPT1_3 	3_RX	3:MCLK	IO-23			
#31	    EMC_36	    3.22				GPT1_2	3_TX	3:TX_DATA	IO-22			
#32	    B0_12	    2.12						1:TX1_RX3	IO-10	2:12		
#33	    EMC_07	    4.07				PWM2_B0		2:MCLK	IO-09	1:7		
#34	    B1_13    	2.29	Serial8(5) RX							2:29,3:29		
#35	    B1_12    	2.28	Serial8(5) TX							2:28,3:28		
#36	    B1_02    	2.18			SPI(4) CS2 	PWM2_A3		1:TX_BCLK 	IO-16	2:18,3:18		
#37	    B1_03    	2.19			SPI(4) CS1 	PWM2_B3		1:TX_SYNC 	IO-17	2:19,3:19		
#38/A14	AD_B1_12 	1.28			SPI1(3) CS0 			1:rx_data 		3:12	A2:1	
#39/A15	AD_B1_13 	1.29			SPI1(3) MISO			1:tx_data 		3:13	A2:2	
#40/A16	AD_B1_04 	1.20								3:4	A1:9,A2:9	USDHC2_DATA0
#41/A17	AD_B1_05 	1.21				GPT2_1				3:5	A1:10,A2:10	USDHC2_DATA1
#42	    SD_B0_03	3.15	Serial5(8) RTS		SPI2(1) MISO	PWM1_B1			IO-07			DATA1
#43	    SD_B0_02	3.14	Serial5(8) CTS		SPI2(1) MOSI	PWM1_A1			IO-06			DATA0
#44	    SD_B0_01	3.13		Wire1(3) SDA	SPI2(1) CS0	PWM1_B0			IO-05			CLK
#45	    SD_B0_00	3.12		Wire1(3) SCL	SPI2(1) SCK	PWM1_A0			IO-04			CMD
#46	    SD_B0_05	3.17	Serial5(8) RX		FLEXSPI B_DQS	PWM1_B2			IO-09			DATA3
#47	    SD_B0_04	3.16	Serial5(8) TX		FLEXSPI B_SSO_B	PWM1_A2			IO-08			DATA2
#48	    EMC_24	    4.24	Serial8(5) RX 		FLEXSPI2_A_SS0_B	PWM1_B0						
#49	    EMC_27	    4.27	Serial8(5) RTS		FLEXSPI2_A_DATA01, SPI2(1) SCK  	PWM1_A2				1:13		
#50	    EMC_28	    4.28	Serial8(5) CTS		FLEXSPI2_A_DATA02, SPI2(1) MOSI	PWM1_B2				1:14		
#51	    EMC_22	    4.22		Wire1(3) SCL	FLEXSPI2_A_SS1_B	PWM3_B3, QT2_3						
#52	    EMC_26	    4.26	Serial1(6) RX 		FLEXSPI2_A_DATA00	PWM1_B1				1:12		
#53	    EMC_25	    4.25	Serial1(6) TX 		FLEXSPI2_A_SCLK	PWM1_A1						
#54	    EMC_29	    4.29	Serial1(6) RTS		FLEXSPI2_A_DATA03, SPI2(1) MISO	PWM3_A0				1:15		



# Teensy4 module MIMXRT1062
class Teensy41(Circuit):
    def __init__(self,refid) -> None:
        U.__init__(self,refid)
        self.name = "Teensy4"
        self.type = "Module"
        self.value = ""
        U1 = MIMXRT1062('U')
        self.devices = [ U1 ]
        pins = [
            Pin(0, "AD_B0_03", "Serial1(6) RX, SPI1(3) CS0, PWM1_X1, 2_RX, IO-17", "IO"),
            Pin(1, "AD_B0_02", "Serial1(6) TX, SPI1(3) MISO, PWM1_X0, 2_TX, IO-16", "IO"),
            Pin(2, "EMC_04", "PWM4_A2, 2:TX_DATA, IO-06, 1:4", "IO"),
            Pin(3, "EMC_05", "PWM4_B2, 2:TX_SYNC, IO-07, 1:5", "IO"),
            Pin(4, "EMC_06", "PWM2_A0, 2:TX_BCLK, IO-08, 1:6", "IO"),
            Pin(5, "EMC_08", "PWM2_A1, 2:RX_DATA, IO-17, 1:8", "IO"),
            Pin(6, "B0_10", "PWM2_A2, QT4_1, 1:TX3_RX1, 2:10", "IO"),
            Pin(7, "B1_01", "Serial2(4) RX, PWM1_B3, 1:TX_DATA, IO-15, 2:17, 3:17", "IO"),
            Pin(8, "B1_00", "Serial2(4) TX, PWM1_A3, 1:RX_DATA, IO-14, 2:16, 3:16", "IO"),
            Pin(9, "B0_11", "PWM2_B2, QT4_2, 1:TX2_RX2, 2:11", "IO"),
            Pin(10, "B0_00", "SPI(4) CS0, QT1_0, MQS_RIGHT, 2:0", "IO"),
            Pin(11, "B0_02", "SPI(4) MOSI, QT1_2, 1_TX, 2:2", "IO"),
            Pin(12, "B0_01", "SPI(4) MISO, QT1_1, MQS_LEFT, 2:1", "IO"),
            Pin(13, "B0_03", "SPI(4) SCK, QT2_0, 1_RX, 2:3", "IO"),
            Pin(14, "AD_B1_02", "Serial3(2) TX, QT3_2, SPDIF_OUT, 3:2, A1:7, A2:7", "IO"),
            Pin(15, "AD_B1_03", "Serial3(2) RX, QT3_3, SPDIF_IN, 3:3, A1:8, A2:8", "IO"),
            Pin(16, "AD_B1_07", "Serial4(3) RX, Wire1(3) SCL, SPDIF_EXTCLK, 3:7, A1:12, A2:12, USDHC2_DATA3", "IO"),
            Pin(17, "AD_B1_06", "Serial4(3) TX, Wire1(3) SDA, SPDIF_LOCK, 3:6, A1:11, A2:11, USDHC2_DATA2", "IO"),
            Pin(18, "AD_B1_01", "Serial3(2) RTS, Wire(1) SDA, QT3_1, 3:1, A1:6, A2:6", "IO"),
            Pin(19, "AD_B1_00", "Serial3(2) CTS, Wire(1) SCL, QT3_0, 3:0, A1:5, A2:5", "IO"),
            Pin(20, "AD_B1_10", "Serial5(8) TX, 1:RX_SYNC, 3:10, A1:15, A2:15", "IO"),
            Pin(21, "AD_B1_11", "Serial5(8) RX, 1:RX_BCLK, 3:11, A1:0, A2:0", "IO"),
            Pin(22, "AD_B1_08", "PWM4_A0, 1_TX, 3:8, A1:13, A2:13, USDHC2_CMD", "IO"),
            Pin(23, "AD_B1_09", "PWM4_A1, 1_RX, 1:MCLK, 3:9, A1:14, A2:14, USDHC2_CLK", "IO"),
            Pin(24, "AD_B0_12", "Serial6(1) TX, Wire2(4) SCL, PWM1_X2, A1:1", "IO"),
            Pin(25, "AD_B0_13", "Serial6(1) RX, Wire2(4) SDA, PWM1_X3, GPT1_CLK, A1:2", "IO"),
            Pin(26, "AD_B1_14", "SPI1(3) MOSI, 1:TX_BCLK, 3:14, A2:3", "IO"),
            Pin(27, "AD_B1_15", "SPI1(3) SCK, 1:TX_SYNC, 3:15, A2:4", "IO"),
            Pin(28, "EMC_32", "Serial7(7) RX, PWM3_B1", "IO"),
            Pin(29, "EMC_31", "Serial7(7) TX, SPI2(1) CS1, PWM3_A1", "IO"),
            Pin(30, "EMC_37", "GPT1_3, 3_RX, 3:MCLK, IO-23", "IO"),
            Pin(31, "EMC_36", "GPT1_2, 3_TX, 3:TX_DATA, IO-22", "IO"),
            Pin(32, "B0_12", "1:TX1_RX3, IO-10, 2:12", "IO"),
            Pin(33, "EMC_07", "PWM2_B0, 2:MCLK, IO-09, 1:7", "IO"),
            Pin(34, "B1_13", "Serial8(5) RX, 2:29, 3:29", "IO"),
            Pin(35, "B1_12", "Serial8(5) TX, 2:28, 3:28", "IO"),
            Pin(36, "B1_02", "SPI(4) CS2, PWM2_A3, 1:TX_BCLK, IO-16, 2:18, 3:18", "IO"),
            Pin(37, "B1_03", "SPI(4) CS1, PWM2_B3, 1:TX_SYNC, IO-17, 2:19, 3:19", "IO"),
            Pin(38, "AD_B1_12", "SPI1(3) CS0, 1:rx_data, 3:12, A2:1", "IO"),
            Pin(39, "AD_B1_13", "SPI1(3) MISO, 1:tx_data, 3:13, A2:2", "IO"),
            Pin(40, "AD_B1_04", "3:4, A1:9, A2:9, USDHC2_DATA0", "IO"),
            Pin(41, "AD_B1_05", "GPT2_1, 3:5, A1:10, A2:10, USDHC2_DATA1", "IO"),
            Pin(42, "SD_B0_03", "Serial5(8) RTS, SPI2(1) MISO, PWM1_B1, IO-07, DATA1", "IO"),
            Pin(43, "SD_B0_02", "Serial5(8) CTS, SPI2(1) MOSI, PWM1_A1, IO-06, DATA0", "IO"),
            Pin(44, "SD_B0_01", "Wire1(3) SDA, SPI2(1) CS0, PWM1_B0, IO-05, CLK", "IO"),
            Pin(45, "SD_B0_00", "Wire1(3) SCL, SPI2(1) SCK, PWM1_A0, IO-04, CMD", "IO"),
            Pin(46, "SD_B0_05", "Serial5(8) RX, FLEXSPI B_DQS, PWM1_B2, IO-09, DATA3", "IO"),
            Pin(47, "SD_B0_04", "Serial5(8) TX, FLEXSPI B_SSO_B, PWM1_A2, IO-08, DATA2", "IO"),
            Pin(48, "EMC_24", "Serial8(5) RX, FLEXSPI2_A_SS0_B, PWM1_B0", "IO"),
            Pin(49, "EMC_27", "Serial8(5) RTS, FLEXSPI2_A_DATA01, SPI2(1) SCK, PWM1_A2, 1:13", "IO"),
            Pin(50, "EMC_28", "Serial8(5) CTS, FLEXSPI2_A_DATA02, SPI2(1) MOSI, PWM1_B2, 1:14", "IO"),
            Pin(51, "EMC_22", "Wire1(3) SCL, FLEXSPI2_A_SS1_B, PWM3_B3, QT2_3", "IO"),
            Pin(52, "EMC_26", "Serial1(6) RX, FLEXSPI2_A_DATA00, PWM1_B1, 1:12", "IO"),
            Pin(53, "EMC_25", "Serial1(6) TX, FLEXSPI2_A_SCLK, PWM1_A1", "IO"),
            Pin(54, "EMC_29", "Serial1(6) RTS, FLEXSPI2_A_DATA03, SPI2(1) MISO, PWM3_A0, 1:15", "IO"),
        ]


