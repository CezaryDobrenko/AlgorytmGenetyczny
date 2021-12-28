from simulation import Simulation

def main():
    #-------------------
    # Population settings
    bounds = (-4, 2)
    bit_size = 32
    population_size = 9
    generations = 50
    tournament_size = 4
    settings = {
        "single_point_mutation": False,
        "swap_mutation": True,
        "scramble_mutation": True,
        "reverse_mutation": False, 
        "full_random_mutation": False,
    }
    #-------------------

    # check output on single populations
    simulation = Simulation(population_size, bit_size, bounds, tournament_size, settings)
    simulation.evolve(generations)
    simulation.draw_animation(0.1, save_animation=True, save_each_frame=True)
    simulation.export_data()

    best_probe = simulation.get_best_probe()
    x, y, value = best_probe.get_genotype_data()
    print(x, y, value)

    # check average best probe value on multiple populations with given settings
    # reps = 100
    # sum = 0
    # for _ in range(reps):
    #     simulation = Simulation(population_size, bit_size, bounds, tournament_size, settings)
    #     simulation.evolve(generations)
    #     best_probe = simulation.get_best_probe()
    #     _, _, value = best_probe.get_genotype_data()
    #     sum += value
    # print(sum/reps)

if __name__ == "__main__":
    main()
