from flask import Flask, render_template, request
from datetime import datetime
import requests
import json

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

app=Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def welcome():

    waluta=''
    waluta1 = ''
    if request.method == "POST":
        dane = request.form
        waluta = dane.get('waluta')
        dlugosc=len(waluta)
        ilosc = dane.get('ilosc')
        waluta1=waluta.strip()
        dlugosc1=len(waluta1)
      #  wynik=0.00

        for item in data[0]["rates"]:
            if item['currency'] == waluta1:
                wynik=item['bid']*float(ilosc)

     #   return "Wybrana waluta: "+waluta1+"dlugosc"+str(dlugosc1)+" wybrana ilosc: "+ilosc+"wynik calkowity to"+str(wynik)
        return render_template("kalkulator_walut.html", message=str(data[0]["effectiveDate"]),
                           tablica=data[0]['table'], data=data[0]["rates"], wynik=round(wynik,2), waluta1=dane.get('waluta'), ilosc=ilosc,
                               opis="Wybrana waluta: "+waluta1+", wybrana ilość: "+ilosc+".   Wynik calkowity to: "+str(round(wynik,2)))


    if request.method == "GET":
        return render_template("kalkulator_walut.html",message=str(data[0]["effectiveDate"]),
                            tablica=data[0]['table'],data= data[0]["rates"],wynik=0.00, waluta1='    ', ilosc=0)


@app.route("/date")
def date():
    return "this page was served at "+str(datetime.now())

counter=0
@app.route("/counter_views")
def counter_views():
    global counter
    counter+=1

    return "this page was served "+str(counter)+ " times"