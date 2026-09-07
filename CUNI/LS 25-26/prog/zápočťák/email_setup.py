vystup = []

def formatujAPripis(vystup, vec):
    vystup.append(f"@, {vec}\n")

with open("nastaveni_emailu.txt", encoding="utf-8") as soubor:
    soubor_radky = soubor.readlines()

    for radek_souboru in soubor_radky: #tady se do proměnné 'vystup' připíší všechny řádky, které NEzačínají '@'
        radek_split = radek_souboru.split(",")
        if radek_split[0] != "@":
            vystup.append(",".join(radek_split))

smtp_server = input("Zadejte adresu SMTP serveru: ")
while not smtp_server:
    print("Špatný formát vstupu.")
    smtp_server = input("Zadejte adresu SMTP serveru: ")
formatujAPripis(vystup, smtp_server)

smtp_port = input("Zadejte port SMTP serveru (většinou 587): ")
while not smtp_port or not smtp_port.strip().isnumeric():
    print("Špatný formát vstupu.")
    smtp_port = input("Zadejte port SMTP serveru (většinou 587): ")
formatujAPripis(vystup, smtp_port)

smtp_username = input("Zadejte uživatelské jméno na SMTP serveru: (většinou celá e-mailová adresa): ")
while not smtp_username:
    print("Špatný formát vstupu.")
    smtp_username = input("Zadejte uživatelské jméno na SMTP serveru: (většinou celá e-mailová adresa): ")
formatujAPripis(vystup, smtp_username)

smtp_password = input("Zadejte heslo pro přihlášení k SMTP serveru (většinou stejné jako pro běžné přihlašování): ")
while not smtp_password:
    print("Špatný formát vstupu.")
    smtp_password = input("Zadejte heslo pro přihlášení k SMTP serveru (většinou stejné jako pro běžné přihlašování): ")
formatujAPripis(vystup, smtp_password)

sender_mail = input("Zadejte svoji e-mailovou adresu: ")
while not sender_mail:
    print("Špatný formát vstupu.")
    sender_mail = input("Zadejte svoji e-mailovou adresu: ")
formatujAPripis(vystup, sender_mail)

recipient_mail = input("Zadejte e-mailovou adresu adresáta (popř. více e-mailových adres oddělených čárkou a mezerou): ")
while not recipient_mail:
    print("Špatný formát vstupu.")
    recipient_mail = input("Zadejte e-mailovou adresu adresáta (popř. více e-mailových adres oddělených čárkou a mezerou): ")
formatujAPripis(vystup, recipient_mail)

days_in_advance = input("Zadejte počet dní do konce lhůty, kdy má program zaslat e-mail: ")
while not days_in_advance or not days_in_advance.strip().isnumeric():
    print("Špatný formát vstupu.")
    days_in_advance = input("Zadejte počet dní do konce lhůty, kdy má program zaslat e-mail: ")
formatujAPripis(vystup, days_in_advance)

with open("nastaveni_emailu.txt", "w", encoding="utf-8") as soubor: #tady se soubor vymaže
    soubor.write("")

with open("nastaveni_emailu.txt", "a", encoding="utf-8") as soubor: #tady se do souboru přepíše proměnná 'vystup'
    for radek in vystup:
        soubor.write(str(radek))
