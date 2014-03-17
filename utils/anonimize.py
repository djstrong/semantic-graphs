import networkx as nx
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# Converts graph to undirected, removes attributes and changes ids to integers.

path = sys.argv[1]

G = nx.read_gexf(path)
G = nx.Graph(G)

mapping = {}

for i, node in enumerate(G.nodes()):
  mapping[node] = i

H = nx.Graph()

for a,b in G.edges():
  H.add_edge(mapping[a],mapping[b])
  
name = path.rsplit('.', 1)[0]
nx.write_gexf(H, name+'_anonimized.gexf')