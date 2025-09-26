idades_alunos = {"Rui" : 17, "Ana":19, "Carlos": 21}
# Imprimir dicionario
print(idades_alunos)
# Imprimir chaves do dicionario
for nome in idades_alunos.keys():
    print (nome)
# Imprimir vcalores do dicionario
for nome in idades_alunos.values():
    print (nome)
    
# Imprimir chaves e valores formatadosfor 
for k,v in idades_alunos.items():
    print(f' O(A) aluno (a) {k} tem {v} anos.')