from ophyd import (EpicsMotor, PseudoSingle, PseudoPositioner,
                   Component as Cpt)
import numpy as np


_hc = 12398.4193
_si_111 = 3.1363


class DCMEnergy(PseudoPositioner):
    # limits and constants from Spec file, "xf10id_site.mac"
    energy = Cpt(PseudoSingle, limits=(7.835, 17.7))

    theta = Cpt(EpicsMotor, 'XF:10IDA-OP{Mono:DCM-Ax:P}Mtr')
    z2 = Cpt(EpicsMotor, 'XF:10IDA-OP{Mono:DCM-Ax:Z2}Mtr')


    def forward(self, pseudo_pos):
        th = np.rad2deg(np.arcsin(_hc/(2.*_si_111*pseudo_pos)))
        # XXX: z2 get a pass through here! Consult Alexey!!
        return self.RealPosition(theta=th, z2=z2.get())

    def inverse(self, real_pos):
        en = _hc/(2.*_si_111*np.sin(np.deg2rad(real_pos.theta)))
        en = float(en)
        return self.PseudoPosition(energy=en)


dcm_en = DCMEnergy('', name='dcm_en', egu='keV')
