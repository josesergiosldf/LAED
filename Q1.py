# Partição percorre a lista uma vez
# Custo da partição = O(n)

# Depois aplicamos Bubble Sort nos dois lados

# Melhor caso:
# partição equilibrada → n/2 | n/2
# Bubble esquerdo = O(n/2)
# Bubble direito = O(n/2)
# Total: O(n) + O(n/2) + O(n/2)
# Melhor caso = Θ(n)

# Pior caso:
# partição desbalanceada → 1 | n−1
# Bubble pequeno = O(1)
# Bubble grande = O((n−1)²)
# Total: O(n) + O(n²)
# Pior caso = Θ(n²)