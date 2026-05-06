import matplotlib.pyplot as plt
import csv
from matplotlib.backends.backend_pdf import PdfPages
plt.style.use("Solarize_Light2")

rok = []
mesic = []
den = []
tavg = []
tma = []
tmi = []
sra = []

with open("PKLM.csv","r") as csvfile:
    plots = csv.reader(csvfile, delimiter=",")

    i = 0
    for row in plots:
        if i != 0:
            rok.append(int(row[0]))
            mesic.append(int(row[1]))
            den.append(int(row[2]))
            tavg.append(float(row[3]))
            tma.append(float(row[4]))
            tmi.append(float(row[5]))
            if row[6] != "":
                sra.append(float(row[6]))
            else:
                sra.append(0)

        i +=1

#graf1
graf1_rok = []
graf1_tavg = []
graf1_tma = []
graf1_tmi = []
k = 0

for rok_cislo in range(min(rok), max(rok) + 1):
    graf1_rok.append(rok_cislo)
    graf1_tavg.append(0)
    graf1_tma.append(-100)
    graf1_tmi.append(100)

    for j in range(len(rok)):
        if rok[j] == rok_cislo:
            graf1_tavg[k] += tavg[j]
            if tma[j] > graf1_tma[k]:
                graf1_tma[k] = tma[j]
            if tmi[j] < graf1_tmi[k]:
                graf1_tmi[k] = tmi[j]
    
    graf1_tavg[k] /= 365

    k +=1

with PdfPages("graf1.pdf") as pdf:
    plt.figure(figsize=(12, 6))
    plt.plot(graf1_rok, graf1_tavg, label="Průměrná teplota", color="green")
    plt.plot(graf1_rok, graf1_tmi, label="Minimální teplota", color="blue")
    plt.plot(graf1_rok, graf1_tma, label="Maximální teplota", color="red")
    plt.title("Roční průměrné, minimální a maximální teploty")
    plt.xlabel("Rok")
    plt.ylabel("Teplota (°C)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    pdf.savefig()
    plt.close()

#graf2
graf2_mesic = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
graf2_tavg = [0] * 12
graf2_tma = [-100] * 12
graf2_tmi = [100] * 12

for mesic_cislo in range(12):
    for l in range(len(mesic)):
        if mesic[l] == mesic_cislo + 1:
            graf2_tavg[mesic_cislo] += tavg[l]
            if tmi[l] < graf2_tmi[mesic_cislo]:
                graf2_tmi[mesic_cislo] = tmi[l]
            if tma[l] > graf2_tma[mesic_cislo]:
                graf2_tma[mesic_cislo] = tma[l]

    graf2_tavg[mesic_cislo] /= (len(mesic) / 12)

with PdfPages("graf2.pdf") as pdf:
    plt.figure(figsize=(12, 6))
    plt.plot(graf2_mesic, graf2_tavg, label="Průměrná teplota", color="green", marker="o")
    plt.plot(graf2_mesic, graf2_tmi, label="Minimální teplota", color="blue", marker="o")
    plt.plot(graf2_mesic, graf2_tma, label="Maximální teplota", color="red", marker="o")
    plt.title("Měsíční průměrné, minimální a maximální teploty")
    plt.xlabel("Měsíc")
    plt.ylabel("Teplota (°C)")
    plt.xticks(graf2_mesic)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    pdf.savefig()
    plt.close()

#graf3
graf3_mesic = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
graf3_sraavg = [0] * 12
graf3_srama = [0] * 12
graf3_srami = [0] * 12

for mesic_cislo in range(12):
    for l in range(len(mesic)):
        if mesic[l] == mesic_cislo + 1:
            graf3_sraavg[mesic_cislo] += sra[l]
            if sra[l] < graf3_srami[mesic_cislo]:
                graf3_srami[mesic_cislo] = sra[l]
            if sra[l] > graf3_srama[mesic_cislo]:
                graf3_srama[mesic_cislo] = sra[l]

    graf3_sraavg[mesic_cislo] /= (len(mesic) / 12)

with PdfPages("graf3.pdf") as pdf:
    plt.figure(figsize=(12, 6))
    plt.plot(graf3_mesic, graf3_sraavg, label="Průměrné srážky", color = "green", marker = "o")
    plt.plot(graf3_mesic, graf3_srama, label="Maximální srážky", color = "red", marker = "o")
    plt.plot(graf3_mesic, graf3_srami, label="Minimální srážky", color = "blue", marker = "o")
    plt.title("Měsíční průměrné, minimální a maximální srážky")
    plt.xlabel("Měsíc")
    plt.ylabel("Srážky (mm)")
    plt.xticks(graf3_mesic)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    pdf.savefig()
    plt.close()

#graf4
graf4_rok = []
graf4_t213 = []
k = 0

for rok_cislo in range(min(rok), max(rok) + 1):
    graf4_rok.append(rok_cislo)
    graf4_t213.append(0)

    for j in range(len(rok)):
        if rok[j] == rok_cislo and den[j] == 21 and mesic[j] == 3:
            graf4_t213[k] = tavg[j]

    k +=1

with PdfPages("graf4.pdf") as pdf:
    plt.figure(figsize=(12, 6))
    plt.plot(graf4_rok, graf4_t213, label="Průměrná teplota", color="green")
    plt.title("Teploty 21. března každého roku")
    plt.xlabel("Rok")
    plt.ylabel("Teplota (°C)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    pdf.savefig()
    plt.close()
