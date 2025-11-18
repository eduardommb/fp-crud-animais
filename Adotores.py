import Cuidados as c

ARQUIVO_ADOTORES = "donos.csv"

# Lista feita
def ListAdotar():
    a = []
    try:
        with open(ARQUIVO_ADOTORES, "r", encoding="utf-8") as arquivo:
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
    c.limpar_tela()
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
    print("\nAnimal atualizado com sucesso!")
    c.pausar()
    return


# Arquivo separado dos animais para organizar
def SaveAdopt(adotores):
    with open(ARQUIVO_ADOTORES, "w", encoding="utf-8") as arquivo:
        for a in adotores:
            linha = f"{a['nome']};{a['idade']};{a['genero']};{a['status']};{a['animal']};{a['comportamento']}\n"
            arquivo.write(linha)


# Mostrar, iqual animal
def MostrarAdopt(adotores):
    if not adotores:
        print("Registre Primeiro!")
    
    print()
    print(f"{'Nome':<15}{'Idade':<15}{'Genero':<15}{'Status':<8}{'Animal Preferido':<20}{'Compatemnto Preferido':<15}")
    print("=" * 108)
    for i in adotores:
        print(f"{i['nome']:<15}{i['idade']:<15}{i['genero']:<15}{i['status']:<8}{i['animal']:<20}{i['comportamento']:<15}")



# editar, mesmo systema
def EditAdopt(adotores):
    c.limpar_tela()
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
            print("\nAnimal atualizado com sucesso!")
            c.pausar()
            return

def DelAdopt(adotores):
    while True:
        c.limpar_tela()
        MostrarAdopt(adotores)
        nm = input("\n \nNome Completo do adotor que deseja deletar: ")
        for a in adotores:
            if a["nome"].lower() == nm.lower():
                adotores.remove(a)
                SaveAdopt(adotores)
                print("\nAdotor deletado com sucesso!")
                c.pausar()
                return
        print("\nAdotor não encontrado. Tentar de novo?")
        yn = input("Y/N: ")
        if (yn == "N"):
            c.pausar()
            return