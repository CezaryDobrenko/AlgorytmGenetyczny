from simulation import Simulation


def main():
    #-------------------
    # Population settings
    bounds = (-4, 2)
    bit_size = 32
    population_size = 9
    generations = 2000
    tournament_size = 4
    settings = {
        "single_point_mutation": True,
        "swap_mutation": False,
        "scramble_mutation": False,
        "reverse_mutation": False, 
        "full_random_mutation": False,
    }
    #-------------------

    simulation = Simulation(population_size, bit_size, bounds, tournament_size, settings)
    simulation.evolve(generations)
    simulation.draw_animation(0.00001)
    simulation.export_data()

    best_probe = simulation.get_best_probe()
    x, y, value = best_probe.get_genotype_data()
    print(x, y, value)

if __name__ == "__main__":
    main()
