class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def separar_pares_e_impares(head):
    dummy_impar = No(0)
    dummy_par = No(0)

    fim_impar = dummy_impar
    fim_par = dummy_par

    atual = head

    while atual:
        if atual.valor % 2 != 0:
            fim_impar.proximo = atual
            fim_impar = fim_impar.proximo
        else:
            fim_par.proximo = atual
            fim_par = fim_par.proximo
        atual = atual.proximo

    fim_impar.proximo = None
    fim_par.proximo = None

    p1 = dummy_impar.proximo
    p2 = dummy_par.proximo

    return p1, p2

n1 = No(1)
n2 = No(2)
n3 = No(3)
n4 = No(4)
n1.proximo = n2
n2.proximo = n3
n3.proximo = n4

p1, p2 = separar_pares_e_impares(n1)

curr = p1
while curr:
    print(curr.valor)
    curr = curr.proximo

curr = p2
while curr:
    print(curr.valor)
    curr = curr.proximo

# Tempo de Execução: O(n)