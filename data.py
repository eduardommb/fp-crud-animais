import datetime
from datetime import datetime,date,timedelta
import datetime
from Cuidados import mostrar_cuidaddos_web

ARQUIVO_ANIMAIS = "animais.csv"
ARQUIVO_CUIDADOS = "cuidados.csv" 

def calcular_data(data_prevista):
    dia, mes, ano = map(int, data_prevista.split("/"))

    data_consulta = datetime.date(ano, mes, dia)
    
    data_atual = datetime.date.today()
    
    diferença = data_consulta - data_atual

    return diferença.days

#calculo data web
def calcular_data_web(data_prevista):
    ano, mes, dia = map(int, data_prevista.split("-"))

    data_consulta = datetime.date(ano, mes, dia)
    
    data_atual = datetime.date.today()
    
    diferença = data_consulta - data_atual

    return diferença.days

def data_cuidados(animal):
    if "cuidados" not in animal or len(animal["cuidados"]) == 0:
        print("\nEste animal não possui cuidados registrados.")
        return
    
    print(f"\nCuidados do animal: {animal['nome']}\n")

    for c in animal["cuidados"]:
        dias = calcular_data(c["data_prevista"])
        print(f"- {c['descricao']} ({c['data_prevista']}):faltam {dias} dias")

def data_cuidados_web(id_pet):
    lista = []

    with open(ARQUIVO_CUIDADOS, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    for linha in linhas:
        campos = linha.strip().split(";")

        id_csv, nome_pet, nome_cuidado, descricao, data_prevista, responsavel, anotacoes = campos

        if str(id_pet) == id_csv.strip():
            dias = calcular_data_web(data_prevista)

            lista.append({
                "nome_cuidado": nome_cuidado,
                "descricao": descricao,
                "data_prevista": data_prevista,
                "responsavel": responsavel,
                "anotacoes": anotacoes,
                "dias_faltando": dias
            })

    return lista

def data_especifica(cuidados):
    nome_do_animal=input("Digite o nome do animal que deseja ver a data: ").lower().strip()
    cuidados_pet = []
    for c in cuidados:
        if 'nome_pet' in c and c['nome_pet'].lower() == nome_do_animal:
            cuidados_pet.append(c)

    if not cuidados_pet:
        print("Este animal não possui cuidados cadastrados.")
        return

    for c in cuidados_pet:
        dias = calcular_data_web(c["data_prevista"])
        print(f"- {c['descricao']} ({c['data_prevista']}): faltam {dias} dias")
            
def data_especifica_web(id_pet):
    cuidados_pet = mostrar_cuidaddos_web(id_pet)

    lista_final = []

    for c in cuidados_pet:
        dias = calcular_data_web(c["data_prevista"])
        lista_final.append({
            "nome_cuidado": c["nome_cuidado"],
            "data_prevista": c["data_prevista"],
            "descricao": c["descricao"],
            "dias_faltando": dias
        })

    return lista_final
