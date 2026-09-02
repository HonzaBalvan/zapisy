#!/usr/bin/python3

### u povinných stačí název u nepovinných název a hodnotu

import argparse

parser = argparse.ArgumentParser(
    description = "Evidence potravin"
)

parser.add_argument("soubor", help = "Cesta k souboru s databází.")
parser.add_argument("--nepovinny", choices = ["moznost_1", "moznost_2"], default = "moznost_1", help = "Nepovinný. Výběr: 'moznost_1', 'moznost_2'")

args = parser.parse_args()

with open(args.soubor, encoding="utf-8") as vstup:
    vstup_radky = vstup.readlines()
    
    databaze = []
    for radek_vstupu in vstup_radky:
        radek_split = radek_vstupu.strip().split(",")
        if radek_split[0] == "@":
            radek_split.pop(0)
            databaze.append(radek_split)

    #print(*databaze)
#něco
