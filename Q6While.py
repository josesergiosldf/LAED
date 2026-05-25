v = [9, 42, 21, 14, 28, 3, 19, 32, 46, 6]
menor_diferenca = abs(v[0] - v[1])
numero_1, numero_2 = v[0], v[1]

i = 0
while i < len(v):
    j = i + 1
    while j < len(v):
        diferenca_atual = abs(v[i] - v[j])
        if diferenca_atual < menor_diferenca:
            numero_1, numero_2 = v[i], v[j]
            menor_diferenca = diferenca_atual
        j += 1
    i += 1

print(f"Os números mais próximos são: {numero_1} e {numero_2} com uma diferença de {menor_diferenca}.")