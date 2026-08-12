class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def particionar_lista(head, k):
    menores_head = No(0)
    maiores_head = No(0)

    menores = menores_head
    maiores = maiores_head

    atual = head

    while atual:
        if atual.valor <= k:
            menores.proximo = atual
            menores = menores.proximo
        else:
            maiores.proximo = atual
            maiores = maiores.proximo
        atual = atual.proximo

    menores.proximo = maiores_head.proximo
    maiores.proximo = None

    return menores_head.proximo

n1 = No(3)
n2 = No(5)
n3 = No(2)
n4 = No(1)
n1.proximo = n2
n2.proximo = n3
n3.proximo = n4

head = particionar_lista(n1, 2)
curr = head
while curr:
    print(curr.valor)
    curr = curr.proximo

# Tempo de Execução: O(n)