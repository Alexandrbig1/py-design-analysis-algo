import networkx as nx

def create_logistics_network():
    G = nx.DiGraph()

    edges = [
        ('Terminal 1', 'Warehouse 1', 25), ('Terminal 1', 'Warehouse 2', 20), ('Terminal 1', 'Warehouse 3', 15),
        ('Terminal 2', 'Warehouse 3', 15), ('Terminal 2', 'Warehouse 4', 30), ('Terminal 2', 'Warehouse 2', 10),
        ('Warehouse 1', 'Store 1', 15), ('Warehouse 1', 'Store 2', 10), ('Warehouse 1', 'Store 3', 20),
        ('Warehouse 2', 'Store 4', 15), ('Warehouse 2', 'Store 5', 10), ('Warehouse 2', 'Store 6', 25),
        ('Warehouse 3', 'Store 7', 20), ('Warehouse 3', 'Store 8', 15), ('Warehouse 3', 'Store 9', 10),
        ('Warehouse 4', 'Store 10', 20), ('Warehouse 4', 'Store 11', 10), ('Warehouse 4', 'Store 12', 15),
        ('Warehouse 4', 'Store 13', 5), ('Warehouse 4', 'Store 14', 10)
    ]

    for u, v, capacity in edges:
        G.add_edge(u, v, capacity=capacity)

    G.add_node('Sink')
    for i in range(1, 15):
        G.add_edge(f'Store {i}', 'Sink', capacity=float('inf'))

    return G


def compute_max_flow(G, source, sink):
    return nx.maximum_flow(G, source, sink)


if __name__ == "__main__":
    G = create_logistics_network()
    source = 'Terminal 1'
    sink = 'Sink'
    flow_value, flow_dict = compute_max_flow(G, source, sink)

    print(f"Maximum flow: {flow_value}")
    print("Flow distribution across edges:")
    for u, flows in flow_dict.items():
        for v, f in flows.items():
            if f > 0:
                print(f"{u} -> {v}: {f}")
