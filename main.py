from robo_gerador import gerar_array, gerar_matriz
from ordenacao import bubble_sort, quick_sort
from buscas import busca_sequencial_matriz
from hands_on import executar_hands_on_1, executar_hands_on_2
import random


# Menu principal
def menu_principal():
    while True:

        # Exibir opções
        print("\n--- MENU ---\n")
        print("1. Experimento de Ordenação (Bubble vs Quick)")
        print("2. Busca em Matrizes")
        print("3. Hands On 1 - Análise de temperatura")
        print("4. Hands On 2 - Monitoramento de Sensores")
        print("0. Sair")

        # Ler opção
        opcao = input("\nEscolha uma opção: ")

        # Opção 1 - Ordenação
        if opcao == "1":
            print("\nExecutando o experimento com listas de 10, 20 e 1000 elementos...\n")

            tamanhos = [10, 20, 1000]

            for cenario in ["Aleatório", "Ordenado", "Invertido"]:

                print(f"\n--- Cenário: {cenario} ---")
                print(f"{'Tamanho':<10} | {'Bubble Comp.':<15} | "
                      f"{'Bubble T.':<12} | {'Quick Comp.':<15} | {'Quick Mov.':<12}")
                print("-" * 75)

                for tam in tamanhos:
                    base = gerar_array(tam)

                    if cenario == "Aleatório":
                        original = base.copy()
                    elif cenario == "Ordenado":
                        original = sorted(base)
                    else:
                        original = sorted(base, reverse=True)

                    # Cria cópias para os dois algoritmos
                    lista_bubble = original.copy()
                    lista_quick = original.copy()

                    _, b_comp, b_trocas = bubble_sort(lista_bubble)
                    _, q_comp, q_mov = quick_sort(lista_quick)

                    print(f"{tam:<10} | {b_comp:<15} | "
                          f"{b_trocas:<12} | {q_comp:<15} | {q_mov:<12}")


        # Opção 2 - Busca em matriz
        elif opcao == "2":
            print("\nBusca em Matriz Personalizada")

            linhas = int(input("Quantidade de linhas: "))
            colunas = int(input("Quantidade de colunas: "))

            matriz = gerar_matriz(linhas, colunas, 1, 100)

            print("\nMatriz gerada:")
            for linha in matriz:
                print("  ".join(f"{num:3}" for num in linha))

            alvo = int(input("\nDigite o número que você quer buscar: "))

            encontrado, lin, col, comparacoes = busca_sequencial_matriz(
                matriz, alvo
            )

            if encontrado:
                print(f"\nValor {alvo} encontrado na posição: "
                      f"Linha {lin}, Coluna {col}")
            else:
                print(f"\nValor {alvo} não encontrado na matriz.")

            print(f"Total de comparações feitas: {comparacoes}")


        # Opção 3 - Hands On 1
        elif opcao == "3":
            temperaturas = []

            print("\n--- HANDS ON 1 - TEMPERATURAS ---")
            print("Digite as 10 temperaturas:\n")

            for i in range(10):
                valor = float(input(f"Temperatura {i + 1}/10: "))
                temperaturas.append(valor)

            executar_hands_on_1(temperaturas)


        # Opção 4 - Hands On 2
        elif opcao == "4":
            matriz_sensores = [
                [round(random.uniform(15.0, 35.0), 1)
                 for _ in range(24)]
                for _ in range(5)
            ]

            try:
                limite = float(
                    input("Informe o limite de temperatura para alerta: ")
                )
            except ValueError:
                limite = 28.0

            executar_hands_on_2(matriz_sensores, limite)


        # Opção 0 - Encerrar
        elif opcao == "0":
            print("\nEncerrando o programa.")
            break


        # Opção inválida
        else:
            print("\nOpção inválida. Tente novamente.")


# Ponto de entrada
if __name__ == "__main__":
    menu_principal()