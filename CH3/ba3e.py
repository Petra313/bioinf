def DeBrujinGraph( text):
    graph = {}
    for i in text:
        prvi_node = i[:- 1]
        drugi_node = i[1:]
        if prvi_node not in graph.keys():
            graph[prvi_node] = drugi_node
        else:
            graph[prvi_node] += "," + drugi_node
    return graph

input_filename = 'rosalind_ba3e.txt'
output_filename = 'output.txt'

with open(input_filename,'r') as f:
    X = f.readlines()
    dna = [i.rstrip('\n') for i in X]


res = DeBrujinGraph( dna)

with open(output_filename, 'w') as output_file:
    for key in sorted(res.keys()):
        output_file.write(key + " -> " + res[key] + "\n")
