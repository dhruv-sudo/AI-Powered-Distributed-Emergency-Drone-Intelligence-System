import networkx as nx

city_graph = nx.Graph()

locations = {

    "A": (0, 0),
    "B": (2, 4),
    "C": (5, 1),
    "D": (7, 7),
    "E": (10, 3)

}

for node, coords in locations.items():

    city_graph.add_node(
        node,
        pos=coords
    )

roads = [

    ("A", "B", 5),
    ("A", "C", 7),
    ("B", "D", 6),
    ("C", "D", 3),
    ("D", "E", 4)

]

for source, destination, distance in roads:

    city_graph.add_edge(
        source,
        destination,
        weight=distance
    )