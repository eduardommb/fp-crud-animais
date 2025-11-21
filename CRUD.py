import os
from datetime import datetime

ARQUIVO_ANIMAIS = "animais.csv"

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\nPressione ENTER para continuar...")

animais = []

def carregar_animais():
    animais.clear()
    try:
        with open(ARQUIVO_ANIMAIS, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")
                if len(dados) == 8:
                    animal = {
                        "id": len(animais) + 1,
                        "nome": dados[0],
                        "especie": dados[1],
                        "raca": dados[2],
                        "idade": int(dados[3]),
                        "saude": dados[4],
                        "data_chegada": dados[5],
                        "comportamento": dados[6],
                        "nome_arquivo": dados[7]
                    }
                    animais.append(animal)
    except FileNotFoundError:
        print("arquivo vazio ou nao encontrado")

    return animais


def salvar_animais(animais):
    with open(ARQUIVO_ANIMAIS, "w", encoding="utf-8") as arquivo:
        for a in animais:
            linha = f"{a['nome']};{a['especie']};{a['raca']};{a['idade']};{a['saude']};{a['data_chegada']};{a['comportamento']};{a['nome_arquivo']}\n"
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


def adicionar_animal(nome, especie, raca, idade, saude, data_chegada, comportamento, nome_arquivo):
    animal = {
        "nome": nome,
        "especie": especie,
        "raca": raca,
        "idade": idade,
        "saude": saude,
        "data_chegada": data_chegada,
        "comportamento": comportamento,
        "nome_arquivo": nome_arquivo
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


def menu():
    animais = carregar_animais()
    while True:
        limpar_tela()
        print("=== Sistema Adoção+ ===")
        print("1. Adicionar Animal")
        print("2. Ver Animais")
        print("3. Editar Animal")
        print("4. Excluir Animal")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            limpar_tela()
            nome = input("Nome: ")
            especie = input("Espécie: ")
            raca = input("Raça: ")
            idade = int(input("Idade: "))
            saude = input("Estado de saúde: ")
            data_chegada = input("Data de chegada: ")
            comportamento = input("Comportamento: ")
            nome_arquivo = input("Nome do arquivo da foto: ")

            adicionar_animal(nome, especie, raca, idade, saude, data_chegada, comportamento, nome_arquivo)

        elif opcao == "2":
            limpar_tela()
            mostrar_tabela(animais)
            pausar()

        elif opcao == "3":
            editar_animal(animais)

        elif opcao == "4":
            excluir_animal(animais)

        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida!")
            pausar()


if __name__ == "__main__":
    menu()


