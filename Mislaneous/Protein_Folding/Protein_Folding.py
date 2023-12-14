import numpy as np
import matplotlib.pyplot as plt

class ProteinModel:
    def __init__(self, length):
        self.length = length #Length of protein
        self.structure = np.zeros(self.length, dtype=int) #Create array with values initialised to zero

    #This simulated J, change if you want
    def calculate_interaction_energy(self, position):
        left_neighbor = (position - 1) % self.length
        right_neighbor = (position + 1) % self.length
        return int(self.structure[position] == self.structure[left_neighbor] == self.structure[right_neighbor])
    
    def calculate_total_energy(self):
        total_energy = 0
        for i in range(self.length):
            total_energy += self.calculate_interaction_energy(i)
        return total_energy

    def metropolis_simulation(self, steps):
        for _ in range(steps):
            position = np.random.randint(self.length)
            energy_before = self.calculate_total_energy()
            self.structure[position] = 1 - self.structure[position]  # Flip the amino acid
            energy_after = self.calculate_total_energy()
            # Metropolis criterion
            if energy_after > energy_before and np.random.rand() > np.exp(energy_before - energy_after):
                # Revert the change if not accepted
                self.structure[position] = 1 - self.structure[position]

    def plot_structure(self):
        plt.plot(range(self.length), self.structure, marker='o')
        plt.title('Protein Structure')
        plt.show()

# Example usage:
sequenceLength = 12
protein = ProteinModel(sequenceLength)
protein.metropolis_simulation(steps=1000)
protein.plot_structure()
