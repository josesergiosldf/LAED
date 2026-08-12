class NoDuplo:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

def remover_no(head, no):
    if no.anterior:
        no.anterior.proximo = no.proximo
    else:
        head = no.proximo

    if no.proximo:
        no.proximo.anterior = no.anterior

    no.anterior = None
    no.proximo = None
    
    return head

def inserir_ordenado(head, no):
    if not head:
        return no

    if no.valor < head.valor:
        no.proximo = head
        head.anterior = no
        return no

    atual = head

    while atual.proximo and atual.proximo.valor < no.valor:
        atual = atual.proximo

    no.proximo = atual.proximo

    if atual.proximo:
        atual.proximo.anterior = no

    atual.proximo = no
    no.anterior = atual

    return head

def atualizar_elemento(head, x, y):
    atual = head

    while atual and atual.valor != x:
        atual = atual.proximo

    if not atual:
        return head

    atual.valor = y

    head = remover_no(head, atual)
    head = inserir_ordenado(head, atual)

    return head

n1 = NoDuplo(1)
n2 = NoDuplo(3)
n3 = NoDuplo(5)

n1.proximo = n2
n2.anterior = n1

n2.proximo = n3
n3.anterior = n2

head = atualizar_elemento(n1, 3, 4)
curr = head
while curr:
    print(curr.valor)
    curr = curr.proximo

# Tempo de Execução: O(n)