v = [9, 42, 21, 14, 28, 3, 19, 32, 46, 6]
maior = 0
i = 0

while i < len(v):
    if v[i] > maior and v[i] % 2 != 0:
        maior = v[i]
    i += 1

print("O maior número ímpar é:", maior)