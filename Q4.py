class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def duplicar_impares(head):
    atual = head

    while atual:
        if atual.valor % 2 != 0:
            novo_no = No(atual.valor)
            novo_no.proximo = atual.proximo
            atual.proximo = novo_no
            atual = novo_no.proximo
        else:
            atual = atual.proximo
    return head

n1 = No(1)
n2 = No(2)
n3 = No(3)
n1.proximo = n2
n2.proximo = n3

head = duplicar_impares(n1)
curr = head
while curr:
    print(curr.valor)
    curr = curr.proximo

# Tempo de Execução: O(n)