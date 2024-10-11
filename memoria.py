import random
from collections import deque

# a) Primeiro, gere uma string de referência de página aleatória, na qual os números de página variam de 0 a 9.
def gerar_referencia(tamanho, intervalopaginas=10):
    return [random.randint(0, intervalopaginas-1) for _ in range(tamanho)]
# b)Aplique a string de referência de página aleatória a cada algoritmo e registre a quantidade de falhas de página incorridas em cada algoritmo.
# FIFO
def FIFO(paginas, quadros):
    memoria = deque(maxlen = quadros)  
    falhas = 0
    for pagina in paginas:
        if pagina not in memoria: 
            falhas += 1
            if len(memoria) == quadros: 
                memoria.popleft()
            memoria.append(pagina)  
    return falhas
# LRU
def LRU(paginas, quadros):
    memoria = []
    falhas = 0
    for pagina in paginas:
        if pagina in memoria:
            memoria.remove(pagina)
            memoria.append(pagina)
        else:
            falhas += 1
            if len(memoria) == quadros:
                memoria.pop(0)
            memoria.append(pagina)
    return falhas
# c)Implemente os algoritmos de substituição de modo que a quantidade de quadros de página possa variar também.
def ALG(tamanho, max_quadros):
    # a) Gerar a string de referência 
    paginas = gerar_referencia(tamanho)
    print(f"String de referência: {paginas}")
    print("\nResultados:")
    print(f"{'Quadros':<10} {'FIFO Falhas':<15} {'LRU Falhas':<15}")
    # b) Aplicar a string de referência
    for quadros in range(1, max_quadros+1):
        falhas_fifo = FIFO(paginas, quadros)
        falhas_lru = LRU(paginas, quadros)
        print(f"{quadros:<10} {falhas_fifo:<15} {falhas_lru:<15}")
        
tamanho = 20  
max_quadros = 5        
# e) Crie e implemente duas funções – LRU e FIFO. Cada uma dessas usa o algoritmo de substituição de página LRU e a outra usando o algoritmo FIFO.
ALG(tamanho, max_quadros)
