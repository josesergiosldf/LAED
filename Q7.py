v = [9, 2, 7, 7, 2, 2, 1, 7, 7, 9]
contador = 0

for i in range(len(v)):
    for j in range(len(v)):
        if i < j and v[i] > v[j]:
            contador += 1

print("O número de inversões é:", contador)