# ParkGuard AI : Système Intelligent de Gestion de Parking (ANPR Maroc)

### 🎓 Projet Interdisciplinaire — ENSAM Rabat (2API)

**ParkGuard AI** est une solution logicielle complète de gestion de parking automatisée par vision par ordinateur. Ce projet vise à moderniser le contrôle d'accès aux parkings en utilisant des modèles de Deep Learning spécialisés dans la détection et la reconnaissance de plaques d'immatriculation marocaines.

---

## 🌟 Points Forts du Projet

* **Double Pipeline YOLO** : Utilisation de **YOLOv8** pour la détection précise de la zone de la plaque et de **YOLOv10** pour la reconnaissance optique de caractères (OCR) spécialisée dans le format marocain.
* **Interface Moderne (GUI)** : Interface utilisateur fluide et sombre développée avec **CustomTkinter**.
* **Gestion de Base de Données** : Système d'archivage des accès, gestion des abonnements clients et suivi des paiements via **SQLite**.
* **Simulation de Contrôle d'Accès** : Intégration d'un serveur de signal pour commander l'ouverture d'une barrière physique ou simulée.

---

## 🛠️ Architecture Technique

### Technologies Utilisées
* **Langage** : Python 3.10+
* **Vision par Ordinateur** : OpenCV, Ultralytics (YOLO)
* **Interface Graphique** : CustomTkinter, PIL (Pillow)
* **Base de Données** : SQLite3

### Structure du Modèle IA
Le système repose sur deux modèles entraînés sur des jeux de données spécifiques (notamment via Roboflow) :
1.  **`yolov8n_plate.pt`** : Localisation de la plaque dans l'image globale du véhicule.
2.  **`PlateReaderyolo.pt`** : Analyse de la plaque découpée pour extraire la série de chiffres et la lettre arabe.

---

## 📁 Organisation du Code

```text
├── main.py              # Point d'entrée de l'application
├── config.py            # Paramètres système et chemins des modèles
├── detector.py          # Logique d'inférence YOLO et traitement OCR
├── database.py          # Gestion des opérations SQL (CRUD)
├── gate_server.py       # Serveur de signal pour la barrière
├── model/               # Dossier contenant les fichiers .pt
├── tabs/                # Modules de l'interface graphique (Caméra, Clients, Logs...)
└── requirements.txt     # Liste des dépendances nécessaires


## 🚀 Installation et Lancement

1.  **Cloner le projet** et accéder au dossier :
    ```bash
    cd car-parking-detection-main
    ```

2.  **Créer et activer un environnement virtuel** :
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Installer les dépendances** :
    ```bash
    pip install -r requirements.txt
    ```

4.  **Lancer l'application** :
    ```bash
    python main.py
    ```

---

## 📋 Utilisation
1.  **Onglet Caméra** : Lancez le flux vidéo pour détecter les plaques en temps réel. Le système compare la plaque lue avec la base de données.
2.  **Onglet Clients** : Enregistrez les véhicules autorisés (format attendu : `12345-A-17`).
3.  **Onglet Logs** : Consultez l'historique des entrées et sorties.
4.  **Onglet Dashboard** : Statistiques d'occupation et de paiements.

---

## 👥 Équipe Projet (2API - ENSAM Rabat)

* **Ilyas LATRACH**
* **Taha ZAKI**
* **Marwa MAHZOUL**
* **Hala RABAI**
* **Aya ERROUDANI**

---
*Projet réalisé dans le cadre de la formation ingénieur à l'École Nationale Supérieure d'Arts et Métiers (ENSAM) de Rabat.*