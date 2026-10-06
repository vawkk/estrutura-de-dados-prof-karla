import heapq
import random


# Guarda as informações e a prioridade de cada cliente
class Cliente:
    def __init__(self, nome, senha, prioridade):
        self.nome = nome
        self.senha = senha
        self.prioridade = prioridade

    def __repr__(self):
        nomes_prioridade = {
            1: "Emergência",
            2: "Prioritário",
            3: "Normal"
        }
        return f"[{self.senha}] {self.nome} (Prioridade: {nomes_prioridade.get(self.prioridade, self.prioridade)})"


# Fila tradicional seguindo a ordem FIFO
class Fila:
    def __init__(self):
        self.itens = []

    # Adiciona o cliente no final da fila
    def enqueue(self, cliente):
        self.itens.append(cliente)

    # Retira o primeiro cliente da fila
    def dequeue(self):
        if self.empty():
            return None
        return self.itens.pop(0)

    # Mostra quem está na frente sem remover
    def head(self):
        if self.empty():
            return None
        return self.itens[0]

    # Retorna a quantidade de clientes
    def tamanho(self):
        return len(self.itens)

    # Verifica se não existem clientes na fila
    def empty(self):
        return len(self.itens) == 0


# Fila circular usando vetor e redimensionamento automático
class FilaCircular:
    def __init__(self, capacidade=5):
        self.capacidade = capacidade
        self.fila = [None] * capacidade
        self.frente = 0
        self.fim = 0
        self.total_itens = 0

    # Aumenta o tamanho da fila quando ela fica cheia
    def _redimensionar(self, nova_capacidade):
        nova_fila = [None] * nova_capacidade

        for i in range(self.total_itens):
            indice = (self.frente + i) % self.capacidade
            nova_fila[i] = self.fila[indice]

        self.fila = nova_fila
        self.frente = 0
        self.fim = self.total_itens
        self.capacidade = nova_capacidade

    # Verifica se a fila chegou ao limite atual
    def cheio(self):
        return self.total_itens == self.capacidade

    # Verifica se a fila está vazia
    def empty(self):
        return self.total_itens == 0

    # Insere um cliente no final da fila
    def enqueue(self, cliente):
        if self.cheio():
            self._redimensionar(self.capacidade * 2)

        self.fila[self.fim] = cliente
        self.fim = (self.fim + 1) % self.capacidade
        self.total_itens += 1

    # Remove o cliente que está na frente
    def dequeue(self):
        if self.empty():
            print("Erro: a fila circular está vazia!")
            return None

        cliente_removido = self.fila[self.frente]
        self.fila[self.frente] = None
        self.frente = (self.frente + 1) % self.capacidade
        self.total_itens -= 1

        return cliente_removido

    # Consulta o primeiro cliente sem removê-lo
    def head(self):
        if self.empty():
            return None
        return self.fila[self.frente]

    # Retorna o número de clientes presentes
    def tamanho(self):
        return self.total_itens

    # Mostra a situação atual dos índices
    def mostrar_indices(self):
        print(
            f"Frente: {self.frente} | "
            f"Fim: {self.fim} | "
            f"Ocupados: {self.total_itens}/{self.capacidade}"
        )


# Fila de prioridade usando Min-Heap
class FilaPrioridade:
    def __init__(self):
        self.heap = []
        self.contador = 0

    # Adiciona o cliente levando em consideração sua prioridade
    def enqueue(self, cliente):
        heapq.heappush(
            self.heap,
            (cliente.prioridade, self.contador, cliente)
        )
        self.contador += 1

    # Retira primeiro quem possui maior prioridade
    def dequeue(self):
        if self.empty():
            return None

        _, _, cliente = heapq.heappop(self.heap)
        return cliente

    # Consulta o próximo cliente
    def head(self):
        if self.empty():
            return None
        return self.heap[0][2]

    # Retorna a quantidade de clientes
    def tamanho(self):
        return len(self.heap)

    # Verifica se a fila está vazia
    def empty(self):
        return len(self.heap) == 0


