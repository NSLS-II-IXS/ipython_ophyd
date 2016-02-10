from ophyd import (EpicsSignalRO, EpicsScaler)


class AH501(Device):
    ch1 = Cpt(EpicsSignalRO, 'Current1:MeanValue_RBV')
    ch2 = Cpt(EpicsSignalRO, 'Current2:MeanValue_RBV')
    ch3 = Cpt(EpicsSignalRO, 'Current3:MeanValue_RBV')
    ch4 = Cpt(EpicsSignalRO, 'Current4:MeanValue_RBV')


d1 = AH501('XF:10ID-BI:AH171:', name='d1')
d2 = AH501('XF:10ID-BI:AH172:', name='d2')
d3 = AH501('XF:10ID-BI:AH173:', name='d3')
d4 = AH501('XF:10ID-BI:AH174:', name='d4')
d5 = AH501('XF:10ID-BI:AH175:', name='d5')

sclr = EpicsScaler('XF:10IDD-ES{Sclr:1}', name='sclr')
