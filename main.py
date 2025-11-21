from flask import Flask, render_template
import CRUD as crud
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
    lista_pets = crud.carregar_animais()
    return render_template('crud_pets.html', lista_pets = lista_pets, )

@app.route('/crud_adotantes')
def ir_crud_adotantes():
    return render_template('crud_adotantes.html')

@app.route('/pet/<int:id_pet>')
def ir_pagina_pet(id_pet):
    animais = crud.carregar_animais()
    for a in animais:
        if a["id"] == id_pet:
            return render_template("pet.html", pet=a)
    return render_template('404.html'), 404

@app.route('/criar_pet')
def ir_criar_pet():
    return render_template('criar_pet.html')

#execucao
app.run(debug="true")