# 3. Inversão de fila com pilha auxiliar

# a. Código Python e Trace de Execução para a Fila <1, 2, 3, 4> com 1 no início
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
            return None
        
        val = self.topo.valor
        self.topo = self.topo.proximo
        return val

    def esta_vazia(self):
        return self.topo is None

class FilaEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def enqueue(self, valor):
        novo = No(valor)

        if self.fim is None:
            self.inicio = self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo

    def dequeue(self):
        if self.inicio is None:
            return None
        
        val = self.inicio.valor
        self.inicio = self.inicio.proximo

        if self.inicio is None:
            self.fim = None
        return val

    def esta_vazia(self):
        return self.inicio is None

def inverter_fila_com_pilha(fila: FilaEncadeada):
    pilha = PilhaEncadeada()

    while not fila.esta_vazia():
        val = fila.dequeue()
        pilha.push(val)
        
    while not pilha.esta_vazia():
        val = pilha.pop()
        fila.enqueue(val)

    return fila

# Trace de execução:
# Fila Inicial F: inicio -> [1] -> [2] -> [3] -> [4] <- fim
# Pilha Auxiliar P: vazia
# Esvaziar a Fila e preencher a Pilha - Dequeue e Push:
# - Iteração 1: Dequeue F -> 1 | Push P, 1 -> P: topo -> [1]
# - Iteração 2: Dequeue F -> 2 | Push P, 2 -> P: topo -> [2] -> [1]
# - Iteração 3: Dequeue F -> 3 | Push P, 3 -> P: topo -> [3] -> [2] -> [1]
# - Iteração 4: Dequeue F -> 4 | Push P, 4 -> P: topo -> [4] -> [3] -> [2] -> [1]
#   Fila F agora está vazia
# Esvaziar a Pilha e re-enfileirar na Fila - Pop e Enqueue:
# - Iteração 1: Pop P -> 4 | Enqueue F, 4 -> F: inicio -> [4] <- fim
# - Iteração 2: Pop P -> 3 | Enqueue F, 3 -> F: inicio -> [4] -> [3] <- fim
# - Iteração 3: Pop P -> 2 | Enqueue F, 2 -> F: inicio -> [4] -> [3] -> [2] <- fim
# - Iteração 4: Pop P -> 1 | Enqueue F, 1 -> F: inicio -> [4] -> [3] -> [2] -> [1] <- fim
#   Pilha P agora está vazia
# Resultado Final da Fila: <4, 3, 2, 1> com 4 no início

# b. Análise de Complexidade
# - Tempo: O(n), pois faz duas passagens pela fila de n elementos e cada operação custa O(1).
# - Espaço: O(n), para armazenar os n elementos na pilha auxiliar.

# c. Inversão in-place sem estrutura auxiliar
# Sim. Como a fila é uma lista encadeada simples, basta inverter o sentido dos ponteiros 'proximo' dos nós usando ponteiros auxiliares (anterior, atual, proximo) e ajustar os ponteiros inicio e fim ao final.
# Custo: Tempo O(n) e Espaço O(1).