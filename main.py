import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import CRUD as crud
import Cuidados as cuidados
import Adotores as adot
import data
import sugestoes

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

@app.route("/crud_pets")
def ir_crud_pets():
    lista_pets = crud.carregar_animais()
    return render_template('crud_pets.html', lista_pets=lista_pets)

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
        nome_arquivo = secure_filename(foto.filename)
        caminho_foto = os.path.join(app.config["UPLOAD_FOLDER"], nome_arquivo)
        foto.save(caminho_foto)
    else:
        nome_arquivo = None

    try:
        idade = int(idade)
    except ValueError:
        idade = 0
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




@app.route('/pet/<int:id_pet>')
def ir_pagina_pet(id_pet):
    animais = crud.carregar_animais()
    for a in animais:
        if a["id"] == id_pet:
            cuidados_info = data.data_cuidados_web(id_pet)
            sugestoes_info = sugestoes.gerar_sugestoes(a)

            print(sugestoes_info)
            
            return render_template("pet.html", pet=a, cuidados_info=cuidados_info, sugestoes_info=sugestoes_info)
    return render_template('404.html'), 404

#editar
@app.route("/encontrar_pet", methods=["POST"])
def encontrar_pet():
    print("entrou na funcao encontrar pet")
    nome = request.form["nome"]
    pet = crud.buscar_pet_por_nome(nome)

    if pet:
        print("redirecionando para editar pet; " + str(pet['id']))
        return redirect(url_for('editar_pet', id=pet['id']))
    else:
        return render_template('404.html'), 404

@app.route("/editar_pet/<int:id>")
def editar_pet(id):
    print("entrou na funcao editar pet<int:id>")
    if id:
        print("id recebido: " + str(id))

    pet = crud.buscar_pet_por_id(id)
    print(pet)
    if not pet:
        return render_template('404.html'), 404
    else:
        return render_template("editar_pet.html", pet=pet)

@app.route("/editar_pet/<int:id>", methods=["POST"])
def editar_pet_post(id):
    print("entrou na funcao editar pet_post<int:id>")
    animais = crud.carregar_animais()
    pet_encontrado = None
    for a in animais:
        if a["id"] == id:
            pet_encontrado = a
            break

    if not pet_encontrado:
        return render_template('404.html'), 404

    # pega dados do form
    pet_encontrado['nome'] = request.form.get('nome')
    pet_encontrado['especie'] = request.form.get('especie')
    pet_encontrado['raca'] = request.form.get('raca')
    pet_encontrado['idade'] = int(request.form.get('idade') or 0)
    pet_encontrado['saude'] = request.form.get('estado_saude')
    pet_encontrado['data_chegada'] = request.form.get('data_chegada')
    pet_encontrado['comportamento'] = request.form.get('comportamento')

    # --- Foto: se o usuário enviou nova foto, salva e atualiza o nome; se não, mantém a antiga ---
    foto = request.files.get('foto')
    if foto and foto.filename != "":
        nome_arquivo = secure_filename(foto.filename)
        caminho = os.path.join(app.config['UPLOAD_FOLDER'], nome_arquivo)
        foto.save(caminho)
        pet_encontrado['nome_arquivo'] = nome_arquivo
    else:
        pet_encontrado['nome_arquivo'] = pet_encontrado.get('nome_arquivo', 'padrao.jpg')
    
    # salva tudo de volta no csv
    crud.salvar_animais(animais)

    return redirect(url_for('ir_crud_pets'))


#apagar
@app.route("/encontrar_pet-apagar", methods=["POST"])
def encontrar_pet_apagar():
    nome = request.form["nome"]
    pet = crud.buscar_pet_por_nome(nome)

    if pet:
        return redirect(url_for('apagar_pet', nome=pet['nome']))
    else:
        return render_template('404.html'), 404

@app.route("/apagar_pet/<nome>")
def apagar_pet(nome):
    crud.apagar_pet_por_nome(nome)
    return redirect("/crud_pets")  # volta para a página principal


#ADD cuidados/tarefas
@app.route("/encontrar_pet-tarefa", methods=["POST"])
def encontrar_pet_tarefa():
    print("entrou na funcao encontrar pet tarefa (post)")
    nome = request.form["nome"]
    tarefa = request.form["tarefa"]
    descricao = request.form["descricao"]
    data_prevista = request.form["data_prevista"]
    responsavel = request.form["responsavel"]
    anotacoes = request.form["anotacoes"]

    pet = crud.buscar_pet_por_nome(nome)

    if not pet:
        return render_template('404.html'), 404

    cuidados.adicionar_cuidado_web(id_pet=pet["id"],
        nome_pet=pet["nome"],
        nome_cuidado=tarefa,
        descricao=descricao,
        data_prevista=data_prevista,
        responsavel=responsavel,
        anotacoes=anotacoes)

    return redirect(url_for('ir_crud_pets'))

