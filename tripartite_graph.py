
import matplotlib.pyplot as plt
import networkx as nx


n = int(input("Enter number of vertices:"))
if(n<=6):
  print("Vertices to be greater than 10. Re-enter")
  while(n <= 6):
   n = int(input("Enter number of vertices:"))

print("\n\n")

p = int(input("Enter number of Vertices in Group 1 : "))
q = int(input("Enter number of Vertices in Group 2 : "))
r = int(input("Enter number of Vertices in Group 3 : "))

if(p+q+r != n):
  print("Vertices not equal to Total Vertices. Re-enter")
  while((p+q)<n):
    print("Vertices not equal to Total Vertices. Re-enter")
    p = int(input("Enter number of Vertices in Group 1 : "))
    q = int(input("Enter number of Vertices in Group 2 : "))
    r = int(input("Enter number of Vertices in Group 3 : "))
    print("\n\n")

g1 = []
g2 =[]
g3 = []

print("\n\n")
print ("Enter Vertices in Group 1 : ")
for i in range(p):
    value = input()
    g1.append(value)

print("\n\n")
print ("Enter Vertices in Group 2 : ")
for i in range(q):
  val = input()
  g2.append(val)

print("\n\n")
print ("Enter Vertices in Group 3 : ")
for i in range(r):
  valu = input()
  g3.append(valu)


g = nx.Graph()
g.add_nodes_from(g1, bipartite=0)
g.add_nodes_from(g2, bipartite=1)
g.add_nodes_from(g2, bipartite=2)

print("\n\n")
for i in range(p):
      num = int(input(f"Enter number of connections with {g1[i]} : "))
      for k in range(num):
        v = input(f"Enter Vertex connected with {g1[i]}: ")
        if(v in g2 or v in g3):
          g.add_edge(g1[i], v)
        else:
          print("Invalid Vertex. Re-enter")
          while v not in g2 or v not in g3:
                    v = input(f"Error! Enter Vertex connected with {g1[i]}: ")
          g.add_edge(g1[i], v)

print("\n\n")
for i in range(q):
      num = int(input(f"Enter number of connections with {g2[i]} : "))
      print("Ignore connections with Group 1")
      for k in range(num):
        v = input(f"Enter Vertex connected with {g2[i]}: ")
        if(v in g3):
          g.add_edge(g2[i], v)
        else:
          print("Invalid Vertex. Re-enter")
          while v not in g3:
                    v = input(f"Error! Enter Vertex connected with {g1[i]}: ")
          g.add_edge(g2[i], v)


pos = {}

for i, node in enumerate(g1):
    pos[node] = (-3, -i)

for i, node in enumerate(g2):
    pos[node] = (3, -i)

for i, node in enumerate(g3):
    pos[node] = (-2 + i * 1.5, 2)

nx.draw_networkx_nodes(g, pos, node_size=150, node_color="skyblue")
nx.draw_networkx_edges(g, pos, edge_color="gray")
nx.draw_networkx_labels(g, pos, font_size=8, font_color="black")

plt.title("Tripartite Graph with {} Vertices".format(n))
plt.axis("off")
plt.show()
