def DeBrujinGraph(k, text):
    graph = {}
    for i in range(len(text) - k + 1):
        prvi_node = text[i:k + i - 1]
        drugi_node = text[i + 1:k + i]
        if prvi_node not in graph.keys():
            graph[prvi_node] = drugi_node
        else:
            graph[prvi_node] += "," + drugi_node
    return graph

input_filename = 'rosalind_ba3d (6).txt'
output_filename = 'output.txt'

with open(input_filename, 'r') as f:
    k = int(f.readline().strip())
    dna = f.readline().strip()

res = DeBrujinGraph(k, dna)

with open(output_filename, 'w') as output_file:
    for key in sorted(res.keys()):
        output_file.write(key + " -> " + res[key] + "\n")
