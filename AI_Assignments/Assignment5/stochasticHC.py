import random

def objective_function(current_number, target_number):
    return -abs(current_number - target_number)

def stochastic_hill_climbing_game(current_number, target_number, max_iterations, exploration_prob):
    for _ in range(max_iterations):
        # Generate neighboring solutions (increment or decrement the current number)
        neighbor_solution = current_number + random.choice([-1, 1])
        neighbor_value = objective_function(neighbor_solution, target_number)

        # Move to the neighbor, even if it has a lower value with a certain probability
        if neighbor_value > objective_function(current_number, target_number) or random.random() < exploration_prob:
            current_number = neighbor_solution

    return current_number, objective_function(current_number, target_number)

if __name__ == "__main__":
    # Example usage for the number game
    initial_number = 78
    target_number = 200
    max_iterations = 100
    exploration_prob = 0.2  # Probability of exploring a worse solution

    best_solution, best_value = stochastic_hill_climbing_game(initial_number, target_number, max_iterations, exploration_prob)

    print("Best Solution:", best_solution)
    print("Best Value:", best_value)
    print("Target Value:", target_number)