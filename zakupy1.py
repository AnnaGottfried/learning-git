zakupy={ 'Piekarnia': ['Chleb', 'Pączek', 'Bułki'],
'Warzywniak':['Marchew', 'Seler', 'Rukola']
}
print('Lista zakupow')

ilosc_przedmiotow=0
for place, item in zakupy.items():
    print('Ide do {}, kupuje {}'.format(place,item))
    for produkt in item:
        ilosc_przedmiotow+=1


print('W sumię kupuje {} produktów'.format(ilosc_przedmiotow))   
print('nie cierpię Monthy Pythona')

