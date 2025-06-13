import tkinter as tk
from tkinter import ttk, messagebox
from Grafo import Grafo

def montar_grafo():
    grafo = Grafo()
    grafo.adicionar_aresta("Arad", "Zerind", 75)
    grafo.adicionar_aresta("Arad", "Sibiu", 140)
    grafo.adicionar_aresta("Arad", "Timisoara", 118)
    grafo.adicionar_aresta("Zerind", "Oradea", 71)
    grafo.adicionar_aresta("Sibiu", "Fagaras", 99)
    grafo.adicionar_aresta("Sibiu", "Rimnicu Vilcea", 80)
    grafo.adicionar_aresta("Fagaras", "Bucharest", 211)
    grafo.adicionar_aresta("Rimnicu Vilcea", "Pitesti", 97)
    grafo.adicionar_aresta("Pitesti", "Bucharest", 101)

    grafo.definir_heuristica({
        "Arad": 366,
        "Zerind": 374,
        "Oradea": 380,
        "Sibiu": 253,
        "Fagaras": 176,
        "Rimnicu Vilcea": 193,
        "Pitesti": 100,
        "Timisoara": 329,
        "Bucharest": 0
    })

    return grafo

def buscar_caminho():
    origem = origem_var.get()
    destino = destino_var.get()

    if origem == destino:
        messagebox.showwarning("Atenção", "Origem e destino são iguais!")
        return

    caminho = grafo.busca_gulosa(origem, destino)
    if caminho:
        custo = grafo.custo_total(caminho)
        resultado_var.set(f"Caminho: {' → '.join(caminho)}\nCusto total: {custo}")
    else:
        resultado_var.set("Nenhum caminho encontrado.")
        
#Interface GUI
# Criar janela principal
root = tk.Tk()
root.title("Busca Gulosa - Mapa da  Romênia")
root.geometry("600x600")
root.resizable(False, False)

grafo = montar_grafo()
cidades = sorted(grafo.heuristica.keys())

origem_var = tk.StringVar()
destino_var = tk.StringVar()
resultado_var = tk.StringVar()

# Título
titulo = tk.Label(root, text="Busca Gulosa", font=("Helvetica", 18, "bold"))
titulo.pack(pady=10)

# Seletor de origem
frame_origem = tk.Frame(root)
frame_origem.pack(pady=5)
tk.Label(frame_origem, text="Origem:").pack(side="left")
origem_combo = ttk.Combobox(frame_origem, textvariable=origem_var, values=cidades, state="readonly")
origem_combo.pack(side="left")

# Seletor de destino
frame_destino = tk.Frame(root)
frame_destino.pack(pady=5)
tk.Label(frame_destino, text="Destino:").pack(side="left")
destino_combo = ttk.Combobox(frame_destino, textvariable=destino_var, values=cidades, state="readonly")
destino_combo.pack(side="left")

# Botão buscar
btn_buscar = tk.Button(root, text="Buscar Caminho", command=buscar_caminho, bg="#4CAF50", fg="white", padx=10)
btn_buscar.pack(pady=15)

# Resultado
resultado_label = tk.Label(root, textvariable=resultado_var, font=("Courier", 12), wraplength=380, justify="center")
resultado_label.pack(pady=10)

root.mainloop()
