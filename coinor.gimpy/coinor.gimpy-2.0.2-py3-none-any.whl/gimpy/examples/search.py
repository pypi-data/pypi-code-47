try:
    from src.gimpy import Graph, UNDIRECTED_GRAPH
except ImportError:
    from coinor.gimpy import Graph, UNDIRECTED_GRAPH

G = Graph(type = UNDIRECTED_GRAPH, splines = 'true', K = 1.5)
G.random(numnodes = 15, Euclidean = False, seedInput = 13, 
         add_labels = True,
         #scale = 10,
         #scale_cost = 10,
         #degree_range = (2, 4),
         #length_range = (1, 10)
         )
G.set_display_mode('matplotlib')
G.display()
#G.dfs(0)
G.search(0, display = 'matplotlib', algo = 'Dijkstra')

#G = Graph(type = UNDIRECTED_GRAPH, splines = 'true', K = 1.5)
#G.random(numnodes = 20, Euclidean = True, seedInput = 11,
#         add_labels = False,
#         scale = 10,
#         scale_cost = 10,
#         #degree_range = (2, 4),
#         #length_range = (1, 10)
#         )
#page_ranks = sorted(G.page_rank().iteritems(), key=operator.itemgetter(1))
#page_ranks.reverse()
#for i in page_ranks:
#    print i    #G = Graph(type = UNDIRECTED_GRAPH, splines = 'true', K = 1.5)
#G.random(numnodes = 10, Euclidean = True, seedInput = 13,
#         add_labels = True,
#         scale = 10,
#         scale_cost = 10,
         #degree_range = (2, 4),
         #length_range = (1, 10)
#         )
#G.set_display_mode('pygame')
#G.display()
#G.dfs(0)
#G.search(0, display = 'pygame', algo = 'Prim')
#G.minimum_spanning_tree_kruskal()

