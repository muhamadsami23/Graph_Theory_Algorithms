
import matplotlib.pyplot as plt
import networkx as nx


n = int(input("Enter number of vertices:"))
if(n<=10):
  print("Vertices to be greater than 10. Re-enter")
  while(n <= 10):
   n = int(input("Enter number of vertices:"))

print("\n\n")

p = int(input("Enter number of Vertices in Group 1 : "))
q = int(input("Enter number of Vertices in Group 2 : "))

if(p+q != n):
  print("Vertices not equal to Total Vertices. Re-enter")
  while((p+q)<n):
    p = int(input("Enter number of Vertices in Group 1 : "))
    q = int(input("Enter number of Vertices in Group 2 : "))

g1 = []
g2 =[]

print ("Enter Vertices in Group 1 : ")
for i in range(p):
    value = input()
    g1.append(value)

print ("Enter Vertices in Group 2 : ")
for i in range(q):
  val = input()
  g2.append(val)


g = nx.Graph()
g.add_nodes_from(g1, bipartite=0)
g.add_nodes_from(g2, bipartite=1)

for i in range(p):
      num = int(input(f"Enter number of connections with {g1[i]} : "))
      for k in range(num):
        v = input(f"Enter Vertex connected with {g1[i]}: ")
        if(v in g2):
          g.add_edge(g1[i], v)
        else:
          print("Invalid Vertex. Re-enter")
          while v not in g2:
                    v = input(f"Error! Enter Vertex connected with {g1[i]}: ")
          g.add_edge(g1[i], v)



pos = nx.bipartite_layout(g, g1)

nx.draw_networkx_nodes(g, pos, node_size=150, node_color="skyblue")
nx.draw_networkx_edges(g, pos, edge_color="gray")
nx.draw_networkx_labels(g, pos, font_size=8, font_color="black")

plt.title("Bipartite Graph with {} Vertices".format(n))
plt.axis("off")
plt.show()
