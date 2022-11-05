import sys
 
# setting path
sys.path.append('../src')
 
from genEDA import *

import PySpice.Logging.Logging as Logging
logger = Logging.setup_logging()


from PySpice.Spice.Netlist import Circuit, SubCircuit, SubCircuitFactory
from PySpice.Unit import *

def unittest():
    R1 = R("R1")
    C1 = C("C1")
    L1 = L("L1")

    #RLC

if __name__ == 'main':
    unittest()

