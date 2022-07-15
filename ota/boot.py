#-----------
#bibliotecas
#-----------
import esp
esp.osdebug(None)
#essa classe garante que toda memoria em desuso vai ser liberada
import gc
gc.collect() 
import network
from time import sleep

#-------------------
#Conectar com o wifi
#-------------------

ssid = "carpeado"
password = "142704@lcs"

#sistema que vai conectar a EPS ao seu wifi
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
sleep(6)

#Caso de tudo certo vai conectar e notificar
if station.isconnected() == True:
    print('Conectado com Sucesso')
    print(station.ifconfig())
    
#Se der errado a mensagem abaixo aparece
else:
    print("Problemas ao se conectar\nReveja os dados da Wi-Fi em boot.py")

#---
#OTA
#---
token = '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'
from duck import Duck
OTA = Duck(user="rafaelbhcosta", repo="teste", working_dir="ota", files=["main.py"], headers={'Authorization': 'token {}'.format(token)})
try:
    if OTA.update():
        print('Novos arquivos encontrados. Baixando!')
        for x in range(6):
            print('.', end='')
            sleep(1)
        print('Reiniciando!')
        sleep(2)
        machine.reset()

except:
    print('Sem atualizações no momento.')
    None

