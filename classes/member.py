class Member:

    def __init__(self, route):
        self.route = route # List of cities defining the route
        self.route_length = 0

    def get_total_route(self):

        temp_total = 0

        for i in range(0, len(self.route)):
            if i == len(self.route) - 1:
                temp = self.route[i].get_distance(self.route[0])
            else:
                temp = self.route[i].get_distance(self.route[i + 1])
            
            temp_total += temp

        self.route_length = temp_total
        return self.route_length

