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

    def busca_gulosa(self, inicio, objetivo):
    # Conjunto para armazenar os nós já visitados
        visitados = set()

        # Fila de prioridade iniciada com o nó de partida
        # Cada item na fila é uma tupla: (heurística, nó atual, caminho até aqui)
        fila = [(self.heuristica[inicio], inicio, [inicio])]

        # Enquanto houver nós na fila
        while fila:
            # Remove da fila o nó com menor valor heurístico
            estimativa, atual, caminho = heapq.heappop(fila)

            # Se chegamos ao objetivo, retornamos o caminho construído
            if atual == objetivo:
                return caminho

            # Se o nó já foi visitado, ignoramos para evitar ciclos
            if atual in visitados:
                continue

            # Marcamos o nó atual como visitado
            visitados.add(atual)

            # Para cada vizinho do nó atual
            for vizinho, custo in self.adjacencias.get(atual, []):
                # Se o vizinho ainda não foi visitado
                if vizinho not in visitados:
                    # Calculamos sua heurística (estimativa de custo até o objetivo)
                    nova_estimativa = self.heuristica[vizinho]
                    # Adicionamos o vizinho à fila com a nova estimativa e caminho atualizado
                    heapq.heappush(fila, (nova_estimativa, vizinho, caminho + [vizinho]))

        # Se não encontramos um caminho até o objetivo, retornamos None
        return None
