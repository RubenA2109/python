# Exercicio 01
# Crie um programa que peça o compriomento e a largura 
# de um ratangulo e mostre a area e o perimetro


comprimento = float(input("Digite o comprimento do retangulo:"))
largura = float(input("Digite a largura do ratangulo:"))
area = comprimento * largura
perimetro = comprimento * 2 + largura * 2

print(area)
print(perimetro)


# Exercicio 02
# Crie uma lista com 10 numeros ae imprima apenas os numeros pares

nums = [1,2,3,4,5,6,7,8,9,10]

for n in nums:
    if n % 2 == 0:
        print(n)



# Exercicio 03
# Crie um dicionario em que as chaves seja, nomes de produtos 
# Os valores sejam o preço de cada produto
# Deve devolver o produto mais caro e a média dos precos

produtos = {"Camisa" : 23.25, "Boné":8.75, "Tenis": 58.11}
soma = 0
preco_mais_caro = 0
produto_mais_caro = ""

for nome_produto,preco in produtos.items():
    soma = soma + preco
    if preco > preco_mais_caro:
        preco_mais_caro =  preco
        produto_mais_caro = nome_produto

media = soma /len(produtos)
print(f"O produto mais caro é {produto_mais_caro}")
print(f"Média dos precos {media:.2f}")
    
    