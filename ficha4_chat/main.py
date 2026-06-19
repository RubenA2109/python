import sys 
sys.dont_write_bytecode = True
from inventario import *

def menu():
    inventario = carregar_inventario()

    while True:
        print("""
========== MENU ==========
1. Ver inventário
2. Adicionar item
3. Atualizar quantidade
4. Remover item
5. Pesquisa avançada
6. Relatório de stock
7. Guardar e sair
""")

        op = input("Opção: ")

        if op == "1":
            ver_inventario(inventario)
        elif op == "2":
            adicionar_item(inventario)
        elif op == "3":
            atualizar_quantidade(inventario)
        elif op == "4":
            remover_item(inventario)
        elif op == "5":
            pesquisa_avancada(inventario)
        elif op == "6":
            relatorio_stock(inventario)
        elif op == "7":
            guardar_inventario(inventario)
            print("Inventário guardado. A sair...")
            break
        else:
            print("Opção inválida.\n")


if __name__ == "__main__":
    menu()
