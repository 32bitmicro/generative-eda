import sys
 
# setting path
sys.path.append('../')
 
from src.genEDA import *

def showPins(pins):
    print('pins:')
    for p in pins:
        print(' ',p.idx,p.name)

def showDevice(dev):
    print(dev.refid)
    print(dev.name)
    print(dev.type)
    showPins(dev.pins)
    print(dev.value)
    print()

def unittest():
    R1 = R("R1")
    C1 = C("C1")
    L1 = L("L1")
    D1 = D("D1")
    N1 = N("N1")
    P1 = P("P1")
    J1 = J("J1")
    K1 = K("K1")
    M1 = M("M1")
    Q1 = Q("Q1")
    U1 = U('U1')

    showDevice(R1)
    showDevice(C1)
    showDevice(L1)
    showDevice(D1)
    showDevice(N1)
    showDevice(P1)
    showDevice(J1)
    showDevice(K1)
    showDevice(M1)
    showDevice(Q1)
    showDevice(U1)


if __name__ == '__main__':
    unittest()
