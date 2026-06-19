def processar_texto(texto):
    texto = texto.lower()
    for caractere in texto:
        if not caractere.isalnum() and caractere != ' ':
            texto = texto.replace(caractere, '')
    return texto.split()

def analisar_texto():
    texto = input("Por favor, insira um texto: ")
    palavras = processar_texto(texto)
    
    frequencia = {}
    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1

    palavras_comuns = sorted(frequencia.items(), key=lambda x: x[1], reverse=True)[:5]

    total_palavras = len(palavras)
    palavras_unicas = len(frequencia)
    comprimento_medio = sum(len(p) for p in palavras) / total_palavras if total_palavras > 0 else 0

    resultados = {
        "Frequência": frequencia,
        "5 Palavras Mais Comuns": palavras_comuns,
        "Total de Palavras": total_palavras,
        "Palavras Únicas": palavras_unicas,
        "Comprimento Médio das Palavras": comprimento_medio
    }

    for chave, valor in resultados.items():
        print(f"{chave}: {valor}")

analisar_texto()