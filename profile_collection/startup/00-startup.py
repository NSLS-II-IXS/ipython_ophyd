import logging


from bluesky.global_state import gs
from bluesky.plans import  *
from bluesky.qt_kicker import install_qt_kicker

# Make ophyd listen to pyepics.
from ophyd import setup_ophyd
setup_ophyd()

import metadatastore.commands
from bluesky.global_state import gs
gs.RE.subscribe_lossless('all', metadatastore.commands.insert)

# Import matplotlib and put it in interactive mode.
import matplotlib.pyplot as plt
plt.ion()

# Make plots update live while scans run.
from bluesky.utils import install_qt_kicker
install_qt_kicker()


RE=gs.RE
RE.md['beamline_id'] = 'IXS'
RE.md['owner'] = 'xf10id'
RE.md['group'] = 'ixs'

# convenience imports
from ophyd.commands import *
from bluesky.callbacks import *
from bluesky.spec_api import *
from bluesky.global_state import gs, abort, stop, resume
from databroker import (DataBroker as db, get_events, get_images,
                        get_table, get_fields, restream, process)
from time import sleep
import numpy as np

RE = gs.RE  # convenience alias

from epics import caput, caget

from functools import partial
from pyOlog import SimpleOlogClient
from bluesky.callbacks.olog import logbook_cb_factory

# Set up the logbook. This configures bluesky's summaries of
# data acquisition (scan type, ID, etc.).

LOGBOOKS = ['Data Acquisition']  # list of logbook names to publish to
simple_olog_client = SimpleOlogClient()
generic_logbook_func = simple_olog_client.log
configured_logbook_func = partial(generic_logbook_func, logbooks=LOGBOOKS)

cb = logbook_cb_factory(configured_logbook_func)
RE.subscribe('start', cb)

import ophyd
from ophyd.commands import (wh_pos, log_pos, mov, movr, setup_ophyd,
                            get_all_positioners)


def relabel_motors():
    mtrs = get_all_positioners()
    for mtr in mtrs:
        attr = getattr(mtr, 'user_readback')
        attr.name = mtr.name

