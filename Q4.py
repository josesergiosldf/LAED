class NoDuplo:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

def particionar_lista_dupla(head, k):
    if not head or not head.proximo:
        return head

    q = head
    r = head

    while r.proximo:
        r = r.proximo

    while q != r and q.anterior != r:
        while q != r and q.anterior != r and q.valor <= k:
            q = q.proximo

        while q != r and q.anterior != r and r.valor > k:
            r = r.anterior

        if q != r and q.anterior != r:
            q.valor, r.valor = r.valor, q.valor
            q = q.proximo
            r = r.anterior

    return head

n1 = NoDuplo(5)
n2 = NoDuplo(2)
n3 = NoDuplo(1)

n1.proximo = n2
n2.anterior = n1

n2.proximo = n3
n3.anterior = n2

head = particionar_lista_dupla(n1, 3)
curr = head
while curr:
    print(curr.valor)
    curr = curr.proximo

# Tempo de Execução: O(n)