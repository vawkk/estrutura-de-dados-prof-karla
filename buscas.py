import heapq
import random


# Classe que representa um cliente
class Cliente:
    def __init__(self, nome, senha, prioridade):
        self.nome = nome
        self.senha = senha
        self.prioridade = prioridade

    def __repr__(self):
        tipos = {
            1: "Emergência",
            2: "Prioritário",
            3: "Normal"
        }

        return f"{self.senha} - {self.nome} | {tipos.get(self.prioridade)}"


# Fila tradicional utilizando o conceito FIFO
class FilaComum:
    def __init__(self):
        self.dados = []

    def adicionar(self, cliente):
        self.dados.append(cliente)

    def remover(self):
        if self.vazia():
            return None
        return self.dados.pop(0)

    def proximo(self):
        if self.vazia():
            return None
        return self.dados[0]

    def tamanho(self):
        return len(self.dados)

    def vazia(self):
        return len(self.dados) == 0


# Fila circular utilizando posições de um vetor
class FilaCircular:
    def __init__(self, capacidade=5):
        self.capacidade = capacidade
        self.dados = [None] * capacidade
        self.inicio = 0
        self.final = 0
        self.quantidade = 0

    # Aumenta o tamanho do vetor quando necessário
    def aumentar_capacidade(self):
        novo_tamanho = self.capacidade * 2
        novo_vetor = [None] * novo_tamanho

        for i in range(self.quantidade):
            posicao = (self.inicio + i) % self.capacidade
            novo_vetor[i] = self.dados[posicao]

        self.dados = novo_vetor
        self.capacidade = novo_tamanho
        self.inicio = 0
        self.final = self.quantidade

    def cheia(self):
        return self.quantidade == self.capacidade

    def vazia(self):
        return self.quantidade == 0

    def adicionar(self, cliente):
        if self.cheia():
            self.aumentar_capacidade()

        self.dados[self.final] = cliente
        self.final = (self.final + 1) % self.capacidade
        self.quantidade += 1

    def remover(self):
        if self.vazia():
            return None

        cliente = self.dados[self.inicio]
        self.dados[self.inicio] = None

        self.inicio = (self.inicio + 1) % self.capacidade
        self.quantidade -= 1

        return cliente

    def proximo(self):
        if self.vazia():
            return None
        return self.dados[self.inicio]

    def tamanho(self):
        return self.quantidade

    def mostrar_estado(self):
        print(
            f"Início: {self.inicio} | "
            f"Final: {self.final} | "
            f"Elementos: {self.quantidade}/{self.capacidade}"
        )


# Fila que atende de acordo com o nível de prioridade
class FilaPrioritaria:
    def __init__(self):
        self.dados = []
        self.ordem = 0

    def adicionar(self, cliente):
        heapq.heappush(
            self.dados,
            (cliente.prioridade, self.ordem, cliente)
        )
        self.ordem += 1

    def remover(self):
        if self.vazia():
            return None

        prioridade, ordem, cliente = heapq.heappop(self.dados)
        return cliente

    def proximo(self):
        if self.vazia():
            return None

        return self.dados[0][2]

    def tamanho(self):
        return len(self.dados)

    def vazia(self):
        return len(self.dados) == 0


# Menu para testar as filas manualmente
def executar_menu():
    print("\n===== SISTEMA DE ATENDIMENTO =====")
    print("1 - Fila comum")
    print("2 - Fila circular")
    print("3 - Fila prioritária")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        fila = FilaComum()
    elif escolha == "2":
        fila = FilaCircular()
    elif escolha == "3":
        fila = FilaPrioritaria()
    else:
        print("Opção inválida!")
        return

    numero_senha = 1

    while True:
        print("\n----- MENU -----")
        print("1 - Adicionar cliente")
        print("2 - Atender cliente")
        print("3 - Ver próximo")
        print("4 - Ver tamanho da fila")
        print("0 - Sair")

        opcao = input("Digite sua opção: ")

        if opcao == "1":
            nome = input("Digite o nome: ")
            prioridade = int(
                input("Prioridade (1-Emergência / 2-Prioritário / 3-Normal): ")
            )

            cliente = Cliente(
                nome,
                f"SENHA-{numero_senha:02d}",
                prioridade
            )

            fila.adicionar(cliente)
            numero_senha += 1

            print("Cliente adicionado!")
            print(cliente)

        elif opcao == "2":
            cliente = fila.remover()

            if cliente:
                print(f"Cliente atendido: {cliente}")
            else:
                print("A fila está vazia.")

        elif opcao == "3":
            cliente = fila.proximo()

            if cliente:
                print(f"Próximo cliente: {cliente}")
            else:
                print("Não existem clientes na fila.")

        elif opcao == "4":
            print(f"Quantidade de clientes: {fila.tamanho()}")

            if isinstance(fila, FilaCircular):
                fila.mostrar_estado()

        elif opcao == "0":
            print("Voltando...")
            break

        else:
            print("Opção inválida!")


