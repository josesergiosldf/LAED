v = [2, 1, 9, 7, 6, 3, 9, 4, 2, 6, 1, 3]
k = 4

achou = False

for i in range(len(v)):
    for j in range(i + 1, len(v)):
        if v[i] == v[j]:
            distancia = j - i

            if distancia <= k:
                print("Sim,", v[i])
                print("Posições:", i+1, "e", j+1)
                achou = True

if not achou:
    print("Não existe")

# O(n^2)