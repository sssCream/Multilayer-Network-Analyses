import csv
import numpy as np
from igraph import *

data = open('merged_2013_PP.csv', 'rb')

# unitid --> institution name
id_to_inst = dict()

# unitid --> predominant degree awarded
id_to_preddeg = dict()

# unitid --> control (public, private nonprofit, private for-profit)
id_to_control = dict()

# unitid --> state FIPS (1: ALabama, 2: Alaska ...)
id_to_stfips = dict()

# unitid --> region (integer denotes region, i.e. mid east ...)
id_to_region = dict()

# unitid --> ccsizset (setting and size)
id_to_ccsizset = dict()

# unitid --> admrate (admission rate)
id_to_admrate = dict()

# unitid --> sat_avg (average admitted SAT score)
id_to_sat = dict()

# unitid --> online_only
id_to_distanceonly = dict()

# unitid --> undergraduate degree seeking (size)
id_to_ugds = dict()

# unitid --> white (percentage of white)
id_to_white = dict()

# unitid --> black (percentage of black)
id_to_black = dict()

# unitid --> hispanic (percentage of hispanic)
id_to_hispanic = dict()

# unitid --> asian (percentage of asian)
id_to_asian = dict()

# unitid --> Average cost of attendance (academic year institutions) COSTT4_A
id_to_acacost = dict()

# unitid --> Average cost of attendance (program-year institutions) COSTT4_P
id_to_procost = dict()

# unitid --> percentatge of undergraduate students receive a Pell Grant PCTPELL
id_to_pctpell = dict()

# Completion rate for first-time, full-time students at four-year institutions C150_4
id_to_comp = dict()

# Dictionary contains all attributes above
id_to_attr = dict()


idlist = []
preddeglist = []
instlist = []
typelist = []
stfipslist = []
regionlist = []
admratelist = []
satlist = []
distanceonlylist = []
pctpelllist = []
complist = []

next(data)
# i = 0
for row in data:
	# i = i + 1
	row = row.split(',')
	unitid = row[0]
	inst = row[3]
	preddeg = row[14]
	control = row[16]
	stfips = row[17]
	region = row[18]
	ccsizset = row[25]
	admrate = row[36]
	sat = row[59]
	distanceonly = row[289]
	ugds = row[290]
	white = row[292]
	black = row[293]
	hispanic = row[294]
	asian = row[295]
	acacost = row[376]
	procost = row[377]
	pctpell = row[385]
	comp = row[386]

	# Genarate list of each attribute for colleges in unitid order 
	idlist.append(unitid)
	instlist.append(inst)
	stfipslist.append(stfips)
	admratelist.append(admrate)
	regionlist.append(region)
	satlist.append(sat)
	typelist.append(control)
	preddeglist.append(preddeg)
	distanceonlylist.append(distanceonly)
	pctpelllist.append(pctpell)
	complist.append(comp)


	# # Obtain dictionary of ('UNIT_ID', one attribute)
	# id_to_inst[unitid] = inst
	# id_to_preddeg[unitid] = preddeg
	# id_to_control[unitid] = control
	# id_to_stfips[unitid] = stfips
	# id_to_region[unitid] = region
	# id_to_ccsizset[unitid] = ccsizset
	# id_to_admrate[unitid] = admrate
	# id_to_sat[unitid] = sat
	# id_to_distanceonly[unitid] = distanceonly
	# id_to_ugds[unitid] = ugds
	# id_to_white[unitid] = white
	# id_to_black[unitid] = black
	# id_to_hispanic[unitid] = hispanic
	# id_to_asian[unitid] = asian
	# id_to_acacost[unitid] = acacost
	# id_to_procost[unitid] = procost
	# id_to_pctpell[unitid] = pctpell
	# id_to_comp[unitid] = comp

	
	# OR Obtain dictionary of ('UNIT_ID', all selected attributes)
	id_to_attr[unitid] = [inst, preddeg, control, stfips, region, ccsizset, admrate, sat, distanceonly, ugds, white, black, hispanic, asian, acacost, procost, pctpell, comp]

data.close()

# mat = np.zeros((len(regionlist), len(regionlist)))
# print id_to_region.items()[0:20]
# print id_to_sat.items()[0:20]

# # Genarate edgelist file for region attribute 
# regionf = open('2013_region.csv', 'wb')
# writerregion = csv.writer(regionf, delimiter = ',', lineterminator = '\n')
# for i in range(0, len(regionlist)-1):
# 	for j in range(i+1,len(regionlist)):
# 		if regionlist[i] == regionlist[j]:
# 			# mat[i][j] = 1
# 			regionresult = [idlist[i], idlist[j]]
# 			writerregion.writerow(regionresult)
# 	# print mat[i]
# regionf.close()


# # Genarate edgelist file for stateID attribute
# stfipsf = open('2013_stfips.csv', 'wb')
# writerstfips = csv.writer(stfipsf, delimiter = ',', lineterminator = '\n')
# for i in range(0,len(stfipslist)-1):
# 	for j in range(i+1,len(stfipslist)):
# 		if stfipslist[i] == stfipslist[j]:
# 			stfipsresult = [idlist[i], idlist[j]]
# 			writerstfips.writerow(stfipsresult)
# stfipsf.close()


