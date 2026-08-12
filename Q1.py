# 1. Operações básicas de pilha encadeada
# Estado inicial: topo -> [42] -> [17] -> [5] -> None

# a. Estado da pilha após Push(topo, 99) e Push(topo, 3)
# 1. Após Push(topo, 99): topo -> [99] -> [42] -> [17] -> [5] -> None
# 2. Após Push(topo, 3):  topo -> [3] -> [99] -> [42] -> [17] -> [5] -> None
# Representação:
# topo -> [ 3 | * ] -> [ 99 | * ] -> [ 42 | * ] -> [ 17 | * ] -> [ 5 | None ]

# b. Estado após dois Pop a partir do estado de a.
# 1. Pop: remove 3. Pilha: topo -> [99] -> [42] -> [17] -> [5] -> None
# 2. Pop: remove 99. Pilha: topo -> [42] -> [17] -> [5] -> None
# Estado final: topo -> [ 42 | * ] -> [ 17 | * ] -> [ 5 | None ]

# c. Uso de variável auxiliar no Pop e efeitos da liberação imediata
# Guarda-se o nó em uma variável auxiliar para acessar seu ponteiro 'proximo' e atualizar o 'topo'.
# Se liberado antes da atualização, perde-se a referência do próximo nó, gerando acesso inválido à memória (dangling pointer) e vazamento de memória.