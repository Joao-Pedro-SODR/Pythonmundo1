import random

listaAluno = []
for i in range(0,4):
    aluno = input("Digite o nome do aluno: ")
    listaAluno.append(aluno)

aluno1 = random.choice(listaAluno)
print(aluno1)
aluno2 = random.choice(listaAluno)
print(aluno2)
aluno3 = random.choice(listaAluno)
print(aluno3)
aluno4 = random.choice(listaAluno)
print(aluno4)
