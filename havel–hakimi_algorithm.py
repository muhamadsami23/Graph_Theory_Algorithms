
import networkx as nx
import matplotlib.pyplot as plt

n = int(input("Enter number of vertices: "))
if n <= 10:
    print("Vertices must be greater than 5. Re-enter.")
    while n <= 10:
        n = int(input("Enter number of vertices: "))

degree = []

g = nx.Graph()

for i in range(n):
    g.add_node(i)

for i in range(n):
    numv = int(input(f"Enter number of vertices connected with {i}: "))
    for j in range(numv):
        v = int(input(f"Enter vertex connected with {i}: "))

        while i == v:
            print("Error. Self-loop not allowed in a simple graph.")
            v = int(input(f"Enter vertex connected with {i}: "))

        while g.has_edge(i, v) or v >= n:
            print("Error. Edge already exists or invalid vertex.")
            v = int(input(f"Enter vertex connected with {i}: "))

        g.add_edge(i, v)

degree = [g.degree[node] for node in g.nodes]
print("Degree of each vertex:", degree)


degree_sequence = sorted(degree, reverse=True)
is_graphical = True

print("Initial sorted degree sequence:", degree_sequence)

while degree_sequence:
    d = degree_sequence.pop(0)
    print(f"Removed degree {d}, remaining sequence: {degree_sequence}")

    if d > len(degree_sequence):
        is_graphical = False
        break

    for i in range(d):
        degree_sequence[i] -= 1
        if degree_sequence[i] < 0:
            is_graphical = False
            break

    if not is_graphical:
        break

    degree_sequence = sorted(degree_sequence, reverse=True)  # Re-sort after modification
    print(f"{degree_sequence}")

if is_graphical:
    print("The degree sequence is graphical and can represent a simple graph.")
else:
    print("The degree sequence is not graphical and cannot represent a simple graph.")