class NoEsparso:
    def __init__(self, valor, posicao):
        self.valor = valor
        self.posicao = posicao
        self.anterior = None
        self.proximo = None

def construir_vetor_esparso(vetor):
    head = None
    ultimo = None

    for i, val in enumerate(vetor, start=1):
        if val != 0:
            novo_no = NoEsparso(val, i)

            if head is None:
                head = novo_no
                ultimo = novo_no
            else:
                ultimo.proximo = novo_no
                novo_no.anterior = ultimo
                ultimo = novo_no

    return head

head = construir_vetor_esparso([0, 5, 0, 9])
curr = head
while curr:
    print(curr.posicao, curr.valor)
    curr = curr.proximo

# Tempo de Execução: O(n)