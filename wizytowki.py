
from faker import Faker

class BaseContact:
   def __init__(self, imie, nazwisko, telefon_priv, email):
       self.imie = imie
       self.nazwisko = nazwisko
       self.telefon_priv = telefon_priv
       self.email=email

   
   def contact(self,imie,nazwisko,telefon_priv):
       print(f"Wybieram numer prywatny {telefon_priv} i dzwonię do {imie} {nazwisko}")

class BusinessContact(BaseContact):

    def __init__(self, stanowisko, nazwa_firmy, telefon_business, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.stanowisko = stanowisko
       self.nazwa_firmy=nazwa_firmy
       self.telefon_business=telefon_business

    def contact(self,imie,nazwisko,telefon_business):
       print(f"Wybieram numer służbowy {telefon_business} i dzwonię do {imie} {nazwisko}")   


def create_contacts(rodzaj,ilosc):
    faker = Faker()
    users = []


    for _ in range(ilosc):

        imie = faker.first_name()
        nazwisko = faker.last_name()
        stanowisko = faker.job()
        telefon_priv = faker.phone_number()
        telefon_business=faker.phone_number()
        email=imie+'.'+nazwisko+'@amazon.com'
        email_firmy=faker.company_email()
        domena_firmy=email_firmy.split('@')[1]
        nazwa_firmy=domena_firmy.split('.')[0]




        if rodzaj=='priv':
            user1=BaseContact(imie,nazwisko,telefon_priv,email)
            print(100*'-')
            user1.contact(imie,nazwisko,telefon_priv)
        else:
            user = BusinessContact(imie,nazwisko,stanowisko,nazwa_firmy, telefon_priv,email, telefon_business)
            print(100*'-')
            user.contact(imie,nazwisko,telefon_business)


   
create_contacts('priv',3)
create_contacts('biz',5)


