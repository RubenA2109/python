import os, getpass
from ficha3.dados.inventario import adicionar, remover, abaixo_do_stock, atualizar, valor_total
   
def menu ():
    print("1 - Adicionar produto")
    print("2 - Atualizar quantidade")
    print("3 - Remover produto")
    print("4 - Listar produtos abaixo do stock")
    print("5 - Valor em stock")
    print("6 - Listar dicionarios de produtos")
    print("7 - Sair da aplicação")
    escolha = int(input("Digite a opção a ser executada: "))
    return escolha

inventario = {}
op = menu()

while op < 7:
    if op == 1:        
        inventario = adicionar(inventario)
    elif op == 2:
        qtde = int(input("Quantidade atualizada"))
        inventario = atualizar(inventario, qtde)
    elif op == 3:
        inventario = remover(inventario)                   
    elif op == 4:
        qtde = int(input("Quantidade considarada abaixo de stock"))
        abaixo_do_stock(inventario, qtde)   
    elif op == 5:
        print(f"Valor em stock: {valor_total(inventario)}")
    elif op == 6:  
        print(inventario)  
    else:
        break                   
    getpass.getpass("Pressione ENTER para voltar para o menu")
    os.system("cls")
    op =  menu ()
print ("Programa terminado")