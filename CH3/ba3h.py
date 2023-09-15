with open('./rosalind_ba3h (1).txt','r') as f:
    k=int(f.readline().strip())
    X = f.readlines()
    dna = [i.rstrip('\n') for i in X]

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



res = DeBrujinGraph( dna)
print(res)
string=''
key=''
for re in res.keys():
    if re not in res.values():
        string=re
        key=re
while key in res:
    string += res[key][-1]
    key = string[-k+1:]

print(string)
#with open(output_filename, 'w') as output_file:
   # for key in sorted(res.keys()):
       # output_file.write(key + " -> " + res[key] + "\n")
