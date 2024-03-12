# Projet 1 : Calculatrice Basique

Ce projet consiste en une calculatrice basique prenant en compte une faible gestion d'erreur et une gestion des opérateurs de base. Seuls les nombres positifs sont acceptés dans cette version. La gestion des nombres négatifs n'est pas implémentée en raison de la vérification du caractère de chiffre qui examine une chaîne de caractères. Si le programme rencontre un signe "-", il vérifie si un chiffre suit immédiatement après (aux positions [:1]), auquel cas le nombre est considéré comme négatif.

## Fonctionnalités

- Addition, soustraction, multiplication et division de nombres positifs.
- Gestion basique des erreurs : affichage d'un message en cas de saisie invalide.

## Utilisation

Pour exécuter la calculatrice, utilisez la commande suivante :

```bash
py -3.6.8 main.py