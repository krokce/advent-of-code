import networkx as nx
import matplotlib.pyplot as plt
import math

with open("day25.txt", "r") as file:
    lines = [l.strip().split(" ") for l in file.readlines() ]

g = nx.Graph()
for c in lines:
    for c1 in c[1:]:
        g.add_edge(c[0].replace(":", ""), c1)

# shortest way to divide a graph into two disconnected parts
for cut_edge in list(nx.minimum_edge_cut(g)):
    g.remove_edge(cut_edge[0], cut_edge[1])
    print(cut_edge)

# visualise network and cut the edges holding the two groups together
# nx.draw_networkx(g)
# plt.show()
                     
#1
print(math.prod([len(n) for n in nx.connected_components(g)]))