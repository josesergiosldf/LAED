v = [9, 42, 21, 14, 25, 3, 19, 33, 45, 6]
k = int(input("Digite o valor de k: "))

v.sort(reverse=True)

print(f"O {k}º maior elemento é: {v[k - 1]}")

# O(n log n)