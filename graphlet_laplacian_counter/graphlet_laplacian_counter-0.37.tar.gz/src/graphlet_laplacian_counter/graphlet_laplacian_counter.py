from array import array
import numpy as np
import networkx as nx
import cppyy
import os


class GrahpletLaplacianCounter(object):

    """Python wrapper for C++ Graphlet Laplacian counter """

    def __init__(self):

    def count_from_adj_matrix(self, A, node=None):
        """returns all graphlet laplacians matrices for up to 4 node graphlets.
        If a node is given, the laplacians are computed only for that single node.

        """

        #"compile" c++ code
        run_dir =os.path.dirname(os.path.abspath(__file__))
        cppyy.include(run_dir + '/src_c++/Counter.cpp')
        cppyy.include(run_dir + '/src_c++/Graph.cpp')

        nodes_src, nodes_dst = np.nonzero(A)
        nodes_src = nodes_src.tolist()
        nodes_dst = nodes_dst.tolist()
        if node is None:
            from cppyy.gbl import count_from_vectors
            return np.asanyarray(count_from_vectors(nodes_src,nodes_dst))
        else:
            from cppyy.gbl import count_from_vectors_single_node
            GL_s = np.asanyarray(count_from_vectors_single_node(nodes_src,nodes_dst,node))
            return GL_s



def main():
    # G = nx.read_edgelist(run_dir+'/src_c++/PPI_exp_950.edgelist')
    G = nx.read_edgelist('../PPI_exp_950.edgelist')
    A = nx.to_numpy_matrix(G)

    counter =  GrahpletLaplacianCounter()
    GL_s = counter.count_from_adj_matrix(A,1)
    pass

if __name__ == "__main__":
    main()

