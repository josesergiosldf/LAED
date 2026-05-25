v = [9, 2, 7, 7, 2, 2, 1, 7, 7, 9]
numero = 0

for i in range(len(v)):
    contador = 0
    for j in range(len(v)):
        if v[i] == v[j] and v[i] % 2 != 0:
            contador += 1

    if contador % 2 != 0:
        numero = v[i]
        break

print("O número ímpar que aparece um número ímpar de vezes é:", numero)