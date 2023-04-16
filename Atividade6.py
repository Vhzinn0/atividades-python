alunos = {}
soma_notas = 0

for i in range(3):
    nome_aluno = input("Digite o nome do aluno: ")
    nota_aluno = float(input("Digite a nota do aluno: "))
    alunos[nome_aluno] = nota_aluno
    soma_notas += nota_aluno

media_notas = soma_notas / 3

print("A média das notas é:", media_notas)