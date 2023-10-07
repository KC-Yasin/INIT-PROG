# Installation de Xubuntu en Dual Boot sur un Disque Dur Externe

Ce fichier README documente le processus d'installation de Xubuntu en dual boot sur un disque dur externe, la configuration de l'environnement Java, l'utilisation de Docker, la synchronisation avec Git pour utiliser VSCode.

## Prérequis

- Un ordinateur.
- Une connexion Internet active.
- Un compte GitHub pour la synchronisation des projets.
- Un disque dur externe ou une clé USB.
- Le logiciel Balena Etcher.

## Installation de Xubuntu en Dual Boot

### Téléchargement de Xubuntu

Téléchargez l'image ISO de Xubuntu à partir du site officiel de Xubuntu : [https://xubuntu.fr/](https://xubuntu.fr/).

### Installation de Balena Etcher

Installez le logiciel Balena Etcher, qui vous permettra de créer une clé USB bootable à partir de l'image ISO.

### Création de la Clé USB Bootable

Utilisez Balena Etcher pour sélectionner le fichier ISO de Xubuntu et votre disque externe comme destination.

### Accès au BIOS

Redémarrez votre ordinateur et accédez au BIOS en appuyant sur les touches F2 ou Suppr (cela dépend du modèle de votre machine).

### Configuration du Boot

Dans le BIOS, définissez la priorité de boot pour que Xubuntu soit en première position. Sauvegardez les modifications et redémarrez.

### Partitionnement du Disque Dur Externe

Lors de l'installation, vous serez invité à partitionner le disque dur externe. Allouez suffisamment d'espace (par exemple, 100 Go) pour Xubuntu.

### Configuration de l'Installation

Suivez les étapes de configuration de l'installation. Une fois terminé, vous atterrirez sur le bureau Xubuntu.

### Sélection du Système au Démarrage

À chaque démarrage de votre machine avec le disque dur externe branché, un menu GRUB apparaîtra, vous permettant de choisir entre Windows et Xubuntu. Si le disque est débranché, un autre menu GRUB s'affichera, il suffira de sélectionner "Exit". 

Si BitLocker est demandé du côté de Windows pour des raisons de sécurité, vous pouvez le trouver dans votre compte Microsoft, dans la section BitLocker.

Votre installation de Xubuntu en dual boot sur le disque dur externe est terminée.

## Mise en place de l'environnement de travail

Maintenant que Xubuntu est installé en dual boot sur votre disque dur externe, vous pouvez commencer à configurer votre environnement de développement. Voici les étapes à suivre :

### Installation de l'Environnement Java

Pour développer en Java, installez le Java Development Kit (JDK) sur Xubuntu. Ouvrez un terminal et exécutez les commandes suivantes pour installer le JDK :

```bash
sudo apt update
sudo apt install default-jdk
```

Cela installera le JDK sur votre système, vous permettant de compiler et d'exécuter des programmes Java.

### Installation de Docker

Docker est un outil puissant pour la gestion de conteneurs. Vous pouvez l'installer en utilisant les commandes suivantes :

```bash
sudo apt update
sudo apt install docker.io
```


Pour tester si Docker fonctionne correctement on va executer cette commande:


```bash
docker run hello-world
```

### Synchronisatin avec Git

Pour synchroniser votre travail avec Git et utiliser VSCode pour le développement, vous devrez également installer Git. Exécutez les commandes suivantes pour installer Git :

```bash
sudo apt update
sudo apt install git
```

Maintenant, vous pouvez suivre ces étapes pour effectuer des commits avec Git :
Étape 1: Ajouter des fichiers au suivi

Utilisez la commande suivante pour ajouter tous les fichiers modifiés et nouveaux au suivi de Git :

```bash
git add .
```

Étape 2: Effectuer un commit

Utilisez la commande suivante pour créer un commit avec un message de description des modifications :

```bash
git commit -m "Votre message de commit ici"
```

Étape 3: Pousser les modifications vers GitHub

Lorsque vous êtes prêt à pousser vos modifications vers GitHub, utilisez la commande suivante :

```bash
git push origin nom_de_votre_branche
```

