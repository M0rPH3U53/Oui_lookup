#!/home/kali/Desktop/scripts/venv/bin/python

import time

from ouilookup import OuiLookup

print(OuiLookup().query(input("Entrez une address MAC: ")))

time.sleep(500)
