# Hands On 1 - Análise das temperaturas
def executar_hands_on_1(temperaturas):
    temperatura = []

    # Exibe as temperaturas armazenadas e seus respectivos índices
    print("\n--- TEMPERATURAS ---")
    for i in range(10):
        print(f"Índice {i}: {temperaturas[i]:.1f} °C")

    # Define os valores iniciais para realizar os cálculos
    soma = 0
    maior = temperaturas[0]
    menor = temperaturas[0]
    indice_maior = 0
    indice_menor = 0
    operacoes = 0

    # Faz a leitura de todos os valores do array
    for i in range(10):
        soma += temperaturas[i]
        operacoes += 1

        # Compara para descobrir a maior temperatura
        operacoes += 1
        if temperaturas[i] > maior:
            maior = temperaturas[i]
            indice_maior = i

        # Compara para encontrar a menor temperatura
        operacoes += 1
        if temperaturas[i] < menor:
            menor = temperaturas[i]
            indice_menor = i

    # Calcula o valor médio das temperaturas
    media = soma / 10
    operacoes += 1

    # Verifica quantas temperaturas ficaram acima da média
    acima_media = 0
    for i in range(10):
        operacoes += 1
        if temperaturas[i] > media:
            acima_media += 1

    # Apresenta os resultados obtidos
    print("\n--- RESULTADOS ---")
    print(f"Média: {media:.2f} °C")
    print(f"Maior temperatura: {maior:.1f} °C")
    print(f"Índice do maior valor: {indice_maior}")
    print(f"Menor temperatura: {menor:.1f} °C")
    print(f"Índice do menor valor: {indice_menor}")
    print(f"Quantidade de valores acima da média: {acima_media}")
    print(f"Total de operações realizadas: {operacoes}")


# Hands On 2 - Análise dos sensores
def executar_hands_on_2(sensores, limite):

    maior_temp = sensores[0][0]
    sensor_maior = 0
    horario_maior = 0
    soma_geral = 0
    acima_limite = 0

    # Guarda a média calculada individualmente para cada sensor
    media_sensor = [0.0] * 5

    # Percorre os 5 sensores
    for i in range(5):
        soma_sensor = 0

        # Analisa as 24 medições realizadas pelo sensor
        for j in range(24):
            temp = sensores[i][j]

            # Acumula os valores para calcular as médias
            soma_sensor += temp
            soma_geral += temp

            print(f" Sensor {i} | Horário {j:02d}h: {temp:.2f}°C")

            # Atualiza o registro caso seja encontrada uma temperatura maior
            if temp > maior_temp:
                maior_temp = temp
                sensor_maior = i
                horario_maior = j

            # Verifica se a temperatura ultrapassou o limite definido
            if temp > limite:
                acima_limite += 1

        # Calcula a média das medições deste sensor
        media_sensor[i] = soma_sensor / 24

    # Calcula a média considerando todas as medições
    media_geral = soma_geral / (5 * 24)

    # Exibe o resumo da análise dos sensores
    print(f"Média geral: {media_geral:.2f}")
    print(f"Maior temperatura: {maior_temp:.2f}")
    print(f"Sensor: {sensor_maior}")
    print(f"Horário: {horario_maior}")
    print(f"Acima do limite ({limite}): {acima_limite}")