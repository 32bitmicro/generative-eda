
class Pin:
    def __init__(self,idx,name,function='',type='') -> None:
        self.idx = idx
        self.name = name
        self.type = type

class Device:
    def __init__(self,refid,name,type) -> None:
        self.refid = refid
        self.name = name
        self.type = type
        self.pins = []
        self.value =''


class R(Device):
    def __init__(self,refid,value=1,name='') -> None:
        Device.__init__(self,refid,name,"resistor")
        self.pins = [Pin(1,"1"),Pin(2,"2")]
        self.value = value

class C(Device):
    def __init__(self,refid,value=1,name='') -> None:
        Device.__init__(self,refid,name,"capacitor")
        self.pins = [Pin(1,"1"),Pin(2,"2")]
        self.value = value

class L(Device):
    def __init__(self,refid,value=1,name='') -> None:
        Device.__init__(self,refid,name,"inductor")
        self.pins = [Pin(1,"1"),Pin(2,"2")]
        self.value = value

class D(Device):
    def __init__(self,refid,name='') -> None:
        Device.__init__(self,refid,name,"diode")
        self.pins = [Pin(1,"anode"),Pin(2,"cathode")]

class BJTtransitor(Device):
    def __init__(self,refid,name,type) -> None:
        Device.__init__(self,refid,name,type)
        self.pins = [Pin(1,"collector"),Pin(2,"base"),Pin(3,"emitter")]

class N(BJTtransitor):
    def __init__(self,refid,name='') -> None:
        BJTtransitor.__init__(self,refid,name,"npn")

class P(BJTtransitor):
    def __init__(self,refid,name='') -> None:
        BJTtransitor.__init__(self,refid,name,"pnp")

class FETTransitor(Device):
    def __init__(self,refid,name,type) -> None:
        Device.__init__(self,refid,name,type)
        self.pins = [Pin(1,"source"),Pin(2,"gate"),Pin(3,"drain")]

class J(FETTransitor):
    def __init__(self,refid,name='') -> None:
        BJTtransitor.__init__(self,refid,name,"n-channel jfet")

class K(FETTransitor):
    def __init__(self,refid,name='') -> None:
        BJTtransitor.__init__(self,refid,name,"p-channel jfet")

class MOSFETTransitor(Device):
    def __init__(self,refid,name,type) -> None:
        Device.__init__(self,refid,name,type)
        self.pins = [Pin(1,"source"),Pin(2,"gate"),Pin(3,"drain")]

class M(MOSFETTransitor):
    def __init__(self,refid,name='') -> None:
        BJTtransitor.__init__(self,refid,name,"n-channel mosfet")

class Q(MOSFETTransitor):
    def __init__(self,refid,name='') -> None:
        BJTtransitor.__init__(self,refid,name,"p-channel mosfet")

class U(Device):
    def __init__(self,refid,name='') -> None:
        Device.__init__(self,refid,name,"")
        self.pins = []
        self.value = ''
class Net:
    def __init__(self,name='') -> None:
        self.name = name
        self.nodes = []
class Circuit:
    def __init__(self,name='') -> None:
        self.name = name
        self.devices = []
        self.nets = []
