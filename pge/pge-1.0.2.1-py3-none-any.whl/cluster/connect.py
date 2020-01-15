import numpy as np
import networkx as nx


def phi(gr, nodes, other=None):
    return nx.algorithms.cuts.conductance(gr.get_nx_graph(), nodes, other)


def conductance_set(gr, root):
    nxt = [root]
    prev2 = 3
    prev1 = 2

    while len(nxt) < gr.size():
        ind = gr.get_degrees(nxt)
        ind = ind[~np.isin(ind, nxt)]

        cnd = [phi(gr, nxt+[node]) for node in ind]
        mn = np.argmin(cnd)

        if prev2 >= prev1 and prev1 <= cnd[mn]:
            break

        nxt.append(ind[mn])
        prev2 = prev1
        prev1 = cnd[mn]
    return nxt


def weak_conductance(gr, root, c):
    nxt = [root]
    prev2 = 3
    prev1 = 2

    res = []
    while len(nxt) < gr.size() - 1:
        ind = gr.get_degrees(nxt)
        ind = ind[~np.isin(ind, nxt)]

        cnd = [phi(gr, nxt + [node]) for node in ind]
        mn = np.argmin(cnd)

        if prev2 >= prev1 and prev1 <= cnd[mn] and len(nxt) >= gr.size()/c:
            sets = nx.algorithms.community.kernighan_lin.kernighan_lin_bisection(gr.subgraph(nxt).get_nx_graph())
            res.append(phi(gr, sets[0], sets[1]))
        nxt.append(ind[mn])
        prev2 = prev1
        prev1 = cnd[mn]

    return res[-1]
