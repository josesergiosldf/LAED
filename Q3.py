class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def inverter_lista(head):
    anterior = None
    atual = head

    while atual:
        proximo_no = atual.proximo
        atual.proximo = anterior
        anterior = atual
        atual = proximo_no

    return anterior

n1 = No(1)
n2 = No(2)
n3 = No(3)
n1.proximo = n2
n2.proximo = n3

head = inverter_lista(n1)
curr = head
while curr:
    print(curr.valor)
    curr = curr.proximo

# Tempo de Execução: O(n)