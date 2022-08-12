import tweepy
import time
import requests
import json
from datetime import datetime

iTOKEN = '5817244e2eee03817157a946ca2ea992'
iCIDADE = 4975

api_key = 'Hb1SjiZT5FnK1qBQQtnvqnpxB'
api_secret_key = 'IRIWqtslJGoBhl9wKpOMRRVACuJmJ2ZN3WgGKRPC5vUdaz8SIE'
acess_key = '1557402665486802948-3QeyZuzJBbnZ193xqZBsTcZ0YqqnXe'
acess_secret = 'xBZBQHRXNCFUUgJeAPbLFuYv1xioQeDlWZpz6A51ughxj'
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(acess_key, acess_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

while True:
    iURL = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/" + str(iCIDADE) + "/current?token=" + iTOKEN
    iRESPONSE = requests.request("GET", iURL)
    iRETORNO_REQ = json.loads(iRESPONSE.text)

    Temperatura = str(iRETORNO_REQ['data']['temperature'])
    Condicao = str(iRETORNO_REQ['data']['condition'])
    sensacao = str(iRETORNO_REQ['data']['sensation'])
    velVento = str(iRETORNO_REQ['data']['wind_velocity'])
 
    formatString = f'Clima em Lages:' + '\n'+datetime.today().strftime('%A, %B %d, %Y %H:%M:%S')+'\nTemperatura: ' + Temperatura + '°C' + '\nSensação Térmica: ' + sensacao + '°C' + '\nCondição Atual: ' + Condicao + '\nVelocidade do vento: ' + velVento +' Km/h'
    api.update_status(formatString)
    print(datetime.today().strftime('%A, %B %d, %Y %H:%M:%S'))
    time.sleep(60*60)