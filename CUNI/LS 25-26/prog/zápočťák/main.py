#!/usr/bin/python3

import argparse

from prace_s_databazi import *
from delani_oken import *
from kontrola_lhut import *

parser = argparse.ArgumentParser(
    description = "Evidence potravin"
)

parser.add_argument("soubor", help = "Cesta k souboru s databází.")

args = parser.parse_args()

if __name__ == "__main__":
    databaze = prectiDatabazi(args)
    udelejOknoHlavni(args, databaze)
    kontrolaLhut(databaze)
