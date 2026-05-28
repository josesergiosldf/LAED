v = [17, 2, 8, 1, 7, 13, 9, 12, 4, 16]
elemento_isolado = 0

for k in v:
    if (k - 1 not in v) and (k + 1 not in v):
        elemento_isolado = k
        break

print(f"O elemento isolado é: {elemento_isolado}")

# O(n)