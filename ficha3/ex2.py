def contar_caracteres(texto):
    d = {}
    for c in texto:
        if c in d.keys():
            d[c] += 1
        else:
            d[c] = 1
    return d

resultado = contar_caracteres("Ruben craque")
print(resultado)