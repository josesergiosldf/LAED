v = [9, 2, 7, 7, 2, 2, 1, 7, 7, 9]
numero = 0
i = 0

while i < len(v):
    contador = 0
    j = 0
    while j < len(v):
        if v[j] == v[i] and v[i] % 2 != 0:
            contador += 1
        j += 1

    if contador % 2 != 0:
        numero = v[i]
        break
    i += 1

print("O número ímpar que aparece um número ímpar de vezes é:", numero)