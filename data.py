import os
import datetime
from datetime import datetime,date,timedelta
import datetime

ARQUIVO_ANIMAIS = "animais.csv"
ARQUIVO_CUIDADOS = "cuidados.csv" 

from Parte_do_CRUD import limpar_tela, mostrar_tabela, pausar
from Cuidados import salvar_animais, adicionar_cuidado

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_tabela(animais):
    if not animais:
        print("Nenhum animal cadastrado ainda.")
        return
    
    print()
    print(f"{'Nome':<15}{'Espécie':<15}{'Raça':<15}{'Idade':<8}{'Saúde':<20}{'Chegada':<15}{'Comportamento':<20}")
    print("-" * 108)
    for a in animais:
        print(f"{a['nome']:<15}{a['especie']:<15}{a['raca']:<15}{a['idade']:<8}{a['saude']:<20}{a['data_chegada']:<15}{a['comportamento']:<20}")
    
def pausar():
    input("\nPressione ENTER para continuar...")

def salvar_animais(animais):
    with open(ARQUIVO_ANIMAIS, "w", encoding="utf-8") as arquivo:
        for a in animais:
            cuidados_list = a.get("cuidados", [])
            cuidados_str = "||".join([f"{c['descricao']}|{c['data_prevista']}|{c['responsavel']}" for c in cuidados_list])
            linha = f"{a['nome']};{a['especie']};{a['raca']};{a['idade']};{a['saude']};{a['data_chegada']};{a['comportamento']};{cuidados_str}\n"
            arquivo.write(linha)


def adicionar_cuidado(animais):
    limpar_tela()
    mostrar_tabela(animais)
    nome = input("\nDigite o nome do animal para adicionar um cuidado/atividade: ")
    for a in animais:
        if a["nome"].lower() == nome.lower():
            print("\n=== Adicionar Cuidado/Atividade ===")
            descricao = input("Descrição do cuidado/atividade: ")
            data_prevista = input("Data prevista (dd/mm/aaaa): ")
            responsavel = input("Responsável: ")
        
            cuidado = {
                "descricao": descricao,
                "data_prevista": data_prevista,
                "responsavel": responsavel
            }
            if "cuidados" not in a:
                a["cuidados"] = []
            a["cuidados"].append(cuidado)
            salvar_animais(animais)
            print("\nCuidado/atividade registrado com sucesso!")
            pausar()
            return
    print("\nAnimal não encontrado.")
    pausar()

#--------------------------------------------------- parte nova -----------------------------------------------------------------

def calcular_data(data_prevista):
    dia, mes, ano = map(int, data_prevista.split("/"))

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

def data_especifica(animais):
    nome_do_animal=input("digite o nome do animal que deseja ver a data:").lower()
    for c in animais:
        if 'cuidados' not in c:
            print("Este animal não possui cuidados cadastrados")

        elif nome_do_animal==c['nome'].lower():
            for d in c['cuidados']:
                dias=calcular_data(d['data prevista'])
                print(f"- {d['descricao']} ({d['data_prevista']}):faltam {dias} dias")
        else:
            print("animal não encontrado")
            

        