from igraph import *
import cairo
import louvain 
from random import randint


admrate_igraph = Graph.Read_Ncol("2013_admrate_igraph_test.csv", directed = False, names = True, weights = True)


# for vertex in admrate_igraph.vs():
# 	print vertex.index, vertex["name"]

# for edge in admrate_igraph.es():
# 	print edge.tuple[0], edge["weight"]


part = louvain.find_partition(admrate_igraph, method = 'Modularity', weight = 'weight')
membership = part.membership
print max(membership)
# for edge in admrate_igraph.es():
# 	print edge.tuple[0], membership[edge.tuple[0]]
 
# part.significance = louvain.quality(admrate_igraph, partition, method='Significance')

# layout = admrate_igraph.layout("kk")
# plot(admrate_igraph, "admrate_graph.pdf", layout = layout)

if membership is not None:
	admrate_copy = admrate_igraph.copy()
	edges = []
	colors = []
	edges_color = []

	for i in range(0, max(membership)+1):
		colors.append('%06X' % randint(0, 0xFFFFFF))

	for edge in admrate_igraph.es():
		if membership[edge.tuple[0]] != membership[edge.tuple[1]]:
			edges.append(edge)
			edges_color.append("gray")
		else:
			edges_color.append(str('#') + colors[membership[edge.tuple[0]]])
	admrate_copy.delete_edges(edges)
	layout = admrate_copy.layout("kk")
	admrate_igraph.es["color"] = edges_color
else:
	layout = admrate_igraph.layout("kk")
	admrate_igraph.es["color"] = "gray"


visual_style = {}
visual_style["vertex_label_dist"] = 0
visual_style["vertex_shape"] = "circle"
visual_style["edge_color"] = admrate_igraph.es["color"]
visual_style["vertex_size"] = 23
visual_style["layout"] = layout
visual_style["bbox"] = (1024, 768)
visual_style["margin"] = 40
# visual_style["edge_label"] = admrate_igraph.es["weight"]


for vertex in admrate_igraph.vs():
	# vertex["label"] = vertex["name"]
	vertex["label"] = vertex.index

if membership is not None:
	for vertex in admrate_igraph.vs():
		vertex["color"] = str('#') + colors[membership[vertex.index]]
	visual_style["vertex_color"] = admrate_igraph.vs["color"]

plot(admrate_igraph, **visual_style)
