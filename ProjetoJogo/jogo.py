from tabuleiro import cria_matriz_inicial, preencher_matriz_com_naves, preencher_matriz_com_tiros, mostrar_tabuleiro, linhas, colunas
from naves import NaveExtra
from funcoes import aplicar_dano, calcular_eficacia, todas_naves_destruidas, salvar_resultado
from colorama import init
import random
import os
import json

init(autoreset=True)

PASTA_RESULTADOS = os.path.join(os.getcwd(), "Resultados")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def capa():
    print("="*40)
    print("        JOGO DAS NAVES")
    print("="*40)

def mostrar_menu():
    print("1 - Iniciar Novo Jogo")
    print("2 - Carregar Jogo Salvo")
    print("3 - Sair")
    return input("Escolha: ")

def menu_rodada():
    print("\nFim da rodada!")
    print("1 - Ir para a próxima rodada")
    print("2 - Salvar progresso do jogo")
    escolha = input("Escolha: ")
    return escolha

def menu_pos_salvar():
    print("\nJogo salvo com sucesso!")
    print("1 - Voltar ao menu inicial")
    print("2 - Sair do jogo")
    escolha = input("Escolha: ")
    return escolha

def escolher_tipo_tiro():
    print("\nComo deseja jogar os tiros desta rodada?")
    print("1 - Manual (digitar os tiros)")
    print("2 - Automático (aleatório)")
    while True:
        escolha = input("Escolha: ")
        if escolha in ['1', '2']:
            return escolha
        print("Opção inválida! Digite 1 ou 2.")

def tiros_automaticos(qt: int, mapa_naves: dict, tiros_já_feitos: list):
    possiveis = [p for p in range(linhas * colunas) if p not in tiros_já_feitos]
    return random.sample(possiveis, qt)

def posicionar_naves_aleatorio(naves):
    posicoes = random.sample(range(linhas * colunas), len(naves))
    return {pos: nave for pos, nave in zip(posicoes, naves)}

def obter_tiros_do_jogador(qt: int, mapa_naves: dict):
    tiros = []
    print(f"\nInforme {qt} tiros (1 a {linhas*colunas}):")
    while len(tiros) < qt:
        try:
            tiro = int(input(f"Tiro {len(tiros)+1}: ")) - 1
            if tiro < 0 or tiro >= linhas * colunas:
                print("Posição inválida!")
            elif tiro in tiros:
                print("Você já atirou nessa posição nesta rodada!")
            elif tiro in mapa_naves and mapa_naves[tiro].energia == 0:
                nave = mapa_naves[tiro]
                print(f"{nave.nome} ({nave.simbolo}) já foi destruída! Escolha outra posição.")
            else:
                tiros.append(tiro)
        except ValueError:
            print("Digite um número inteiro válido.")
    return tiros

def iniciar_jogo():
    n1 = NaveExtra("Falcon", "BLUE", "F", 5, 10)
    n2 = NaveExtra("Eagle", "GREEN", "E", 10, 15)
    n3 = NaveExtra("Hawk", "YELLOW", "H", 7, 12)
    naves = [n1, n2, n3]

    mapa_naves = posicionar_naves_aleatorio(naves)
    tiros_totais = []
    return tiros_totais, mapa_naves, naves

def salvar_progresso(tiros_totais, mapa_naves, naves, numero_rodada):
    tiros_acertados = sum(1 for t in tiros_totais if t in mapa_naves and mapa_naves[t].energia < mapa_naves[t].perda_energia)
    eficacia = calcular_eficacia(len(tiros_totais), tiros_acertados)
    jogo_data = {
        "tiros_totais": tiros_totais,
        "tiros_acertados": tiros_acertados,
        "eficacia": eficacia,
        "posicoes_naves": list(mapa_naves.keys()),
        "naves_estado": [{ "nome": n.nome, "energia": n.energia, "simbolo": n.simbolo, "cor": n.cor, "perda_energia": n.perda_energia, "energia_extra": getattr(n, 'energia_extra',0)} for n in naves]
    }

    if not os.path.exists(PASTA_RESULTADOS):
        os.makedirs(PASTA_RESULTADOS)

    arquivo = os.path.join(PASTA_RESULTADOS, f"Jogo_Progresso_Rodada{numero_rodada}.json")
    with open(arquivo, "w") as f:
        json.dump(jogo_data, f)
    print(f"\n Progresso do jogo salvo com sucesso na rodada {numero_rodada}!\n")

def carregar_jogo():
    if not os.path.exists(PASTA_RESULTADOS):
        print("\nNenhum jogo salvo encontrado!")
        input("Pressione Enter para continuar...")
        return None, None, None, 1

    arquivos = [f for f in os.listdir(PASTA_RESULTADOS) if f.endswith(".json")]
    jogos_validos = []

    for arq in arquivos:
        caminho = os.path.join(PASTA_RESULTADOS, arq)
        with open(caminho, "r") as f:
            data = json.load(f)
        if len(data["tiros_totais"]) < 105 and not all(n["energia"] == 0 for n in data["naves_estado"]):
            jogos_validos.append(arq)

    if not jogos_validos:
        print("\nNenhum jogo incompleto disponível.")
        input("Pressione Enter para continuar...")
        return None, None, None, 1

    print("\nJogos disponíveis para continuar:")
    for i, j in enumerate(jogos_validos, start=1):
        print(f"{i} - {j}")

    escolha = int(input("Escolha um jogo: ")) - 1
    if escolha < 0 or escolha >= len(jogos_validos):
        print("Escolha inválida!")
        return None, None, None, 1

    caminho = os.path.join(PASTA_RESULTADOS, jogos_validos[escolha])
    with open(caminho, "r") as f:
        data = json.load(f)

    naves = []
    for n in data["naves_estado"]:
        nave = NaveExtra(n["nome"], n["cor"], n["simbolo"], n["perda_energia"], n.get("energia_extra",0))
        nave.energia = n["energia"]
        naves.append(nave)

    mapa_naves = {}
    posicoes = data.get("posicoes_naves", list(range(len(naves))))
    for pos, nave in zip(posicoes, naves):
        mapa_naves[pos] = nave

    tiros_totais = data["tiros_totais"]
    numero_rodada = 1
    return tiros_totais, mapa_naves, naves, numero_rodada

