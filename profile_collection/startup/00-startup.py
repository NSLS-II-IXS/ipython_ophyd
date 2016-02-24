import logging
from bluesky.standard_config import *  # gs, etc.
from bluesky.scientific_callbacks import plot_peak_stats
from bluesky.plans import  *
from bluesky import qt_kicker

qt_kicker.install_qt_kicker()
RE=gs.RE
RE.md['beamline_id'] = 'IXS'
RE.md['owner'] = 'xf10id'
RE.md['group'] = 'ixs'


import matplotlib.pyplot as plt
plt.ion()

from databroker import DataBroker as db, get_events, get_images, get_table

from epics import caput, caget

# connect olog
# gs.RE.logbook = olog_wrapper(olog_client, ['Data Acquisition'])

# ophyd expects to find 'logbook' in the IPython namespace
from pyOlog import SimpleOlogClient
logbook = SimpleOlogClient()

from functools import partial
from bluesky.callbacks.olog import logbook_cb_factory

# Set up the logbook. This configures bluesky's summaries of
# data acquisition (scan type, ID, etc.).

logbook_func = logbook.log
configured_logbook_func = partial(logbook_func, logbooks=['Data Acquisition'])

cb = logbook_cb_factory(configured_logbook_func)
RE.subscribe('start', cb)

import ophyd
from ophyd.command import (wh_pos, log_pos, mov, movr)
