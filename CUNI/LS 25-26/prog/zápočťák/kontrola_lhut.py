import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta
import time

def posliEmail(subject, body, nastaveni):
    SMTP_SERVER = nastaveni[0][0].strip()
    SMTP_PORT = int(nastaveni[1][0])
    SMTP_USERNAME = nastaveni[2][0].strip()
    SMTP_PASSWORD = nastaveni[3][0].strip()
    SENDER_EMAIL = nastaveni[4][0].strip()
    RECIPIENT_EMAIL = [email.strip() for email in nastaveni[5]]


    print(SMTP_SERVER)
    print(SMTP_PORT)
    print(SMTP_USERNAME)
    print(SMTP_PASSWORD)
    print(SENDER_EMAIL)
    print(RECIPIENT_EMAIL)

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = ", ".join(RECIPIENT_EMAIL)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())

def kontrolaLhut(databaze):
    with open("nastaveni_emailu.txt", "r") as nastaveni_emailu:
        nastaveni_radky = nastaveni_emailu.readlines()
    
        nastaveni = []

        for radek_nastaveni in nastaveni_radky:
            radek_split = radek_nastaveni.split(",")

            if radek_split[0] == "@": #kontrola formátu
                radek_split.pop(0)
                nastaveni.append(radek_split)

    DAYS_IN_ADVANCE = int(nastaveni[6][0])

    datum_dnes = datetime.now().date()
    for polozka in databaze:
        datum_polozky = polozka[2].split("/")
        if (datetime(int(datum_polozky[0]), int(datum_polozky[1]), int(datum_polozky[2])).date() - datum_dnes) == timedelta(days=DAYS_IN_ADVANCE):
            subject = f"Upozornění z evidence"
            body = f"Lhůta položky '{polozka[1]}' se blíží!\nJméno: {polozka[1]}\nDatum: {polozka[2]}\nPočet: {polozka[3]}\nKategorie: {polozka[4]}"
            posliEmail(subject, body, nastaveni)
            print(f"Email sent for {polozka[1]}")
