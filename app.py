import random

class ParticleSimulation:
    def __init__(self, particle_count):
        self.particle_count = particle_count
        self.particles = [random.random() for _ in range(particle_count)]  # Initialize particles with random values

    def update(self):
        # Simulate some changes in the particle system
        self.particles = [particle + random.uniform(-0.1, 0.1) for particle in self.particles]

    def get_state(self):
        return self.particles

class GrandSimulation:
    def __init__(self, num_simulations, particle_counts):
        self.simulations = [ParticleSimulation(count) for count in particle_counts]

    def run(self, steps):
        for step in range(steps):
            print(f"Step {step + 1}:")
            for i, sim in enumerate(self.simulations):
                sim.update()
                print(f" Simulation {i + 1} state: {sim.get_state()}")

# Configuration for the grand simulation
num_simulations = 3
particle_counts = [10, 20, 30]  # Number of particles in each simulation

# Create and run the grand simulation
grand_sim = GrandSimulation(num_simulations, particle_counts)
grand_sim.run(5)  # Run for 5 steps
