class NoDuplo:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.proximo = None

def encontrar_sublista(L, x):
    idx = 0

    while idx < len(L) - 1:
        if L[idx + 1] and x < L[idx + 1].valor:
            break
        idx += 1

    return idx

def busca(L, x):
    if not L:
        return False

    idx = encontrar_sublista(L, x)
    atual = L[idx]

    while atual:
        if atual.valor == x:
            return True
        elif atual.valor > x:
            break
        atual = atual.proximo

    return False

def insercao(L, x):
    novo = NoDuplo(x)

    if not L:
        L.append(novo)
        return L

    idx = encontrar_sublista(L, x)
    head = L[idx]

    if not head or x < head.valor:
        novo.proximo = head

        if head:
            head.anterior = novo
        L[idx] = novo

        return L

    atual = head

    while atual.proximo and atual.proximo.valor < x:
        atual = atual.proximo

    novo.proximo = atual.proximo

    if atual.proximo:
        atual.proximo.anterior = novo

    atual.proximo = novo
    novo.anterior = atual

    return L

def remocao(L, x):
    if not L:
        return L

    idx = encontrar_sublista(L, x)
    atual = L[idx]

    while atual and atual.valor != x:
        atual = atual.proximo

    if atual:
        if atual.anterior:
            atual.anterior.proximo = atual.proximo
        else:
            L[idx] = atual.proximo

        if atual.proximo:
            atual.proximo.anterior = atual.anterior

    return L

L = []
L = insercao(L, 10)
L = insercao(L, 5)

print(busca(L, 5))

L = remocao(L, 10)
for sub in L:
    curr = sub
    while curr:
        print(curr.valor)
        curr = curr.proximo

# Busca: O(k + m)
# Inserção: O(k + m)
# Remoção: O(k + m)