# Realiza a comparação entre os diferentes tipos de fila
def executar_simulacao():

    nomes = [
        "Ana", "Bruno", "Carlos", "Daniela", "Eduardo",
        "Fernanda", "Gabriel", "Helena", "Igor", "Juliana",
        "Lucas", "Mariana", "Nicolas", "Olivia", "Pedro",
        "Rafaela", "Samuel", "Tatiana", "Vinicius", "Yasmin"
    ]

    # Criação dos 20 clientes
    lista_clientes = []

    for i in range(20):
        cliente = Cliente(
            nomes[i],
            f"SENHA-{i + 1:02d}",
            random.randint(1, 3)
        )

        lista_clientes.append(cliente)

    print("\n" + "=" * 65)
    print("CLIENTES GERADOS")
    print("=" * 65)

    for cliente in lista_clientes:
        print(cliente)

    # ---------------- FILA COMUM ----------------

    fila = FilaComum()

    for cliente in lista_clientes:
        fila.adicionar(cliente)

    atendidos_comum = []

    while not fila.vazia():
        atendidos_comum.append(fila.remover())

    print("\n" + "=" * 65)
    print("ATENDIMENTO - FILA COMUM")
    print("=" * 65)

    for cliente in atendidos_comum:
        print("Atendido:", cliente)

    # ---------------- FILA CIRCULAR ----------------

    circular = FilaCircular(5)

    print("\n" + "=" * 65)
    print("FUNCIONAMENTO DA FILA CIRCULAR")
    print("=" * 65)

    for cliente in lista_clientes:
        circular.adicionar(cliente)

        print(
            f"{cliente.senha} inserido | "
            f"Início: {circular.inicio} | "
            f"Final: {circular.final} | "
            f"Quantidade: {circular.quantidade}/{circular.capacidade}"
        )

    atendidos_circular = []

    while not circular.vazia():
        cliente = circular.remover()
        atendidos_circular.append(cliente)

        print(
            f"Atendido: {cliente} | "
            f"Restantes: {circular.quantidade}"
        )

    # ---------------- FILA PRIORITÁRIA ----------------

    prioridade = FilaPrioritaria()

    for cliente in lista_clientes:
        prioridade.adicionar(cliente)

    atendidos_prioridade = []

    print("\n" + "=" * 65)
    print("ATENDIMENTO - FILA PRIORITÁRIA")
    print("=" * 65)

    while not prioridade.vazia():
        cliente = prioridade.remover()
        atendidos_prioridade.append(cliente)

        print("Atendido:", cliente)

    # ---------------- COMPARAÇÃO ----------------

    print("\n" + "=" * 75)
    print("COMPARAÇÃO ENTRE FILA COMUM E FILA PRIORITÁRIA")
    print("=" * 75)

    print(
        f"{'Nº':<5} | "
        f"{'Fila Comum':<32} | "
        f"{'Fila Prioritária':<32}"
    )

    print("-" * 75)

    for i in range(20):
        print(
            f"{i + 1:<5} | "
            f"{str(atendidos_comum[i]):<32} | "
            f"{str(atendidos_prioridade[i]):<32}"
        )


# Início do programa
if __name__ == "__main__":
    executar_simulacao()
    executar_menu()