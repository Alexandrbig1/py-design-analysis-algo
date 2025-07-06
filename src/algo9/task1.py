import random
import math


def sphere_function(x):
    return sum(xi ** 2 for xi in x)


def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    current = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current)

    for _ in range(iterations):
        neighbour = [c + random.uniform(-0.1, 0.1) for c in current]
        neighbour = [max(bounds[i][0], min(bounds[i][1], neighbour[i])) for i in range(len(bounds))]
        next_value = func(neighbour)

        if next_value < current_value:
            current, current_value = neighbour, next_value

        if abs(current_value - next_value) < epsilon:
            break

    return current, current_value


def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    best = [random.uniform(b[0], b[1]) for b in bounds]
    best_value = func(best)

    for _ in range(iterations):
        candidate = [random.uniform(b[0], b[1]) for b in bounds]
        candidate_value = func(candidate)

        if candidate_value < best_value:
            best, best_value = candidate, candidate_value

        if best_value < epsilon:
            break

    return best, best_value


def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    current = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current)

    for _ in range(iterations):
        neighbour = [c + random.uniform(-0.1, 0.1) for c in current]
        neighbour = [max(bounds[i][0], min(bounds[i][1], neighbour[i])) for i in range(len(bounds))]
        next_value = func(neighbour)
        temp *= cooling_rate

        if next_value < current_value or random.random() < math.exp((current_value - next_value) / temp):
            current, current_value = neighbour, next_value

        if temp < epsilon:
            break

    return current, current_value


if __name__ == "__main__":
    bounds = [(-5, 5), (-5, 5)]

    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Solution:", hc_solution, "Value:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Solution:", rls_solution, "Value:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Solution:", sa_solution, "Value:", sa_value)