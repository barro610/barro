from flask import Flask

# Créer une instance de l'application Flask
app = Flask(__name__)

# Définir une route pour la page d'accueil
@app.route('/')
def home():
    return "Bonjour, bienvenue dans mon application Flask!"

# Lancer l'application
if __name__ == '__main__':
    app.run(debug=True)
