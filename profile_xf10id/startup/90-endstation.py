from ophyd import (Component as Cpt, Device, EpicsMotor)


class Spectrometer(Device):
    sty = Cpt(EpicsMotor, '-Ax:Y}Mtr')
    stx = Cpt(EpicsMotor, '-Ax:X}Mtr')
    stz = Cpt(EpicsMotor, '-Ax:Z}Mtr')
    tth = Cpt(EpicsMotor, '-Ax:2Th}Mtr')
    th =  Cpt(EpicsMotor, '-Ax:Th}Mtr')
    chi = Cpt(EpicsMotor, '-Ax:ChiA}Mtr')
    phi = Cpt(EpicsMotor, '-Ax:PhiA}Mtr')


class Ez4(Device):
    acfth = Cpt(EpicsMotor, '1-Ax:1}Mtr')
    acchi = Cpt(EpicsMotor, '1-Ax:2}Mtr')
    awfth = Cpt(EpicsMotor, '1-Ax:3}Mtr')
    awchi = Cpt(EpicsMotor, '1-Ax:4}Mtr')
    d1the = Cpt(EpicsMotor, '2-Ax:1}Mtr')
    d1phi = Cpt(EpicsMotor, '2-Ax:2}Mtr')
    d2the = Cpt(EpicsMotor, '2-Ax:3}Mtr')
    d2phi = Cpt(EpicsMotor, '2-Ax:4}Mtr')
    d3the = Cpt(EpicsMotor, '3-Ax:1}Mtr')
    d3phi = Cpt(EpicsMotor, '3-Ax:2}Mtr')
    d4the = Cpt(EpicsMotor, '3-Ax:3}Mtr')
    d4phi = Cpt(EpicsMotor, '3-Ax:4}Mtr')
    d5the = Cpt(EpicsMotor, '4-Ax:1}Mtr')
    d5phi = Cpt(EpicsMotor, '4-Ax:2}Mtr')
    d6the = Cpt(EpicsMotor, '4-Ax:3}Mtr')
    d6phi = Cpt(EpicsMotor, '4-Ax:4}Mtr')
    sant = Cpt(EpicsMotor,  '5-Ax:2}Mtr')
    sanb = Cpt(EpicsMotor,  '5-Ax:3}Mtr')
    anpd = Cpt(EpicsMotor,  '5-Ax:1}Mtr')
    ms2i = Cpt(EpicsMotor,  '7-Ax:1}Mtr')
    ms2o = Cpt(EpicsMotor,  '7-Ax:2}Mtr')


# are these mis-named? OP ---> ES? They do exist, as named...
# mcmst = Cpt(EpicsMotor, 'XF:10IDD-OP{Ez4:6-Ax:3}Mtr', name='mcmst')
# mcmsb = Cpt(EpicsMotor, 'XF:10IDD-OP{Ez4:6-Ax:4}Mtr', name='mcmsb')


class SampleEnv(Device):
    y = Cpt(EpicsMotor, '-Ax:Y}Mtr')
    x = Cpt(EpicsMotor, '-Ax:X}Mtr')
    z = Cpt(EpicsMotor, '-Ax:Z}Mtr')


spec = Spectrometer('XF:10IDD-OP{Spec:1', name='spec')
ez4 = Ez4('XF:10IDD-ES{Ez4:', name='ez4')
sample_env = SampleEnv('XF:10IDD-OP{Env:1', name='sample_env')

