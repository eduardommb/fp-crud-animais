# -*- coding: utf-8 -*-

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
    elif "calmo" in comportamento:
        sugestoes["perfil_adotante"].append("Ótimo para iniciantes ou pessoas de rotina tranquila.")
        sugestoes["compatibilidade"].append("Boa convivência com crianças e idosos.")
    elif "arisco" in comportamento:
        sugestoes["cuidados_especiais"].append("Processo de socialização gradual.")
        sugestoes["perfil_adotante"].append("Indicado para adotante experiente.")
        sugestoes["compatibilidade"].append("Melhor em ambiente sem muito movimento.")


    #compatibilidade

    if especie == "cachorro":
        if "agitado" in comportamento:
            sugestoes["compatibilidade"].append("Compatível com outros cães ativos.")
        else:
            sugestoes["compatibilidade"].append("Compatível com gatos e outros cães tranquilos.")
    elif especie == "gato":
        if "arisco" in comportamento:
            sugestoes["compatibilidade"].append("Requer ambiente calmo e poucas pessoas.")
        else:
            sugestoes["compatibilidade"].append("Boa convivência com outros gatos dóceis.")

    return sugestoes




def mostrar_sugestoes(animais):
    from Cuidados import limpar_tela, mostrar_tabela, pausar

    limpar_tela()
    mostrar_tabela(animais)
    nome = input("\nDigite o nome do animal para gerar sugestões: ")

    for a in animais:
        if a["nome"].lower() == nome.lower():
            limpar_tela()
            print(f"=== Sugestões Personalizadas para {a['nome']} ===\n")

            sugestoes = gerar_sugestoes(a)

            print("\n Perfil ideal de adotante:")
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
