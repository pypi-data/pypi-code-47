from soio.algo import BBO, CGWO, CWOA, DE,GWO, HS, ICA, JADE, WOA
from soio.benchmark.Ackley import Ackley
import matplotlib.pyplot as plt

problem = Ackley(20)

# algorithm = BBO.BBO(
#     problem = problem,
#     habitats_size = 100,
#     max_nfes = 10000,
# )
# algorithm.run()
# print("Time:", algorithm.total_computing_time)
# print("Minimum Obj:", algorithm.get_result().objective)
# plt.plot(algorithm.records)
# plt.show()

# algorithm = CGWO.CellularGreyWolfOptimizer(
#     problem = problem,
#     max_nfes = 10000,
#     grid_shape=[10, 10],
#     neighbor_structure=CGWO.CA_C9,
# )
# algorithm.run()
# print("Time:", algorithm.total_computing_time)
# print("Minimum Obj:", algorithm.get_result().objective)
# plt.plot(algorithm.records)
# plt.show()

# algorithm = CWOA.CellularWhaleOptimizer(
#     problem = problem,
#     max_nfes = 10000,
#     grid_shape=[10, 10],
#     neighbor_structure=CWOA.CA_C9,
# )
# algorithm.run()
# print("Time:", algorithm.total_computing_time)
# print("Minimum Obj:", algorithm.get_result().objective)
# plt.plot(algorithm.records)
# plt.show()

# algorithm = DE.DifferentialEvolution(
#     problem = problem,
#     max_nfes = 10000,
#     population_size=100,
#     CR = 0.5,
#     F = 0.1,
# )
# algorithm.run()
# print("Time:", algorithm.total_computing_time)
# print("Minimum Obj:", algorithm.get_result().objective)
# plt.plot(algorithm.records)
# plt.show()

# algorithm = GWO.GreyWolfOptimizer(
#     problem = problem,
#     max_nfes = 10000,
#     swarm_size=100,
# )
# algorithm.run()
# print("Time:", algorithm.total_computing_time)
# print("Minimum Obj:", algorithm.get_result().objective)
# plt.plot(algorithm.records)
# plt.show()

# algorithm = HS.HarmonySearch(
#     problem = problem,
#     max_nfes = 10000,
#     harmony_memory_size=100,
#     memory_consider_rate = 0.9,
#     pitch_adjust_rate = 0.5,
#     band_width = 0.5
# )
# algorithm.run()
# print("Time:", algorithm.total_computing_time)
# print("Minimum Obj:", algorithm.get_result().objective)

# algorithm = ICA.ImperialistCompetitiveAlgorithm(
#     problem = problem,
#     max_nfes = 10000,
#     population_size= 100,
#     imperialists_size = 10,
# )
# algorithm.run()
# print("Time:", algorithm.total_computing_time)
# print("Minimum Obj:", algorithm.get_result().objective)
# plt.plot(algorithm.records)
# plt.show()

# algorithm = JADE.JADE(
#     problem = problem,
#     max_nfes = 10000,
#     population_size= 30,
#     archive_size = 0,
#     p = 0.05,
#     c = 0.1
# )
# algorithm.run()
# print("Time:", algorithm.total_computing_time)
# print("Minimum Obj:", algorithm.get_result().objective)
# plt.plot(algorithm.records)
# plt.show()

# algorithm = WOA.WhaleOptimizer(
#     problem = problem,
#     max_nfes = 10000,
#     swarm_size= 100,
# )
# algorithm.run()
# print("Time:", algorithm.total_computing_time)
# print("Minimum Obj:", algorithm.get_result().objective)
# plt.plot(algorithm.records)
# plt.show()