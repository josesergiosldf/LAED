def trocar_elemento_x_por_y(lista, x, y):
    n = len(lista)
    indice_x = -1

    for i in range(n):
        if lista[i] == x:
            indice_x = i
            break

    if indice_x == -1:
        return lista
    
    lista[indice_x] = y

    i = indice_x

    if y < x:
        while i > 0 and lista[i] < lista[i - 1]:
            lista[i], lista[i - 1] = lista[i - 1], lista[i]
            i -= 1
    elif y > x:
        while i < n - 1 and lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            i += 1

    return lista

V = [3, 4, 7, 8, 10, 14, 16, 19, 24, 0, 0, 0]

print(trocar_elemento_x_por_y(V, 10, 5))
print(trocar_elemento_x_por_y(V, 5, 12))

# O(n)