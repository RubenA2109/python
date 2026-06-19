aluno = {
    "Nome": "Ana Silva",
    "Idade": 17,
    "Disciplinas": ["Matemática", "Física", "Informática"],
    "Notas": {"Matemática": 18, "Física": 17, "Informática": 19}
}

aluno["Disciplinas"].append("Português")
aluno["Notas"]["Português"] = 16

notas_aluno = aluno['Notas']
notas = [nota for nota in notas_aluno.values()]
media = sum(notas) / len(notas)
print(f"Média das notas: {media:.2f} valores")