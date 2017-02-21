#!/home/pi python
# -*- coding: utf-8 -*-

# Le Raspbery Pi envoie des messages à l'Arduino

import serial # bibliothèque permettant la communication série
import time # pour le délai d'attente entre les messages
import random # pour créer des chiffres aléatoires

portUSB = serial.Serial("/dev/ttyACM0", 115200)

portCARBERRY = serial.Serial("/dev/ttyAMA0", 115200)

def envoi(variable, nomparametre):
	message = nomparametre + ("={}".format(variable))
	portUSB.write(message)
	time.sleep(0.01)

def envoidetouteslesvariables():
	envoi(braketempFL, "braketempFL")
	envoi(braketempFR, "braketempFR")
	envoi(braketempRL, "braketempRL")
	envoi(braketempRR, "braketempRR")
	envoi(gear, "gear")
	envoi(vehiclespeed, "vehiclespeed")
	envoi(TC, "TC")
	envoi(fuelconsumption, "fuelconsumption")
	envoi(enginetemp, "enginetemp")
	envoi(oiltemp, "oiltemp")
	envoi(mapposition, "mapposition")
	envoi(RPM, "RPM")
	envoi(boiteauto, "boiteauto")
	envoi(boitesequentielle, "boitesequentielle")
	
def programmeCAN():
	portCARBERRY.write("AT\r\n")
	envoipossible = testreceptionOK("initialisation Carberry")
	
	if (envoipossible == 1)
	 	braketempFL = receptiondonneeCAN("CH2", adresse, "100") 
		braketempFR = receptiondonneeCAN("CH2", adresse, "100")
		braketempRL = receptiondonneeCAN("CH2", adresse, "100")
		braketempRR = receptiondonneeCAN("CH2", adresse, "100")
		gear = receptiondonneeCAN("CH1", adresse, "200")
		vehiclespeed = receptiondonneeCAN("CH1", adresse, "200")
		TC = receptiondonneeCAN()
		fuelconsumption = receptiondonneeCAN("CH1", adresse, "200")
		enginetemp = receptiondonneeCAN("CH1", adresse, "20")
		oiltemp = receptiondonneeCAN("CH1", adresse, "20")
		mapposition = receptiondonneeCAN("CH1", adresse, "10")
		RPM = receptiondonneeCAN("CH1", adresse, "200")
		boiteauto = receptiondonneeCAN()
		boitesequentielle = receptiondonneeCAN()



def receptiondonneeCAN(numeroCAN, adresse, rafraichissement)
	mode = ("CAN MODE USER")
	portCARBERRY.write(mode)
	etapesuivante = testreceptionOK("mode")
	
	if (etapesuivante = 1)
		open = ("CAN USER OPEN {} {}".format(numeroCAN, rafraichissement))
		portCARBERRY.write(open)
		etapesuivante = testreceptionOK("open")
		
		if (etapesuivante = 1)
			alignement = ("CAN USER ALIGN RIGHT")
			portCARBERRY.write(alignement)
			etapesuivante = testreceptionOK("alignement")
			
			if (etapesuivante = 1)
				ODBquerry = ("OBD QUERY {} {}".format(numeroCAN, adresse))
				portCARBERRY.write(ODBquerry)
				messagebrut = portCARBERRY.read()
				valeurducapteur = decodage(messagebrut)
	return valeurducapteur
	
def decodage(messagecarberrybrut) # message brut du type : 1A 2B 32 <CR><LF>
	messagecarberrybrut = messagecarberrybrut.replace(("\r","") # on enleve le <CR> du fin de message : 1A 2B 32 <LF>
	messagecarberrybrut = messagecarberrybrut.replace(("\n","") # puis on enleve le <LF> : 1A 2B 32 
	variablestring = messagecarberrybrut.replace(" ", "") # on enleve maintenant les espaces seperant les differents caracteres : 1A2B32 (du type str)
	variableint = int(variablestring, 16) # on transforme le string en int tout en passant en base 10 : 1714994 (du type int)
	return variableint

def testreceptionOK(typeerreur):
	reponsetest = portCARBERRY.read()
	if (reponsetest == "OK\r\n")
		return 1
	else
		message = ("erreur CARBERRY ") + typeerreur
		portUSB.write(message)
		time.sleep(0.01)
		return 0

	

while True: # boucle répétée jusqu'à l'interruption du programme
	
	programmeCAN()
	envoidetouteslesvariables()

