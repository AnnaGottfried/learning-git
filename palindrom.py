def palindrom(tekst):
    txt=tekst[::-1]
    
    print(txt)    
    if tekst==txt:
        print(' nazwa %s jest palindromem'% tekst)
        return True
    else:
         print(' nazwa %s nie jest palindromem'% tekst) 
         return False  

palindrom('kajak')

palindrom('potop')

palindrom('zamek')

