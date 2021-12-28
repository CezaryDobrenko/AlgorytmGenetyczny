from typing import List, Tuple

import matplotlib.pyplot as plt
import numpy as np
import imageio
import os


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

    def draw_animated_eveloution(self, generations: int, save_animation: bool, save_each_frame: bool) -> None:
        for i in range(generations):
            self.draw_frame(i)
        if save_animation:
            self.__export_animation(generations)
        if not save_each_frame:
            self.__save_each_frame(generations)

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
        plt.savefig(f"frames/{generation}.png")

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

    def __export_animation(self, generations: int) -> None:
            with imageio.get_writer('animations/result.gif', mode='I') as writer:
                for generation in range(generations):
                    image = imageio.imread(f"frames/{generation}.png")
                    writer.append_data(image)

    def __save_each_frame(self, generations: int) -> None:
        for generation in range(generations):
            os.remove(f"frames/{generation}.png")
