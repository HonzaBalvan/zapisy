def vypis_hvezdicky(n):
    print("*" * n)

def vypis_nozicku(sirka, nozicka, n):
    if n == sirka:
        print("*" * nozicka, end="")
    else:
        print(" " * nozicka, end="")

def sipka(sirka, nozicka, n=1):
    if sirka == n:
        vypis_nozicku(sirka, nozicka, n)
        vypis_hvezdicky(n)
    else:
        vypis_nozicku(sirka, nozicka, n)
        vypis_hvezdicky(n)
        sipka(sirka, nozicka, n+1)
        vypis_nozicku(sirka, nozicka, n)
        vypis_hvezdicky(n)

sipka(6, 20) 