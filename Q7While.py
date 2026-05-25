v = [9, 2, 7, 7, 2, 2, 1, 7, 7, 9]
contador = 0
i = 0

while i < len(v):
    j = 0
    while j < len(v):
        if i < j and v[i] > v[j]:
            contador += 1
        j += 1
    i += 1

print("O número de inversões é:", contador)