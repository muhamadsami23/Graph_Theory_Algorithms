

import matplotlib.pyplot as plt
import networkx as nx


n = int(input("Enter number of vertices:"))
if(n<=10):
  print("Vertices to be greater than 10. Re-enter")
  while(n <= 10):
   n = int(input("Enter number of vertices:"))

print("\n\n")

g = nx.Graph()

for i in range(n):
  g.add_node(i);
j = 1
for i in range(n):
  for j in range(n):
      if(i!=j):
        g.add_edge(i,j)


pos = nx.spring_layout(g)

nx.draw_networkx_nodes(g, pos, node_size=150, node_color="skyblue")
nx.draw_networkx_edges(g, pos, edge_color="gray")
nx.draw_networkx_labels(g, pos, font_size=8, font_color="black")

plt.title("Complete Graph with {} Vertices".format(n))
plt.axis("off")
plt.show()