# # Genarate edgelist file for admission rate attribute read by gephi
# admratef = open('2013_admrate.csv', 'wb')
# writeradmrate = csv.writer(admratef, delimiter = ',', lineterminator = '\n')
# #writeradmrate.writerow(["Source", "Target", "Weight"])
# for i in range(0,len(admratelist)-1):
# 	if admratelist[i] != 'NULL':
# 		for j in range(i+1,len(admratelist)):
# 			if admratelist[j] != 'NULL':
# 				admratesimilarity = 1 - abs(float(admratelist[i]) - float(admratelist[j]))
# 				admrateresult = [idlist[i], idlist[j], admratesimilarity]
# 				writeradmrate.writerow(admrateresult)
# admratef.close()


# # Genarate edgelist and weight file for admission rate attribute read by IGraph
# admratef = open('2013_admrate_igraph.csv', 'wb')
# writeradmrate = csv.writer(admratef, delimiter = ' ', lineterminator = '\n')
# for i in range(0,len(admratelist)-1):
# 	if admratelist[i] != 'NULL':
# 		for j in range(i+1,len(admratelist)):
# 			if admratelist[j] != 'NULL':
# 				admratesimilarity = 1 - abs(float(admratelist[i]) - float(admratelist[j]))
# 				admrateresult = [idlist[i], idlist[j], admratesimilarity]
# 				writeradmrate.writerow(admrateresult)
# admratef.close()


# # Genarate edgelist file for average accepted SAT attribute
# satf = open('2013_sat.csv', 'wb')
# writersat = csv.writer(satf, delimiter = ',', lineterminator = '\n')
# for i in range(0,len(satlist)-1):
# 	if satlist[i] != 'NULL':
# 		for j in range(i+1,len(satlist)):
# 			if satlist[j] != 'NULL':
# 				satsimilarity = 1600 - abs(float(satlist[i]) - float(satlist[j]))
# 				satresult = [idlist[i], idlist[j], satsimilarity]
# 				writersat.writerow(satresult)
# satf.close()


# typef = open('2013_type.csv', 'wb')
# writertype = csv.writer(typef, delimiter = ',', lineterminator = '\n')
# for i in range(0,len(typelist)-1, 20):
# 	for j in range(i+1,len(typelist), 20):
# 		if typelist[i] == typelist[j]:
# 			typeresult = [idlist[i], idlist[j]]
# 			writertype.writerow(typeresult)
# typef.close()


distanceonlyf = open('2013_distanceonly.csv', 'wb')
writerdistanceonly = csv.writer(distanceonlyf, delimiter = ',', lineterminator = '\n')
for i in range(0, len(distanceonlylist)-1):
	for j in range(i+1,len(distanceonlylist)):
		if distanceonlylist[i] == distanceonlylist[j]:
			distanceonlyresult = [idlist[i], idlist[j]]
			writerdistanceonly.writerow(distanceonlyresult)
distanceonlyf.close()


preddegf = open('2013_preddeg.csv', 'wb')
writerpreddeg = csv.writer(preddegf, delimiter = ',', lineterminator = '\n')
for i in range(0, len(preddeglist)-1):
	for j in range(i+1,len(preddeglist)):
		if preddeglist[i] == preddeglist[j]:
			preddegresult = [idlist[i], idlist[j]]
			writerpreddeg.writerow(preddegresult)
preddegf.close()


# Genarate edgelist and weight file for completion rate of first-time four-year full graduation
compf = open('2013_comp.csv', 'wb')
writercomp = csv.writer(compf, delimiter = ',', lineterminator = '\n')
for i in range(0,len(complist)-1):
	if complist[i] != 'NULL':
		for j in range(i+1,len(complist)):
			if complist[j] != 'NULL':
				compsimilarity = 1 - abs(float(complist[i]) - float(complist[j]))
				compresult = [idlist[i], idlist[j], compsimilarity]
				writercomp.writerow(compresult)
compf.close()


# Genarate edgelist and weight file for percentatge of undergraduate students receive a Pell Grant
pctpellf = open('2013_pctpell.csv', 'wb')
writerpctpell = csv.writer(pctpellf, delimiter = ',', lineterminator = '\n')
for i in range(0,len(pctpelllist)-1):
	if pctpelllist[i] != 'NULL':
		for j in range(i+1,len(pctpelllist)):
			if pctpelllist[j] != 'NULL':
				pctpellsimilarity = 1 - abs(float(pctpelllist[i]) - float(pctpelllist[j]))
				pctpellresult = [idlist[i], idlist[j], pctpellsimilarity]
				writerpctpell.writerow(pctpellresult)
pctpellf.close()

#print id_to_attr
#print type(id_to_attr)
#print len(id_to_attr)
#print mat[0:5][0:5]
