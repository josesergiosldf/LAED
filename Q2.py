# 2. Fila encadeada com ponteiros inicio e fim
# Estado inicial: inicio -> [ 8 | * ] -> [ 15 | * ] -> [ 23 | None ] <- fim

# a. Inserção dos valores 7 e 11 na fila
# 1. Enqueue 7: nó 23 aponta para 7, fim passa a apontar para 7.
# 2. Enqueue 11: nó 7 aponta para 11, fim passa a apontar para 11.
# Estado resultante:
# inicio -> [ 8 | * ] -> [ 15 | * ] -> [ 23 | * ] -> [ 7 | * ] -> [ 11 | None ] <- fim

# b. Dois Dequeue a partir de a.
# 1. Dequeue: remove 8, inicio passa para 15.
# 2. Dequeue: remove 15, inicio passa para 23.
# Estado resultante:
# inicio -> [ 23 | * ] -> [ 7 | * ] -> [ 11 | None ] <- fim

# c. Esvaziamento da fila e desatualização do ponteiro fim
# Ao esvaziar a fila, inicio e fim devem ser atualizados para None.
# Se apenas inicio for zerado, fim vira um dangling pointer. Num novo Enqueue, a checagem de fila vazia pode falhar ao acessar fim.proximo, gerando erro de acesso à memória (Segmentation Fault).