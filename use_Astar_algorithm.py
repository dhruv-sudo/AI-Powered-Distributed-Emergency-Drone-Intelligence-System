import networkx as nx

from routing.city_graph import city_graph

def heuristic(node1, node2):

    x1, y1 = city_graph.nodes[node1]['pos']

    x2, y2 = city_graph.nodes[node2]['pos']

    return abs(x1 - x2) + abs(y1 - y2)

def a_star_path(start, end):

    path = nx.astar_path(
        city_graph,
        start,
        end,
        heuristic=heuristic,
        weight='weight'
    )

    return path

print(a_star_path("A", "E"))

