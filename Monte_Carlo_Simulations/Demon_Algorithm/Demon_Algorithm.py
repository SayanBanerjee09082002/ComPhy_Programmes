import random

T_hot = float(input("Enter higher temperature in kelvin: "))
T_cold = float(input("Enter lower temperature in kelvin: "))
particles = int(input("Enter the number of particles: "))
steps = int(input("Enter number of simulation steps: "))

compartment_a = []
compartment_b = []
barrier_open = False


def Demon_Algorithm():
    global barrier_open
    velocity = random.uniform(0, T_hot)
    if barrier_open or velocity >= T_cold:
        compartment_b.append(velocity)
    else:
        compartment_a.append(velocity)
    barrier_open = (random.random() < (velocity / T_hot))


for _ in range(steps):
    Demon_Algorithm()

energy_a = sum([0.5 * v**2 for v in compartment_a])
energy_b = sum([0.5 * v**2 for v in compartment_b])

print(f"Number of particles in compartment A: {len(compartment_a)}")
print(f"Number of particles in compartment B: {len(compartment_b)}")
print(f"Total energy in compartment A: {energy_a}")
print(f"Total energy in compartment B: {energy_b}")
