# Busca sequencial em matriz bidimensional
def busca_sequencial_matriz(matriz, valor_procurado):

    # 1. Obter as dimensões da matriz
    linhas = len(matriz)
    colunas = len(matriz[0]) if linhas > 0 else 0

    # 2. Inicializar o contador de comparações
    comparacoes = 0

    # 3. Percorrer todas as linhas e colunas da matriz
    for i in range(linhas):
        for j in range(colunas):

            # Cada elemento analisado conta como uma comparação
            comparacoes += 1

            # Verificar se o valor procurado foi encontrado
            if matriz[i][j] == valor_procurado:
                return True, i, j, comparacoes

    # 4. Caso o valor não seja encontrado
    # Retorna -1 para linha e coluna
    return False, -1, -1, comparacoes


# Função para criar uma matriz preenchida com números
def criar_matriz(linhas, colunas):

    matriz = []
    numero = 1

    # Percorrer as linhas
    for i in range(linhas):

        linha = []

        # Preencher as colunas
        for j in range(colunas):
            linha.append(numero)
            numero += 1

        matriz.append(linha)

    return matriz


# Função para realizar os testes
def testar_matriz(linhas, colunas):

    # Criar a matriz
    matriz = criar_matriz(linhas, colunas)

    # 1. Valor localizado no início da matriz
    valor_inicio = 1

    # 2. Valor localizado próximo ao final da matriz
    valor_final = (linhas * colunas) - 1

    # 3. Valor que não existe na matriz
    valor_inexistente = -1

    # Realizar a busca do valor no início
    resultado_inicio = busca_sequencial_matriz(
        matriz, valor_inicio
    )

    # Realizar a busca do valor próximo ao final
    resultado_final = busca_sequencial_matriz(
        matriz, valor_final
    )

    # Realizar a busca do valor inexistente
    resultado_inexistente = busca_sequencial_matriz(
        matriz, valor_inexistente
    )

    # Mostrar os resultados
    print("\nMatriz:", linhas, "x", colunas)
    print("Número de elementos:", linhas * colunas)

    print(
        "Busca no início:",
        resultado_inicio[3],
        "comparação(ões)"
    )

    print(
        "Busca no final:",
        resultado_final[3],
        "comparações"
    )

    print(
        "Valor inexistente:",
        resultado_inexistente[3],
        "comparações"
    )


# Teste com matriz 2 x 2
testar_matriz(2, 2)

# Teste com matriz 10 x 10
testar_matriz(10, 10)

# Teste com matriz 100 x 100
testar_matriz(100, 100)
