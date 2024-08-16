def calcular_area_comodos():
    # Calcula a área total de uma casa
    total_area = 0

    while True:

        largura = float(input("Digite a largura do cômodo (em metros): "))
        # Solicita a largura do cômodo, utilizando o float para aceitar números decimais
        comprimento = float(input("Digite o comprimento do cômodo (em metros): "))
        # Solicita o comprimento do cômodo, utilizando o float para aceitar números decimais

        area_comodo = largura * comprimento
        # Calcula a área do cômodo

        print(f"A área deste cômodo é: {area_comodo:.2f} metros quadrados.")
        # Exibe a área do cômodo

        total_area += area_comodo # Adiciona a área do cômodo à área total

        mais_comodos = input("Deseja adicionar mais cômodos? (s/n): ").strip().lower()
        # Pergunta se o usuário deseja adicionar mais cômodos, Strip remove espaços em branco e Lower converte para minúsculas

        if mais_comodos != 's': # Se a resposta não for 's', encerra o loop
            break

        return total_area

area_total = calcular_area_comodos()
# Chama a função calcular_area_comodos e guarda o valor retornado
print(f"A área total da casa é: {area_total:.2f} metros quadrados.")
# Exibe a área total da casa