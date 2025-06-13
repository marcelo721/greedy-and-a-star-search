import heapq

class Grafo:
    def __init__(self):
        self.adjacencias = {}
        self.heuristica = {}

    def adicionar_aresta(self, origem, destino, custo):
        if origem not in self.adjacencias:
            self.adjacencias[origem] = []
        if destino not in self.adjacencias:
            self.adjacencias[destino] = []
        self.adjacencias[origem].append((destino, custo))
        self.adjacencias[destino].append((origem, custo))  # grafo bidirecional

    def definir_heuristica(self, heuristica):
        self.heuristica = heuristica
        
    def custo_total(self, caminho):
        custo = 0
        for i in range(len(caminho) - 1):
            atual = caminho[i]
            proximo = caminho[i + 1]
            for vizinho, custo_vizinho in self.adjacencias[atual]:
                if vizinho == proximo:
                    custo += custo_vizinho
                    break
        return custo

    def busca_a_estrela(self, inicio, objetivo):
        # Conjunto para armazenar os nós já visitados
        visitados = set()

        # Fila de prioridade (heap), cada item tem:
        # (f(n), g(n), nó atual, caminho até aqui)
        # f(n) = g(n) + h(n)
        fila = [(self.heuristica[inicio], 0, inicio, [inicio])]

        # Enquanto houver nós na fila
        while fila:
            # Remove o nó com menor f(n) da fila
            f, g, atual, caminho = heapq.heappop(fila)

            # Se chegamos ao objetivo, retornamos o caminho
            if atual == objetivo:
                return caminho

            # Ignora nós já visitados
            if atual in visitados:
                continue

            # Marca o nó atual como visitado
            visitados.add(atual)

            # Para cada vizinho do nó atual
            for vizinho, custo in self.adjacencias.get(atual, []):
                # Se ainda não visitado
                if vizinho not in visitados:
                    # g(n) novo é o custo acumulado até aqui + custo da aresta
                    novo_g = g + custo
                    # f(n) = g(n) + h(n)
                    f_vizinho = novo_g + self.heuristica[vizinho]
                    # Adiciona o vizinho na fila com valores atualizados
                    heapq.heappush(fila, (f_vizinho, novo_g, vizinho, caminho + [vizinho]))

        # Se nenhum caminho foi encontrado
        return None

