v = [9, 42, 21, 14, 28, 3, 19, 32, 46, 6]
maior = 0
segundo_maior = 0

for i in range(len(v)):
    if v[i] > maior and v[i] % 2 != 0:
        segundo_maior = maior
        maior = v[i]
    elif v[i] > segundo_maior and v[i] % 2 != 0:
        segundo_maior = v[i]

print("O maior número ímpar é:", maior)
print("O segundo maior número ímpar é:", segundo_maior)