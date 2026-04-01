import csv

def main():
    with open('task0.csv', 'r') as f:
        edges = csv.reader(f)
        edges = [(int(u), int(v)) for u, v in edges]
        n = max([max(u, v) for u,v in edges])
        adj = [[0 for j in range(n)] for i in range(n)]
        for u, v in edges:
            u -= 1
            v -= 1
            adj[u][v] = adj[v][u] = 1
    
    for row in adj:
        print(*row)
