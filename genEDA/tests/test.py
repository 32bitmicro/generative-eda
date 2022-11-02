import sys
 
# setting path
sys.path.append('../')
 
from src.genEDA import *

# devices 

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

# nets
Net1 = Net("Net1")
Net2 = Net("Net2")

# circutis
Circuit1 = Circuit("Circuit1")

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

def unittestDevices():
    global R1,C1,L1,D1,N1,P1,J1,K1,M1,Q1,U1

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

def showNode(node):
    d,p = node
    print('device: ' + d.refid + ' pin: ' + str(p.idx))

def showNodes(nodes):
    print('nodes:')
    for n in nodes:
        showNode(n)

def showNet(net):
    print()
    print('----')
    print('net:')
    print('name: ' + net.name)
    showNodes(net.nodes)

def unittestNets():
    global R1,C1,L1,D1,N1,P1,J1,K1,M1,Q1,U1
    global Net1, Net2
    
    print()
    Net1.nodes.append((R1,R1.pins[0]))
    Net1.nodes.append((C1,C1.pins[0]))
    showNet(Net1)

    print()
    Net2.nodes.append((R1,R1.pins[1]))
    Net2.nodes.append((C1,C1.pins[1]))
    showNet(Net2)

def showCircuit(circuit):
    print()
    print('--------')
    print('circuit: ' + circuit.name)
    print('devices:')
    for d in circuit.devices:
        showDevice(d)
    print('nets:')
    for n in circuit.nets:
        showNet(n)

def unittestCircuit():
    global R1,C1,L1,D1,N1,P1,J1,K1,M1,Q1,U1
    global Net1, Net2
    global Circuit1

    Circuit1.devices.append(R1)
    Circuit1.devices.append(C1)
    Circuit1.devices.append(L1)
    Circuit1.devices.append(D1)
    Circuit1.devices.append(N1)
    Circuit1.devices.append(P1)
    Circuit1.devices.append(J1)
    Circuit1.devices.append(K1)
    Circuit1.devices.append(M1)
    Circuit1.devices.append(Q1)
    Circuit1.devices.append(U1)

    Circuit1.nets.append(Net1)
    Circuit1.nets.append(Net2)
    showCircuit(Circuit1)


if __name__ == '__main__':
    unittestDevices()
    unittestNets()
    unittestCircuit()
