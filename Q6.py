# 6. Fila com duas pilhas encadeadas

# a. Escreva os códigos de Enqueue e Dequeue usando essa ideia.
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class PilhaEncadeada:
    def __init__(self):
        self.topo = None

    def push(self, valor):
        novo = No(valor)
        novo.proximo = self.topo
        self.topo = novo

    def pop(self):
        if self.topo is None:
            raise IndexError("Pilha Vazia")
        
        val = self.topo.valor
        self.topo = self.topo.proximo
        
        return val

    def esta_vazia(self):
        return self.topo is None

class FilaComDuasPilhas:
    def __init__(self):
        self.p1 = PilhaEncadeada()
        self.p2 = PilhaEncadeada()

    def enqueue(self, valor):
        self.p1.push(valor)

    def dequeue(self):
        if self.p2.esta_vazia():
            while not self.p1.esta_vazia():
                self.p2.push(self.p1.pop())

        if self.p2.esta_vazia():
            raise IndexError("Fila Vazia")

        return self.p2.pop()

# b. Custo amortizado do Dequeue usando método do potencial (Phi = elementos em P1)
# 1. Enqueue: Custo real = 1, Delta_Phi = +1. Custo amortizado = 1 + 1 = 2 = O(1).
# 2. Dequeue:
#    - Se P2 não está vazia: Custo real = 1, Delta_Phi = 0. Custo amortizado = 1 = O(1).
#    - Se P2 está vazia (com k elementos em P1): Custo real = 2k + 1, Delta_Phi = -k. Custo amortizado = (2k + 1) - k = k + 1.
# O potencial acumulado paga as transferências de P1 para P2, mantendo custo amortizado O(1).

# c. Manutenção da propriedade FIFO na transferência de P1 para P2
# Sim. Ao transferir de P1 para P2, a ordem é invertida duas vezes, restaurando a ordem de inserção (FIFO).
# Exemplo: Enqueue(1, 2, 3) deixa P1 com topo=3. Ao mover para P2, o topo de P2 vira 1, sendo o primeiro a sair no Dequeue.