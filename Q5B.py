v = [9, 42, 21, 14, 25, 3, 19, 33, 45, 6]
v = sorted(v)
encontrado = False

i = 0
j = 1

while i < len(v) and j < len(v):
    if i == j:
        j += 1
        continue

    if v[j] == 2 * v[i]:
        print(f"Encontrado: {v[j]} é o dobro de {v[i]}")
        encontrado = True
        i += 1
        j += 1
    elif v[j] < 2 * v[i]:
        j += 1
    else:
        i += 1

if not encontrado:
    print("Nenhum par encontrado onde um número é o dobro do outro.")