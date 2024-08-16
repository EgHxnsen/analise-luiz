def calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso):
    # Calcula o valor total a ser pago e o valor dos juros
    taxa_juros_diaria = taxa_juros_anual / 365 / 100
    juros = valor_principal * taxa_juros_diaria * dias_atraso
    valor_total = valor_principal + juros
    return valor_total, juros

valor_principal = 1000.00
taxa_juros_anual = 5.0
dias_atraso = 30

valor_total, juros = calcular_juros_atraso(valor_principal, taxa_juros_anual, dias_atraso)
# Chama a função calcular_juros_atraso e guarda os valores retornados
print(f"Valor total a ser pago: R${valor_total:.2f}")
# Exibe o valor que deve ser pago
print(f"Valor dos juros: R${juros:.2f}")
#Exibe o valor dos juros
