from bluesky.global_state import (resume, abort, stop, panic, all_is_well,
                                  state)

from bluesky.callbacks.olog import OlogCallback
from bluesky.global_state import gs


olog_cb = OlogCallback('Data Acquisition')
gs.RE.subscribe('start', olog_cb)

gs.DETS.append(det4)

#from bluesky.scientific_callbacks import plot_peak_stats

from bluesky.plans import *

from bluesky.spec_api import ct, ascan, dscan
