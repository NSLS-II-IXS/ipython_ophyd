from ophyd import (Device, EpicsSignal, EpicsSignalRO,
                   EpicsMotor, PVPositioner, Component as Cpt)


# SR current
# CNT012 src  SRcur  SR:C03-BI{DCCT:1}I:Real-I
sr_curr = EpicsSignalRO('SR:C10-BI{DCCT:1}I:Real-I', name='sr_curr')

class CRL(Device):
    x = Cpt(EpicsMotor, '-Ax:X}Mtr')
    y = Cpt(EpicsMotor, '-Ax:Y}Mtr')
    th =Cpt(EpicsMotor, '-Ax:P}Mtr')


class FESlits(Device):
    top = Cpt(EpicsMotor, '1-Ax:T}Mtr')
    bottom = Cpt(EpicsMotor, '2-Ax:B}Mtr')
    outboard = Cpt(EpicsMotor, '1-Ax:O}Mtr')
    inboard = Cpt(EpicsMotor, '2-Ax:I}Mtr')


# TODO: revisit the IVU as a PseudoPositioner
class Undulator(PVPositioner):
    setpoint = Cpt(EpicsSignal, '}Man:SP:Gap')
    # Note: there are actually 2 readbacks for gap position, Y1 & Y2.
    # This should be fixed at the EPICS level to provide an avg gap
    readback = Cpt(EpicsSignalRO, '}Y1:Rbv')
    actuate = Cpt(EpicsSignal, '}ManG:Go_.PROC')
    actuate_value = 1
    done = Cpt(EpicsSignalRO, '-Mtr:Gap}.DMOV')
    done_value = 1
    stop_signal = Cpt(EpicsSignal, '}Man:Stop_.PROC')
    stop_value = 1


ivu22 = Undulator('SR:C10-ID:G1{IVU22:1', name='ivu22')
fes = FESlits('FE:C10A-OP{Slt:', name='fes')
crl = CRL('FE:C10A-OP{CRL:1', name='crl')
