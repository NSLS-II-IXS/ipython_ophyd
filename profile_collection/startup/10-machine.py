from ophyd import (Device, EpicsSignal, EpicsSignalRO,
                   EpicsMotor, PVPositioner, Component as Cpt,
                   FormattedComponent as FCpt)


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

    hgap = FCpt(EpicsSignal, 'FE:C10A-OP{Slt:12-Ax:X}size.VAL', add_prefix=())
    hoff = FCpt(EpicsSignal, 'FE:C10A-OP{Slt:12-Ax:X}center.VAL', add_prefix=())
    vgap = FCpt(EpicsSignal, 'FE:C10A-OP{Slt:12-Ax:Y}size.VAL', add_prefix=())
    voff = FCpt(EpicsSignal, 'FE:C10A-OP{Slt:12-Ax:Y}center.VAL', add_prefix=())
    stop_all = FCpt(EpicsSignal, 'FE:C10A-CT{MC:1}allstop.VAL', add_prefix=())


    def stop(self):
        self.stop_all.put(1)
        super().stop()


# TODO: revisit the IVU as a PseudoPositioner
class Undulator(PVPositioner):
    setpoint = Cpt(EpicsSignal, '}Man:SP:Gap')
    # Note: there are actually 2 readbacks for gap position, Y1 & Y2.
    # This should be fixed at the EPICS level to provide an avg gap
    readback = Cpt(EpicsSignalRO, '}Y1:Rbv')
    actuate = Cpt(EpicsSignal, '}ManG:Go_.PROC')
    done = Cpt(EpicsSignalRO, '-Mtr:Gap}.DMOV')
    stop_signal = Cpt(EpicsSignal, '}Man:Stop_.PROC')

    actuate_value = 1
    done_value = 1
    stop_value = 1


ivu22 = Undulator('SR:C10-ID:G1{IVU22:1', name='ivu22')
fes = FESlits('FE:C10A-OP{Slt:', name='fes')
crl = CRL('FE:C10A-OP{CRL:1', name='crl')
