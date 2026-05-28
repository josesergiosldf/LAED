v = [5, 3, 1, 10, 2, 13, 9, 12, 4, 7]
media = sum(v) / len(v)
mais_proximo = v[0]
diferenca = abs(v[0] - media)

for i in range(1, len(v)):
    diferenca_atual = abs(v[i] - media)

    if diferenca_atual < diferenca:
        diferenca = diferenca_atual
        mais_proximo = v[i]

print(f"O número mais próximo da média é: {mais_proximo}")

# O(n)