def calcular_media_e_aprovacao(notas, nota_minima_aprovacao):
    # Calcula a média da turma e verifica quais alunos foram aprovados e reprovados
    total_notas = 0
    num_alunos = len(notas)
    aprovados = []
    reprovados = []

    for aluno, nota in notas.items():
        # Percorre as notas, somando as notas e separando os alunos aprovados e reprovados
        total_notas += nota

    if nota >= nota_minima_aprovacao:
        # Verifica se a nota é maior ou igual à nota mínima de aprovação
        aprovados.append(aluno)
    else:
        reprovados.append(aluno)

    media_turma = total_notas / num_alunos # Calcula a média da turma

    return media_turma, aprovados, reprovados
    # Retorna a média da turma, alunos aprovados e reprovados

notas = {
    "Alice": 85,
    "Bruno": 72,
    "Carlos": 60,
    "Diana": 95,
    "Eduardo": 55
}

nota_minima_aprovacao = 70

media_turma, aprovados, reprovados = calcular_media_e_aprovacao(notas, nota_minima_aprovacao)
# Chama a função calcular_media_e_aprovacao e guarda os valores retornados

print(f"Média da turma: {media_turma:.2f}")
print(f"Alunos aprovados: {', '.join(aprovados)}")
print(f"Alunos reprovados: {', '.join(reprovados)}")