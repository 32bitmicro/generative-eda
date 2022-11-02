# Introduction

Generative EDA

Circuit representation in Python

Pins
Pin is touples of (index,name)

Devices
Device is a class 

Reference ID

Passive devices:

R - Resistor
C - Capacitor
L - Inductor
Pins: 1,2
Value: numeric or code 

Active devices:

D - Diode
Pins: Anode Cathode
Model: text

N - NPN Bipolar transitor    
Pins: Base,Collector,Emmiter
Model: text

P - PNP Bipolar transitor 
Pins: Base,Collector,Emmiter
Model: text

M - N channel MOSFET tansistor
Pins: Gate,Drain,Source
Model: text

Q - P channel MOSFET tansistor
Pins: Gate,Drain,Source
Model: text

U - integrated circuit
Model: text

Nets
Collection of tupples (Componnent,Pin)



