from exception import Error, RouteNotFound


def calculate(graph, origin, destination):
    if not origin or not destination:
        raise Error("Please input the getting on and off station.")

    shortest_paths = {origin: (None, 0)}
    shortest_paths_without_trip_time = {origin: (None, 0)}
    current_station = origin
    visited_stations = list()
    total_time = 0
    stops_count = 0

    # Find visited stations, shortest paths, and shortest paths without trip time
    while current_station != destination:
        visited_stations.append(current_station)
        available_stations = graph.edges[current_station]
        time_to_current_station = shortest_paths[current_station][1]

        for next_station in available_stations:
            trip_time = (
                graph.times[(current_station, next_station)] + time_to_current_station
            )

            if next_station not in shortest_paths:
                shortest_paths[next_station] = (current_station, trip_time)
                shortest_paths_without_trip_time[next_station] = (
                    current_station,
                    trip_time - time_to_current_station,
                )
            else:
                current_shortest_time = shortest_paths[next_station][1]
                if current_shortest_time > trip_time:
                    shortest_paths[next_station] = (current_station, trip_time)
                    shortest_paths_without_trip_time[next_station] = (
                        current_station,
                        trip_time - time_to_current_station,
                    )

        next_stations = dict()
        for station in shortest_paths:
            if station not in visited_stations:
                next_stations[station] = shortest_paths[station]

        if not next_stations:
            raise RouteNotFound(f"No routes from {origin} to {destination}")

        # Set current station to station with the lowest trip time
        current_station = min(next_stations, key=lambda k: next_stations[k][1])

    # Find stops count and total time used
    while current_station:
        if current_station not in [origin, destination]:
            stops_count += 1
        total_time += shortest_paths_without_trip_time[current_station][1]
        next_station = shortest_paths[current_station][0]
        current_station = next_station
    return stops_count, total_time
