from bluesky.global_state import (resume, abort, stop, panic, all_is_well,
                                  state)

from bluesky.callbacks.olog import OlogCallback
from bluesky.callbacks import LivePlot
from bluesky.global_state import gs


olog_cb = OlogCallback('Data Acquisition')
gs.RE.subscribe('start', olog_cb)

gs.DETS.append(det4)

#from bluesky.scientific_callbacks import plot_peak_stats

from bluesky.plans import *

from bluesky.spec_api import ct, ascan, dscan


from suitcase.spec import DocumentToSpec

spec_cb = DocumentToSpec('/IXS/specfiles/spec0.spec')

for spec_scan in [ascan, dscan, ct]:
    spec_scan.subs['all'].append(spec_cb)

#relabel_motors()
