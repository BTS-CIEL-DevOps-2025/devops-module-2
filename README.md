# 🧪 Exercice GitHub : Collaboration avec Pull Requests

## 🎯 Objectif
Trois équipes collaborent sur une même application Flask en utilisant des branches et des pull requests.

## 🚀 Étapes

### 1. Initialisation
- Clonez ce dépôt
- Créez une branche dédiée à votre équipe :
  - `feature/team-alpha`
  - `feature/team-beta`
  - `feature/team-gamma`

### 2. Répartition des tâches
- **Team Alpha** : Ajout d’un formulaire de création
- **Team Beta** : Ajout d’un système de filtrage
- **Team Gamma** : Ajout d’un système de tri

### 3. Développement
- Travaillez sur votre branche
- Poussez vos modifications
- Créez une pull request vers `main`

### 4. Revue de code croisée
- Alpha → PR de Beta
- Beta → PR de Gamma
- Gamma → PR de Alpha

### 5. Résolution des conflits
- Résolvez les conflits ensemble si nécessaire

### 6. Merge final
- Une fois validées, les PR sont mergées dans `main`

## 📁 Structure
- `app.py` : Application Flask principale
- `templates/index.html` : Page d’accueil
- `static/` : Dossier pour les fichiers statiques