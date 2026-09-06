vystup = []

with open("nastaveni_emailu.txt", encoding="utf-8") as soubor:
    soubor_radky = soubor.readlines()

    for radek_souboru in soubor_radky: #tady se do proměnné 'vystup' připíší všechny řádky, které NEzačínají '@'
        radek_split = radek_souboru.split(",")
        if radek_split[0] != "@":
            vystup.append(",".join(radek_split))

vystup.append(f"@, {input("Zadejte adresu SMTP serveru: ")}\n")
print(vystup[-1])
while not vystup[-1]:
    print("Špatný formát vstupu.")
    vystup.pop()
    vystup.append(f"@, {input("Zadejte adresu SMTP serveru: ")}\n")

vystup.append(f"@, {input("Zadejte port SMTP serveru (většinou 587): ")}\n")
while not vystup[-1] or not vystup[-1].strip().isnumeric():
    print("Špatný formát vstupu.")
    vystup.pop()
    vystup.append(f"@, {input("Zadejte port SMTP serveru (většinou 587): ")}\n")

vystup.append(f"@, {input("Zadejte uživatelské jméno na SMTP serveru: (většinou celá e-mailová adresa): ")}\n")
while not vystup[-1]:
    print("Špatný formát vstupu.")
    vystup.pop()
    vystup.append(f"@, {input("Zadejte uživatelské jméno na SMTP serveru: (většinou celá e-mailová adresa): ")}\n")

vystup.append(f"@, {input("Zadejte heslo pro přihlášení k SMTP serveru (většinou stejné jako pro běžné přihlašování): ")}\n")
while not vystup[-1]:
    print("Špatný formát vstupu.")
    vystup.pop()
    vystup.append(f"@, {input("Zadejte heslo pro přihlášení k SMTP serveru (většinou stejné jako pro běžné přihlašování): ")}\n")

vystup.append(f"@, {input("Zadejte svoji e-mailovou adresu: ")}\n")
while not vystup[-1]:
    print("Špatný formát vstupu.")
    vystup.pop()
    vystup.append(f"@, {input("Zadejte svoji e-mailovou adresu: ")}\n")

vystup.append(f"@, {input("Zadejte e-mailovou adresu adresáta (popř. více e-mailových adres oddělených čárkou a mezerou): ")}\n")
while not vystup[-1]:
    print("Špatný formát vstupu.")
    vystup.pop()
    vystup.append(f"@, {input("Zadejte e-mailovou adresu adresáta (popř. více e-mailových adres oddělených čárkou a mezerou): ")}\n")

vystup.append(f"@, {input("Zadejte počet dní do konce lhůty, kdy má program zaslat e-mail: ")}\n")
while not vystup[-1] or not vystup[-1].strip().isnumeric():
    print("Špatný formát vstupu.")
    vystup.pop()
    vystup.append(f"@, {input("Zadejte počet dní do konce lhůty, kdy má program zaslat e-mail: ")}\n")

with open("nastaveni_emailu.txt", "w", encoding="utf-8") as soubor: #tady se soubor vymaže
    soubor.write("")

with open("nastaveni_emailu.txt", "a", encoding="utf-8") as soubor: #tady se do souboru přepíše proměnná 'vystup'
    for radek in vystup:
        soubor.write(str(radek))
