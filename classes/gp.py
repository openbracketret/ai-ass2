import random
import operator
from .member import Member

import math


class GP:

    def __init__(self, init_population, population_size, generations, elite_perc, mute_rate, crossover_rate):

        self.init_population = init_population
        self.population_size = population_size
        self.generations = generations
        self.elite_perc = elite_perc
        self.mute_rate = mute_rate
        self.crossover_rate = crossover_rate
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
        total_elites = math.ceil((self.mute_rate / self.population_size) * 100)
        return self.population[0:total_elites]

    def get_total_elites(self):
        return math.ceil((self.mute_rate / self.population_size) * 100)

    def get_total_mute_rate(self):
        return math.ceil((self.mute_rate / self.population_size) * 100)

    def get_total_crossover_rate(self):
        return math.ceil((self.crossover_rate / self.population_size) * 100)

    def get_best_distance(self):
        return self.population[0].route_length

    def next_generation(self):

        temp_population = self.get_elites()

        for item in temp_population:
            index = self.population.index(item)
            self.population.pop(index)

        # Mutation first
        for i in range(0, self.get_total_mute_rate()):
            temp_member = random.choice(self.population)
            index = self.population.index(temp_member)
            self.population.pop(index)
            temp_member.mutate_route()
            temp_population.append(temp_member)

        # Crossover
        for i in range(0, self.get_total_crossover_rate()):
            temp_member = random.choice(self.population)
            index = self.population.index(temp_member)
            self.population.pop(index)

            temp_member2 = random.choice(self.population)
            index = self.population.index(temp_member2)
            self.population.pop(index)

            if temp_member.route_length < temp_member2.route_length:
                temp_member.cross_route(temp_member2)
                self.population.append(temp_member2)
                temp_population.append(temp_member)
            else:
                temp_member2.cross_route(temp_member)
                self.population.append(temp_member)
                temp_population.append(temp_member2)


        total_left = self.population_size - self.get_total_elites() - self.get_total_mute_rate()

        for i in range(0, total_left):
            random.shuffle(self.init_population)
            temp_population.append(Member(list(self.init_population)))

        # print("new pop length: {}".format(len(temp_population)))
        self.population = temp_population

        