import networkx as nx
import collections
from progress.bar import Bar
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

path = sys.argv[1]
G = nx.read_gexf(path)

print 'number_of_nodes', nx.number_of_nodes(G)
print 'number_of_edges', nx.number_of_edges(G)
print 'number_strongly_connected_components', nx.number_strongly_connected_components(G)

print 'average_clustering', nx.average_clustering(G) # C
print 'degree_histogram', nx.degree_histogram(G) # P(k)
  
diameter = 0
summ = 0

for node in Bar('Processing', suffix = '%(index)d/%(max)d %(percent).1f%% - %(eta_td)s').iter(G):
  path_length = nx.single_source_shortest_path_length(G, node)
  summ += sum(path_length.values())
  diameter = max(diameter, max(path_length.values()))

n=len(G)
average_shortest_path_length = float(summ)/(n*(n-1))
print 'diameter', diameter # D
print 'average_shortest_path_length', average_shortest_path_length # L
