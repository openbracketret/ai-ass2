import random
import operator
from .member import Member

import math


class GP:

    def __init__(self, init_population, population_size, generations, elite_perc, mute_rate):

        self.init_population = init_population
        self.population_size = population_size
        self.generations = generations
        self.elite_perc = elite_perc
        self.mute_rate = mute_rate
        temp = []
        for i in range(0, population_size):
            random.shuffle(self.init_population)
            temp.append(Member(list(self.init_population)))
        self.population = temp

        self.current_generation = 1


    def calculate_member_distances(self):
        max = 0
        for member in self.population:
            test = member.get_total_route()
            if test > max:
                max = test

        return max

    def sort_population(self):
        self.population.sort(key=operator.attrgetter('route_length'))

    def get_elites(self):
        total_elites = math.ceil(self.population_size / self.elite_perc)
        return self.population[0:total_elites]

    def get_total_elites(self):
        return math.ceil(self.population_size / self.elite_perc)

    def get_total_mute_rate(self):
        return math.ceil(self.population_size / self.mute_rate)

    def next_generation(self):

        # Mutation first

        for i in range(0, self.get_total_mute_rate()):
            temp_member = random.choice(self.population[self.get_total_elites():])
            temp_member.mutate_route()

        