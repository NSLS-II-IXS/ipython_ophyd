import logging
from bluesky.standard_config import *  # gs, etc.
from bluesky.scientific_callbacks import plot_peak_stats
from bluesky.plans import  *
from bluesky import qt_kicker

qt_kicker.install_qt_kicker()
RE=gs.RE

import matplotlib.pyplot as plt
plt.ion()

from databroker import DataBroker as db, get_events, get_images, get_table

from epics import caput, caget

# connect olog
# gs.RE.logbook = olog_wrapper(olog_client, ['Data Acquisition'])

# ophyd expects to find 'logbook' in the IPython namespace
from pyOlog import SimpleOlogClient
logbook = SimpleOlogClient()

import ophyd
