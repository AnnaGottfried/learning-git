import random


class Filmy:
    liczba_odtw=0

    def __init__(self,tytul,rok,gatunek,liczba_odtw):
        self.tytul=tytul
        self.rok=rok
        self.gatunek=gatunek
        self.liczba_odtw=liczba_odtw

    def play(self):
        liczba_odtw+=1
        '''Po wyświetleniu filmu jako string widoczne są tytuł i rok wydania np. “Pulp Fiction (1994)”.'''

    def __str__(self):
        return f" {self.tytul} {self.rok}" 


class Seriale(Filmy):

    def __init__(self,numer_odc,numer_sezonu,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.numer_odc=numer_odc
        self.numer_sezonu=numer_sezonu
        

    def play(self):
        liczba_odtw+=1
        

    '''Po wyświetleniu serialu jako string, pokazują się informacje o konkretnym odcinku,
     np.: “The Simpsons S01E05”
     (gdzie po S pokazany jest numer sezonu w notacji dwucyfrowej,
      natomiast po E - numer odcinka, również w zapisie dwucyfrowym)    '''

    def __str__(self):
        return f" {self.tytul} {self.numer_sezonu}{self.numer_odc}" 





biblioteka=[]

biblioteka.append(Seriale(tytul="The Simpsons",rok="1995",gatunek="serial",liczba_odtw=0,numer_sezonu="S01",numer_odc="E05"))
biblioteka.append(Filmy(tytul="French Kiss",rok="1998", gatunek="film", liczba_odtw=0))
biblioteka.append(Seriale(tytul="Hallo Hallo",rok="1985",gatunek="serial",liczba_odtw=0,numer_sezonu="S01",numer_odc="E05"))
biblioteka.append(Filmy(tytul="Wszystko co słyszą kobiety",rok="2004", gatunek="film", liczba_odtw=0))
biblioteka.append(Seriale(tytul="Sex and the City",rok="1999",gatunek="serial",liczba_odtw=0,numer_sezonu="S01",numer_odc="E05"))
biblioteka.append(Filmy(tytul="Brigitte Jones",rok="2000", gatunek="film", liczba_odtw=0))
biblioteka.append(Filmy(tytul="Rambo",rok="1986", gatunek="film", liczba_odtw=0))
biblioteka.append(Filmy(tytul="Nietykalni",rok="2011", gatunek="film", liczba_odtw=0))
biblioteka.append(Filmy(tytul="Lista Schindlera",rok="1995", gatunek="film", liczba_odtw=0))


dlugosc=len(biblioteka)

lista_filmow=[]
lista_seriali=[]


def get_movies():

    for item in range(dlugosc):


       # print(biblioteka[item].gatunek)
        if biblioteka[item].gatunek=='film':
            lista_filmow.append(biblioteka[item].tytul)
        
    return lista_filmow           

def get_series():

    for item in range(dlugosc):


        if biblioteka[item].gatunek=='serial':
            lista_seriali.append(biblioteka[item].tytul)
        
    return lista_seriali       

wynik=get_movies()
wynik.sort()
print(f"Lista filmów: {wynik} ")


wynik1=get_series()
wynik1.sort()
print(f"Lista seriali: {wynik1}")
print("*"*70)

def search(szukany_tytul):

    for item in range(dlugosc):


        if biblioteka[item].tytul==szukany_tytul:
            print(f'Szukany film to: {biblioteka[item]}')


def generate_views():
    n = random.randint(0,dlugosc-1)
    losowo=random.randint(0,100)
   
    biblioteka[n].liczba_odtw=losowo
   
#    print(biblioteka[n].liczba_odtw)

    
def wielokrotne_views():

    for item in range(10):
        generate_views()



def sorttitles(movie):
    return movie.liczba_odtw

'''
def top_titles():

    biblioteka.sort(key=lambda x: x.liczba_odtw, reverse=True)
    for obj in biblioteka:
        print("Najlepsze filmy: " +str(obj.tytul) + " z rankingiem: " +str(obj.liczba_odtw))
'''
def top_titles(kategoria):

    biblioteka.sort(key=lambda x: x.liczba_odtw, reverse=True)
    for obj in biblioteka:
        if kategoria=="serial":
            if obj.gatunek=="serial":
                print("Najlepsze seriale: " +str(obj.tytul) + " z rankingiem: " +str(obj.liczba_odtw))
        else:
             if obj.gatunek=="film":
                 print("Najlepsze filmy: " +str(obj.tytul) + " z rankingiem: " +str(obj.liczba_odtw))   



search("Hallo Hallo")
wielokrotne_views()

top_titles("serial")
top_titles("film")





   

