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
                if len(dados) == 9:
                    try:
                        id_pet = int(dados[0])
                    except ValueError:
                        id_pet = len(animais) + 1

                    animal = {
                        "id": id_pet,
                        "nome": dados[1],
                        "especie": dados[2],
                        "raca": dados[3],
                        "idade": int(dados[4]),
                        "saude": dados[5],
                        "data_chegada": dados[6],
                        "comportamento": dados[7],
                        "nome_arquivo": dados[8]
                    }
                    animais.append(animal)
    except FileNotFoundError:
        print("arquivo vazio ou nao encontrado")

    return animais

def salvar_animais(animais):
    with open(ARQUIVO_ANIMAIS, "w", encoding="utf-8") as arquivo:
        for a in animais:
            linha = f"{a['id']};{a['nome']};{a['especie']};{a['raca']};{a['idade']};{a['saude']};{a['data_chegada']};{a['comportamento']};{a['nome_arquivo']}\n"
            arquivo.write(linha)

def calcular_novo_id():
    carregar_animais()
    if not animais:
        return 1
    else:
        maior_id = 0
        for animal in animais:
            if animal.get("id", 0) > maior_id:
                maior_id = animal["id"]
        return maior_id + 1

#buscar pet pelo html
def buscar_pet_por_nome(nome):
    print("entrou na funcao buscar pet por nome")
    carregar_animais()
    nome_procurar = nome.strip().lower()
    for a in animais:
        if a["nome"].strip().lower() == nome_procurar:
            print("Pet encontrado!")
            return a
    return None
def buscar_pet_por_id(id_procurar):
    carregar_animais()
    for a in animais:
        if a["id"] == int(id_procurar):
                print("Pet encontrado!")
                return a
    return None


def mostrar_tabela(animais):
    if not animais:
        print("Nenhum animal cadastrado ainda.")
        return

    print()
    print(f"{'ID':<5}{'Nome':<15}{'Espécie':<15}{'Raça':<15}{'Idade':<8}{'Saúde':<20}{'Chegada':<15}{'Comportamento':<20}")
    print("-" * 108)
    for a in animais:
        print(f"{a['id']:<5}{a['nome']:<15}{a['especie']:<15}{a['raca']:<15}{a['idade']:<8}{a['saude']:<20}{a['data_chegada']:<15}{a['comportamento']:<20}")

def adicionar_animal(nome, especie, raca, idade, saude, data_chegada, comportamento, nome_arquivo):
    carregar_animais()
    novo_id = calcular_novo_id()
    animal = {
        "id": novo_id,
        "nome": nome,
        "especie": especie,
        "raca": raca,
        "idade": idade,
        "saude": saude,
        "data_chegada": data_chegada,
        "comportamento": comportamento,
        "nome_arquivo": nome_arquivo or "padrao.jpg"
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

#apagar pet pelo html
def apagar_pet_por_nome(nome):
    carregar_animais()
    nome_procurar = nome.strip().lower()
    for a in animais:
        if a["nome"].strip().lower() == nome_procurar:
            animais.remove(a)
            salvar_animais(animais)
            print("Pet apagado com sucesso!")
            return True


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


