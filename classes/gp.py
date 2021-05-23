import random
import operator
from .member import Member


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


    def calculate_member_distances(self):
        max = 0
        for member in self.population:
            test = member.get_total_route()
            if test > max:
                max = test

        return max

    def sort_population(self):
        self.population.sort(key=operator.attrgetter('route_length'))