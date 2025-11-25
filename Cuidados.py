import os
from datetime import datetime
from sugestoes import mostrar_sugestoes
import Adotores as a
import CRUD as crud

ARQUIVO_ANIMAIS = "animais.csv"
ARQUIVO_CUIDADOS = "cuidados.csv" 

def salvar_cuidado(id_pet, nome_animal, nome_cuidado, descricao, data_prevista, responsavel, anotacoes):
    """Salva um cuidado diretamente no ARQUIVO_CUIDADOS."""
    try:
        with open(ARQUIVO_CUIDADOS, "a", encoding="utf-8") as arquivo:
            linha = f"{id_pet};{nome_animal};{nome_cuidado};{descricao};{data_prevista};{responsavel};{anotacoes}\n"
            arquivo.write(linha)
    except Exception as e:
        print(f"Erro ao salvar cuidado: {e}")

def carregar_cuidados_animal(nome_animal):
    """Carrega todos os cuidados para um animal específico a partir do ARQUIVO_CUIDADOS."""
    cuidados = []
    try:
        with open(ARQUIVO_CUIDADOS, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")
                if len(dados) == 7 and dados[1].lower() == nome_animal.lower():
                    cuidado = {
                        "id_pet": dados[0],
                        "nome_pet": dados[1],
                        "nome_cuidado": dados[2],
                        "descricao": dados[3],
                        "data_prevista": dados[4],
                        "responsavel": dados[5],
                        "anotacoes": dados[6]
                    }
                    cuidados.append(cuidado)
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Erro ao carregar cuidados: {e}")
    return cuidados

def carregar_cuidados():
    cuidados = []
    try:
        with open(ARQUIVO_CUIDADOS, "r", encoding="utf-8") as f:
            for linha in f:
                dados = linha.strip().split(";")
                if len(dados) == 7:
                    cuidados.append({
                        "id_pet": int(dados[0]),
                        "nome_pet": dados[1],
                        "nome_cuidado": dados[2],
                        "descricao": dados[3],
                        "data_prevista": dados[4],
                        "responsavel": dados[5],
                        "anotacoes": dados[6]
                    })
    except FileNotFoundError:
        pass
    return cuidados

def mostrar_cuidados_pet(id_pet):
    cuidados = carregar_cuidados()
    resultados = []
    for c in cuidados:
        if c["id_pet"] == id_pet:
            resultados.append(c)

    return print(resultados)


def mostrar_tabela_cuidados(cuidados):
    if not cuidados:
        print("Nenhum cuidado cadastrado ainda.")
        return

    print()
    print(f"{'Nome':<15}{'Nome do cuidado':<15}{'Descrição':<15}{'Responsável':<8}{'Data prevista':<20}{'Anotações':<15}")
    print("-" * 108)
    for a in cuidados:
        print(f"{a['nome_pet']:<15}{a['nome_cuidado']:<15}{a['descricao']:<15}{a['responsavel']:<8}{a['data_prevista']:<20}{a['anotacoes']:<15}")

def adicionar_cuidado(animais):
    crud.limpar_tela()
    mostrar_tabela(animais)
    nome = input("\nDigite o nome do animal para adicionar um cuidado/atividade: ")
    for a in animais:
        if a["nome"].lower() == nome.lower():
            print("\n=== Adicionar Cuidado/Atividade ===")
            id_pet = a["id"]
            nome_cuidado = input("Nome do cuidado/atividade: ")
            descricao = input("Descrição do cuidado/atividade: ")
            data_prevista = input("Data prevista (dd-mm-aaaa): ")
            responsavel = input("Responsável: ")
            anotacoes = input("Anotações adicionais: ")

            salvar_cuidado(id_pet, a["nome"], nome_cuidado, descricao, data_prevista, responsavel, anotacoes)
            
            print("\nCuidado/atividade registrado com sucesso!")
            crud.pausar()
            return
    print("\nAnimal não encontrado.")
    crud.pausar()

def adicionar_cuidado_web(id_pet, nome_pet, nome_cuidado, descricao, data_prevista, responsavel, anotacoes):
    crud.limpar_tela()
    with open(ARQUIVO_CUIDADOS, "a", encoding="utf-8") as f:
        linha = f"{id_pet};{nome_pet};{nome_cuidado};{descricao};{data_prevista};{responsavel};{anotacoes}\n"
        f.write(linha)
        print("\nCuidado/atividade registrado com sucesso!")
    return

def mostrar_cuidados(animais):
    crud.limpar_tela()
    mostrar_tabela_cuidados(animais)
    nome = input("\nDigite o nome do animal para ver os cuidados/atividades: ")
    for a in animais:
        if a["nome_pet"].lower() == nome.lower():
            crud.limpar_tela()
            print(f"=== Cuidados/Atividades para {a['nome_pet']} ===")
            
            cuidados_do_animal = carregar_cuidados_animal(a["nome_pet"])
            if cuidados_do_animal:
                for cuidado in cuidados_do_animal:
                    print(f"- ID do pet: {cuidado['id_pet']}")
                    print(f"- Nome do cuidado: {cuidado['nome_cuidado']}")
                    print(f"- Descrição: {cuidado['descricao']}")
                    print(f"  Data Prevista: {cuidado['data_prevista']}")
                    print(f"  Responsável: {cuidado['responsavel']}")
                    print(f"  Anotações: {cuidado['anotacoes']}")
                    print("-" * 30)
            else:
                print("Nenhum cuidado/atividade registrado para este animal ainda.")
            crud.pausar()
            return
    print("\nAnimal não encontrado.")
    crud.pausar()

def mostrar_cuidaddos_web(pet_id):
    id_procurar = str(pet_id).strip()
    cuidados = []
    try:
        with open(ARQUIVO_CUIDADOS, "r", encoding="utf-8") as f:
            for linha in f:
                dados = linha.strip().split(";")
                if len(dados) >= 7 and dados[0] == id_procurar:
                    cuidado = {
                        "id": dados[0],
                        "nome_pet": dados[1],
                        "nome_cuidado": dados[2],
                        "descricao": dados[3],
                        "data_prevista": dados[4],
                        "responsavel": dados[5],
                        "anotacoes": dados[6]
                    }
                    cuidados.append(cuidado)
    except FileNotFoundError:
        pass
    return cuidados
