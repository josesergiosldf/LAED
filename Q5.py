# 5. Balanceamento de delimitadores

# a. Escreva o algoritmo usando uma pilha encadeada.
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def verificar_balanceamento(expressao):
    topo = None
    pares = {')': '(', ']': '[', '}': '{'}
    abridores = {'(', '[', '{'}
    fechadores = {')', ']', '}'}

    for i, c in enumerate(expressao):
        if c in abridores:
            novo = No(c)
            novo.proximo = topo
            topo = novo
        elif c in fechadores:
            if topo is None:
                return False, f"Posição {i}: Fechador '{c}' sem abridor correspondente"
            
            topo_val = topo.valor
            topo = topo.proximo
            
            if topo_val != pares[c]:
                return False, f"Posição {i}: Fechador '{c}' não combina com o abridor '{topo_val}'"

    if topo is not None:
        return False, f"Fim da cadeia: Sobraram abridores não fechados, ex: '{topo.valor}'"

    return True, "Válida"

# b. Análise de complexidade
# - Tempo: O(n), pois percorre a expressão uma vez e cada operação de pilha é O(1).
# - Espaço: O(n), pois no pior caso (apenas abridores) a pilha armazena até n elementos.

# c. Aplicação às cadeias do exemplo:
# 1. ({[]}) -> Válida
# 2. ({[]}] -> Inválida (Posição 5: fechador ']' incompatível com abridor '(')
# 3. ({[]}[()]{}) -> Válida