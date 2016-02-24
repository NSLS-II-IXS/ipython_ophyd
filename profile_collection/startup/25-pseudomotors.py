from ophyd import (EpicsMotor, PseudoSingle, PseudoPositioner,
                   Component as Cpt)
import numpy as np
from scipy import interpolate


_Gm = [ 6184.0,
       6368.0,
       6550.0,
       6730.0,
       6909.0,
       7086.0,
       7262.0,
       7438.0,
       7613.0,
       7788.0,
       7962.0,
       8138.0,
       8311.0,
       8486.0,
       8662.0,
       8840.0,
       9019.0,
       9200.0,
       9382.0,
       9567.0,
       9753.0,
       9943.0,
       10136.0,
       10332.0,
       10531.0,
       10740.0,
       10960.0,
       11385.0]

_Tm = [ 16.401781,
       15.821071,
       15.280587,
       14.776273,
       14.304428,
       13.862182,
       13.446656,
       13.055574,
       12.686789,
       12.338436,
       12.008851,
       11.696607,
       11.400018,
       11.118472,
       10.850483,
       10.595196,
       10.351707,
       10.119222,
       9.896987,
       9.684357,
       9.480717,
       9.28554,
       9.098203,
       8.918375,
       8.7455,
       8.579178,
       8.41915,
       8.11645 ]

gcalc = interpolate.interp1d(_Gm, _Tm)

_hc = 12398.4193
_si_111 = 3.1363


class BLEnergy(PseudoPositioner):
    # limits and constants from Spec file, "xf10id_site.mac"
    energy = Cpt(PseudoSingle, limits=(7.835, 17.7))

    theta = Cpt(EpicsMotor, 'XF:10IDA-OP{Mono:DCM-Ax:P}Mtr')
    z2 = Cpt(EpicsMotor, 'XF:10IDA-OP{Mono:DCM-Ax:Z2}Mtr')
    ugap = Cpt(Undulator, 'SR:C10-ID:G1{IVU22:1')


    def forward(self, pseudo_pos):
        _th = np.rad2deg(np.arcsin(_hc/(2.*_si_111*pseudo_pos)))
        _z2 = 15./np.cos(np.deg2rad(_th)) - 15.
        _ugap = gcalc(_th)

        return self.RealPosition(theta=_th, z2=_z2, ugap=_ugap)

    def inverse(self, real_pos):
        en = _hc/(2.*_si_111*np.sin(np.deg2rad(real_pos.theta)))
        en = float(en)
        return self.PseudoPosition(energy=en)


bl_energy = BLEnergy('', name='bl_energy', egu='eV')
