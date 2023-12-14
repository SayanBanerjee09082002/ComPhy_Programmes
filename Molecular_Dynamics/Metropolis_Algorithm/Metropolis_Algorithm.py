import numpy as np
import matplotlib.pyplot as plt

def metropolis_algorithm(initial_state, num_steps, temperature, energy_function):
    current_state = initial_state
    state_trajectory = [current_state]

    for step in range(num_steps):
        # Propose a new state
        proposed_state = "B" if current_state == "A" else "A"

        # Calculate energy difference
        delta_energy = energy_function(proposed_state) - energy_function(current_state)

        # Acceptance criteria
        if delta_energy < 0 or np.random.rand() < np.exp(-delta_energy / temperature):
            current_state = proposed_state

        # Record the current state in the trajectory
        state_trajectory.append(current_state)

    return state_trajectory

# Energy levels for states A and B
energy_A = -1.0
energy_B = 0.0

# Function to calculate energy for a given state
def calculate_energy(state):
    if state == "A":
        return energy_A
    elif state == "B":
        return energy_B
    else:
        raise ValueError("Invalid state")

# Example usage
initial_state = "A"
num_steps = 1000
temperature = 1.0

trajectory = metropolis_algorithm(initial_state, num_steps, temperature, calculate_energy)

# Plot the trajectory
plt.figure(figsize=(8, 4))
plt.plot(range(num_steps + 1), trajectory, marker='o', linestyle='-', color='b')
plt.title('Metropolis Algorithm: State Trajectory')
plt.xlabel('Steps')
plt.ylabel('State')
plt.yticks(["A", "B"])
plt.show()
