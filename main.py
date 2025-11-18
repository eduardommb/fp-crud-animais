from flask import Flask, render_template, url_for

#inicializacao
app = Flask(__name__)

pag = "/outra"

#rotas
@app.route("/") #caminho principal (home)
def teste():
    return render_template('index.html', pag=pag)

@app.route("/outra")
def outra_pag():
    return "teste" 


#execucao
app.run(debug="true")