def particao_por_k(lista, inicio, fim, k):
    i = inicio

    for j in range(inicio, fim + 1):
        if lista[j] < k:
            lista[i], lista[j] = lista[j], lista[i]
            i += 1

    return i

L = [9, 2, 7, 4, 10, 1, 8, 5]
valor_k = 6

indice_fronteira = particao_por_k(L, 0, len(L) - 1, valor_k)

print(f"Lista particionada: {L}")
print(f"O primeiro elemento >= {valor_k} está no índice: {indice_fronteira}")

# O(n)