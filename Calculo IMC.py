def calcular_imc(peso, altura):
    # Calcula o IMC com base no peso e altura fornecidos
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    # Classifica o IMC em categorias de acordo com a tabela da OMS
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"

def sugestao_atividade_fisica(classificacao_imc):
    # Sugere atividades físicas de acordo com a classificação do IMC

    if classificacao_imc == "Abaixo do peso":
        return "Sugere-se atividades de fortalecimento muscular, como musculação, e uma dieta rica em proteínas e calorias."
    elif classificacao_imc == "Peso normal":
        return "Sugere-se a manutenção com atividades aeróbicas regulares, como caminhada, corrida leve e natação, junto a um treino de força moderado."
    elif classificacao_imc == "Sobrepeso":
        return "Sugere-se atividades aeróbicas moderadas, como caminhada rápida, ciclismo e natação, além de exercícios de resistência."
    elif classificacao_imc == "Obesidade grau 1":
        return "Sugere-se atividades de baixo impacto, como caminhadas, natação e hidroginástica, junto a um programa de reeducação alimentar."
    elif classificacao_imc == "Obesidade grau 2":
        return "Sugere-se exercícios de baixo impacto com supervisão, como hidroginástica e pilates, e acompanhamento nutricional."
    else:
        return "Sugere-se atividades físicas supervisionadas por profissionais de saúde, como hidroginástica, fisioterapia, e consultas regulares com um nutricionista."

peso = float(input("Digite seu peso (em kg): "))
# Solicita o peso, utilizando o float para aceitar números decimais

altura = float(input("Digite sua altura (em metros): "))
# Solicita a altura, utilizando o float para aceitar números decimais

imc = calcular_imc(peso, altura)
# Chama a função calcular_imc e guarda o valor retornado

classificacao_imc = classificar_imc(imc)
# Chama a função classificar_imc e guarda a classificação do IMC

sugestao = sugestao_atividade_fisica(classificacao_imc)
# Chama a função sugestao_atividade_fisica e guarda a sugestão de atividade física

# Exibe o IMC, classificação e sugestão de atividade física
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao_imc}")
print(f"Sugestão de atividade física: {sugestao}")