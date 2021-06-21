from classes.city import City
from classes.member import Member
from classes.gp import GP


def main():

    # Start by reading the file and getting all the lats and longs

    # filename = input("Please input TSP file name: ")

    file = open("wi29.tsp", 'r')

    lines = file.readlines()

    temp = []
    passed_headers = False
    for line in lines:
        test_split = line.split(" ")
        test_split = [x.replace("\n", "") for x in test_split]
        if not passed_headers:
            try:
                test = test_split[0]
                # print(test)
                test = int(test)
                passed_headers = True
            except Exception as _:
                continue
        if len(test_split) == 1:
            continue
        temp.append((float(test_split[1]), float(test_split[2])))

    init_population = []
    for item in temp:
        init_population.append(City(item[0], item[1]))
    TOTAL_GENS = 100
    program = GP(init_population, 50, TOTAL_GENS, 10, 10, 1)

    print(program.calculate_member_distances())
    program.sort_population()
    print("memes")

    for i in range(0, TOTAL_GENS):
        print("Run: {}".format(i))
        program.calculate_member_distances()
        program.sort_population()
        print("Best: {}".format(program.get_best_distance()))
        program.next_generation()


main()