class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def intersecao_listas(p1, p2):
    elementos_p2 = set()
    atual_p2 = p2

    while atual_p2:
        elementos_p2.add(atual_p2.valor)
        atual_p2 = atual_p2.proximo

    dummy = No(0)
    fim_resultado = dummy
    visitados_intersecao = set()

    atual_p1 = p1

    while atual_p1:
        if atual_p1.valor in elementos_p2 and atual_p1.valor not in visitados_intersecao:
            fim_resultado.proximo = No(atual_p1.valor)
            fim_resultado = fim_resultado.proximo
            visitados_intersecao.add(atual_p1.valor)
            
        atual_p1 = atual_p1.proximo

    return dummy.proximo

a1 = No(1)
a2 = No(2)
a3 = No(3)
a1.proximo = a2
a2.proximo = a3

b1 = No(2)
b2 = No(3)
b3 = No(4)
b1.proximo = b2
b2.proximo = b3

res = intersecao_listas(a1, b1)
curr = res
while curr:
    print(curr.valor)
    curr = curr.proximo

# Tempo de Execução: O(n + m)