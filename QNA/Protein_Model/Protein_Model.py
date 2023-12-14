import random
import math
import matplotlib.pyplot as plt

def initialize_protein(num_amino_acids):
    # Initialize a 2D lattice representing the protein structure
    protein_structure = [[i,0] for i in range(num_amino_acids)]
    return protein_structure

def calculate_energy(protein_structure):
    # Calculate the energy of the protein structure based on a simple criterion
    energy = 0
    for i in range(len(protein_structure) - 1):
        distance_squared = (protein_structure[i][0] - protein_structure[i + 1][0])**2 + (protein_structure[i][1] - protein_structure[i + 1][1])**2
        # Avoid division by zero
        #Logic here: Interaction energy is directly roportional to (1/distance^2) so I set proportionality const to 1 for simplicity
        if distance_squared != 0:
            energy += 1 / distance_squared  # Simplified energy function

    return energy

def metropolis_algorithm(protein_structure, num_steps, temperature):
    for step in range(num_steps):
        # Choose a random amino acid to move
        amino_acid_index = random.randint(0, len(protein_structure) - 1)

        # Propose a random move (up, down, left, or right)
        move = random.choice([(1, 1), (1, -1), (-1, 1), (-1, -1)])

        # Make a copy of the current protein structure
        new_structure = [coord.copy() for coord in protein_structure]

        # Apply the proposed move to the chosen amino acid
        new_structure[amino_acid_index][0] += move[0]
        new_structure[amino_acid_index][1] += move[1]

        # Calculate energy differences
        current_energy = calculate_energy(protein_structure)
        new_energy = calculate_energy(new_structure)
        
        # Accept or reject the move based on the Metropolis criterion
        if new_energy < current_energy :
            protein_structure = new_structure
        else :
            w = math.exp((current_energy - new_energy) / ((1.380649 * 10**23) * temperature))
            if w >= random.random():
                protein_structure = new_structure

    return protein_structure

# Parameters
num_amino_acids = 25
temperature = 1.0
num_steps = 100

# Initialize protein structure
protein_structure = initialize_protein(num_amino_acids)

# Perform Metropolis algorithm
final_structure = metropolis_algorithm(protein_structure, num_steps, temperature)

# Plot the final protein structure
x_coords, y_coords = zip(*final_structure)
plt.figure(figsize=(8, 8))
plt.plot(x_coords, y_coords, 'bo-', markersize=10)
plt.title('Final Protein Structure')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.show()