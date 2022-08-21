import tweepy
import time
import requests
import json
from datetime import datetime, timedelta

iTOKEN = '5817244e2eee03817157a946ca2ea992'
iCIDADE = 4975

api_key = 'Hb1SjiZT5FnK1qBQQtnvqnpxB'
api_secret_key = 'IRIWqtslJGoBhl9wKpOMRRVACuJmJ2ZN3WgGKRPC5vUdaz8SIE'
acess_key = '1557402665486802948-3QeyZuzJBbnZ193xqZBsTcZ0YqqnXe'
acess_secret = 'xBZBQHRXNCFUUgJeAPbLFuYv1xioQeDlWZpz6A51ughxj'
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(acess_key, acess_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
print('Iniciando o Bot')


def principal():
    try:
        iURL = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/" + str(iCIDADE) + "/current?token=" + iTOKEN
        iRESPONSE = requests.request("GET", iURL)
        iRETORNO_REQ = json.loads(iRESPONSE.text)

        Temperatura = iRETORNO_REQ['data']['temperature']
        Condicao = str(iRETORNO_REQ['data']['condition'])
        sensacao = str(iRETORNO_REQ['data']['sensation'])
        velVento = str(iRETORNO_REQ['data']['wind_velocity'])
        
    
        if Temperatura < 20 and Temperatura > 6 :
            formatString = f'Clima em Lages:' + '\n'+ 'Hora local: '+datetime.today().strftime('%A, %B %d, %Y %H:%M:%S') + '\nSaia de Japona Homee!'+'\nTemperatura: ' + str(Temperatura) + '°C' + '\nSensação Térmica: ' + sensacao + '°C' + '\nCondição Atual: ' + Condicao + '\nVelocidade do vento: ' + velVento +' Km/h'
        elif Temperatura <= 6:
            formatString = f'Clima em Lages:' + '\n'+ 'Hora local: '+datetime.today().strftime('%A, %B %d, %Y %H:%M:%S') + '\nSaia com umas 3 Japona Homee!'+'\nTemperatura: ' + str(Temperatura) + '°C' + '\nSensação Térmica: ' + sensacao + '°C' + '\nCondição Atual: ' + Condicao + '\nVelocidade do vento: ' + velVento +' Km/h'
        
        else:
            formatString = f'Clima em Lages:' + '\n'+ 'Hora local: '+datetime.today().strftime('%A, %B %d, %Y %H:%M:%S') + '\nMas bah hame do ceu, ta calor.'+'\nTemperatura: ' + str(Temperatura) + '°C' + '\nSensação Térmica: ' + sensacao + '°C' + '\nCondição Atual: ' + Condicao + '\nVelocidade do vento: ' + velVento +' Km/h'
        
        api.update_status(formatString)
        print(f'Status Update '+ datetime.today().strftime('%A, %B %d, %Y %H:%M:%S'))
    except:
        print(f'Bot deu problema ' + datetime.today().strftime('%A, %B %d, %Y %H:%M:%S'))

while True:
    dt = datetime.now() + timedelta(hours=2)
    principal()
    dt = dt.replace(minute=10)

    
    while datetime.now() < dt:
        time.sleep(1)
        if (datetime.now().minute % 10) == 0 and datetime.now().second == 00:
            print(f'Estou funcionando '+ datetime.today().strftime('%A, %B %d, %Y %H:%M:%S'))

#py -3 bot.py