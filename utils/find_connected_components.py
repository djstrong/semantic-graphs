import networkx as nx
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# Convert graph to undirected, finds the biggest connected components and write it to files.

NUMBER_OF_COMPONENTS = 5

path = sys.argv[1]

G = nx.read_gexf(path)
G = nx.Graph(G)

print 'number_of_nodes', nx.number_of_nodes(G)
print 'number_of_edges', nx.number_of_edges(G)
print 'number_strongly_connected_components', nx.number_strongly_connected_components(G)
print

strongly_connected_components = nx.strongly_connected_component_subgraphs(G)

name = path.rsplit('.', 1)[0]

print 'the biggest components:'
for i, component in enumerate(strongly_connected_components[:NUMBER_OF_COMPONENTS]):
  print i
  print 'number_of_nodes', nx.number_of_nodes(component)
  print 'number_of_edges', nx.number_of_edges(component)
  print
  
  nx.write_gexf(component, name+str(i)+'.gexf')