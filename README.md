# Romania Pathfinding Algorithms 🗺️

This project implements two **informed search algorithms** to find the shortest path between cities in Romania: **A* (A-star)** and **Greedy Best-First Search**. These algorithms solve the classic pathfinding problem using heuristic-based approaches.

## 📌 Features
- **Interactive Python GUI**:
  - Dropdown menus to select start/goal cities
  - Algorithm selection (A* or Greedy)
  - Visual path animation
  - Detailed output with cities visited and total cost
- **Search Algorithms**:
  - **A*** (optimal, guarantees shortest path)
  - **Greedy Best-First** (fast but not always optimal)
- **Romania Map Data** with accurate distances and coordinates

## 🚀 Algorithms

### A* Search
- **Optimal**: Guarantees the shortest path
- **Evaluation Function**: `f(n) = g(n) + h(n)`
  - `g(n)`: Actual cost from start to current node
  - `h(n)`: Heuristic estimate to goal (straight-line distance)
- **Complete**: Always finds a solution if one exists

### Greedy Best-First Search
- **Fast**: Prioritizes nodes closest to goal
- **Evaluation Function**: `f(n) = h(n)`
- **Not Optimal**: May not find the shortest path
- **Memory Efficient**: Expands fewer nodes than A*
