def kontrola(vstup_list: list, zavorky):
    for zavorka in zavorky:
        if len(zavorka[0]) == 1 and vstup_list.count(zavorka[0]) != vstup_list.count(zavorka[1]):
            return "ne"

        if len(zavorka[0]) == 2:
            pocitadlo = 0
			
            i = 0
            while i < len(vstup_list) - 1:
                if vstup_list[i] == zavorka[0][0] and vstup_list[i+1] == zavorka[0][1]:
                    pocitadlo += 1

                    vstup_list.pop(i)
                    vstup_list.pop(i)
                    
                    i -= 1
                    
                if vstup_list[i] == zavorka[1][0] and vstup_list[i+1] == zavorka[1][1]:
                    pocitadlo -= 1

                    vstup_list.pop(i)
                    vstup_list.pop(i)

                    i -= 1
                i += 1

            if pocitadlo != 0:
                return "ne"

    return "ano"

zavorky = [("(", ")"), ("[", "]"), ("{", "}"), ("/*", "*/"), ("<?", "?>")]

vstup_file = open("zavorky.in", encoding="utf-8")
vstup_list = list(vstup_file.read())

print(kontrola(vstup_list, zavorky))
