quadrados = {x: x**2 for x in range(1, 11)}
print("Quadrados:", quadrados)

palavras = ["Rui", "Ruben", "Tomas", "Amorim"]
comprimentos = {palavra: len(palavra) for palavra in palavras}
print("Comprimentos:", comprimentos)

notas = {"Ana": 18, "Bruno": 15, "Carla": 17,"David": 12, "Eva": 19}
notas_superiores_15 = {aluno: nota for aluno, nota in notas.items() if nota >= 15}
print("Notas maiores ou iguais a 15:", notas_superiores_15)