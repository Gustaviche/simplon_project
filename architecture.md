# Architecture du projet

## Objectif
Creer un environnement avec deux service avec docker.

Un pour éxécuter du code en python et un pour stocker les données en SQLite.

## Les services
Service 1 : app
    Sert à exécuter les scripts Python
    Contient le langage Python
    Télécharge les fichiers CSV
    Crée ou met à jour la base de données

Service 2 : db
    Sert à stocker la base de données SQLite
    Contient le fichier db.sqlite3
    Permet de garder les données entre chaque exécution

## Communication
Les deux services communiquent avec un dossier commun qui contient le fichier de base de données sqlite.

## Schéma

+---------------------------+
|       docker-compose      |
|                           |
|  +----------+   +-------+ |
|  |   app    |   |  db   | |
|  | (Python) |<->|SQLite | |
|  +----------+   +-------+ |
|       ↑ dossier partagé   |
|       |                   |
|       -> db.sqlite3       |
+---------------------------+
