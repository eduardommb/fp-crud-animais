from flask import Flask, render_template, url_for

#inicializacao
app = Flask(__name__, static_folder='static')

crud_pets = 'crud_pets'
crud_adotantes = 'crud_adotantes'

#rotas
@app.route("/") #caminho principal (home)
def ir_home():
    return render_template('index.html', crud_pets = crud_pets, crud_adotantes = crud_adotantes)

@app.route("/crud_pets")
def ir_crud_pets():
    return render_template('crud_pets.html')

@app.route('/crud_adotantes')
def ir_crud_adotantes():
    return render_template('crud_adotantes.html')

#execucao
app.run(debug="true")