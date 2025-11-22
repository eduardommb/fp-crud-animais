import os
from datetime import datetime
from datetime import date
ARQUIVO_ANIMAIS = "animais.csv"
ARQUIVO_CUIDADOS = "cuidados.csv" 
ARQUIVO_ADOTADORES = "donos.csv"

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\nPressione ENTER para continuar...")

animais = []

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

def calcular_data(data_prevista):
    dia, mes, ano = map(int, data_prevista.split("/"))

    data_consulta = date(ano, mes, dia)

    data_atual = date.today()

    diferença = data_consulta - data_atual

    return diferença.days

def data_especifica(animais):
    limpar_tela()
    mostrar_tabela(animais)

    nome_do_animal = input("\nDigite o nome do animal que deseja ver a data: ").lower()

    encontrado = False  

    for c in animais:
        if nome_do_animal == c["nome"].lower():
            encontrado = True
            limpar_tela()
            if "cuidados" not in c or len(c["cuidados"]) == 0:
                print("Este animal não possui cuidados cadastrados")
                pausar()
                return
            
            print(f"\n-------Cuidados de {c['nome']}:--------\n")
            for d in c['cuidados']:
                dias = calcular_data(d['data_prevista'])
                print(f"- {d['descricao']} ({d['data_prevista']}): faltam {dias} dias")

            pausar()
            return  

    if not encontrado:
        print("Animal não encontrado.")
        pausar()

def gerar_sugestoes(animal):
    especie = animal["especie"].lower()
    idade = animal["idade"]
    comportamento = animal["comportamento"].lower()

    sugestoes = {
        "perfil_adotante": [],
        "compatibilidade": [],
        "cuidados_especiais": [],
        "atividades_recomendadas": [],
    }

    #especie
    
    if especie == "cachorro":
        sugestoes["perfil_adotante"].append(
            "Famílias ativas ou pessoas que gostam de caminhadas."
        )
        sugestoes["atividades_recomendadas"].append(
            "Passeios frequentes, brincadeiras ao ar livre e treinamento básico."
        )
    elif especie == "gato":
        sugestoes["perfil_adotante"].append(
            "Lares tranquilos; ótimo para apartamentos."
        )
        sugestoes["atividades_recomendadas"].append(
            "Arranhadores, brinquedos interativos e enriquecimento ambiental."
        )
    else:
        sugestoes["perfil_adotante"].append(
            "Adotantes flexíveis; espécie com boa adaptação geral."
        )
        sugestoes["atividades_recomendadas"].append(
            "Atividades específicas da espécie."
        )


    #idade

    if idade <= 1:
        sugestoes["cuidados_especiais"].append("Requer bastante atenção e treinamento inicial.")
        sugestoes["perfil_adotante"].append("Pessoas com tempo disponível para educar e brincar.")
    elif idade <= 7:
        sugestoes["perfil_adotante"].append("Adotante buscando comportamento previsível.")
        sugestoes["atividades_recomendadas"].append("Rotina equilibrada entre atividade e descanso.")
    else:
        sugestoes["cuidados_especiais"].append("Cuidados geriátricos e acompanhamento de saúde.")
        sugestoes["perfil_adotante"].append("Pessoas tranquilas, preferencialmente experientes.")


    #comportamento

    if "agitado" in comportamento:
        sugestoes["atividades_recomendadas"].append("Exercícios diários e brinquedos que gastem energia.")
        sugestoes["perfil_adotante"].append("Pessoas com rotina ativa.")
        sugestoes["compatibilidade"].append("Ideal com famílias jovens; pode não ir bem com idosos.")

    elif "calmo" in comportamento or "tranquilo" in comportamento:
        sugestoes["perfil_adotante"].append("Ótimo para iniciantes ou pessoas de rotina tranquila.")
        sugestoes["compatibilidade"].append("Boa convivência com crianças e idosos.")

    elif "arisco" in comportamento or "agressivo" in comportamento or "violento" in comportamento:
        sugestoes["cuidados_especiais"].append("Processo de socialização gradual.")
        sugestoes["perfil_adotante"].append("Indicado para adotante experiente.")
        sugestoes["compatibilidade"].append("Melhor em ambiente sem muito movimento.")

    #compatibilidade

    if especie == "cachorro":
        if "agitado" in comportamento or "agressivo" in comportamento or "violento" in comportamento:
            sugestoes["compatibilidade"].append("Compatível com outros cães ativos.")
        else:
            sugestoes["compatibilidade"].append("Compatível com gatos e outros cães tranquilos.")

    elif especie == "gato":
        if "arisco" in comportamento or "agressivo" in comportamento or "violento" in comportamento:
            sugestoes["compatibilidade"].append("Requer ambiente calmo e poucas pessoas.")
        else:
            sugestoes["compatibilidade"].append("Boa convivência com outros gatos dóceis.")

    return sugestoes

