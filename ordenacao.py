import random


# BUBBLE SORT
def bubble_sort(lista):
    comparacoes = 0
    trocas = 0

    n = len(lista)

    for i in range(n):
        trocou = False

# Compara os elementos vizinhos da lista

        for j in range(0, n - 1 - i):
            comparacoes += 1

# Se o elemento atual for maior que o próximo,
 # eles trocam de posição

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1
                trocou = True

# Se não houve nenhuma troca, a lista já está ordenada

        if not trocou:
            break

    return comparacoes, trocas


# QUICK SORT
def quick_sort(lista):
    comparacoes = 0
    movimentacoes = 0

    def ordenar(inicio, fim):
        nonlocal comparacoes, movimentacoes

# Para quando não houver mais elementos para dividir

        if inicio >= fim:
            return

# O último elemento será usado como pivô

        pivo = lista[fim]
        i = inicio - 1

# Percorre os elementos comparando com o pivô

        for j in range(inicio, fim):
            comparacoes += 1

            if lista[j] <= pivo:
                i += 1

# Faz a troca dos elementos quando necessario

                if i != j:
                    lista[i], lista[j] = lista[j], lista[i]
                    movimentacoes += 1

# Coloca o pivô na posição correta

        if i + 1 != fim:
            lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
            movimentacoes += 1

        posicao_pivo = i + 1

# Ordena a parte esquerda da lista

        ordenar(inicio, posicao_pivo - 1)
        ordenar(posicao_pivo + 1, fim)

    ordenar(0, len(lista) - 1)

    return comparacoes, movimentacoes

# Testados arrays

tamanhos = [10, 20, 1000]

print("=" * 75)
print("COMPARAÇÃO ENTRE BUBBLE SORT E QUICK SORT")
print("=" * 75)

print(
    f"{'Tamanho':<12}"
    f"{'Bubble Comp.':<18}"
    f"{'Bubble Trocas':<18}"
    f"{'Quick Comp.':<18}"
    f"{'Quick Mov.':<18}"
)

print("-" * 75)


for tamanho in tamanhos:

    # Gera os dados originais
    lista_original = [random.randint(1, 10000) for _ in range(tamanho)]

    # Cria uma cópia dos mesmos dados para cada algoritmo
    lista_bubble = lista_original.copy()
    lista_quick = lista_original.copy()

    # Executa Bubble Sort
    bubble_comparacoes, bubble_trocas = bubble_sort(lista_bubble)

    # Executa Quick Sort
    quick_comparacoes, quick_movimentacoes = quick_sort(lista_quick)

    # Mostra os resultados
    print(
        f"{tamanho:<12}"
        f"{bubble_comparacoes:<18}"
        f"{bubble_trocas:<18}"
        f"{quick_comparacoes:<18}"
        f"{quick_movimentacoes:<18}"
    )


print("-" * 75)