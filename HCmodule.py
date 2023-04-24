import random
import math

class TSPHillClimbingSolver:
    
    def __init__(self, coords, num_iter):
        self.coords = coords
        self.num_cities = len(coords)
        self.num_iter = num_iter
        
    def solve(self):
        # Generate an initial solution
        current_order = list(range(self.num_cities))
        random.shuffle(current_order)
        
        # Evaluate the initial solution
        current_cost = self.evaluate_order(current_order)
        
        # Hill climbing loop
        for i in range(self.num_iter):
            # Generate a random neighbor
            neighbor_order = self.get_neighbor_order(current_order)
            
            # Evaluate the neighbor
            neighbor_cost = self.evaluate_order(neighbor_order)
            
            # If the neighbor is better, move to it
            if neighbor_cost < current_cost:
                current_order = neighbor_order
                current_cost = neighbor_cost
        
        return current_order, current_cost
    
    def get_neighbor_order(self, order):
        # Swap two cities in the order to get a neighbor
        i = random.randint(0, self.num_cities-1)
        j = random.randint(0, self.num_cities-1)
        neighbor_order = order.copy()
        neighbor_order[i], neighbor_order[j] = neighbor_order[j], neighbor_order[i]
        return neighbor_order
    
    def evaluate_order(self, order):
        # Calculate the total distance of the order
        total_dist = 0
        for i in range(self.num_cities):
            j = (i+1) % self.num_cities
            city_i = self.coords[order[i]]
            city_j = self.coords[order[j]]
            dist = math.sqrt((city_i[0]-city_j[0])**2 + (city_i[1]-city_j[1])**2)
            total_dist += dist
        return total_dist
