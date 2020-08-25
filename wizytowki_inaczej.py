
from faker import Faker

class BaseContact:
   def __init__(self, imie, nazwisko, telefon_priv, email):
       self.imie = imie
       self.nazwisko = nazwisko
       self.telefon_priv = telefon_priv
       self.email=email

   
   def contact(self):
       print("Wybieram numer prywatny {} i dzwonię do {} {}".format(self.telefon_priv,self.imie,self.nazwisko))

class BusinessContact(BaseContact):

    def __init__(self, stanowisko, nazwa_firmy, telefon_business, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.stanowisko = stanowisko
       self.nazwa_firmy=nazwa_firmy
       self.telefon_business=telefon_business

    def contact(self):
       print(f"Wybieram numer służbowy {self.telefon_business} i dzwonię do {self.imie} {self.nazwisko}")   


def create_contacts(rodzaj,ilosc):
    faker = Faker()
    users=[]

    if rodzaj=='priv':
        return [BaseContact(imie=faker.first_name(), nazwisko=faker.last_name(),telefon_priv=faker.phone_number(),email=faker.company_email()) for _ in range(ilosc)]

    elif rodzaj=='biz':
        return [BusinessContact(imie=faker.first_name(), nazwisko=faker.last_name(),stanowisko=faker.job(),nazwa_firmy=faker.company(), email=faker.company_email(), telefon_priv=faker.phone_number(), telefon_business=faker.phone_number()) for _ in range(ilosc)]

    else:
        return []

kontakty = create_contacts('priv', 8) + create_contacts('biz', 10)

for card in kontakty:
    card.contact()  




    



