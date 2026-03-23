# Budget Buddy 💰

**Votre allié financier intelligent** pour une gestion simple et sécurisée de vos comptes.

Une application desktop développée en Python permettant de suivre ses transactions (dépôts, retraits, transferts), consulter son historique et visualiser un tableau de bord complet.

## ✨ Fonctionnalités

- Inscription et connexion sécurisée (mot de passe hashé avec PBKDF2)
- Dépôts, retraits et transferts entre utilisateurs
- Historique complet des transactions avec filtres avancés
- Tableau de bord avec solde en temps réel et statistiques
- Interface graphique moderne avec CustomTkinter

## 🛠 Technologies

- **Python 3.12**
- **CustomTkinter** (interface graphique)
- **MySQL** (base de données)
- **mysql-connector-python**
- **hashlib + PBKDF2** (sécurisation des mots de passe)

## 🚀 Installation & Lancement

1. Clone le repository :
   ```bash
   git clone https://github.com/Angelo-Njarasoa/budget_buddy.git
   cd budget_buddy

Installe les dépendances :Bashpip install customtkinter mysql-connector-python
Configure la base de données :
Crée une base MySQL nommée budget_buddy
Exécute le fichier database/init.sql

Lance l’application :Bashpython main.py

Fais par Alya Annabi, Angelo Njarasoa  et Yaniss aouri