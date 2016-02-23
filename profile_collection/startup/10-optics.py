from ophyd import (Device, Component as Cpt, EpicsMotor)


# defined here, also used in 10-optics.py
# why do none of the 'slits' constructs feature gap, center motions?
class Blades(Device):
    top = Cpt(EpicsMotor, '-Ax:T}Mtr')
    bottom = Cpt(EpicsMotor, '-Ax:B}Mtr')
    outboard = Cpt(EpicsMotor, '-Ax:O}Mtr')
    inboard = Cpt(EpicsMotor, '-Ax:I}Mtr')


class DCM(Device):
    y =  Cpt(EpicsMotor, '-Ax:Y}Mtr')
    th = Cpt(EpicsMotor, '-Ax:P}Mtr')
    z2 = Cpt(EpicsMotor, '-Ax:Z2}Mtr')
    p1 = Cpt(EpicsMotor, '-Ax:P1}Mtr')
    r2 = Cpt(EpicsMotor, '-Ax:R2}Mtr')
    pf = Cpt(EpicsMotor, '-Ax:PF}Mtr')


class HRM2(Device):
    ux =  Cpt(EpicsMotor, '-Ax:UX}Mtr')
    uy =  Cpt(EpicsMotor, '-Ax:UY}Mtr')
    uth = Cpt(EpicsMotor, '-Ax:UTc}Mtr')
    uch = Cpt(EpicsMotor, '-Ax:UC}Mtr')
    uif = Cpt(EpicsMotor, '-Ax:UTI}Mtr')
    uof = Cpt(EpicsMotor, '-Ax:UTO}Mtr')
    dx =  Cpt(EpicsMotor, '-Ax:DX}Mtr')
    dy =  Cpt(EpicsMotor, '-Ax:DY}Mtr')
    dth = Cpt(EpicsMotor, '-Ax:DTc}Mtr')
    dch = Cpt(EpicsMotor, '-Ax:DC}Mtr')
    dif = Cpt(EpicsMotor, '-Ax:DTI}Mtr')
    dof = Cpt(EpicsMotor, '-Ax:DTO}Mtr')
    d1 =  Cpt(EpicsMotor, '-Pico:m1}Mtr')
    d2 =  Cpt(EpicsMotor, '-Pico:m2}Mtr')
    d3 =  Cpt(EpicsMotor, '-Pico:m3}Mtr')
    d4 =  Cpt(EpicsMotor, '-Pico:m4}Mtr')
    d5 =  Cpt(EpicsMotor, '-Pico:m5}Mtr')
    bs =  Cpt(EpicsMotor, '-Pico:m6}Mtr')



class VFM(Device):
    ux = Cpt(EpicsMotor, '-Ax:UX}Mtr')
    uy = Cpt(EpicsMotor, '-Ax:UY}Mtr')
    dx = Cpt(EpicsMotor, '-Ax:DX}Mtr')
    dy = Cpt(EpicsMotor, '-Ax:DY}Mtr')
    ub = Cpt(EpicsMotor, '-Ax:UB}Mtr')
    db = Cpt(EpicsMotor, '-Ax:DB}Mtr')


class HFM(Device):
    ux = Cpt(EpicsMotor, '-Ax:UX}Mtr')
    uy = Cpt(EpicsMotor, '-Ax:UY}Mtr')
    dx = Cpt(EpicsMotor, '-Ax:DX}Mtr')
    dy = Cpt(EpicsMotor, '-Ax:DY}Mtr')
    ub = Cpt(EpicsMotor, '-Ax:UB}Mtr')
    db = Cpt(EpicsMotor, '-Ax:DB}Mtr')


class XYMotor(Device):
    x = Cpt(EpicsMotor, '-Ax:X}Mtr')
    y = Cpt(EpicsMotor, '-Ax:Y}Mtr')


class SSA(Device):
    top = Cpt(EpicsMotor, '-Ax:T}Mtr')
    bottom = Cpt(EpicsMotor, '-Ax:B}Mtr')


class Table(Device):
    x = Cpt(EpicsMotor, '-Ax:X4}Mtr')
    y = Cpt(EpicsMotor, '-Ax:Y4}Mtr')
    th =Cpt(EpicsMotor, '-Ax:X4a1}Mtr')


class Pinhole(Device):
    ux = Cpt(EpicsMotor, '-Ax:UX}Mtr')
    uy = Cpt(EpicsMotor, '-Ax:UY}Mtr')
    dx = Cpt(EpicsMotor, '-Ax:DX}Mtr')
    dy = Cpt(EpicsMotor, '-Ax:DY}Mtr')



dcm = DCM('XF:10IDA-OP{Mono:DCM', name='dcm')
vfm = VFM('XF:10IDD-OP{VFM:1', name='vfm')
hfm = HFM('XF:10IDD-OP{HFM:1', name='hfm')
hrm2 = HRM2('XF:10IDB-OP{Mono:HRM2', name='hrm2')

s1 = Blades('XF:10IDA-OP{Slt:1', name='s1')
s2 = Blades('XF:10IDA-OP{Slt:4', name='s2')
s3 = Blades('XF:10IDA-OP{Slt:5', name='s3')

bpm1 = XYMotor('XF:10IDA-OP{BPM:1', name='bpm1')
bpm1_diag = EpicsMotor('XF:10IDA-BI{BPM:1-Ax:YFoil}Mtr', name='bpm1_diag')
bpm2 = XYMotor('XF:10IDC-OP{BPM:2', name='bpm2')
bpm2_diag = EpicsMotor('XF:10IDC-BI{BPM:2-Ax:Y}Mtr', name='bpm2_diag')

ssa = SSA('XF:10IDB-OP{SSA:1', name='ssa')
k3 = Table('XF:10IDC-OP{Tbl:1', name='k3')
ph = Pinhole('XF:10IDD-OP{Pinh:1', name='ph')
