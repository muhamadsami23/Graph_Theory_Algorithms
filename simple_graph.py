import matplotlib.pyplot as plt
import networkx as nx


n = int(input("Enter number of vertices:"))
if(n<=10):
  print("Vertices to be greater than 10. Re-enter")
  while(n <= 10):
   n = int(input("Enter number of vertices:"))


g = nx.Graph()

for i in range(n):
  g.add_node(i);

for i in range(n):
    numv = int(input(f"Enter Number of Vertex connected with {i}: "))
    for j in range(numv):
      v = int(input(f"Enter Vertex connected with {i}: "))

      if( i == v):
        print("Error. Slef Loop not allowed in Simple Graph")
        v = int(input(f"Enter Vertex connected with {i}: "))

      if(g.has_edge(i,v)):
        print("Error. Edge already exists")
        v = int(input(f"Enter Vertex connected with {i}: "))
      g.add_edge(i,v)


pos = nx.spring_layout(g)

nx.draw_networkx_nodes(g, pos, node_size=100, node_color="skyblue")
nx.draw_networkx_edges(g, pos, edge_color="gray")
nx.draw_networkx_labels(g, pos, font_size=8, font_color="black")

plt.title("Simple Graph with {} Vertices".format(n))
plt.axis("off")
plt.show()