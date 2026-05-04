import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Load the data using numpy
data = np.genfromtxt(
    "PKLM.csv",
    delimiter=",",
    skip_header=1,
    encoding="utf-8",
    filling_values=np.nan,
    dtype=None,
    names=["rok", "měsíc", "den", "T_AVG", "TMA", "TMI", "SRA", "Flag"]
)

# Extract columns
year = data["rok"].astype(int)
month = data["měsíc"].astype(int)
day = data["den"].astype(int)
avg_temp = data["T_AVG"].astype(float)
max_temp = data["TMA"].astype(float)
min_temp = data["TMI"].astype(float)
precipitation = data["SRA"].astype(float)

# --- Helper function to safely compute min/max ---
def safe_min(arr):
    valid = arr[~np.isnan(arr)]
    return np.min(valid) if len(valid) > 0 else np.nan

def safe_max(arr):
    valid = arr[~np.isnan(arr)]
    return np.max(valid) if len(valid) > 0 else np.nan

# --- Plot 1: Annual Average, Min, Max Temperatures ---
unique_years = np.unique(year)
annual_avg_temp = []
annual_min_temp = []
annual_max_temp = []

for y in unique_years:
    mask = (year == y)
    annual_avg_temp.append(np.nanmean(avg_temp[mask]))
    annual_min_temp.append(safe_min(min_temp[mask]))
    annual_max_temp.append(safe_max(max_temp[mask]))

annual_avg_temp = np.array(annual_avg_temp)
annual_min_temp = np.array(annual_min_temp)
annual_max_temp = np.array(annual_max_temp)

# --- Plot 2: Monthly Average, Min, Max Temperatures ---
unique_months = np.arange(1, 13)
monthly_avg_temp = []
monthly_min_temp = []
monthly_max_temp = []

for m in unique_months:
    mask = (month == m)
    monthly_avg_temp.append(np.nanmean(avg_temp[mask]))
    monthly_min_temp.append(safe_min(min_temp[mask]))
    monthly_max_temp.append(safe_max(max_temp[mask]))

monthly_avg_temp = np.array(monthly_avg_temp)
monthly_min_temp = np.array(monthly_min_temp)
monthly_max_temp = np.array(monthly_max_temp)

# --- Plot 3: Monthly Average, Min, Max Precipitation ---
mask_precip = (year == 1804) & (month >= 4) | (year > 1804)
filtered_precip = precipitation[mask_precip]
filtered_month_precip = month[mask_precip]

monthly_avg_precip = []
monthly_min_precip = []
monthly_max_precip = []

for m in unique_months:
    mask = (filtered_month_precip == m)
    monthly_avg_precip.append(np.nanmean(filtered_precip[mask]))
    monthly_min_precip.append(safe_min(filtered_precip[mask]))
    monthly_max_precip.append(safe_max(filtered_precip[mask]))

monthly_avg_precip = np.array(monthly_avg_precip)
monthly_min_precip = np.array(monthly_min_precip)
monthly_max_precip = np.array(monthly_max_precip)

# --- Plot 4: Temperatures for march 21st ---
mask_march_21 = (month == 3) & (day == 21)
march_21_years = year[mask_march_21]
march_21_avg_temp = avg_temp[mask_march_21]
march_21_min_temp = min_temp[mask_march_21]
march_21_max_temp = max_temp[mask_march_21]

# --- Save all plots to PDF ---
with PdfPages("graf1.pdf") as pdf:
    # Plot 1: Annual Temperatures
    plt.figure(figsize=(12, 6))
    plt.plot(unique_years, annual_avg_temp, label="Průměrná teplota", color="green")
    plt.plot(unique_years, annual_min_temp, label="Minimální teplota", color="blue")
    plt.plot(unique_years, annual_max_temp, label="Maximální teplota", color="red")
    plt.title("Roční průměrné, minimální a maximální teploty")
    plt.xlabel("Rok")
    plt.ylabel("Teplota (°C)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    pdf.savefig()
    plt.close()

with PdfPages("graf2.pdf") as pdf:
    # Plot 2: Monthly Temperatures
    plt.figure(figsize=(12, 6))
    plt.plot(unique_months, monthly_avg_temp, label="Průměrná teplota", color="green", marker="o")
    plt.plot(unique_months, monthly_min_temp, label="Minimální teplota", color="blue", marker="o")
    plt.plot(unique_months, monthly_max_temp, label="Maximální teplota", color="red", marker="o")
    plt.title("Měsíční průměrné, minimální a maximální teploty")
    plt.xlabel("Měsíc")
    plt.ylabel("Teplota (°C)")
    plt.xticks(unique_months)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    pdf.savefig()
    plt.close()

with PdfPages("graf3.pdf") as pdf:
    # Plot 3: Monthly Precipitation
    plt.figure(figsize=(12, 6))
    plt.plot(unique_months, monthly_avg_precip, label="Průměrné srážky", color="green", marker="o")
    plt.plot(unique_months, monthly_min_precip, label="Minimální srážky", color="blue", marker="o")
    plt.plot(unique_months, monthly_max_precip, label="Maximální srážky", color="red", marker="o")
    plt.title("Měsíční průměrné, minimální a maximální srážky")
    plt.xlabel("Měsíc")
    plt.ylabel("Srážky (mm)")
    plt.xticks(unique_months)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    pdf.savefig()
    plt.close()

with PdfPages("graf4.pdf") as pdf:
    # Plot 4: march 21st Temperatures
    plt.figure(figsize=(12, 6))
    plt.plot(march_21_years, march_21_avg_temp, label="Průměrná teplota", color="green", marker="o")
    #plt.plot(march_21_years, march_21_min_temp, label="Minimální teplota", color="blue", marker="o")
    #plt.plot(march_21_years, march_21_max_temp, label="Maximální teplota", color="red", marker="o")
    plt.title("Teploty 21. března každého roku")
    plt.xlabel("Rok")
    plt.ylabel("Teplota (°C)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    pdf.savefig()
    plt.close()
