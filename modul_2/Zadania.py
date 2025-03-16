

def zadanie_1():
    dane_wejsciowe = input("Dane wejściowe: \n")
    separator_zrodlowy = input("Separator źródłowy: \n")
    separator_docelowy = input("Separator docelowy: \n")

    dane_split = dane_wejsciowe.split(separator_zrodlowy)
    dane_join = separator_docelowy.join(dane_split)
    print(dane_join)



def zadanie_2():
    print("zadanie 2")

def zadanie_3():
    print("zadanie 3")


def zadanie_4():
    print("zadanie 4")
       

def main():
    zadanie_1()
    # zadanie_2()
    # zadanie_3()
    # zadanie_4()


if __name__ == "__main__":
    main()
