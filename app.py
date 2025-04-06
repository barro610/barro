from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def entree():
    if request.method == 'POST':
        code = request.form['code']
        nom = request.form['nom']
        prenom = request.form['prenom']
        grade = request.form['grade']
        nbheures = int(request.form['nbheures'])

        # Calcul du salaire brut
        if grade == 'P':
            salaire_brut = 15000 * nbheures
        elif grade == 'A':
            salaire_brut = 10000 * nbheures
        else:
            salaire_brut = 0

        # Calcul de la taxe (5%)
        taxe = salaire_brut * 0.05

        # Calcul du salaire net
        salaire_net = salaire_brut - taxe

        # Retourner les résultats à la vue sortie
        return render_template('sortie.html', code=code, nom=nom, prenom=prenom, grade=grade,
                               nbheures=nbheures, salaire_brut=salaire_brut, taxe=taxe, salaire_net=salaire_net)

    return render_template('entree.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
