def encontrar_linhas_iguais(matriz):
    linhas_vistas = set()

    for linha in matriz:
        linha_imutavel = tuple(linha)

        if linha_imutavel in linhas_vistas:
            return True
        
        linhas_vistas.add(linha_imutavel)

    return False

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

if encontrar_linhas_iguais(matriz):
    print("Sim, a matriz M contém duas linhas exatamente iguais.")
else:
    print("Não, todas as linhas são diferentes.")

# O(n)