# 7. Radix Sort e estabilidade

# a. Substituição de filas por pilhas no Radix Sort
# O Radix Sort exige estabilidade. Como pilhas usam LIFO, a ordem relativa dos elementos com o mesmo dígito é invertida a cada passo, quebrando a ordenação.
# Contra-exemplo: Entrada [12, 22, 11]
# - Unidades com pilhas: balde '1': [11]; balde '2': [22, 12] (topo 22). Coleta: [11, 22, 12].
# - Dezenas com pilhas: balde '1': [12, 11] (topo 12); balde '2': [22]. Coleta final incorreta: [12, 11, 22].

# b. Trace do Radix Sort para [481, 329, 143, 612, 937, 480, 256]
# Passagem 1 (unidades):
# Filas: 0:[480], 1:[481], 2:[612], 3:[143], 6:[256], 7:[937], 9:[329]
# Coleta: [480, 481, 612, 143, 256, 937, 329]
# Passagem 2 (dezenas):
# Filas: 1:[612], 2:[329], 3:[937], 4:[143], 5:[256], 8:[480, 481]
# Coleta: [612, 329, 937, 143, 256, 480, 481]
# Passagem 3 (centenas):
# Filas: 1:[143], 2:[256], 3:[329], 4:[480, 481], 6:[612], 9:[937]
# Coleta final: [143, 256, 329, 480, 481, 612, 937]

# c. Complexidade do Radix Sort para n strings de tamanho l e alfabeto sigma comparado ao Merge Sort
# - Radix Sort: Tempo O(l * (n + sigma)), Espaço O(n + sigma).
# - Merge Sort: Tempo O(l * n log n), Espaço O(n).
# Se l e sigma forem pequenos, o Radix Sort executa em tempo linear O(n). Se l for grande (ex: l ~= log n), o desempenho dos dois se equivale.