from typing import List, Tuple

import matplotlib.pyplot as plt
import numpy as np


class Plotter:
    fig: object
    ax: List[object]
    arguments: List[float]
    values: List[float]
    bounds: Tuple[int, int]
    animation_speed: float
    X: List[float]
    Y: List[float]
    V: List[float]

    def __init__(self, data: List[List[float]], bounds: Tuple[int, int], animation_speed: float):
        self.fig, self.ax = plt.subplots()
        self.arguments, self.values = self.parse_data(data)
        self.animation_speed = animation_speed
        self.bounds = bounds
        left_bound, right_bound = bounds
        map_x = np.linspace(left_bound, right_bound)
        map_y = np.linspace(left_bound, right_bound)
        self.X, self.Y = np.meshgrid(map_x, map_y)
        self.V = np.power(self.X, 2) + self.X * self.Y + 2 * self.X + np.power(self.Y, 2)

    def draw_animated_eveloution(self, generations: int) -> None:
        for i in range(generations):
            self.draw_frame(i)

    def draw_frame(self, generation: int) -> None:
        plt.cla()
        self.draw_background(generation)
        plt.xlabel("variable x")
        plt.ylabel("variable y")
        left_bound, right_bound = self.bounds
        plt.xlim([left_bound, right_bound])
        plt.ylim([left_bound, right_bound])
        plt.scatter(self.arguments[generation][1], self.values[generation][1], marker="s", c='b', label="parents")
        plt.scatter(self.arguments[generation][2], self.values[generation][2], marker="^", c='g', label="offsprings")
        plt.scatter(self.arguments[generation][0], self.values[generation][0], marker="*", c='r', label="best probe")
        plt.legend()
        plt.pause(self.animation_speed)

    def draw_background(self, generation: int) -> None:
        CS = self.ax.contour(self.X, self.Y, self.V)
        self.ax.clabel(CS, inline=True, fontsize=10)
        self.ax.set_title(f"Generation: {generation}")

    def parse_data(self, data: List[List[float]]) -> Tuple[List[float], List[float]]:
        arguments = []
        values = []
        for single_generation in data:
            list_x, list_y = single_generation
            arguments.append(list_x)
            values.append(list_y)
        return arguments, values