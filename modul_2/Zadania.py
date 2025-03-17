

def zadanie_1():
    print("**** Zadanie 1 ****")

    dane_wejsciowe = input("dane wejsciowe: \n")
    separator_zrodlowy = input("separator zrodlowy: \n")
    separator_docelowy = input("separator docelowy: \n")

    dane_split = dane_wejsciowe.split(separator_zrodlowy)
    dane_join = separator_docelowy.join(dane_split)
    print(dane_join)



def zadanie_2():
    print("**** Zadanie 2 ****")

    dane_wejsciowe = input("Dane wejściowe:\n")

    slice = len(dane_wejsciowe) // 2
    print(dane_wejsciowe[slice:])
    print(dane_wejsciowe[:slice])
    print(dane_wejsciowe[::-2])


def zadanie_3():
    print("**** Zadanie 3 ****")

    dane_wejsciowe = "Ala ma kota"

    print(dane_wejsciowe.title())
    print(dane_wejsciowe.capitalize())
    print(dane_wejsciowe.zfill(30))
    print(dane_wejsciowe.upper())
    print(dane_wejsciowe.count("a"))
    print(dane_wejsciowe.center(50))


def zadanie_4():
    print("**** Zadanie 4 ****")

    dane_wejsciowe = input("Podaj lancuch znaków:\n")

    print(f"Lancuch {dane_wejsciowe} isalpha(): {dane_wejsciowe.isalpha()}")
    print(f"Lancuch {dane_wejsciowe} isascii(): {dane_wejsciowe.isascii()}")
    print(f"Lancuch {dane_wejsciowe} isprintable(): {dane_wejsciowe.isprintable()}")
    print(f"Lancuch {dane_wejsciowe} istitle(): {dane_wejsciowe.istitle()}")
    print(f"Lancuch {dane_wejsciowe} isupper(): {dane_wejsciowe.isupper()}")
       

def main():
    # zadanie_1()
    # zadanie_2()
    # zadanie_3()
    # zadanie_4()


if __name__ == "__main__":
    main()
