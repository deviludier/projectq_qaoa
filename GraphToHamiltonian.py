# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Graph To Hamiltonian Functions
#
# This file contains a few different functions to convert
# user-inputted graphs into hamiltonians for use in ProjectQ to then 
# feed into whatever algorithm you need a hamiltonian for, be it VQE
# or QAOA. 
#
# We will continue to add different cost/mixer hamiltonian functions
# for different problems
#
# Graphs must be given as a networkx graph
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


from projectq.ops import QubitOperator


# Creates the MaxCut cost hamiltonian given a graph
# Graph   ==>   ∑ 1/2(I - sigmaZ_i • sigmaZ_j)
def maxcut_cost_ham(graph):
  ham = QubitOperator('', 0.0)
  for i, j in graph.edges():
    operator_i = 'Z' + str(i)
    operator_j = 'Z' + str(j)
    ham += QubitOperator(operator_i + ' ' + operator_j, 0.5) + QubitOperator('', -0.5)
  return ham
  
# Creates the MaxCut mixer hamiltonian given a graph
# Graph  ==>  ∑ sigmaX_i
def maxcut_mixer_ham(graph):
  ham = QubitOperator('', 0.0)
  for i in graph.nodes():
    operator = 'X' + str(i)
    ham += QubitOperator(operator, -1.0)
  return ham





# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                 Test
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == "__main__":
  
  # This test will simply construct a MaxCut cost and mixer Hamiltonian
  # for the following triangular graph:  0-1-2-0
  
  # Just import networkx, useful for making graphs with edges and nodes
  import networkx as nx
  
  # Construct a graph with n nodes
  n = 3
  G = nx.Graph()
  G.add_nodes_from(list(range(0, n, 1)))

  # tuple is (i, j) where (i, j) is the edge
  # This line just tells our graph how the edges are connected to each other
  edge_list = [(0, 1), (1, 2), (2, 0)]

  # Feed the edges to our graph:
  G.add_edges_from(edge_list)
  
  # Construct a mixer and a cost!  
  G_maxcut_cost = maxcut_cost_ham(graph=G)
  G_maxcut_mixer = maxcut_mixer_ham(graph=G)
  
  print("Cost Hamiltonian:\n{}\nMixer Hamiltonian:\n{}".format(G_maxcut_cost, G_maxcut_mixer))
  


