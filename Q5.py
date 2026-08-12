class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def intercalar_listas(p1, p2):
    dummy = No(0)
    atual = dummy

    while p1 and p2:
        if p1.valor <= p2.valor:
            atual.proximo = p1
            p1 = p1.proximo
        else:
            atual.proximo = p2
            p2 = p2.proximo
        atual = atual.proximo

    atual.proximo = p1 if p1 else p2

    return dummy.proximo

a1 = No(1)
a2 = No(3)
a1.proximo = a2

b1 = No(2)
b2 = No(4)
b1.proximo = b2

res = intercalar_listas(a1, b1)
curr = res
while curr:
    print(curr.valor)
    curr = curr.proximo

# Tempo de Execução: O(n + m)