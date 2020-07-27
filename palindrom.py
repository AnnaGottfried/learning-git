def palindrom(tekst):
    txt=tekst[::-1]
    
    print(txt)    
    if tekst==txt:
        print(' nazwa %s jest palindromem'% tekst)
    else:
         print(' nazwa %s nie jest palindromem'% tekst)   

palindrom('kajak')

palindrom('potop')

palindrom('zamek')

