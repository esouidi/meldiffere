# Meldiffere - Projet technologique 3A

Application pour envoyer des mails en différé avec Postfix

Fichiers de configuration master.cf, main.cf et transport nécessaires pour faire fonctionner l'application.

Le fichier python est un script permettant de récupérer un mail à envoyer en différé, le traiter et de le renvoyer vers le bon destinataire via Postfix.

Ce code est un script Python qui gère les emails entrants reçus par le démon.

Le script récupère les informations des mails entrants, extrait le sujet, le destinataire, l'expéditeur et le contenu du message en traitant chaque ligne du mail entrant, et utilise des expressions régulières pour extraire les informations du destinataire.

Le script vérifie si la nomenclature de l'adresse mail est bonne et récupère l'adresse de destination originale sans le « To: » avec le caractère « * » et l'heure d'arrivée souhaitée du courrier. Il convertit la date cible en timestamp UNIX pour pouvoir faire un sleep en utilisant la fonction time.sleep() et envoie finalement le courrier.

Il est important de noter que le script ne contient pas de mécanismes pour vérifier si les emails entrants sont valides ou malveillants, et pourrait être amélioré en ce sens.
