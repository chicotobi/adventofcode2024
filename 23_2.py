d = [i.split('-') for i in open('23').read().splitlines()]

nodes = list(set(j for i in d for j in i))
nodes_dct = dict(zip(nodes, range(len(nodes))))

edges1 = set(tuple([nodes_dct[i],nodes_dct[j]]) for i,j in d)
edges2 = set(tuple([nodes_dct[j],nodes_dct[i]]) for i,j in d)
cliques = edges1.union(edges2)

t_comps = [v for k,v in nodes_dct.items() if k[0] == 't']

import tqdm

new_cliques = set()
for k in range(3,20):
  # Look for k-cliques - edges are 2-cliques
  # Choose a k-1-clique
  print("k",k,"len cliques",len(cliques))
  for c in tqdm.tqdm(cliques):
    # Choose a node
    for n in range(len(nodes)):
      if n in c:
        continue
      pos_new_clique = tuple(sorted(c+(n,)))
      if pos_new_clique in new_cliques:
        continue
      is_k_clique = True
      #print("check for ",k,"-clique ",c,n)
      # Define the other k-1 cliques
      for i in range(k-1):
        # Remove the i-th node from the current clique
        # Add the chosen node
        pos_c = tuple(sorted(c[:i] + c[i+1:] + (n,)))
        #print("  check ",k-1,"-clique",pos_c)
        if pos_c not in cliques:
          is_k_clique = False
          break
      if is_k_clique:
        #print("  is ",k,"clique:",pos_new_clique)
        new_cliques.add(pos_new_clique)
  if len(new_cliques) == 0:
    break
  cliques = new_cliques
  new_cliques = set()
# Should be length one
res = sorted(sorted(nodes[i] for i in c) for c in cliques)[0]
res2 = ','.join(res)
print(res2)