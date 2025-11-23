import os
from datetime import datetime
from sugestoes import mostrar_sugestoes
import Adotores as a

ARQUIVO_ANIMAIS = "animais.csv"
ARQUIVO_CUIDADOS = "cuidados.csv"

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\nPressione ENTER para continuar...")

def carregar_animais():
    animais = []
    try:
        with open(ARQUIVO_ANIMAIS, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")
                if len(dados) >= 7:
                    animal = {
                        "nome": dados[0],
                        "especie": dados[1],
                        "raca": dados[2],
                        "idade": int(dados[3]),
                        "saude": dados[4],
                        "data_chegada": dados[5],
                        "comportamento": dados[6]
                    }
                    if len(dados) > 7 and dados[7]:
                        care_activities_str = dados[7]
                        animal["cuidados"] = []
                        if care_activities_str:
                            for care_str in care_activities_str.split("||"):
                                care_data = care_str.split("|")
                                if len(care_data) == 3:
                                    cuidado = {
                                        "descricao": care_data[0],
                                        "data_prevista": care_data[1],
                                        "responsavel": care_data[2]
                                    }
                                    animal["cuidados"].append(cuidado)
                    else:
                        animal["cuidados"] = []
                    animais.append(animal)
    except FileNotFoundError:
        pass
    return animais

def salvar_animais(animais):
    with open(ARQUIVO_ANIMAIS, "w", encoding="utf-8") as arquivo:
        for a in animais:
            cuidados_list = a.get("cuidados", [])
            cuidados_str = "||".join([f"{c['descricao']}|{c['data_prevista']}|{c['responsavel']}" for c in cuidados_list])
            linha = f"{a['nome']};{a['especie']};{a['raca']};{a['idade']};{a['saude']};{a['data_chegada']};{a['comportamento']};{cuidados_str}\n"
            arquivo.write(linha)

def mostrar_tabela(animais):
    if not animais:
        print("Nenhum animal cadastrado ainda.")
        return

    print()
    print(f"{'Nome':<15}{'Espécie':<15}{'Raça':<15}{'Idade':<8}{'Saúde':<20}{'Chegada':<15}{'Comportamento':<20}")
    print("-" * 108)
    for a in animais:
        print(f"{a['nome']:<15}{a['especie']:<15}{a['raca']:<15}{a['idade']:<8}{a['saude']:<20}{a['data_chegada']:<15}{a['comportamento']:<20}")

def adicionar_animal(animais):
    limpar_tela()
    print("=== Adicionar Novo Animal ===")
    nome = input("Nome: ")
    especie = input("Espécie: ")
    raca = input("Raça: ")
    idade = int(input("Idade: "))
    saude = input("Estado de saúde: ")
    data_chegada = input("Data de chegada (dd/mm/aaaa): ")
    comportamento = input("Comportamento: ")

    animal = {
        "nome": nome,
        "especie": especie,
        "raca": raca,
        "idade": idade,
        "saude": saude,
        "data_chegada": data_chegada,
        "comportamento": comportamento,
        "cuidados": [] 
    }
    animais.append(animal)
    salvar_animais(animais)
    print("\nAnimal cadastrado com sucesso!")
    pausar()

def editar_animal(animais):
    limpar_tela()
    mostrar_tabela(animais)
    nome = input("\nDigite o nome do animal que deseja editar: ")
    for a in animais:
        if a["nome"].lower() == nome.lower():
            print("\nDeixe em branco caso não queira alterar.")
            a["especie"] = input(f"Nova espécie ({a['especie']}): ") or a["especie"]
            a["raca"] = input(f"Nova raça ({a['raca']}): ") or a["raca"]
            nova_idade = input(f"Nova idade ({a['idade']}): ")
            if nova_idade:
                a["idade"] = int(nova_idade)
            a["saude"] = input(f"Novo estado de saúde ({a['saude']}): ") or a["saude"]
            a["data_chegada"] = input(f"Nova data de chegada ({a['data_chegada']}): ") or a["data_chegada"]
            a["comportamento"] = input(f"Novo comportamento ({a['comportamento']}): ") or a["comportamento"]
            salvar_animais(animais)
            print("\nAnimal atualizado com sucesso!")
            pausar()
            return
    print("\nAnimal não encontrado.")
    pausar()

def excluir_animal(animais):
    limpar_tela()
    mostrar_tabela(animais)
    nome = input("\nDigite o nome do animal que deseja excluir: ")
    for a in animais:
        if a["nome"].lower() == nome.lower():
            animais.remove(a)
            salvar_animais(animais)
            print("\nAnimal removido com sucesso!")
            pausar()
            return
    print("\nAnimal não encontrado.")
    pausar()

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

def adicionar_cuidado_web(id_pet, nome_pet, nome_cuidado, descricao, data_prevista, responsavel, anotacoes):
    limpar_tela()
    with open(ARQUIVO_CUIDADOS, "a", encoding="utf-8") as f:
        linha = f"{id_pet};{nome_pet};{nome_cuidado};{descricao};{data_prevista};{responsavel};{anotacoes}\n"
        f.write(linha)
        print("\nCuidado/atividade registrado com sucesso!")
    return

def mostrar_cuidados(animais):
    limpar_tela()
    mostrar_tabela(animais)
    nome = input("\nDigite o nome do animal para ver os cuidados/atividades: ")
    for a in animais:
        if a["nome"].lower() == nome.lower():
            limpar_tela()
            print(f"=== Cuidados/Atividades para {a['nome']} ===")
            if "cuidados" in a and a["cuidados"]:
                for cuidado in a["cuidados"]:
                    print(f"- Descrição: {cuidado['descricao']}")
                    print(f"  Data Prevista: {cuidado['data_prevista']}")
                    print(f"  Responsável: {cuidado['responsavel']}")
                    print("-" * 30)
            else:
                print("Nenhum cuidado/atividade registrado para este animal ainda.")
            pausar()
            return
    print("\nAnimal não encontrado.")
    pausar()


def menu():
    animais = carregar_animais()
    adotores = a.ListAdotar()
    while True:
        limpar_tela()
        print("=== Sistema Adoção+ ===")
        print("1. Adicionar Animal")
        print("2. Ver Animais")
        print("3. Editar Animal")
        print("4. Excluir Animal")
        print("5. Adicionar Cuidado/Atividade")
        print("6. Ver Cuidados/Atividades") 
        print("7. Sugestões Personalizadas")
        print("8. Adicionar Adotor")
        print("9. Ver Adotores")
        print("10. Editar Adotores")
        print("11. Deletar Adotores")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_animal(animais)
        elif opcao == "2":
            limpar_tela()
            mostrar_tabela(animais)
            pausar()
        elif opcao == "3":
            editar_animal(animais)
        elif opcao == "4":
            excluir_animal(animais)
        elif opcao == "5": 
            adicionar_cuidado(animais)
        elif opcao == "6": 
            mostrar_cuidados(animais)
        elif opcao == "7":
            mostrar_sugestoes(animais)
        elif opcao == "8":
            a.AddAdotar(adotores)
        elif opcao == "9":
            limpar_tela()
            a.MostrarAdopt(adotores)
            pausar()
        elif opcao == "10":
            a.EditAdopt(adotores)
        elif opcao == "11":
            a.DelAdopt(adotores)
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")
            pausar()

if __name__ == "__main__":
    menu()
