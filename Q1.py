v = [9, 42, 21, 14, 28, 3, 19, 32, 46, 6]
maior = 0

for i in range(len(v)):
    if v[i] > maior and v[i] % 2 != 0:
        maior = v[i]

print("O maior número ímpar é:", maior)