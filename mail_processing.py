#!/usr/bin/env python3

# Script python pour gérer et traiter les mails entrant (récupérés par le démon)

import smtplib 
import sys
import re
import datetime
import time


'''
Received: by souidi-GL63-8RD.univ-rennes1.fr (Postfix, from userid 1000)
	id E8F0882F6A; Thu, 12 Jan 2023 15:37:14 +0100 (CET)
Subject: mail sujet
To: <meldiffere+toto*enssat.fr-2023/02/09T14/20/00@enssat.fr>
User-Agent: mail (GNU Mailutils 3.14)
Date: Thu, 12 Jan 2023 15:37:14 +0100
Message-Id: <20230112143714.E8F0882F6A@souidi-GL63-8RD.univ-rennes1.fr>
From: Souidi <souidi@souidi-GL63-8RD>

mail body
'''

content=[]
for line in sys.stdin:
    content.append(line.rstrip())       # Récupération du mail par lignes

sujet = content[2][9:]                                          # Récupération du sujet du mail
destinataire = re.findall(r"<(.*?)>", content[3])[0]            # Récupération du destinataire (To: <meldiffere+toto*enssat.fr-2023/02/09T14/20/00@enssat.fr>) 3ème ligne
expediteur = re.findall(r"<(.*?)>", content[7])[0]              # Récupération de l'expéditeur (From: Souidi)
message = content[-1]                                           # Récupération du body du mail

try:                                                                           # Le mail est à differer
    dest_original_asterisk = re.findall(r"\+(.*?)-", destinataire)[0]          # Extraction de l'adresse de destination sans "To: " avec *
    date_cible_str = re.findall(r"-(.*?)@", destinataire)[0]                   # Exctraction de l'heure d'arrivée voulue du mail
    print(date_cible_str)
    print(dest_original_asterisk)

except:
    print("erreur dans l'adresse mail")

else:
    print("mail à différer")

    dest_original = dest_original_asterisk.replace('*','@')                         # Remplacement de l'* par @ dans l'adresse de destination
    date_cible = datetime.datetime.strptime(date_cible_str, "%Y/%m/%dT%H/%M/%S")    # Récupération de la date cible en format ISO
    time_cible = int(time.mktime(date_cible.timetuple()))                           # Conversion de la date cible en timestamp UNIX pour pouvoir faire un sleep derrière

    time_to_sleep = time_cible - int(time.time())                                   # Temps de sommeil :  différence entre le temps actuel et le temps cible

    time.sleep(time_to_sleep)

    server = smtplib.SMTP('localhost')                                              # Envoi du mail
    server.set_debuglevel(1)
    server.sendmail(expediteur, dest_original, message + "\n \n \t envoye en differe")
