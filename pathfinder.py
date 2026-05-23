import networkx as nx

from routing.city_graph import city_graph

def find_shortest_path(start, end):

    shortest_path = nx.dijkstra_path(
        city_graph,
        start,
        end,
        weight="weight"
    )

    total_distance = nx.dijkstra_path_length(
        city_graph,
        start,
        end,
        weight="weight"
    )

    return {

        "path": shortest_path,
        "distance": total_distance

    }

result = find_shortest_path("A", "E")

print(result)