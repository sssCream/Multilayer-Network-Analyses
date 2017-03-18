import igraph

def detect_communities():
    # load data into a graph
    g = igraph.Graph.Read_Ncol('final.txt')

    dendrogram = g.community_walktrap()

    num_communities = dendrogram.optimal_count

    clusters = dendrogram.as_clustering()

    membership = clusters.membership

    import csv
    from itertools import izip

    writer = csv.writer(open("output.txt", "wb"))
    nodes = []
    for name, membership in izip(g.vs["name"], membership):
        nodes.append((membership, name))

    nodes = sorted(nodes)

    for node in nodes:
        writer.writerow([node[0], node[1]])

    return num_communities

def add_vertices_to_file(current_community, vertex_list, last):
    n = len(vertex_list)
    fo=open('json_file.txt','a')
    parent_string = '{\n\t\t"id": "' + current_community + '",\n\t\t"name": "' + current_community + '",\n\t\t"size": 10,\n\t\t"children": [' 
    fo.write(parent_string)
    for i,vertex in enumerate(vertex_list):
        child_string = ''
        if i == (n-1):
            child_string = '{\n\t\t\t"id": "' + vertex + '",\n\t\t\t"name": "' + vertex + '",\n\t\t\t"size": 10\n\t\t}]'
        else:
            child_string = '{\n\t\t\t"id": "' + vertex + '",\n\t\t\t"name": "' + vertex + '",\n\t\t\t"size": 10\n\t\t},'
        fo.write(child_string)
    if last:
        fo.write('\n}]}')
    else:
        fo.write('\n},')
    fo.close()

def create_file(n):
    count = 0
    f = open('output.txt', 'r')

    current_community = ''
    vertex_list = []
    for line in f:
            count += 1
            last = False
            line = str(line)
            line = line.strip()
            (community, vertex) = line.split(",")
            if current_community != community:
                if current_community != '':
                    add_vertices_to_file(current_community, vertex_list, last)
                current_community = community
                vertex_list = []
            vertex_list.append(vertex)
    last = True
    add_vertices_to_file(current_community, vertex_list, last)
                
n = detect_communities()
create_file(n)
 
