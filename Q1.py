class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def mover_maior_para_o_fim(head):
    if not head or not head.proximo:
        return head

    no_atual = head
    maior_no = head
    ant_maior = None
    ant_atual = None

    while no_atual:
        if no_atual.valor > maior_no.valor:
            maior_no = no_atual
            ant_maior = ant_atual
        ant_atual = no_atual
        no_atual = no_atual.proximo

    if maior_no.proximo is None:
        return head

    if ant_maior is None:
        head = head.proximo
    else:
        ant_maior.proximo = maior_no.proximo

    ultimo = head
    while ultimo.proximo:
        ultimo = ultimo.proximo

    ultimo.proximo = maior_no
    maior_no.proximo = None

    return head

n1 = No(1)
n2 = No(5)
n3 = No(2)
n1.proximo = n2
n2.proximo = n3

head = mover_maior_para_o_fim(n1)
curr = head
while curr:
    print(curr.valor)
    curr = curr.proximo

# Tempo de Execução: O(n)