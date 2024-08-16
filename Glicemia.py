def diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial):
    # Função que recebe os valores de glicemia em jejum e pós-prandial e retorna o diagnóstico

    if glicemia_em_jejum >= 126 or glicemia_pos_prandial >= 200:
        return "Diabetes"
    elif 100 <= glicemia_em_jejum < 126 or 140 <= glicemia_pos_prandial < 200:
        return "Pré-diabetes"
    else:
        return "Saudável"

glicemia_em_jejum = float(input("Digite o valor da glicemia em jejum (mg/dL): "))
# Solicita o valor da glicemia em jejum, utilizando o float para aceitar números decimais

glicemia_pos_prandial = float(input("Digite o valor da glicemia pós-prandial (mg/dL): "))
# Solicita o valor da glicemia pós-prandial, utilizando o float para aceitar números decimais

resultado = diagnosticar_diabetes(glicemia_em_jejum, glicemia_pos_prandial)
# Chama a função diagnosticar_diabetes e guarda o resultado retornado

print(f"Resultado do diagnóstico: {resultado}")
# Exibe o diagnóstico obtido
