import argparse
import csv

from graph import Graph
from calculator import calculate
from exception import Error, RouteNotFound


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", metavar="", help="Route CSV file.", required=True)
    args = parser.parse_args()

    graph = Graph()

    with open(args.file) as routes_file:
        reader = csv.reader(routes_file)
        for row in reader:
            graph.add_edge(row[0], row[1], int(row[2]))

    origin = input("What station are you getting on the train? : ").upper()
    destination = input("What station are you getting off the train? : ").upper()

    try:
        stops_count, total_time = calculate(graph, origin, destination)
        print(
            f"\nYour trip from {origin} to {destination} includes {stops_count} stops and will take {total_time} minutes."
        )
    except RouteNotFound as not_found_ex:
        print(f"\n{not_found_ex}")
    except Error as error_ex:
        print(f"\n{error_ex}")
