from colorama import Fore, Style

linhas = 6
colunas = 6

def cria_matriz_inicial():
    return [['.' for _ in range(colunas)] for _ in range(linhas)]

def mostrar_tabuleiro(matriz, legenda="Tabuleiro"):
    print("=" * 30)
    print(legenda)
    print("=" * 30)

    header = "   " + " ".join(f"{c + 1:2d}" for c in range(colunas))
    print(header)

    for i, linha in enumerate(matriz):
        linha_str = f"{i:2d} "
        for cel in linha:
            if cel == 'F':
                linha_str += Fore.BLUE + cel + Style.RESET_ALL + " "
            elif cel == 'E':
                linha_str += Fore.GREEN + cel + Style.RESET_ALL + " "
            elif cel == 'H':
                linha_str += Fore.YELLOW + cel + Style.RESET_ALL + " "
            elif cel == '✔':
                linha_str += Fore.YELLOW + cel + Style.RESET_ALL + " "
            elif cel == 'X':
                linha_str += Fore.MAGENTA + cel + Style.RESET_ALL + " "
            else:
                linha_str += cel + " "
        print(linha_str)
    print()

def preencher_matriz_com_naves(matriz, mapa_naves: dict):
    for ind, nave in mapa_naves.items():
        linha = ind // colunas
        coluna = ind % colunas
        matriz[linha][coluna] = nave.simbolo if nave.energia > 0 else 'X'

def preencher_matriz_com_tiros(matriz, tiros: list, mapa_naves: dict):
    for tiro in tiros:
        linha = tiro // colunas
        coluna = tiro % colunas
        if tiro in mapa_naves and mapa_naves[tiro].energia > 0:
            matriz[linha][coluna] = '✔'
        else:
            matriz[linha][coluna] = 'X'
