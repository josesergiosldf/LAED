class NoDuplo:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

def trocar_nos_adjacentes(head, no1, no2):
    ant = no1.anterior
    prox = no2.proximo

    if ant:
        ant.proximo = no2
    else:
        head = no2

    if prox:
        prox.anterior = no1

    no2.anterior = ant
    no2.proximo = no1
    no1.anterior = no2
    no1.proximo = prox

    return head

def varredura(head):
    if not head or not head.proximo:
        return head

    atual = head

    while atual and atual.proximo:
        if atual.valor > atual.proximo.valor:
            proximo_no = atual.proximo
            head = trocar_nos_adjacentes(head, atual, proximo_no)
        else:
            atual = atual.proximo

    return head

n1 = NoDuplo(5)
n2 = NoDuplo(2)
n3 = NoDuplo(1)

n1.proximo = n2
n2.anterior = n1

n2.proximo = n3
n3.anterior = n2

head = varredura(n1)
curr = head
while curr:
    print(curr.valor)
    curr = curr.proximo

# Tempo de Execução: O(n)