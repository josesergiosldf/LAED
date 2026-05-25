v = [9, 42, 21, 14, 25, 3, 19, 33, 45, 6]
encontrado = False

for i in range(len(v)):
    for j in range(i + 1, len(v)):
        if v[i] == 2 * v[j] or v[j] == 2 * v[i]:
            print(f"Encontrado: {v[i]} é o dobro de {v[j]}")
            encontrado = True

if not encontrado:
    print("Nenhum par encontrado onde um número é o dobro do outro.")