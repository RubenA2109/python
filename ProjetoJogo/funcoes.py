from typing import List
import os
from datetime import datetime

def aplicar_dano(nave, dano: int):
    nave.energia = max(0, nave.energia - dano)

def aplicar_energia_extra(nave):
    if hasattr(nave, "energia_extra"):
        nave.energia = min(100, nave.energia + nave.energia_extra)

def calcular_eficacia(tiros_dados: int, tiros_acertados: int) -> float:
    if tiros_dados == 0:
        return 0.0
    return round((tiros_acertados / tiros_dados) * 100, 2)

def todas_naves_destruidas(naves: List) -> bool:
    return all(nave.energia == 0 for nave in naves)

def salvar_resultado(jogo_data: dict):
    """
    Cria um ficheiro com os resultados do jogo.
    jogo_data deve conter:
    {
        "tiros_totais": int,
        "tiros_acertados": int,
        "eficacia": float,
        "posicoes_naves": list[int],
        "posicoes_tiros": list[int],
        "naves": list[NaveExtra]
    }
    """
    pasta = os.path.join(os.getcwd(), "Resultados")
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    nome_ficheiro = f"Jogo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    caminho = os.path.join(pasta, nome_ficheiro)

    with open(caminho, "w") as f:
        f.write("=== Resultado do Jogo ===\n\n")
        f.write(f"Tiros dados: {jogo_data['tiros_totais']}\n")
        f.write(f"Tiros acertados: {jogo_data['tiros_acertados']}\n")
        f.write(f"Eficacia: {jogo_data['eficacia']}%\n\n")

        f.write("=== Posicoes das Naves ===\n")
        for pos, nave in zip(jogo_data['posicoes_naves'], jogo_data['naves']):
            f.write(f"Pos {pos}: {nave.nome} ({nave.simbolo}) - Energia final: {nave.energia}\n")

        f.write("\n=== Posicoes dos Tiros ===\n")
        f.write(", ".join(str(t + 1) for t in jogo_data['posicoes_tiros']) + "\n")
