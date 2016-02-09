from ophyd import (EpicsSignalRO, EpicsScaler)

sclr = EpicsScaler('XF:10IDD-ES{Sclr:1}', name='sclr')

d11 = EpicsSignalRO('XF:10ID-BI:AH171:Current1:MeanValue_RBV', name='d11')
d12 = EpicsSignalRO('XF:10ID-BI:AH171:Current2:MeanValue_RBV', name='d12')
d13 = EpicsSignalRO('XF:10ID-BI:AH171:Current3:MeanValue_RBV', name='d13')
d14 = EpicsSignalRO('XF:10ID-BI:AH171:Current4:MeanValue_RBV', name='d14')

d21 = EpicsSignalRO('XF:10ID-BI:AH172:Current1:MeanValue_RBV', name='d21')
d22 = EpicsSignalRO('XF:10ID-BI:AH172:Current2:MeanValue_RBV', name='d22')
d23 = EpicsSignalRO('XF:10ID-BI:AH172:Current3:MeanValue_RBV', name='d23')
d24 = EpicsSignalRO('XF:10ID-BI:AH172:Current4:MeanValue_RBV', name='d24')

d31 = EpicsSignalRO('XF:10ID-BI:AH173:Current1:MeanValue_RBV', name='d31')
d32 = EpicsSignalRO('XF:10ID-BI:AH173:Current2:MeanValue_RBV', name='d32')
d33 = EpicsSignalRO('XF:10ID-BI:AH173:Current3:MeanValue_RBV', name='d33')
d34 = EpicsSignalRO('XF:10ID-BI:AH173:Current4:MeanValue_RBV', name='d34')

d41 = EpicsSignalRO('XF:10ID-BI:AH174:Current1:MeanValue_RBV', name='d41')
d42 = EpicsSignalRO('XF:10ID-BI:AH174:Current2:MeanValue_RBV', name='d42')
d43 = EpicsSignalRO('XF:10ID-BI:AH174:Current3:MeanValue_RBV', name='d43')
d44 = EpicsSignalRO('XF:10ID-BI:AH174:Current4:MeanValue_RBV', name='d44')

d51 = EpicsSignalRO('XF:10ID-BI:AH175:Current1:MeanValue_RBV', name='d51')
d52 = EpicsSignalRO('XF:10ID-BI:AH175:Current2:MeanValue_RBV', name='d52')
