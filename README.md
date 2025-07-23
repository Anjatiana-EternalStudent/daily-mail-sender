# daily-mail-sender
Ce projet envoie automatiquement un e-mail à une ou plusieurs personnes à l’aide de Python et GitHub Actions.(Les variables sensibles sécurisées via les Secrets GitHub)

## Fonctionnalités
* Envoi automatique d’un e-mail via SMTP (Gmail)
* Planification automatique grâce à GitHub Actions (cron)
* Sécurisation des identifiants et adresses e-mail avec .env et Secrets GitHub

## Technologies
* Python 3
* SMTP
* `smtplib`, `email`, `dotenv`
* GitHub Actions
* Fichier `.env`

## Variables d'environnement(`.env`)
```
EMAIL=adresse@gmail.com
MDP=mot_de_passe_app
RECIPIENTS=destinataire@example.com, destinataire2@gmail.com
```

## Secrets GitHub à configurer
1. Dans le dépôt → Settings → Secrets and variables → Actions → New repository secret.
2. Création des trois secrets:
   * EMAIL: L'adresse gmail qui envoie le message
   * MDP: Le mot de passe d'application Gmail
   * Recipients: Adresse du ou des destinataires(séparées par des virgules)

## Automatisation via GitHub Actions
Le workflow est défini dans `.github/workflows/daily.yml`. Il:
* Récupère le code
* Installe python
* Installe les dépendances
* Génère le fichier `.env`
* Lance le script Python

## Pour lancer le projet
1. Cloner le dépôt
2. [Ajouter un mot de passe d'application Gmail](https://myaccount.google.com/apppasswords)
3. Créer les secrets dans GitHub
4. Le mail s'enverra automatiquement selon le planning (peut aussi être envoyé ,manuellement)

## Remarques
* Le mot de passe utilisé n'est pas celui du compte Gmail mais un mot de passe d'application que l'on génère depuis le [compte google](https://myaccount.google.com/apppasswords).
