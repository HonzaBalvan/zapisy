#!/usr/bin/python3

import argparse

from prace_s_databazi import *
from delani_oken import *
from kontrola_lhut import *

parser = argparse.ArgumentParser(
    description = "Evidence potravin"
)

parser.add_argument("--soubor", default = "databaze.txt", help = "Cesta k souboru s databází. Výchozí možnost je soubor 'databaze.txt' ve složce programu.")
parser.add_argument("--mode", choices  = ["gui", "nogui"], default = "gui", help = "Volba spuštění v grafickém režimu ('gui') nebo bez grafiky ('nogui'). Výchozí možnost je 'gui'.")

args = parser.parse_args() #parsování možností z konzole, a to výběru s grafikou / bez grafiky pomocí '--mode' a alternativního souboru databáze pomocí možnosti '--soubor cesta_k_souboru'

databaze = prectiDatabazi(args) #udělá databázi

if args.mode == "gui": 
    udelejOknoHlavni(args, databaze) #dělá veškerá okna, a to pouze v režimu 'gui'

kontrolaLhut(databaze) #kontroluje lhůty a posílá e-maily
