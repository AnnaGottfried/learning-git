import requests
import csv
import json

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()


with open('waluty.csv', 'w', newline='') as file:
    writer = csv.writer(file,delimiter=";")
    writer.writerow(['Kursy kupna i sprzedaży walut obcych – tabela C- NBP'])
    writer.writerow(['na dzien: '+data[0]["effectiveDate"] ])
    writer.writerow(["Currency", "Code", "Bid","Ask"])
    for item in data[0]["rates"]:
        
        writer.writerow([item['currency'],item['code'],item['bid'],item['ask']])

 #   for item in data[0]["rates"]:

 #       print(item['currency'])



#currency;code;bid;ask





'''
[
    {'table': 'C', 
    
    'no': '168/C/NBP/2020', 
    'tradingDate': '2020-08-27', 
    'effectiveDate': '2020-08-28', 
    'rates': 
       [
        {'currency': 'dolar amerykański',
         'code': 'USD', 
         'bid': 3.6976, 
         'ask': 3.7724}, 
         
         {'currency': 'dolar australijski', 
         'code': 'AUD', 
         'bid': 2.6789, 
         'ask': 2.7331}, 
         
         {
         'currency': 'dolar kanadyjski', 
         'code': 'CAD', 
         'bid': 2.819, 
         'ask': 2.876}, 
         
         {'currency': 'euro', 
         'code': 'EUR', 
         'bid': 4.3647, 
         'ask': 4.4529},
          {'currency': 'forint (Węgry)', 
          'code': 'HUF', 
          'bid': 0.012252, 
          'ask': 0.0125}, 
          
          {'currency': 'frank szwajcarski', 
          'code': 'CHF', 
          'bid': 4.0672, 
          'ask': 4.1494}
          , 
          {'currency': 'funt szterling', 
          'code': 'GBP', 
          'bid': 4.8822, 
          'ask': 4.9808},
           {'currency': 'jen (Japonia)', 'code': 'JPY', 'bid': 0.034809, 'ask': 0.035513}, {'currency': 'korona czeska', 'code': 'CZK', 'bid': 0.1661, 'ask': 0.1695}, {'currency': 'korona duńska', 'code': 'DKK', 'bid': 0.5865, 'ask': 0.5983}, {'currency': 'korona norweska', 'code': 'NOK', 'bid': 0.4149, 'ask': 0.4233}, {'currency': 'korona szwedzka', 'code': 'SEK', 'bid': 0.4235, 'ask': 0.4321}, {'currency': 'SDR (MFW)', 'code': 'XDR', 'bid': 5.2284, 'ask': 5.334}
        ]
        }
           
     ]
'''

