import os
osDrive = os.getenv("SYSTEMDRIVE")
SCHTASK_ROOT = "{}\\Windows\\System32".format(osDrive)
SCHTASK_CMD = "{}\\Schtasks.exe".format(SCHTASK_ROOT)