from nltk.corpus import wordnet as wn
import networkx as nx

# In NLTK 2.0.4 plWordNet is not working properly, because of not using Unicode.

pos_tags = ['n','a','v'] # 'r' (adv) is empty

# TODO choose appropriate 

#empty_relations = ['also_sees', 'entailments',  'instance_hypernyms', 'instance_hyponyms', 'region_domains', 'similar_tos', 'topic_domains',  'usage_domains', 'verb_groups']

relations = ['attributes', 'causes', 'hypernyms', 'hyponyms', 'member_holonyms', 'member_meronyms',  'part_holonyms', 'part_meronyms',  'substance_holonyms', 'substance_meronyms'] # 'hypernym_paths' ? 'root_hypernyms'

relations = ['attributes', 'causes', 'hypernyms', 'member_holonyms', 'part_holonyms', 'substance_holonyms']

G = nx.MultiDiGraph()

# TODO add pos to nodes ?

for pos in pos_tags:
  for synset in wn.all_synsets(pos):
    #print synset.name
    synset_name = synset.name.decode('utf-8') 
    G.add_node(synset_name, depth=synset.max_depth())
    for method in relations:
      result = getattr(synset, method)()
      #if result:
        #print synset_name
        #print method
        #print result
      for related_synset in result:
        related_synset_name = related_synset.name.decode('utf-8') 
        G.add_node(related_synset_name, depth=related_synset.max_depth())
        G.add_edge(synset_name, related_synset_name, relation=method)

nx.write_gexf(G, "slowosiec.gexf")
nx.write_graphml(G, "slowosiec.graphml")
#nx.write_gml(G,"slowosiec.gml") # don't work with unicode


