v = [9, 42, 21, 14, 25, 3, 19, 33, 45, 6]
terceiro_maior = 0
segundo_maior = 0
maior = 0
i = 0

while i < len(v):
    if v[i] > maior:
        terceiro_maior = segundo_maior
        segundo_maior = maior
        maior = v[i]
    elif v[i] > segundo_maior:
        terceiro_maior = segundo_maior
        segundo_maior = v[i]
    elif v[i] > terceiro_maior:
        terceiro_maior = v[i]
    i += 1

print("O maior número é:", maior)
print("O segundo maior número é:", segundo_maior)
print("O terceiro maior número é:", terceiro_maior)

# O(n)