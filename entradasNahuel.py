#!/usr/bin/python3
import json
import requests
import datetime
import time
import re

TOKEN = "5649405085:AAEGtL1PMSbMhsn2HNbOLLRUq0tiGoZVgCs"
chat_id = "360371488"
lector=open("control/entradas.txt", "r")
today = time.strftime("%d:%m:%Y")
      
for linea in lector:
    linea = linea.rstrip()
    if re.search('^1229:.+:.+:.+:.+:6666', linea):
        cadena = linea
        separador = ":"
separado_por_espacios = cadena.split(separador)

HORAS_DE_TRABAJO= 700
legajo = separado_por_espacios [0]
dia = separado_por_espacios [1]
mes = separado_por_espacios [2]
ano = separado_por_espacios [3]
horas = separado_por_espacios [4]
minutos = separado_por_espacios [5]
reloj_entrada = separado_por_espacios [7]
hora = int(horas)
minuto = int(minutos)
entre = (horas)+':'+(minutos)
calSalida= horas + minutos
salida= int(calSalida) + int(HORAS_DE_TRABAJO)
exit=str(salida)
andate= (exit[0]+exit[1]+":"+exit[2]+exit[3])
print (andate)
msgTelegram=("Buenos dias Nahuel" +" "+"hoy"+" ")+(dia+"/"+mes+"/"+ano)+(" "+"llegastes a las:"+" ")+(entre)+(" "+"hs."+" "+ "La jornada laboral concluye a las:"+" ") + (andate)+" Hs."  
lector.close()
print (msgTelegram)
url = f" https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={msgTelegram}"
print(requests.get(url).json())
