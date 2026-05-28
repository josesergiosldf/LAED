# Ordenamos os primeiros 2n/3 elementos com Bubble Sort
# Ordenamos os últimos 2n/3 elementos com Bubble Sort
# Ordenamos os primeiros 2n/3 elementos novamente

# a) A lista fica completamente ordenada?
# Sim.
# Porque as regiões se sobrepõem (sobreposição de n/3 elementos)
# Os elementos fora de posição acabam sendo ajustados nas 3 etapas

# b) Tempo de execução

# Bubble Sort em m elementos = O(m²)

# Cada ordenação trabalha em 2n/3 elementos
# Cada passo custa O((2n/3)²)

# Existem 3 ordenações

# Total:
# 3 × O((2n/3)²)
# = 3 × O(4n²/9)
# = O(n²)

# Tempo final = Θ(n²)