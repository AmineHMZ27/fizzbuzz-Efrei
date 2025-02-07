# Utilise une image officielle de Python
FROM python:3.12.9-alpine

# Définis le répertoire de travail dans le conteneur
WORKDIR /app

# Copie tous les fichiers de ton projet dans le conteneur
COPY . .

# Installe les dépendances si un fichier requirements.txt existe
RUN pip install --no-cache-dir -r requirements.txt

# Définit la commande de démarrage par défaut
CMD ["python", "main.py"]
