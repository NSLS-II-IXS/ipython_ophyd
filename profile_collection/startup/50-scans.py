from ophyd.userapi.scan_api import Scan, AScan, DScan, Count

scan = Scan()
ascan = AScan()
ascan.default_triggers = []
ascan.default_detectors = [d1, s2_1]
dscan = DScan()

# Use ct as a count which is a single scan.

ct = Count()