def mostrar_sugestoes(animais):
    limpar_tela()
    mostrar_tabela(animais)
    nome = input("\nDigite o nome do animal para gerar sugestões: ")

    for a in animais:
        if a["nome"].lower() == nome.lower():
            limpar_tela()
            print(f"=== Sugestões Personalizadas para {a['nome']} ===\n")

            sugestoes = gerar_sugestoes(a)

            print("Perfil ideal de adotante:")
            for s in sugestoes["perfil_adotante"]:
                print(f"  - {s}")

            print("\n Compatibilidade:")
            for s in sugestoes["compatibilidade"]:
                print(f"  - {s}")

            print("\n Cuidados especiais:")
            for s in sugestoes["cuidados_especiais"]:
                print(f"  - {s}")

            print("\n Atividades recomendadas:")
            for s in sugestoes["atividades_recomendadas"]:
                print(f"  - {s}")

            pausar()
            return

    print("\nAnimal não encontrado.")
    pausar()

# Lista feita
def ListAdotar():
    a = []
    try:
        with open(ARQUIVO_ADOTADORES, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")
                if len(dados) == 6:
                    adopt = {
                        "nome": dados[0],
                        "idade": int(dados[1]),
                        "genero": dados[2],
                        "status": dados[3],
                        "animal": dados[4],
                        "comportamento": dados[5]
                    }
                    a.append(adopt)
    except FileNotFoundError:
        pass
    return a


# Adionar pessoa
def AddAdotar(adotores):
    limpar_tela()
    print("=========CADASTRO DE ADOÇÃO========")
    nm = input("Nome Completo: ")
    age = int(input("Idade: "))
    sex = input("Genero: ")
    status = input("Status: ")
    animal = input("Animal querido: ")
    comp = input("Comportamento Animal: ")

    guy = {
        "nome": nm,
        "idade": age,
        "genero": sex,
        "status": status,
        "animal": animal,
        "comportamento": comp
    }
    adotores.append(guy)
    SaveAdopt(adotores)
    print("\nAdotante atualizado com sucesso!")
    pausar()
    return


# Arquivo separado dos animais para organizar
def SaveAdopt(adotores):
    with open(ARQUIVO_ADOTADORES, "w", encoding="utf-8") as arquivo:
        for a in adotores:
            linha = f"{a['nome']};{a['idade']};{a['genero']};{a['status']};{a['animal']};{a['comportamento']}\n"
            arquivo.write(linha)


# Mostrar, iqual animal
def MostrarAdopt(adotores):
    if not adotores:
        print("Registre Primeiro!")
    
    print()
    print(f"{'Nome':<35}{'Idade':<15}{'Genero':<15}{'Status':<15}{'Animal Preferido':<20}{'Comportamento Preferido':<20}")
    print("=" * 120)
    for i in adotores:
        print(f"{i['nome']:<35}{i['idade']:<15}{i['genero']:<15}{i['status']:<15}{i['animal']:<20}{i['comportamento']:<20}")



# editar, mesmo systema
def EditAdopt(adotores):
    limpar_tela()
    MostrarAdopt(adotores)
    sel = input("\n \nnome de quem quer Editar: ")
    for a in adotores:
        if a["nome"].lower() == sel.lower():
            print("\nDeixe em branco caso não queira alterar.")
            nova_idade = input(f"Nova idade ({a['idade']}): ")
            if nova_idade:
                a["idade"] = int(nova_idade)
            a["genero"] = input(f"Nova Genero ({a['genero']}): ") or a["genero"]
            a["status"] = input(f"Novo Status da Adoção ({a['status']}): ") or a["status"]
            a["animal"] = input(f"Novo Animal querido ({a['animal']}): ") or a["animal"]
            a["comportamento"] = input(f"Novo comportamento querido ({a['comportamento']}): ") or a["comportamento"]
            SaveAdopt(adotores)
            print("\nAdotante atualizado com sucesso!")
            pausar()
            return

def DelAdopt(adotores):
    while True:
        limpar_tela()
        MostrarAdopt(adotores)
        nm = input("\n \nNome Completo do adotor que deseja deletar: ")
        for a in adotores:
            if a["nome"].lower() == nm.lower():
                adotores.remove(a)
                SaveAdopt(adotores)
                print("\nAdotor deletado com sucesso!")
                pausar()
                return
        print("\nAdotor não encontrado. Tentar de novo?")
        yn = input("Y/N: ")
        if (yn == "N"):
            pausar()
            return


def menu():
    animais = carregar_animais()
    adotores = ListAdotar()
    while True:
        limpar_tela()
        print("=== Sistema Adoção+ ===")
        print("1. Adicionar Animal")
        print("2. Ver Animais")
        print("3. Editar Animal")
        print("4. Excluir Animal")
        print("5. Adicionar Cuidado/Atividade")
        print("6. Ver Cuidados/Atividades") 
        print("7. Ver Datas")
        print("8. Sugestões Personalizadas")
        print("9. Adicionar Adotor")
        print("10. Ver Adotores")
        print("11. Editar Adotores")
        print("12. Deletar Adotores")
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
            data_especifica(animais)
        elif opcao == "8":
            mostrar_sugestoes(animais)
        elif opcao == "9":
            AddAdotar(adotores)
        elif opcao == "10":
            limpar_tela()
            MostrarAdopt(adotores)
            pausar()
        elif opcao == "11":
            EditAdopt(adotores)
        elif opcao == "12":
            DelAdopt(adotores)
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")
            pausar()


if __name__ == "__main__":
    menu()


