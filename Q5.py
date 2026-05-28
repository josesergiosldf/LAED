v = [7, 1, 9, 1, 7, 3, 9, 2, 1, 6, 8, 3]
k = int(input("Digite um número: "))
numero = 0

for i in range(len(v)):
    contador = 0
    for j in range(len(v)):
        if v[i] == v[j]:
            contador += 1
        if contador == k:
            numero = v[i]
            break

print(f"O número que aparece {k} vezes é: {numero}")

# O(n^2)