import json
import os

# Caminho absoluto para garantir que guarda sempre na mesma pasta do script
BASE_DIR = os.path.dirname(__file__)
FICHEIRO = os.path.join(BASE_DIR, "inventario.json")

# ============================
# CARREGAR E GUARDAR INVENTÁRIO
# ============================

def carregar_inventario():
    # Se o ficheiro não existir, cria um inventário vazio e guarda
    if not os.path.exists(FICHEIRO):
        guardar_inventario([])
        return []

    try:
        # Tenta abrir e ler o conteúdo do ficheiro JSON
        with open(FICHEIRO, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        # Se houver erro (ficheiro vazio ou mal formado), cria inventário vazio
        guardar_inventario([])
        return []

def guardar_inventario(inventario):
    # Guarda a lista de itens no ficheiro JSON com formatação legível
    with open(FICHEIRO, "w", encoding="utf-8") as f:
        json.dump(inventario, f, indent=4, ensure_ascii=False)

# ============================
# FUNÇÕES AUXILIARES
# ============================

def gerar_novo_id(inventario):
    # Gera um novo ID baseado no maior ID atual + 1
    if not inventario:
        return 1
    return max(item["id"] for item in inventario) + 1

def input_inteiro_positivo(msg):
    # Pede ao utilizador um inteiro positivo e valida a entrada
    while True:
        try:
            v = int(input(msg))
            if v < 0:
                print("Tem de ser positivo.")
                continue
            return v
        except:
            print("Número inválido!")

def input_float_positivo(msg):
    # Pede ao utilizador um float positivo e valida a entrada
    while True:
        try:
            v = float(input(msg))
            if v < 0:
                print("Tem de ser positivo.")
                continue
            return v
        except:
            print("Número inválido!")

def encontrar_item_por_id(inventario, id_item):
    # Procura um item pelo seu ID no inventário e devolve-o (ou None se não existir)
    for item in inventario:
        if item["id"] == id_item:
            return item
    return None

# ============================
# CRUD - FUNÇÕES PRINCIPAIS
# ============================

def ver_inventario(inventario):
    # Mostra o inventário formatado
    if not inventario:
        print("\nInventário vazio.\n")
        return

    print("\n===== INVENTÁRIO =====")
    print(f"{'ID':<5}{'Título':<30}{'Autor':<25}{'Qtd':<5}{'Preço (€)':<10}")
    print("-" * 75)

    for item in inventario:
        print(f"{item['id']:<5}{item['titulo']:<30}{item['autor']:<25}{item['quantidade']:<5}{item['preco']:<10.2f}")

    print()

def adicionar_item(inventario):
    # Adiciona um novo livro ao inventário pedindo dados ao utilizador
    print("\n--- Adicionar Livro ---")
    titulo = input("Título: ")
    autor = input("Autor: ")
    quantidade = input_inteiro_positivo("Quantidade: ")
    preco = input_float_positivo("Preço (€): ")

    novo = {
        "id": gerar_novo_id(inventario),
        "titulo": titulo,
        "autor": autor,
        "quantidade": quantidade,
        "preco": preco
    }

    inventario.append(novo)
    print("Livro adicionado!\n")

def atualizar_quantidade(inventario):
    # Atualiza a quantidade de um item existente pelo ID
    id_item = input_inteiro_positivo("ID: ")
    item = encontrar_item_por_id(inventario, id_item)

    if not item:
        print("Item não encontrado.\n")
        return

    nova = input_inteiro_positivo("Nova quantidade: ")
    item["quantidade"] = nova
    print("Quantidade atualizada!\n")

def remover_item(inventario):
    # Remove um item do inventário pelo ID
    id_item = input_inteiro_positivo("ID: ")
    item = encontrar_item_por_id(inventario, id_item)

    if not item:
        print("Item não encontrado.\n")
        return

    inventario.remove(item)
    print("Item removido!\n")

def pesquisa_avancada(inventario):
    # Pesquisa livros por título ou autor, insensível a maiúsculas
    termo = input("Pesquisar por título ou autor: ").lower()

    resultados = [
        item for item in inventario
        if termo in item["titulo"].lower() or termo in item["autor"].lower()
    ]

    if not resultados:
        print("Nenhum resultado.\n")
    else:
        ver_inventario(resultados)

def relatorio_stock(inventario):
    # Calcula e mostra o valor total do stock em euros
    total = sum(item["quantidade"] * item["preco"] for item in inventario)
    print(f"\nValor total do stock: {total:.2f} €\n")
