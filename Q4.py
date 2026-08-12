# 4. Pilha com mínimo em O(1)

# a. Estrutura de dados
# Cada nó contém 3 campos:
# 1. 'valor': dado armazenado no nó.
# 2. 'min_atual': menor valor da pilha do topo até aquele nó.
# 3. 'proximo': ponteiro para o nó abaixo na pilha.

# b. Códigos Python de Push, Pop e Min, todos em O(1)
class NoMinimo:
    def __init__(self, valor, min_atual):
        self.valor = valor
        self.min_atual = min_atual
        self.proximo = None

class PilhaComMinimo:
    def __init__(self):
        self.topo = None

    def push(self, valor):
        if self.topo is None:
            novo_min = valor
        else:
            novo_min = min(valor, self.topo.min_atual)

        novo_no = NoMinimo(valor, novo_min)
        novo_no.proximo = self.topo
        self.topo = novo_no

    def pop(self):
        if self.topo is None:
            raise IndexError("Pilha Vazia")
        
        valor_removido = self.topo.valor
        self.topo = self.topo.proximo
        return valor_removido

    def min(self):
        if self.topo is None:
            raise IndexError("Pilha Vazia")
        
        return self.topo.min_atual

# c. Trace da sequência de operações: Push 5, Push 3, Push 7, Push 1, Pop, Min
# 1. Push 5: topo -> [5 | min: 5] -> None. Mínimo: 5
# 2. Push 3: topo -> [3 | min: 3] -> [5 | min: 5] -> None. Mínimo: 3
# 3. Push 7: topo -> [7 | min: 3] -> [3 | min: 3] -> [5 | min: 5] -> None. Mínimo: 3
# 4. Push 1: topo -> [1 | min: 1] -> [7 | min: 3] -> [3 | min: 3] -> [5 | min: 5] -> None. Mínimo: 1
# 5. Pop: remove 1. Pilha: topo -> [7 | min: 3] -> [3 | min: 3] -> [5 | min: 5] -> None. Mínimo: 3
# 6. Min: retorna 3

# d. Custo extra de memória em relação a uma pilha comum
# O(1) por nó (variável min_atual), totalizando O(n) de espaço adicional para n elementos.