# Menu para testar as três estruturas manualmente
def menu_interativo():
    fila_atual = None

    print("\n--- MENU INTERATIVO ---")
    print("1 - Fila Tradicional")
    print("2 - Fila Circular")
    print("3 - Fila por Prioridade")

    escolha = input("Escolha o tipo de fila: ")

    if escolha == "1":
        fila_atual = Fila()
    elif escolha == "2":
        fila_atual = FilaCircular(5)
    elif escolha == "3":
        fila_atual = FilaPrioridade()
    else:
        print("Opção inválida!")
        return

    numero_senha = 1

    while True:
        print("\n1 - Cadastrar cliente")
        print("2 - Atender cliente")
        print("3 - Ver próximo cliente")
        print("4 - Mostrar tamanho/estado")
        print("0 - Sair")

        opcao = input("Digite uma opção: ")

        if opcao == "1":
            nome = input("Nome do cliente: ")
            prioridade = int(
                input("Prioridade (1-Emergência, 2-Prioritário, 3-Normal): ")
            )

            cliente = Cliente(
                nome,
                f"SENHA-{numero_senha}",
                prioridade
            )

            numero_senha += 1
            fila_atual.enqueue(cliente)

            print(f"Cliente inserido: {cliente}")

        elif opcao == "2":
            cliente = fila_atual.dequeue()

            if cliente:
                print(f"Cliente atendido: {cliente}")
            else:
                print("Não há clientes na fila.")

        elif opcao == "3":
            proximo = fila_atual.head()

            if proximo:
                print(f"Próximo cliente: {proximo}")
            else:
                print("A fila está vazia.")

        elif opcao == "4":
            print(f"Tamanho atual: {fila_atual.tamanho()}")

            if isinstance(fila_atual, FilaCircular):
                fila_atual.mostrar_indices()

        elif opcao == "0":
            break

        else:
            print("Opção inválida!")


# Cria clientes e compara o funcionamento das filas
def simular_desafio():

    nomes = [
        "Ana", "Bruno", "Carlos", "Daniela", "Eduardo",
        "Fernanda", "Gabriel", "Helena", "Igor", "Juliana",
        "Lucas", "Mariana", "Nicolas", "Olivia", "Pedro",
        "Rafaela", "Samuel", "Tatiana", "Vinicius", "Yasmin"
    ]

    # Cria 20 clientes com prioridades aleatórias
    clientes = [
        Cliente(
            nome=nomes[i],
            senha=f"SENHA-{i + 1:02d}",
            prioridade=random.randint(1, 3)
        )
        for i in range(20)
    ]

    # Mostra a ordem em que os clientes chegaram
    print("=" * 60)
    print("1. CLIENTES NA ORDEM DE CHEGADA")
    print("=" * 60)

    for cliente in clientes:
        print(cliente)

    # Teste da fila tradicional
    fila_normal = Fila()

    for cliente in clientes:
        fila_normal.enqueue(cliente)

    print("\n" + "=" * 60)
    print("2. ORDEM DE ATENDIMENTO - FILA TRADICIONAL")
    print("=" * 60)

    atendidos_normal = []

    while not fila_normal.empty():
        cliente = fila_normal.dequeue()
        atendidos_normal.append(cliente)
        print(f"Atendido: {cliente}")

    # Teste da fila circular
    fila_circular = FilaCircular(capacidade=5)

    print("\n" + "=" * 60)
    print("3. FUNCIONAMENTO DA FILA CIRCULAR")
    print("=" * 60)

    print("-> Inserindo clientes:")

    for cliente in clientes:
        fila_circular.enqueue(cliente)

        print(
            f"Inserido {cliente.senha} | "
            f"Frente: {fila_circular.frente} | "
            f"Fim: {fila_circular.fim} | "
            f"Ocupados: {fila_circular.total_itens}/{fila_circular.capacidade}"
        )

    print("\n-> Atendimento da fila circular:")

    atendidos_circular = []

    while not fila_circular.empty():
        cliente = fila_circular.dequeue()
        atendidos_circular.append(cliente)

        print(
            f"Atendido: {cliente} | "
            f"Restantes: {fila_circular.total_itens}"
        )

    # Teste da fila de prioridade
    fila_prioridade = FilaPrioridade()

    for cliente in clientes:
        fila_prioridade.enqueue(cliente)

    print("\n" + "=" * 60)
    print("4. ORDEM DE ATENDIMENTO - FILA DE PRIORIDADE")
    print("=" * 60)

    atendidos_prioridade = []

    while not fila_prioridade.empty():
        cliente = fila_prioridade.dequeue()
        atendidos_prioridade.append(cliente)
        print(f"Atendido: {cliente}")

    # Comparação final das duas formas de atendimento
    print("\n" + "=" * 60)
    print("5. COMPARAÇÃO DOS RESULTADOS")
    print("=" * 60)

    print(
        f"{'Ordem':<6} | "
        f"{'Fila Tradicional':<30} | "
        f"{'Fila Prioridade':<30}"
    )

    print("-" * 72)

    for i in range(20):
        print(
            f"{i + 1:02d}     | "
            f"{str(atendidos_normal[i]):<30} | "
            f"{str(atendidos_prioridade[i]):<30}"
        )


# Inicia primeiro a simulação e depois disponibiliza o menu
if __name__ == "__main__":
    simular_desafio()
    menu_interativo()
