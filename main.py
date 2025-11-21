import os
from flask import Flask, render_template, request, redirect, url_for
import CRUD as crud

# inicializacao
app = Flask(__name__, static_folder='static')
app.config["UPLOAD_FOLDER"] = "static/fotos_pets"

# garante que a pasta de fotos existe
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

crud_pets = 'crud_pets'
crud_adotantes = 'crud_adotantes'


# rotas
@app.route("/") 
def ir_home():
    return render_template('index.html', crud_pets=crud_pets, crud_adotantes=crud_adotantes)


# ---------- GET (abre o formulário) ----------
@app.route('/criar_pet', methods=['GET'])
def ir_criar_pet():
    return render_template('criar_pet.html')


# ---------- POST (salva o pet + foto) ----------
@app.route('/criar_pet', methods=['POST'])
def criar_pet():
    nome = request.form['nome']
    especie = request.form['especie']
    raca = request.form['raca']
    idade = request.form['idade']
    estado_saude = request.form['estado_saude']
    data_chegada = request.form['data_chegada']
    comportamento = request.form['comportamento']

    # --- Upload da foto ---
    foto = request.files.get("foto")
    if foto and foto.filename != "":
        caminho_foto = os.path.join(app.config["UPLOAD_FOLDER"], foto.filename)
        foto.save(caminho_foto)
        nome_arquivo = foto.filename
    else:
        nome_arquivo = None

    # salvar no csv
    crud.adicionar_animal(
        nome,
        especie,
        raca,
        idade,
        estado_saude,
        data_chegada,
        comportamento,
        nome_arquivo
    )

    return redirect(url_for('ir_crud_pets'))


@app.route("/crud_pets")
def ir_crud_pets():
    lista_pets = crud.carregar_animais()
    return render_template('crud_pets.html', lista_pets=lista_pets)


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


# execucao
app.run(debug=True)
