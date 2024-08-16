def calcular_custo_viagem(distancia, custo_combustivel, consumo_veiculo, numero_pedagios, custo_pedagio):
 # Calcula o custo total da viagem, o custo total com combustível e o custo total com pedágios

    custo_combustivel_total = (distancia / consumo_veiculo) * custo_combustivel
    custo_pedagio_total = numero_pedagios * custo_pedagio
    custo_total = custo_combustivel_total + custo_pedagio_total
    return custo_total, custo_combustivel_total, custo_pedagio_total

# Solicita os dados para o calcular do custo da viagem
distancia = float(input("Digite a distância da viagem (em km): "))
custo_combustivel = float(input("Digite o custo do combustível por litro (em R$): "))
consumo_veiculo = float(input("Digite o consumo do veículo (km por litro): "))
numero_pedagios = int(input("Digite o número de pedágios no percurso: "))
custo_pedagio = float(input("Digite o custo de um pedágio (em R$): "))


custo_total, custo_combustivel_total, custo_pedagio_total = calcular_custo_viagem(distancia, custo_combustivel, consumo_veiculo, numero_pedagios, custo_pedagio)
# Chama a função calcular_custo_viagem e guarda os valores retornados

# Exibe os resultados
print("|-------------Custo---------------|")
print(f"Custo total da viagem: R${custo_total:.2f}")
print(f"Custo total com combustível: R${custo_combustivel_total:.2f}")
print(f"Custo total com pedágios: R${custo_pedagio_total:.2f}")

