from igraph import * 

region_igraph = Graph.Read_Ncol('2013_region.csv', directed = False, weights = False)

layout = region_igraph.layout("kk")
plot(region_igraph, "region_graph.pdf", layout = layout)