def main():
    while True:
        limpar_tela()
        capa()
        escolha = mostrar_menu()

        if escolha == '3':
            print("Saindo do jogo...")
            return
        elif escolha == '2':
            tiros_totais, mapa_naves, naves, numero_rodada = carregar_jogo()
            if tiros_totais is None:
                continue
        elif escolha == '1':
            tiros_totais, mapa_naves, naves = iniciar_jogo()
            numero_rodada = 1

        tiros_acertados = sum(1 for t in tiros_totais if t in mapa_naves and mapa_naves[t].energia < mapa_naves[t].perda_energia)
        posicoes_naves = list(mapa_naves.keys())

        while len(tiros_totais) < 105:
            if todas_naves_destruidas(naves):
                limpar_tela()
                print("\n🎉 PARABÉNS! Você destruiu todas as naves e venceu o jogo! 🎉\n")
                break

            limpar_tela()

            # ESCOLHER TIPO DE TIRO
            tipo_tiro = escolher_tipo_tiro()
            if tipo_tiro == '1':
                tiros_rodada = obter_tiros_do_jogador(3, mapa_naves)
            else:
                tiros_rodada = tiros_automaticos(3, mapa_naves, tiros_totais)
                print(f"Tiros automáticos desta rodada: {[t+1 for t in tiros_rodada]}")

            tiros_totais.extend(tiros_rodada)

            for tiro in tiros_rodada:
                if tiro in mapa_naves and mapa_naves[tiro].energia > 0:
                    nave = mapa_naves[tiro]
                    aplicar_dano(nave, nave.perda_energia)
                    tiros_acertados += 1
                    print(f"Acertou na {nave.nome}! Perdeu {nave.perda_energia} de energia. Energia restante: {nave.energia}")
                    if nave.energia == 0:
                        print(f"{nave.nome} foi destruída!")

            matriz_naves_rodada = cria_matriz_inicial()
            preencher_matriz_com_naves(matriz_naves_rodada, mapa_naves)
            mostrar_tabuleiro(matriz_naves_rodada, f"Tabuleiro das Naves - Rodada {numero_rodada}")

            matriz_tiros = cria_matriz_inicial()
            preencher_matriz_com_tiros(matriz_tiros, tiros_rodada, mapa_naves)
            mostrar_tabuleiro(matriz_tiros, f"Tabuleiro dos Tiros - Rodada {numero_rodada}")

            for nave in naves:
                nave.mostrar_dados()

            eficacia = calcular_eficacia(len(tiros_totais), tiros_acertados)
            print(f"Tiros dados: {len(tiros_totais)}, Tiros certeiros: {tiros_acertados}, Eficácia: {eficacia}%")

            while True:
                opc = menu_rodada()
                if opc == '1':
                    break
                elif opc == '2':
                    salvar_progresso(tiros_totais, mapa_naves, naves, numero_rodada)
                    escolha_pos_salvar = menu_pos_salvar()
                    if escolha_pos_salvar == '1':
                        break
                    elif escolha_pos_salvar == '2':
                        print("Saindo do jogo...")
                        return
                    else:
                        print("Opção inválida!")
                else:
                    print("Opção inválida!")

            numero_rodada += 1

            naves_vivas = [n for n in naves if n.energia > 0]
            if naves_vivas:
                novas_posicoes = posicionar_naves_aleatorio(naves_vivas)
                for pos, nave in mapa_naves.items():
                    if nave.energia == 0:
                        novas_posicoes[pos] = nave
                mapa_naves = novas_posicoes
                posicoes_naves = list(mapa_naves.keys())

        limpar_tela()
        print("\n=== FIM DO JOGO ===\n")
        matriz_final_naves = cria_matriz_inicial()
        preencher_matriz_com_naves(matriz_final_naves, mapa_naves)
        mostrar_tabuleiro(matriz_final_naves, "Tabuleiro FINAL das Naves")

        matriz_final_tiros = cria_matriz_inicial()
        preencher_matriz_com_tiros(matriz_final_tiros, tiros_totais, mapa_naves)
        mostrar_tabuleiro(matriz_final_tiros, "Tabuleiro FINAL dos Tiros")

        print("=== Estado final das naves ===")
        for nave in naves:
            nave.mostrar_dados()

        if not todas_naves_destruidas(naves):
            print("\n Você não conseguiu destruir todas as naves. Fim de jogo. \n")

        eficacia = calcular_eficacia(len(tiros_totais), tiros_acertados)
        print(f"Tiros dados: {len(tiros_totais)}")
        print(f"Tiros acertados: {tiros_acertados}")
        print(f"Eficácia final: {eficacia}%\n")

        salvar_progresso(tiros_totais, mapa_naves, naves, numero_rodada)

# Chamando main
if __name__ == "__main__":
    main()
