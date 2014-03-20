import networkx as nx
import collections
from progress.bar import Bar
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

NODES = 10

path = sys.argv[1]
G = nx.read_gexf(path)

print 'The highest degree nodes with attributes'

for node, degree in sorted(G.degree_iter(),key=lambda x: x[1],reverse=True)[:NODES]:
  print degree, node, G.node[node]