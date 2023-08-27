from ba3f import rosalindInputToGraph,eulerianCycle

def RebalanceGraphFromEulerianPathToCycle(graph):
    from collections import Counter

    graph = graph.copy()

    outbalance = {first: len(graph[first]) for first in graph.keys()}

    new_list = []
    for v in graph.values():
        new_list.extend(v)
    inbalance = Counter(new_list)

    all_nodes = set(list(outbalance.keys()) + list(inbalance.keys()))

    for node in all_nodes:
        balance = outbalance.get(node, 0) - inbalance.get(node, 0)
        if balance == 1:
            second = node
        if balance == -1:
            first = node

    if first not in graph:
        graph[first] = [second]
    else:
        graph[first].append(second)

    return graph, first, second

with open("rosalind_ba3g (1).txt","r")as f:
    inlines = [x.strip() for x in f.readlines()]

graph = rosalindInputToGraph(inlines)

graph, first, second = RebalanceGraphFromEulerianPathToCycle(graph)

cycle = eulerianCycle(graph)

# could be improved ;)
parts = cycle.split(f"{first}->{second}", maxsplit=1)
if parts[0] == '':
    path = parts[1]
elif parts[1] == '':
    path = parts[0]
else:
    part1 = parts[0] + first
    part1_trimmed = part1.split("->", maxsplit=1)[1]
    part2 = second + parts[1]
    path = part2 + "->" + part1_trimmed

print(path)