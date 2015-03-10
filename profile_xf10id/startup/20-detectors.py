from ophyd.controls import EpicsSignal

########### Counters ###########
# CNT001 s1_1  SMR1-S1  XF:10ID-BI:AH172:Current1:MeanValue_RBV
s1_1 = EpicsSignal('XF:10ID-BI:AH172:Current1:MeanValue_RBV', rw=False, name='s1_1')
# CNT002 s1_2  SMR1-S2  XF:10ID-BI:AH172:Current2:MeanValue_RBV
s1_2 = EpicsSignal('XF:10ID-BI:AH172:Current2:MeanValue_RBV', rw=False, name='s1_2')
# CNT003 s1_3  SMR1-S3  XF:10ID-BI:AH172:Current3:MeanValue_RBV
s1_3 = EpicsSignal('XF:10ID-BI:AH172:Current3:MeanValue_RBV', rw=False, name='s1_3')
# CNT004 s1_4  SMR1-S4  XF:10ID-BI:AH172:Current4:MeanValue_RBV
s1_4 = EpicsSignal('XF:10ID-BI:AH172:Current4:MeanValue_RBV', rw=False, name='s1_4')
# CNT005 d1  BPM1-PN  XF:10ID-BI:AH171:Current1:MeanValue_RBV
d1 = EpicsSignal('XF:10ID-BI:AH171:Current1:MeanValue_RBV', rw=False, name='d1')
# CNT006 s2_1  SMR2-S1  XF:10ID-BI:AH173:Current1:MeanValue_RBV
s2_1 = EpicsSignal('XF:10ID-BI:AH173:Current1:MeanValue_RBV', rw=False, name='s2_1')
# CNT007 s2_2  SMR2-S2  XF:10ID-BI:AH173:Current2:MeanValue_RBV
s2_2 = EpicsSignal('XF:10ID-BI:AH173:Current2:MeanValue_RBV', rw=False, name='s2_2')
# CNT008 s2_3  SMR2-S3  XF:10ID-BI:AH173:Current3:MeanValue_RBV
s2_3 = EpicsSignal('XF:10ID-BI:AH173:Current3:MeanValue_RBV', rw=False, name='s2_3')
# CNT009 s2_4  SMR2-S4  XF:10ID-BI:AH173:Current4:MeanValue_RBV
s2_4 = EpicsSignal('XF:10ID-BI:AH173:Current4:MeanValue_RBV', rw=False, name='s2_4')
# CNT010 d3  D-PN1  XF:10ID-BI:AH174:Current1:MeanValue_RBV
d3 = EpicsSignal('XF:10ID-BI:AH174:Current1:MeanValue_RBV', rw=False, name='d3')
# CNT011 d4  D-PN2  XF:10ID-BI:AH175:Current1:MeanValue_RBV
d4 = EpicsSignal('XF:10ID-BI:AH175:Current1:MeanValue_RBV', rw=False, name='d4')
