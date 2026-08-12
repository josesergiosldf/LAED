class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def tem_elemento_repetido(head):
    visitados = set()
    atual = head

    while atual:
        if atual.valor in visitados:
            return True
        visitados.add(atual.valor)
        atual = atual.proximo

    return False

n1 = No(1)
n2 = No(2)
n3 = No(2)
n1.proximo = n2
n2.proximo = n3

print(tem_elemento_repetido(n1))

# Tempo de Execução: O(n)