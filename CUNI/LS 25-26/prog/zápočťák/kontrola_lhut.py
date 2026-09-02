import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta
import time

# Email configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "muj"
SMTP_PASSWORD = ""
SENDER_EMAIL = "muj"
RECIPIENT_EMAIL = "jeho"

# How many days in advance to send the email
DAYS_IN_ADVANCE = 7

def posliEmail(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SENDER_EMAIL, [RECIPIENT_EMAIL], msg.as_string())

def kontrolaLhut(databaze):
    while True:
        datum_dnes = datetime.now().date()
        for polozka in databaze:
            datum_polozky = polozka[2].split("/")
            print(*datum_polozky)
            if (datetime(int(datum_polozky[0]), int(datum_polozky[1]), int(datum_polozky[2])).date() - datum_dnes) == timedelta(days=DAYS_IN_ADVANCE):
                subject = f"Upozornění z evidence"
                body = f"Lhůta položky '{polozka[1]}' se blíží!\nJméno: {polozka[1]}\nDatum: {polozka[2]}\nPočet: {polozka[3]}\nKategorie: {polozka[4]}"
                posliEmail(subject, body)
                print(f"Email sent for {polozka[1]}")
        
        #time.sleep(60*30)
