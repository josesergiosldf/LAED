def encontrar_elementos_repetidos(matriz):
    vistos = set()

    for linha in matriz:
        for numero in linha:
            if numero in vistos:
                return numero
            vistos.add(numero)
    return None


matriz = [
    [3, 9, 4, 2, 4, 1, 8, 5, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [5, 8, 2, 3, 9, 8, 4, 1, 7],
    [8, 3, 4, 2, 3, 1, 3, 9, 4],
    [3, 7, 2, 9, 4, 2, 1, 2, 3],
    [7, 5, 3, 1, 2, 4, 5, 8, 2],
    [4, 7, 3, 6, 5, 1, 9, 3, 2],
    [1, 5, 3, 2, 9, 8, 7, 6, 5],
    [3, 9, 4, 2, 4, 1, 8, 5, 1]
]

repetido = encontrar_elementos_repetidos(matriz)

if repetido is not None:
    print(f"Sim, o elemento {repetido} aparece mais de uma vez.")
else:
    print("Não existem elementos repetidos.")

# O(n^2)