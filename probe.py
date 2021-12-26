import math
from typing import Tuple

from converter import Converter


class Probe:
    __chromosome_x: str
    __chromosome_y: str
    __bounds: Tuple[int, int]

    def __init__(self, chromosome_x: str, chromosome_y: str, bounds: Tuple[int, int]):
        self.__bounds = bounds
        self.__chromosome_x = chromosome_x
        self.__chromosome_y = chromosome_y

    def set_chromosome_x(self, chromosome_x:str) -> None:
        self.__chromosome_x = chromosome_x

    def set_chromosome_y(self, chromosome_y:str) -> None:
        self.__chromosome_y = chromosome_y

    def get_chromosomes(self) -> Tuple[str, str]:
        return self.__chromosome_x, self.__chromosome_y

    def get_bit_size(self) -> int:
        return len(self.__chromosome_x)

    def get_bounds(self) -> Tuple[int, int]:
        return self.__bounds

    def calculate_value(self, x: float, y: float) -> float:
        return math.pow(x, 2) + x * y + 2 * x + math.pow(y, 2)

    def get_probe_coordinates(self) -> Tuple[float, float]:
        decoded_x = Converter.gray_to_dec(self.__chromosome_x)
        decoded_y = Converter.gray_to_dec(self.__chromosome_y)
        bit_size = len(self.__chromosome_x)
        left_bound, right_bound = self.__bounds
        old_min = 0
        old_max = (2 ** bit_size) - 1
        new_min = left_bound
        new_max = right_bound 
        rescaled_x = (((decoded_x - old_min) * (new_max - new_min)) / (old_max - old_min)) + new_min 
        rescaled_y = (((decoded_y - old_min) * (new_max - new_min)) / (old_max - old_min)) + new_min
        return rescaled_x, rescaled_y

    def get_genotype_data(self) -> Tuple[float, float, float]:
        rescaled_x, rescaled_y = self.get_probe_coordinates()
        value = self.calculate_value(rescaled_x, rescaled_y)
        return rescaled_x, rescaled_y, value

    def __str__(self):
        return f"Probe: chromosome_x: {self.__chromosome_x} chromosome_y: {self.__chromosome_y}"

    def __repr__(self):
        return f"\nProbe: chromosome_x: {self.__chromosome_x} chromosome_y: {self.__chromosome_y}"