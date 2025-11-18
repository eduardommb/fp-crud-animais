import os
from datetime import datetime

#Essa biblioteca é importante para manipular datas e horas, 
# suportando extração eficiente de atributos para formatação e manipulação.

ARQUIVO_ANIMAIS = "animais.csv"

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

#Como TUDO tem que ser com função, aqui está a função restritiva do import os, normalmente conhecido, mas 
#adaptado para outros sistemas operacionais, como Linux e MacOS

def pausar():
    input("\nPressione ENTER para continuar...")

#Usado após efetuar com sucesso a opcção escolhida

def carregar_animais():
    animais = []
    try:
        with open(ARQUIVO_ANIMAIS, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")
                if len(dados) == 7:
                    animal = {
                        "nome": dados[0],
                        "especie": dados[1],
                        "raca": dados[2],
                        "idade": int(dados[3]),
                        "saude": dados[4],
                        "data_chegada": dados[5],
                        "comportamento": dados[6]
                    }
                    animais.append(animal)
    except FileNotFoundError:
        pass
    return animais

#Aqui cria-se uma lista para os animais cadastrados e relaciona o arquivo com a seleção das opções
#Primeiro lê-se o arquivo para depois, faz-se um for para percorrê-lo e lê a opção escolhida

def salvar_animais(animais):
    with open(ARQUIVO_ANIMAIS, "w", encoding="utf-8") as arquivo:
        for a in animais:
            linha = f"{a['nome']};{a['especie']};{a['raca']};{a['idade']};{a['saude']};{a['data_chegada']};{a['comportamento']}\n"
            arquivo.write(linha)

#Aqui, após ler o arquivo, vai-se permitir adicionar (escrever = write) os dados, o nome, espécie, raça, idade...

def mostrar_tabela(animais):
    if not animais:
        print("Nenhum animal cadastrado ainda.")
        return

#Se o arquivo quando for lido não tiver animal algum cadastrado ele retorna um print dizendo que nenhum animal foi cadastrado

    print()
    print(f"{'Nome':<15}{'Espécie':<15}{'Raça':<15}{'Idade':<8}{'Saúde':<20}{'Chegada':<15}{'Comportamento':<20}")
    print("-" * 108)
    for a in animais:
        print(f"{a['nome']:<15}{a['especie']:<15}{a['raca']:<15}{a['idade']:<8}{a['saude']:<20}{a['data_chegada']:<15}{a['comportamento']:<20}")

#Aqui ele vai percorrer o arquivo e correlacionar com a quantidade de caracteres

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

#Aqui cria-se uma função restritiva para adicionar um animal, nela vai ter uma sequência de inputs que
#serão usados para preencher a "cardeneta"

    animal = {
        "nome": nome,
        "especie": especie,
        "raca": raca,
        "idade": idade,
        "saude": saude,
        "data_chegada": data_chegada,
        "comportamento": comportamento
    }

    #Aqui cria-se um dicionário para apenas ligar as variáveis aos resultados obtidos pelo input,
    #como uma espécie de chave e fechadura (analogia)

    animais.append(animal) #Adiciona os animais na lista e salva em seguida
    salvar_animais(animais) 
    print("\nAnimal cadastrado com sucesso!") #Aquela mensagem que se repetirá em cada ação realizada com êxito
    pausar() #A função que relaciona ela

def editar_animal(animais): #Aqui vamos criar uma função que permita ao usuário editar o animal sem precisar apagar tudo, só os pontos que deseja
    limpar_tela() #Limpa o terminal (sempre vai ficar aparecendo porque o objetivo é deixar o código limpo e organizado para o usuário)
    mostrar_tabela(animais) #Exibe a tabela para o usuário visualizar os conteúdos
    nome = input("\nDigite o nome do animal que deseja editar: ") #A partir da visualização ele escolhe qual quer editar
    for a in animais: #Percorre a lista dos animais
        if a["nome"].lower() == nome.lower(): #Após percorrer verifica se o nome digitado pela pessoa é o mesmo de algum nome dentro dessa lista
            print("\nDeixe em branco caso não queira alterar.") #Aqui foi só para caso a pessoa tenha clidado sem querer não ser obrigada a editar nada
            a["especie"] = input(f"Nova espécie ({a['especie']}): ") or a["especie"] #Aqui substitui a espécie
            a["raca"] = input(f"Nova raça ({a['raca']}): ") or a["raca"] #Aqui substitui a raça
            nova_idade = input(f"Nova idade ({a['idade']}): ") #Aqui substitui a idade
            if nova_idade:
                a["idade"] = int(nova_idade) #Se substituir a idade, ele vai começar a correlacionar com outros dados
            a["saude"] = input(f"Novo estado de saúde ({a['saude']}): ") or a["saude"] 
            a["data_chegada"] = input(f"Nova data de chegada ({a['data_chegada']}): ") or a["data_chegada"]
            a["comportamento"] = input(f"Novo comportamento ({a['comportamento']}): ") or a["comportamento"]
            salvar_animais(animais) #Salva
            print("\nAnimal atualizado com sucesso!") 
            pausar()
            return 
    print("\nAnimal não encontrado.") #Se o animal não for encontrado, ou seja, se a["nome"].lower() =! nome.lower():
    pausar()

def excluir_animal(animais): #Função restritiva para excluir animal
    limpar_tela() #Limpa, sempre
    mostrar_tabela(animais) #Exibe ao usuário
    nome = input("\nDigite o nome do animal que deseja excluir: ") 
    for a in animais:
        if a["nome"].lower() == nome.lower(): #Verifica se o nome existe para seguir 
            animais.remove(a) #Usa essa função própria para remover
            salvar_animais(animais) #Salva a lista com o resultado após remover
            print("\nAnimal removido com sucesso!")
            pausar()
            return
    print("\nAnimal não encontrado.") |#Caso não encontre na lista o nome do animal
    pausar()

#Aqui estamos criando uma função apenas para salvar o menu

def menu():
    animais = carregar_animais()
    while True:

        limpar_tela() #limpa a cada exibição do menu, assim mantém o código limpo e organizado para o usuário

        print("=== Sistema Adoção+ ===")
        print("1. Adicionar Animal")
        print("2. Ver Animais")
        print("3. Editar Animal")
        print("4. Excluir Animal")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

#Aqui está só relacionando as opções com as funções já criadas no início do código

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
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")
            pausar()

if __name__ == "__main__":
    menu()

