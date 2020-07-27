operacja=input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
liczba1=int(input("Podaj pierwszą liczbę: "))
liczba2=int(input("Podaj drugą liczbę: "))

if operacja=="1":
    wynik=liczba1+liczba2
    rodzaj="dodawanie"
elif operacja=="2":
    wynik=liczba1-liczba2
    rodzaj="odejmowanie"
elif operacja=="3":
    wynik=liczba1*liczba2
    rodzaj="mnożenie"
elif operacja=="4":
    wynik=liczba1/liczba2
    rodzaj="dzielenie"
else:
    exit(1)      


print("wynikiem operacji {} jest {}".format(rodzaj, wynik))              