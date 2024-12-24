d = [i.split('-') for i in open('23').read().splitlines()]

nodes = list(set(j for i in d for j in i))
nodes_dct = dict(zip(nodes, range(len(nodes))))

edges1 = set(tuple([nodes_dct[i],nodes_dct[j]]) for i,j in d)
edges2 = set(tuple([nodes_dct[j],nodes_dct[i]]) for i,j in d)
edges = edges1.union(edges2)

t_comps = [v for k,v in nodes_dct.items() if k[0] == 't']

# Look for 3-cliques
edges_lst = list(edges)
n = len(edges_lst)
cliques = set()
for i in range(n):
  for j in range(i+1,n):
    n1, n2 = edges_lst[i]
    n3, n4 = edges_lst[j]
    if n1 == n3 and (n2,n4) in edges:
      if n1 in t_comps or n2 in t_comps or n4 in t_comps:
        cliques.add(tuple(sorted([n1,n2,n4])))
print(len(cliques))