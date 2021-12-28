import random
from typing import Tuple

from converter import Converter
from probe import Probe


class Mutator:

    @staticmethod
    def execute_mutations(probe: Probe, settings: dict) -> Probe:
        if settings.get("single_point_mutation"):
            probe = Mutator.single_point_mutation(probe)
        if settings.get("swap_mutation"):
            probe = Mutator.swap_mutation(probe)
        if settings.get("scramble_mutation"):
            probe = Mutator.scramble_mutation(probe)
        if settings.get("reverse_mutation"):
            probe = Mutator.reverse_mutation(probe)
        if settings.get("full_random_mutation"):
            probe = Mutator.full_random_mutation(probe)
        return probe

    @staticmethod
    def single_point_mutation(probe: Probe) -> Probe:
        bit_size = probe.get_bit_size()
        random_bit_x =  random.randrange(0, bit_size)
        random_bit_y =  random.randrange(0, bit_size)
        p_chromosome_x, p_chromosome_y = probe.get_chromosomes()
        probe.set_chromosome_x(Mutator.__inverse_bit(p_chromosome_x, random_bit_x))
        probe.set_chromosome_y(Mutator.__inverse_bit(p_chromosome_y, random_bit_y))
        return probe

    @staticmethod
    def full_random_mutation(probe: Probe) -> Probe:
        bit_size = probe.get_bit_size()
        max_unsigned_int = (2 ** bit_size) - 1
        x = random.randrange(0, max_unsigned_int)
        y = random.randrange(0, max_unsigned_int)
        encoded_x = Converter.dec_to_gray(x, bit_size)
        encoded_y = Converter.dec_to_gray(y, bit_size)
        probe.set_chromosome_x(encoded_x)
        probe.set_chromosome_y(encoded_y)
        return probe

    @staticmethod
    def scramble_mutation(probe: Probe) -> Probe:
        chromosome_x, chromosome_y = probe.get_chromosomes()
        bit_size = probe.get_bit_size()
        start_bit_x = random.randrange(0, bit_size)
        end_bit_x = random.randrange(0, bit_size)
        start_bit_y = random.randrange(0, bit_size)
        end_bit_y = random.randrange(0, bit_size)
        new_chromosome_x = Mutator.__swap_bits(chromosome_x, start_bit_x, end_bit_x)
        new_chromosome_y = Mutator.__swap_bits(chromosome_y, start_bit_y, end_bit_y)
        probe.set_chromosome_x(new_chromosome_x)
        probe.set_chromosome_y(new_chromosome_y)
        return probe

    @staticmethod
    def reverse_mutation(probe: Probe) -> Probe:
        chromosome_x, chromosome_y = probe.get_chromosomes()
        bit_size = probe.get_bit_size()
        start_bit_x = random.randrange(0, bit_size)
        end_bit_x = random.randrange(0, bit_size)
        start_bit_y = random.randrange(0, bit_size)
        end_bit_y = random.randrange(0, bit_size)
        new_chromosome_x = Mutator.__reverse_bits(chromosome_x, start_bit_x, end_bit_x)
        new_chromosome_y = Mutator.__reverse_bits(chromosome_y, start_bit_y, end_bit_y)
        probe.set_chromosome_x(new_chromosome_x)
        probe.set_chromosome_y(new_chromosome_y)
        return probe

    @staticmethod
    def swap_mutation(probe: Probe) -> Probe:
        chromosome_x, chromosome_y = probe.get_chromosomes()
        bit_size = probe.get_bit_size()
        start_bit_x = random.randrange(0, bit_size)
        end_bit_x = random.randrange(0, bit_size)
        start_bit_y = random.randrange(0, bit_size)
        end_bit_y = random.randrange(0, bit_size)
        new_chromosome_x = Mutator.__scramble_bits(chromosome_x, start_bit_x, end_bit_x)
        new_chromosome_y = Mutator.__scramble_bits(chromosome_y, start_bit_y, end_bit_y)
        probe.set_chromosome_x(new_chromosome_x)
        probe.set_chromosome_y(new_chromosome_y)
        return probe

    @staticmethod
    def cross_over_mutation(base_parent1: Probe, base_parent2: Probe) -> Probe:
        bit_size = base_parent1.get_bit_size()
        bounds = base_parent1.get_bounds()
        cross_point =  random.randrange(0, bit_size)
        p1_chromosome_x, p1_chromosome_y = base_parent1.get_chromosomes()
        p2_chromosome_x, p2_chromosome_y = base_parent2.get_chromosomes()
        c_chromosome_x = f"{p1_chromosome_x[0:cross_point]}{p2_chromosome_x[cross_point:]}"
        c_chromosome_y = f"{p1_chromosome_y[0:cross_point]}{p2_chromosome_y[cross_point:]}"
        children = Probe(c_chromosome_x, c_chromosome_y, bounds)
        return children

    def __reverse_bits(chromosome: str, index_1: int, index_2: int) -> str:
        start_index, end_index = Mutator.__compare_index(index_1, index_2)
        list_of_bits = [bit for bit in chromosome]
        selected_bits = [list_of_bits[i] for i in range(start_index, end_index)]
        reversed_bits = selected_bits[::-1]
        next_bit_index = 0
        for i in range (start_index, end_index):
            list_of_bits[i] = reversed_bits[next_bit_index]
            next_bit_index += 1
        return "".join(list_of_bits)

    def __scramble_bits(chromosome: str, index_1: int, index_2: int) -> str:
        start_index, end_index = Mutator.__compare_index(index_1, index_2)
        list_of_bits = [bit for bit in chromosome]
        selected_bits = [list_of_bits[i] for i in range(start_index, end_index)]
        random.shuffle(selected_bits)
        next_bit_index = 0
        for i in range (start_index, end_index):
            list_of_bits[i] = selected_bits[next_bit_index]
            next_bit_index += 1
        return "".join(list_of_bits)

    def __swap_bits(chromosome: str, index_1: int, index_2: int) -> str:
        list_of_bits = [bit for bit in chromosome]
        list_of_bits[index_1] = chromosome[index_2]
        list_of_bits[index_2] = chromosome[index_1]
        return "".join(list_of_bits)

    def __inverse_bit(chromosome: str, index: int) -> str:
        if chromosome[index] == "1":
            replace_bit = 0
        else:
            replace_bit = 1
        return f"{chromosome[:index]}{replace_bit}{chromosome[index+1:]}"

    def __compare_index(index_1: int, index_2: int) -> Tuple[int, int]:
        if index_1 > index_2:
            start_index = index_2
            end_index = index_1
        else:
            start_index = index_1
            end_index = index_2
        return start_index, end_index