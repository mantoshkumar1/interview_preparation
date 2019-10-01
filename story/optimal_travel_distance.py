"""
For a truck, forward and backward shipping routes are provided. Also the max distance the truck could operate is
also given. The forward and backward shipping routes is a list of pair of integers where first int represents
the unique shipping route and the second int represents the amount of travel distance required by this shipping
route.

Optimise the total operating time distance of the truck. A forward/return shipping route is considered to be
optimal if there does not exist another pair that has a higher operating travel distance than this pair, and
also has a total less than or equal to the maximum operating travel distance of the truck.

Find a list of pairs of integers representing the pairs of IDs of forward and backward shipping routes that
optimally utilize the truck. If no route is possible, return an empty list.
"""


class Route:
    def __init__(self, forward_route_id, forward_route_weight, backward_route_id, backward_route_weight):
        self.forward_route_id = forward_route_id
        self.forward_route_weight = forward_route_weight
        self.backward_route_id = backward_route_id
        self.backward_route_weight = backward_route_weight

    def get_total_route_weight(self):
        return self.forward_route_weight + self.backward_route_weight

    def __eq__(self, other):
        return self.get_total_route_weight() == other.get_total_route_weight()

    def __ne__(self, other):
        return self.get_total_route_weight() != other.get_total_route_weight()

    def __lt__(self, other):
        return self.get_total_route_weight() < other.get_total_route_weight()

    def __le__(self, other):
        return self.get_total_route_weight() <= other.get_total_route_weight()

    def __gt__(self, other):
        return self.get_total_route_weight() > other.get_total_route_weight()

    def __ge__(self, other):
        return self.get_total_route_weight() >= other.get_total_route_weight()


class Solution:
    def update_optimal_route(self, optimal_routes, route):
        if not optimal_routes:
            optimal_routes.append(route)
            return optimal_routes

        last_optimal_route = optimal_routes[-1]

        if last_optimal_route > route:
            return optimal_routes

        if last_optimal_route == route:
            optimal_routes.append(route)
            return optimal_routes

        return [route]

    def optimal_distance_utilization(self, maxTravelDist, forwardRouteList, returnRouteList):
        optimal_routes = []

        for f_route_id, f_weight in forwardRouteList:
            for b_route_id, b_weight in returnRouteList:
                if f_weight + b_weight > maxTravelDist:
                    continue

                route = Route(f_route_id, f_weight, b_route_id, b_weight)
                optimal_routes = self.update_optimal_route(optimal_routes, route)

        optimal_routes = list(map(lambda x: [x.forward_route_id, x.backward_route_id], optimal_routes))
        return optimal_routes


s = Solution()

forwardRouteList = [[1, 3000], [2, 5000], [3, 7000], [4, 10000]]
returnRouteList = [[1, 2000], [2, 3000], [3, 4000], [4, 5000]]
assert [] == s.optimal_distance_utilization(10, forwardRouteList, returnRouteList)

forwardRouteList = [[1, 3000], [2, 5000], [3, 7000], [4, 10000]]
returnRouteList = [[1, 2000], [2, 3000], [3, 4000], [4, 5000]]
assert [[2, 4], [3, 2]] == s.optimal_distance_utilization(10000, forwardRouteList, returnRouteList)

forwardRouteList = [[1, 2000], [2, 4000], [3, 6000]]
returnRouteList = [[1, 2000]]
assert [[2, 1]] == s.optimal_distance_utilization(7000, forwardRouteList, returnRouteList)
