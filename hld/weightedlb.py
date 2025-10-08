import random
from collections import defaultdict

class Server:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

class WeightedRoundRobinBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.total_weight = self.calculate_total_weight(servers)
        self.cumulative_weights = self.calculate_cumulative_weights(servers)
        # Note: self.current_index is unnecessary for this randomized method
        self.random = random.Random()

    def calculate_total_weight(self, servers):
        total_weight = 0
        for server in servers:
            total_weight += server.get_weight()
        return total_weight

    def calculate_cumulative_weights(self, servers):
        cumulative_weights = [0] * len(servers)
        cumulative_weights[0] = servers[0].get_weight()
        for i in range(1, len(servers)):
            cumulative_weights[i] = cumulative_weights[i - 1] + servers[i].get_weight()
        print(cumulative_weights)
        return cumulative_weights

    def get_next_server(self):
        # 1. Generate a random value in the range [0, total_weight - 1]
        random_value = self.random.randint(0, self.total_weight - 1)
        
        # 2. Find the segment the random value falls into
        for i in range(len(self.cumulative_weights)):
            if random_value < self.cumulative_weights[i]:
                # The selected server is the one whose weight segment was hit
                return self.servers[i]
        
        # Should not be reached if total_weight is calculated correctly
        return None 


if __name__ == "__main__":
    # Sample list of servers with weights
    server_list = [
        Server("Server1", 3), # Expected 50%
        Server("Server2", 2), # Expected 33.3%
        Server("Server3", 1)  # Expected 16.7%
    ]

    # Create a weighted load balancer
    balancer = WeightedRoundRobinBalancer(server_list)
    
    # Simulate a large number of requests to observe the distribution
    NUM_REQUESTS = 10
    counts = defaultdict(int)

    for _ in range(NUM_REQUESTS):
        next_server = balancer.get_next_server()
        counts[next_server.get_name()] += 1

    print(f"--- Weighted Random Load Balancer Simulation ({NUM_REQUESTS} Requests) ---")
    print(f"Total Weight: {balancer.total_weight}")
    
    for server in server_list:
        name = server.get_name()
        weight = server.get_weight()
        count = counts[name]
        percentage = (count / NUM_REQUESTS) * 100
        
        print(f"[{name} (Weight: {weight})]: {count} hits ({percentage:.1f}%)")
    
    print("\nNote: The distribution is random, so the exact counts vary but should approximate the 3:2:1 ratio.")