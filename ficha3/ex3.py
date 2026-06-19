biblioteca = {
    "livro1": {
        "titulo": "Python Fluente",
        "autor": "Luciano Ramalho",
        "ano": 2015,
        "disponivel": True
    },
    "livro2": {
        "titulo": "Pense em Python",
        "autor": "Allen B. Downey",
        "ano": 2012,
        "disponivel": False
    },
    "livro3": {
        "titulo": "Introdução à Programação com Python",
        "autor": "Nilo Ney Coutinho Menezes",
        "ano": 2019,
        "disponivel": True
    }
}

# Titulos disponivel
for livro in biblioteca.values():
    if livro["disponivel"]:
        print(livro['titulo'])
        
# Novo livro da biblioteca 
biblioteca['livro4']= {
    "titulo": "Ruben o melhor",
    "autor": "Ruben",
    "ano": 2009,
    "disponivel": True
}

# Livro 1 indisponivel
biblioteca['livro1']['disponivel'] = False

# Livros do autor
def livros_do_autor(autor):
    livros_do_autor = []
    for livro in biblioteca.values():
        if livro['autor'] == autor:
            livros_do_autor.append(livro['titulo'])
    return livros_do_autor