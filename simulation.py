import copy
import json
import math
import random
from typing import Dict, List, Tuple

from converter import Converter
from mutator import Mutator
from plotter import Plotter
from probe import Probe


class Simulation:
    __population: List[Probe]
    __tournament_size: int
    __bounds: Tuple[int, int]
    __population_ratio: int
    __settings: Dict
    __population_data: List[List[float]]
    __generations: int

    def __init__(self, population_size: int, bit_size: int, bounds: Tuple[int, int], tournament_size: int, settings: Dict):
        self.__bounds = bounds
        self.__tournament_size = tournament_size
        self.__population_ratio = (math.floor(population_size/2)-1, math.ceil(population_size/2))
        self.__population = self.generate_population(population_size, bit_size)
        self.__settings = settings

    def evolve(self, generations: int):
        population_data = []
        for _ in range(generations):
            parents_count, childrens_count = self.__population_ratio
            current_data = [[],[]]
            # best probe section
            best_probe = self.operator_hot_deck(self.__population)
            self.__population.remove(best_probe)
            current_data = self.__parse_data(current_data, [best_probe])

            # parents section
            preserved_parents = [best_probe]
            for _ in range(parents_count):
                tournament_winner = self.operator_tournament_selection(self.__population, self.__tournament_size)
                preserved_parents.append(tournament_winner)
            current_data = self.__parse_data(current_data, preserved_parents)

            # offsprings section
            offsprings = []
            for _ in range(childrens_count):
                base_parent1, base_parent2 = random.sample(preserved_parents, 2)
                children = Mutator.cross_over_mutation(base_parent1, base_parent2)
                mutated_children = Mutator.execute_mutations(children, self.__settings)
                offsprings.append(mutated_children)
            current_data = self.__parse_data(current_data, offsprings)

            # override population
            self.__population = preserved_parents + offsprings
            population_data.append(current_data)

        self.__population_data = population_data
        self.__generations = generations

    def operator_tournament_selection(self, population: List[Probe], tournament_size: int) -> Probe:
        tournament_pool = random.sample(population, tournament_size)
        tournament_winner = self.operator_hot_deck(tournament_pool)
        population.remove(tournament_winner)
        return copy.deepcopy(tournament_winner)

    def operator_hot_deck(self, population: List[Probe]) -> Probe:
        best_probe = population[0]
        current_best_value = best_probe.get_genotype_data()[2]
        for probe in population[1:]:
            probe_value = probe.get_genotype_data()[2]
            if probe_value < current_best_value:
                best_probe = probe
                current_best_value = probe_value
        return best_probe

    def get_best_probe(self) -> Probe:
        return self.operator_hot_deck(self.__population)

    def generate_population(self, population_size: int, bit_size: int) -> List[Probe]:
        population = []
        for _ in range(population_size):
            max_unsigned_int = (2 ** bit_size) - 1
            x = random.randrange(0, max_unsigned_int)
            y = random.randrange(0, max_unsigned_int)
            encoded_x = Converter.dec_to_gray(x, bit_size)
            encoded_y = Converter.dec_to_gray(y, bit_size)
            population.append(Probe(encoded_x, encoded_y, self.__bounds))
        return population
      
    def get_probe(self, index: int) -> Probe:
        return self.__population[index]

    def draw_animation(self, animation_speed: int, save_animation: bool, save_each_frame: bool) -> None:
        if self.__population_data is None:
            raise Exception("You need to iniciate evolution proces first!")

        plotter = Plotter(self.__population_data, self.__bounds, animation_speed)
        plotter.draw_animated_eveloution(self.__generations, save_animation, save_each_frame)

    def export_data(self) -> None:
        if self.__population_data is None:
            raise Exception("You need to iniciate evolution proces first!")

        json_data = json.dumps(self.__population_data)
        f = open("export_data/result.json", "w")
        f.write(json_data)
        f.close()

    def __parse_data(self, current_data: List[List[float]], probes: List[Probe]) -> List[List[float]]:
        list_x = []
        list_y = []
        for probe in probes:
            x, y = probe.get_probe_coordinates()
            list_x.append(x)
            list_y.append(y)
        current_data[0].append(list_x)
        current_data[1].append(list_y)
        return current_data

    def __str__(self):
        return f"Current population: {self.__population}"