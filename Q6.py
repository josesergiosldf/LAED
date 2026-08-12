class NoEsparso:
    def __init__(self, valor, posicao):
        self.valor = valor
        self.posicao = posicao
        self.anterior = None
        self.proximo = None

def buscar_por_indice(head, k):
    atual = head

    while atual:
        if atual.posicao == k:
            return atual.valor

        if atual.posicao > k:
            break

        atual = atual.proximo

    return 0

def buscar_por_valor(head, x):
    atual = head

    while atual:
        if atual.valor == x:
            return atual.posicao
        atual = atual.proximo

    return -1

def atualizacao(head, x, k):
    atual = head
    anterior = None

    while atual and atual.posicao < k:
        anterior = atual
        atual = atual.proximo

    if atual and atual.posicao == k:
        if x != 0:
            atual.valor = x
        else:
            if atual.anterior:
                atual.anterior.proximo = atual.proximo
            else:
                head = atual.proximo
            if atual.proximo:
                atual.proximo.anterior = atual.anterior

    elif x != 0:
        novo = NoEsparso(x, k)
        if anterior is None:
            novo.proximo = head

            if head:
                head.anterior = novo
            head = novo
        else:
            novo.proximo = anterior.proximo
            novo.anterior = anterior

            if anterior.proximo:
                anterior.proximo.anterior = novo
            anterior.proximo = novo

    return head

n1 = NoEsparso(5, 2)
n2 = NoEsparso(9, 4)
n1.proximo = n2
n2.anterior = n1

print(buscar_por_indice(n1, 2))
print(buscar_por_valor(n1, 9))

head = atualizacao(n1, 7, 3)
curr = head
while curr:
    print(curr.posicao, curr.valor)
    curr = curr.proximo

# Busca por Indice: O(m)
# Busca por Valor: O(m)
# Atualização: O(m)