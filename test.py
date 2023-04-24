from HCmodule import TSPHillClimbingSolver


coords = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
num_iter = 1000
solver = TSPHillClimbingSolver(coords, num_iter)

best_order, best_cost = solver.solve()
print("Best order:", best_order)
print("Best cost:", best_cost)
