v = [9, 42, 21, 14, 28, 3, 19, 32, 46, 6]
k = int(input("Digite o valor de k: "))
menor_diferenca = abs(v[0] - k)
numero_mais_proximo = v[0]
encontrado = False
i = 0

while i < len(v):
    if v[i] == k:
        print("Encontrado o número exato:", v[i])
        encontrado = True
        break
    
    diferenca_atual = abs(v[i] - k)

    if diferenca_atual < menor_diferenca:
        menor_diferenca = diferenca_atual
        numero_mais_proximo = v[i]
    i += 1

if not encontrado:
    print("Número mais próximo:", numero_mais_proximo)