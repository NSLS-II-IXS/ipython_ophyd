from ophyd import (EpicsSignalRO, EpicsScaler, DetectorBase, SingleTrigger,
                   Component as Cpt, Device, EpicsSignal)
from ophyd.areadetector.cam import AreaDetectorCam
from ophyd.areadetector import EpicsSignalWithRBV


class AH501(Device):
    ch1 = Cpt(EpicsSignalRO, 'Current1:MeanValue_RBV')
    ch2 = Cpt(EpicsSignalRO, 'Current2:MeanValue_RBV')
    ch3 = Cpt(EpicsSignalRO, 'Current3:MeanValue_RBV')
    ch4 = Cpt(EpicsSignalRO, 'Current4:MeanValue_RBV')


det1 = AH501('XF10ID-BI:AH171:', name='det1')
det2 = AH501('XF10ID-BI:AH172:', name='det2')
det3 = AH501('XF10ID-BI:AH173:', name='det3')
det4 = AH501('XF10ID-BI:AH174:', name='det4')
det5 = AH501('XF10ID-BI:AH175:', name='det5')

sclr = EpicsScaler('XF:10IDD-ES{Sclr:1}', name='sclr')


class QuadEM(DetectorBase):
    model = Cpt(EpicsSignalRO, 'Model')
    firmware = Cpt(EpicsSignalRO, 'Firmware')

    acquire_mode = Cpt(EpicsSignalWithRBV, 'AcquireMode')
    acquire = Cpt(EpicsSignal, 'Acquire')

    read_format = Cpt(EpicsSignalWithRBV, 'ReadFormat')
    em_range = Cpt(EpicsSignalWithRBV, 'Range')
    ping_pong = Cpt(EpicsSignalWithRBV, 'PingPong')

    integration_time = Cpt(EpicsSignalWithRBV, 'IntegrationTime')
    num_channels = Cpt(EpicsSignalWithRBV, 'NumChannels')
    geometry = Cpt(EpicsSignalWithRBV, 'Geometry')
    resolution = Cpt(EpicsSignalWithRBV, 'Resolution')

    bias_state = Cpt(EpicsSignalWithRBV, 'BiasState')
    bias_interlock = Cpt(EpicsSignalWithRBV, 'BiasInterlock')
    bias_voltage = Cpt(EpicsSignalWithRBV, 'BiasVoltage')
    hvs_readback = Cpt(EpicsSignalRO, 'HVSReadback')
    hvv_readback = Cpt(EpicsSignalRO, 'HVVReadback')
    hvi_readback = Cpt(EpicsSignalRO, 'HVIReadback')

    values_per_read = Cpt(EpicsSignalWithRBV, 'ValuesPerRead')
    sample_time = Cpt(EpicsSignalRO, 'SampleTime_RBV') # yay for consistency
    averaging_time = Cpt(EpicsSignalWithRBV, 'AveragingTime')
    num_average = Cpt(EpicsSignalRO, 'NumAverage_RBV')
    num_averaged = Cpt(EpicsSignalRO, 'NumAveraged_RBV')
    num_acquire = Cpt(EpicsSignalWithRBV, 'NumAcquire')
    num_acquired = Cpt(EpicsSignalRO, 'NumAcquired')
    read_data = Cpt(EpicsSignalRO, 'ReadData')
    ring_overflows = Cpt(EpicsSignalRO, 'RingOverflows')
    trigger_mode = Cpt(EpicsSignal, 'TriggerMode')
    reset = Cpt(EpicsSignal, 'Reset')



ah501 = QuadEM('XF10ID-BI:AH175:', name='ah501')
