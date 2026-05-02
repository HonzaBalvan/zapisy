### !# bin/python něco

### u povinných stačí název u nepovinných název a hodnotu

import argparse

parser = argparse.ArgumentParser(
    description = "Evidence potravin"
)

parser.add_argument("soubor", help = "Cesta k souboru s databází.")
parser.add_argument("--nepovinny", choices = ["moznost_1", "moznost_2"], default = "moznost_1", help = "Nepovinný. Výběr: 'moznost_1', 'moznost_2'")

args = parser.parse_args()

databaze = open(args.soubor, encoding="utf-8")

#něco

databaze.close()
