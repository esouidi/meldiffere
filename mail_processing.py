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
Subject: mail body
To: <meldiffere+toto*gmail.com@enssat.fr>
User-Agent: mail (GNU Mailutils 3.14)
Date: Thu, 12 Jan 2023 15:37:14 +0100
Message-Id: <20230112143714.E8F0882F6A@souidi-GL63-8RD.univ-rennes1.fr>
From: Souidi <souidi@souidi-GL63-8RD>

mail sujet
'''

content=[]
for line in sys.stdin:
    content.append(line.rstrip())       # Récupération du mail par lignes

sujet = content[2][9:]                                          # Sujet du mail
destinataire = re.findall(r"<(.*?)>", content[3])[0]            # Destinataire (To: <meldiffere+toto*enssat.fr--1500@enssat.fr>) 3ème ligne
expediteur = re.findall(r"<(.*?)>", content[7])[0]              # Expediteur (From: Souidi)
message = content[-1]                                           # Body du mail

try:                                                                           # Le mail est à differer
    dest_original_asterisk = re.findall(r"\+(.*?)-", destinataire)[0]          # Extraction de l'adresse de destination sans "To: " avec *
    date_dest = re.findall(r"-(.*?)@", destinataire)[0]                        # Exctraction de l'heure d'arrivée voulue du mail

except:
    print("erreur dans l'adresse mail")

else:
    print("mail à différer")

    dest_original = dest_original_asterisk.replace('*','@')                         # Remplacement de l'* par @
    heure_dest, minute_dest = int(date_dest[0] + date_dest[1]), int(date_dest[2] + date_dest[3])
    current_time = datetime.datetime.now()

    temp_hour = heure_dest - current_time.hour
    if (temp_hour > 0):
        sleep_hour = temp_hour
    else:
        sleep_hour = 24 + temp_hour

    sleep_minute = abs(minute_dest - current_time.minute)

    time_to_sleep = sleep_hour*3600 + sleep_minute*60

    print(time_to_sleep)

    time.sleep(time_to_sleep)

    server = smtplib.SMTP('localhost')
    server.set_debuglevel(1)
    server.sendmail(expediteur, dest_original, message + "\n \n \t envoye en differe")
