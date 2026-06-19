# Exercício 1: Adicionar uma tarefa ao final da lista

tarefas = []
tarefas.append(["O Granja ficar calado"])
print("Lista de tarefas atual:", tarefas)

# 2. Adicionar Múltiplas Tarefas: Adicionar várias tarefas de uma vez.

tarefas = []
tarefas.append("Ir ao cinema")
tarefas.append("Lavar roupa")
tarefas.append("Secar cabelo")
print(tarefas)

# 3. Inserir Tarefa em Posição Específica: Adicionar uma tarefa numa posição específica
# da lista.



# 4. Remover Tarefa por Nome : Remover uma tarefa específica da lista pelo seu conteúdo.

tarefas.remove("Secar cabelo")

# 5. Remover Última Tarefa ou por Índice: Remover a última tarefa ou uma tarefa numa
# posição específica.

tarefas = []
tarefas.append("Ir ao cinema")
tarefas.append("Lavar roupa")
tarefas.append("Secar cabelo")
print(tarefas)
tarefas.pop(1)
print(tarefas.index("Ir ao cinema"))

# 6. Remover todas as Tarefas: Remover todas as tarefas da lista.



# 7. Contar Ocorrências de Tarefa: Verificar quantas vezes uma tarefa específica aparece
# na lista.

lista = [1,2,3,4,5,6,7,8]
print(lista.count(3))
lista.insert(3,8)
print(lista)

# 8. Encontrar Índice de Tarefa: Localizar a primeira ocorrência de uma tarefa na lista.

print(tarefas.index("Ir ao cinema"))

# 9. Ordenar Tarefas: Organizar as tarefas em ordem alfabética.

tarefas.sort()

# 10. Inverter Ordem das Tarefas: Reverter a ordem atual das tarefas.

tarefas.reverse()

# 11. Copiar Lista de Tarefas: Criar uma cópia independente da lista de tarefas.

tarefas2 = tarefas.copy()