import random

#BUBBLE SORT

def bubble_sort(lista):
    comparacoes = 0
    trocas = 0

    n = len(lista)

    for i in range(n):
        trocou = False

        for j in range(0, n - 1 - i):
            comparacoes += 1

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

                trocas += 1
                trocou = True

        #Se não houve troca, o array já está ordenado
        if not trocou:
            break

    return comparacoes, trocas

#QUICK SORT

def quick_sort(lista):
    comparacoes = 0
    movimentacoes = 0

    def ordenar(inicio, fim):

        nonlocal comparacoes, movimentacoes

        if inicio >= fim:
            return

        #Escolhe o último elemento como pivô
        pivo = lista[fim]

        i = inicio

        for j in range(inicio, fim):
            comparacoes += 1

            if lista[j] <= pivo:

                if i != j:
                    lista[i], lista[j] = lista[j], lista[i]
                    movimentacoes += 1

                i += 1

        # Coloca o pivô na posição correta
        if i != fim:
            lista[i], lista[fim] = lista[fim], lista[i]
            movimentacoes += 1

        ordenar(inicio, i - 1)
        ordenar(i + 1, fim)

    ordenar(0, len(lista) - 1)

    return comparacoes, movimentacoes

#Testes

tamanhos = [10, 20, 1000]

print("RESULTADOS DOS TESTES")
print("-" * 75)

print(
    f"{'Tamanho':<10}"
    f"{'Bubble Comp.':<18}"
    f"{'Bubble Trocas':<18}"
    f"{'Quick Comp.':<18}"
    f"{'Quick Mov.':<15}"
)

print("-" * 75)


for tamanho in tamanhos:

    #Cria os dados
    dados = [random.randint(1, 10000) for _ in range(tamanho)]

    #Faz duas cópias dos mesmos dados
    lista_bubble = dados.copy()
    lista_quick = dados.copy()

    #Bubble Sort
    comp_bubble, trocas_bubble = bubble_sort(lista_bubble)

    #Quick Sort
    comp_quick, mov_quick = quick_sort(lista_quick)

    print(
        f"{tamanho:<10}"
        f"{comp_bubble:<18}"
        f"{trocas_bubble:<18}"
        f"{comp_quick:<18}"
        f"{mov_quick:<15}"
    )
