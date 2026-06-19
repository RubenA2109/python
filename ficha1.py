# 1. Crie uma lista com os números pares de 1 a 10.

lista = [i for i in range(1,11) if i % 2 == 0]
print(lista)

# 2. Crie uma lista com os quadrados dos números de 1 a 10.

quadrados = [x**2 for x in range(1, 11)]
print("Quadrados:", quadrados)
print()

# 3. Dada uma lista de palavras, crie uma nova lista que indique o tamanho de cada
# palavra.

nomes = ["Ruben", "Rui", "Amorim", "Granja"]
tamanho = [len(l) for l in nomes]
print("Tamanho:", tamanho)
print()

# 4. Dada uma lista de números, crie uma lista apenas com os números maiores que 5.

nums = [1,2,3,4,5,6,7,8,9]
maiores_que_5 = [x for x in nums if x > 5]
print("Maiores que 5:", maiores_que_5)
print()

# 5. Crie uma lista com as letras maiúsculas de uma string. (nome = 'MarcelO ViEiRa
# amorIM')

nome = "MarcelO ViEiRa amorIM"
m = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
maiusculas = [letra for letra in nome if letra in m]
print(maiusculas)

# 6. Dada uma lista de números, crie uma nova lista onde se o número for múltiplo de 3,
# é apresentado o dobro deste caso contrário aparece o mesmo número da lista original.

numeros = [1, 2, 3, 4, 5, 6, 7, 9, 10]
lista = [x*2 if x % 3 == 0 else x for x in numeros]
print(lista)
print()

# 7. Dada uma lista de nomes, crie uma nova lista apenas com os nomes que começam
# com a letra "A". Todos os nomes da nova lista devem aparecer em maiúsculas.

nome  = ["Ana", "Rui", "joão", "Mariana", "Alice", "Luana"]
nomes_A = [nome.upper() for nome in nomes if nome.startswith('A')]

# 8. Dada uma lista de frutas, crie uma nova lista com o comprimento de cada fruta,
# apenas para as frutas com mais de 5 letras. Caso contrário, deve aparecer 0.

frutas = ["Pera", "Banana", "Maca", "Melao", "Melancia", ]
nova_lista = [len(fruta) if len(fruta) > 5 else 0 for fruta in frutas]
print(nova_lista)