@app.route("/adicionar_tarefa/<int:pet_id>", methods=["GET"])
def adicionar_tarefa_get(pet_id):
    print("entrou na funcao adicionar tarefa get")
    pet = crud.buscar_pet_por_id(pet_id)
    if not pet:
        return render_template('404.html'), 404
    else:
        return redirect(url_for('ir_crud_pets'))

@app.route("/adicionar_tarefa/<int:pet_id>", methods=["POST"])
def adicionar_tarefa(pet_id):
    print("entrou na funcao adicionar tarefa post")
    tarefa = request.form["tarefa"]
    descricao = request.form["descricao"]
    data_prevista = request.form["data_prevista"]
    responsavel = request.form["responsavel"]
    anotacoes = request.form["anotacoes"]

    pet = crud.buscar_pet_por_id(pet_id)

    

    return redirect(url_for('ir_crud_pets'))

#pag tarefas
@app.route("/tarefas/<int:pet_id>")
def ir_tarefas(pet_id):
    pet = cuidados.mostrar_cuidaddos_web(pet_id)
    pet_info = crud.buscar_pet_por_id(pet_id)
    if not pet:
        return render_template('404.html'), 404
    return render_template("tarefas.html", pet=pet, pet_info=pet_info)




#---------------------pagina adotantes------------------------
@app.route('/crud_adotantes')
def ir_crud_adotantes():
    return render_template('crud_adotantes.html', lista_adotantes=adot.ListAdotar())

@app.route('/criar_adotante', methods=['GET'])
def ir_criar_adotantes():
    return render_template('criar_adotante.html')

@app.route('/criar_adotante', methods=['POST'])
def criar_adotantes():
    nome = request.form['nome']
    idade = request.form['idade']
    genero = request.form['genero']
    status = request.form['status']
    animal = request.form['animal']
    comportamento = request.form['comportamento']

    try:
        idade = int(idade)
    except ValueError:
        idade = 0

    # salvar no csv
    adot.adicionar_adotante(
        nome,
        idade,
        genero,
        status,
        animal,
        comportamento
    )

    return redirect(url_for('ir_crud_adotantes'))

#editar
@app.route("/encontrar_adotante", methods=["POST"])
def encontrar_adotante():
    nome = request.form["nome"]
    adotante = adot.buscar_adotante_por_nome(nome)

    if adotante:
        return redirect(url_for('editar_adotante', nome=adotante['nome']))
    else:
        return render_template('404.html'), 404

@app.route("/editar_adotante/<nome>")
def editar_adotante(nome):
    adotantes = adot.ListAdotar()
    adotante = adot.buscar_adotante_por_nome(nome)
    if not adotantes:
        return render_template('404.html'), 404
    else:
        return render_template("editar_adotante.html", adotante=adotante)

@app.route("/editar_adotante/<nome>", methods=["POST"])
def editar_adotante_post(nome):
    print("entrou na funcao editar adotante_post<str:nome>")
    adotantes = adot.ListAdotar()
    adotante_encontrado = None
    for a in adotantes:
        if a["nome"] == nome:
            adotante_encontrado = a
            break

    if not adotante_encontrado:
        return render_template('404.html'), 404

    # pega dados do form
    adotante_encontrado['nome'] = request.form.get('nome')
    adotante_encontrado['idade'] = int(request.form.get('idade')) or 0
    adotante_encontrado['genero'] = request.form.get('genero')
    adotante_encontrado['status'] = request.form.get('status')
    adotante_encontrado['animal'] = request.form.get('animal')
    adotante_encontrado['comportamento'] = request.form.get('comportamento')
    
    # salva tudo de volta no csv
    adot.SaveAdopt(adotantes)

    return redirect(url_for('ir_crud_adotantes'))

#apagar
@app.route("/encontrar_adotante-apagar", methods=["POST"])
def encontrar_adotante_apagar():
    nome = request.form["nome"]
    adotante = adot.buscar_adotante_por_nome(nome)

    if adotante:
        return redirect(url_for('apagar_adotante', nome=adotante['nome']))
    else:
        return render_template('404.html'), 404

@app.route("/apagar_adotante/<nome>")
def apagar_adotante(nome):
    adot.apagar_adotante_por_nome(nome)
    return redirect("/crud_adotantes")  # volta para a página principal

# execucao
app.run(debug=True)
