import csv
import numpy as np

layer_region = open('region_m_20.csv', 'rb')
layer_admrate = open('admrate_m_20.csv', 'rb')
layer_comp = open('comp_m_20.csv', 'rb')
layer_preddeg = open('preddeg_m_20.csv', 'rb')
layer_type = open('type_m_20.csv', 'rb')

regionlist = []
admratelist = []
complist = []
preddeglist = []
typelist = []

sourcelist = []
targetlist = []
totallist = []

i = 0

for row in layer_region:
	row = row.split(' ')
	sourcelist.append(row[0])
	targetlist.append(row[1])
	regionweight = float(row[2])
	regionlist.append(regionweight)


for row in layer_admrate:
	row = row.split(' ')
	admrateweight = float(row[2])
	admratelist.append(admrateweight)


for row in layer_comp:
	row = row.split(' ')
	compweight = float(row[2])
	complist.append(compweight)


for row in layer_preddeg:
	row = row.split(' ')
	preddegweight = float(row[2])
	preddeglist.append(preddegweight)


for row in layer_type:
	row = row.split(' ')
	typeweight = float(row[2])
	typelist.append(typeweight)

layer_type.close()
layer_preddeg.close()
layer_comp.close()
layer_admrate.close()
layer_region.close()

# print len(regionlist)
# print complist[0: 10]
# print len(admratelist)
# print len(complist)
# print len(preddeglist)
# print len(typelist)

totalf = open('../multi/total_20.csv', 'wb')
writertotal = csv.writer(totalf, delimiter = ' ', lineterminator = '\n')
for i in range(0, len(regionlist)):
	totalweight = regionlist[i] + admratelist[i] + complist[i] + preddeglist[i] + typelist[i]
	nodeA = sourcelist[i]
	nodeB = targetlist[i]
	totalresult = [nodeA, nodeB, totalweight/5]
	writertotal.writerow(totalresult)

totalf.close()

