# test odpovědi podle čísla


cas = float(input("Zadejte čas: "))

if cas<0:
    print("Zadejte platný čas")
elif cas>=24:
    print("Zadejte platný čas")
elif cas<6:
    print("Dobrou noc")
elif cas<10:
    print("Dobré ráno")
elif cas == 12:
    print("Dobré poledne")
elif cas<18:
    print("Dobrý den")
elif cas<22:
    print("Dobrý večer")
else:
    print("Dobrou noc")