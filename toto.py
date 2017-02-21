#!/home/pi python
# -*- coding: utf-8 -*-

# Le Raspbery Pi envoie des messages à l'Arduino

import serial # bibliothèque permettant la communication série
import time # pour le délai d'attente entre les messages
import random # pour créer des chiffres aléatoires

portUSB = serial.Serial('/dev/ttyACM0', 115200)

portCARBERRY = serial.Serial('/dev/ttyAMA0', 115200)

def envoi(variable, nomparametre):
	message = nomparametre + ("={}".format(variable))
	portUSB.write(message)
	time.sleep(0.01)

def envoidetouteslesvariables():
	envoi(braketempFL, 'braketempFL')
	envoi(braketempFR, 'braketempFR')
	envoi(braketempRL, 'braketempRL')
	envoi(braketempRR, 'braketempRR')
	envoi(gear, 'gear')
	envoi(vehiclespeed, 'vehiclespeed')
	envoi(TC, 'TC')
	envoi(fuelconsumption, 'fuelconsumption')
	envoi(enginetemp, 'enginetemp')
	envoi(oiltemp, 'oiltemp')
	envoi(mapposition, 'mapposition')
	envoi(RPM, 'RPM')
	envoi(boiteauto, 'boiteauto')
	envoi(boitesequentielle, 'boitesequentielle')
	
def programmeCAN():
	portCARBERRY.write('AT\r\n')
	reponsetest = portCARBERRY.read()
	if (reponsetest == 'OK\r\n')
	 	braketempFL = receptiondonneeCAN('CH2', adresse, '100') 
		braketempFR = receptiondonneeCAN('CH2', adresse, '100')
		braketempRL = receptiondonneeCAN('CH2', adresse, '100')
		braketempRR = receptiondonneeCAN('CH2', adresse, '100')
		gear = receptiondonneeCAN('CH1', adresse, '200')
		vehiclespeed = receptiondonneeCAN('CH1', adresse, '200')
		TC = receptiondonneeCAN()
		fuelconsumption = receptiondonneeCAN('CH1', adresse, '200')
		enginetemp = receptiondonneeCAN('CH1', adresse, '20')
		oiltemp = receptiondonneeCAN('CH1', adresse, '20')
		mapposition = receptiondonneeCAN('CH1', adresse, '10')
		RPM = receptiondonneeCAN('CH1', adresse, '200')
		boiteauto = receptiondonneeCAN()
		boitesequentielle = receptiondonneeCAN()
	else
		message = ("erreur CARBERRY")
		portUSB.write(message)
		time.sleep(0.01)


def receptiondonneeCAN(numeroCAN, adresse, rafraichissement)
	mode = ("CAN MODE USER")
	portCARBERRY.write(mode)
	valeurerreur = testreceptionOK('mode')
	
	if (valeurerreur = 1)
		open = ("CAN USER OPEN {} {}".format(numeroCAN, rafraichissement))
		portCARBERRY.write(open)
		valeurerreur = testreceptionOK('open')
		
		if (valeurerreur = 1)
			alignement = ("CAN USER ALIGN RIGHT")
			portCARBERRY.write(alignement)
			valeurerreur = testreceptionOK('alignement')
			
			if (valeurerreur = 1)
				ODBquerry = ("OBD QUERY {} {}".format(numeroCAN, adresse))
				messagebrut = portCARBERRY.read()
				valeur = decodage(messagebrut)
	return valeur
	
def decodage(messagecarberrybrut)
	i=0
	while (messagecarberrybrut[i]!= '\r\n')
		messagecarberry[i]=messagecarberrybrut[i]
		i += 1
	variablestring = messagecarberry.replace(' ', '')
	variableint = int(variablestring)
	return variableint

def testreceptionOK(typeerreur):
	reponsetest = portCARBERRY.read()
	if (reponsetest == 'OK\r\n')
		receptiondonneeCAN()
		return 1
	else
		message = ("erreur CARBERRY ") + typeerreur
		portUSB.write(message)
		time.sleep(0.01)
		return 0

	

while True: # boucle répétée jusqu'à l'interruption du programme
	envoidetouteslesvariables()
	programmeCAN()

