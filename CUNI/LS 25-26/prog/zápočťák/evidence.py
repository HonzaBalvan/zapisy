#!/usr/bin/python3

import argparse

from prace_s_databazi import *
from delani_oken import *
from kontrola_lhut import *

parser = argparse.ArgumentParser(
    description = "Evidence potravin"
)

parser.add_argument("--soubor", default = "databaze.txt", help = "Cesta k souboru s databází. Výchozí možnost je soubor 'databaze.txt' ve složce programu.")

args = parser.parse_args() #parsování možností z konzole, a to alternativního souboru databáze pomocí možnosti '--soubor cesta_k_souboru'

if __name__ == "__main__":
    databaze = prectiDatabazi(args) #udělá databázi
    udelejOknoHlavni(args, databaze) #dělá veškerá okna
    kontrolaLhut(databaze) #kontroluje lhůty a posílá e-maily
