v = [9, 42, 21, 14, 25, 3, 19, 33, 45, 6]
k = int(input("Digite o valor de k: "))

for i in range(len(v)):
    maior = i
    for j in range(i + 1, len(v)):
        if v[j] > v[maior]:
            maior = j

    v[i], v[maior] = v[maior], v[i]

print(f"O {k}º maior elemento é: {v[k - 1]}")

# O(n^2)