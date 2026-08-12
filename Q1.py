class NoDuplo:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

def imprimir_elemento_central(head):
    if not head:
        print("A lista está vazia.")
        return

    lento = head
    rapido = head

    while rapido.proximo and rapido.proximo.proximo:
        lento = lento.proximo
        rapido = rapido.proximo.proximo

    print(f"O elemento central é: {lento.valor}")

n1 = NoDuplo(1)
n2 = NoDuplo(2)
n3 = NoDuplo(3)

n1.proximo = n2
n2.anterior = n1

n2.proximo = n3
n3.anterior = n2

imprimir_elemento_central(n1)

# Tempo de Execução: O(n)