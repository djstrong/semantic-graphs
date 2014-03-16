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
count = 0

for n in Bar('Processing', suffix = '%(index)d/%(max)d %(percent).1f%% - %(eta_td)s').iter(G):
  paths = nx.single_source_shortest_path_length(G,n)
  del paths[n] # remove path to self
  for length in paths.itervalues():
    summ += length
    count += 1
    if length > diameter: diameter = length

average_shortest_path_length = float(summ)/count
print 'diameter', diameter # D
print 'average_shortest_path_length', average_shortest_path_length # L
  

