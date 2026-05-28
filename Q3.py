def mediana_duas_listas(lista1, lista2):
    def buscar_mediana(iniciou, fimu, iniciov, fimv):
        tam = fimu - iniciou + 1

        if tam == 1:
            return (lista1[iniciou] + lista2[iniciov]) / 2
        
        if tam == 2:
            elemento_central_1 = max(lista1[iniciou], lista2[iniciov])
            elemento_central_2 = min(lista1[fimu], lista2[fimv])
            return (elemento_central_1 + elemento_central_2) / 2
        
        meiou = iniciou + (tam - 1) // 2
        meiov = iniciov + (tam - 1) // 2

        m1 = lista1[meiou]
        m2 = lista2[meiov]

        if m1 == m2:
            return m1
        
        if m1 < m2:
            if tam % 2 == 0:
                return buscar_mediana(meiou + 1, fimu, iniciov, meiov)
            else:
                return buscar_mediana(meiou, fimu, iniciov, meiov)
        else:
            if tam % 2 == 0:
                return buscar_mediana(iniciou, meiou, meiov + 1, fimv)
            else:
                return buscar_mediana(iniciou, meiou, meiov, fimv)
    return buscar_mediana(0, len(lista1) - 1, 0, len(lista2) - 1)

u = [1, 6, 10, 15, 19]
v = [3, 7, 11, 17, 21]

resultado = mediana_duas_listas(u, v)
print(f"A mediana combinada é: {resultado}")

# O(log n)