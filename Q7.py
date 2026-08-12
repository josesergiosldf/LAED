class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def remover_copias(head, k):
    dummy = No(0)
    dummy.proximo = head

    atual = dummy

    while atual.proximo:
        if atual.proximo.valor == k:
            atual.proximo = atual.proximo.proximo
        else:
            atual = atual.proximo

    return dummy.proximo

n1 = No(1)
n2 = No(2)
n3 = No(2)
n4 = No(3)
n1.proximo = n2
n2.proximo = n3
n3.proximo = n4

head = remover_copias(n1, 2)
curr = head
while curr:
    print(curr.valor)
    curr = curr.proximo

# Tempo de Execução: O(n)