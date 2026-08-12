class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def elemento_mais_frequente(head):
    if not head:
        return None, 0

    frequencias = {}
    atual = head

    while atual:
        frequencias[atual.valor] = frequencias.get(atual.valor, 0) + 1
        atual = atual.proximo

    mais_frequente = None
    maior_contagem = 0

    for valor, contagem in frequencias.items():
        if contagem > maior_contagem:
            maior_contagem = contagem
            mais_frequente = valor

    return mais_frequente, maior_contagem

n1 = No(1)
n2 = No(2)
n3 = No(2)
n4 = No(3)
n1.proximo = n2
n2.proximo = n3
n3.proximo = n4

val, count = elemento_mais_frequente(n1)
print(val, count)

# Tempo de Execução: O(n)