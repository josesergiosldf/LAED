class NoDuplo:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

def transformar_em_lista_de_listas(head, k):
    if not head or k <= 0:
        return []

    n = 0
    atual = head

    while atual:
        n += 1
        atual = atual.proximo

    tamanho_base = n // k
    resto = n % k

    L = []
    atual = head

    for i in range(k):
        if not atual:
            break

        L.append(atual)

        tamanho_sublista = tamanho_base + (1 if i < resto else 0)

        for _ in range(tamanho_sublista - 1):
            if atual:
                atual = atual.proximo

        if atual and atual.proximo:
            proximo_inicio = atual.proximo
            atual.proximo = None
            proximo_inicio.anterior = None
            atual = proximo_inicio
        else:
            atual = None

    return L

n1 = NoDuplo(1)
n2 = NoDuplo(2)
n3 = NoDuplo(3)
n4 = NoDuplo(4)

n1.proximo = n2
n2.anterior = n1
n2.proximo = n3
n3.anterior = n2
n3.proximo = n4
n4.anterior = n3

sublistas = transformar_em_lista_de_listas(n1, 2)
for sub in sublistas:
    curr = sub
    while curr:
        print(curr.valor)
        curr = curr.proximo

# Tempo de Execução: O(n)