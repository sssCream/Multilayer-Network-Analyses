mydata13 = read.csv("MERGED2013_PP.csv") 
student=subset(mydata13, select=c(UNITID,INSTNM,HBCU,PBI,ANNHI,TRIBAL,AANAPII,HSI,NANTI,MENONLY,WOMENONLY,RELAFFIL,NPT41_PUB,NPT42_PUB,NPT43_PUB,NPT44_PUB,NPT45_PUB,NPT41_PRIV,NPT42_PRIV,NPT43_PRIV,NPT44_PRIV,NPT45_PRIV,NPT41_PROG,NPT42_PROG,NPT43_PROG,NPT44_PROG,NPT45_PROG,NPT41_OTHER,NPT42_OTHER,NPT43_OTHER,NPT44_OTHER,NPT45_OTHER,NUM41_PUB,NUM42_PUB,NPT4_048_PROG, NPT4_048_OTHER, NPT4_3075_PUB, NPT4_3075_PRIV, NPT4_75UP_PUB, NPT4_75UP_PRIV, NPT4_3075_PROG, NPT4_3075_OTHER, NPT4_75UP_PROG, NPT4_75UP_OTHER, NUM4_PUB, NUM4_PRIV, NUM4_PROG, NUM4_OTHER, NUM41_PUB, NUM42_PUB, NUM43_PUB, NUM44_PUB, NUM45_PUB, NUM41_PRIV, NUM42_PRIV, NUM43_PRIV, NUM44_PRIV, NUM45_PRIV, NUM41_PROG, NUM42_PROG, NUM43_PROG, NUM44_PROG, NUM45_PROG, NUM41_OTHER, NUM42_OTHER, NUM43_OTHER, NUM44_OTHER, NUM45_OTHER, TUITFTE,INEXPFTE,C150_4_BLACK,C150_4_HISP,C150_4_ASIAN,C150_4_AIAN,C150_4_NHPI,C150_4_2MOR,C150_4_NRA,C150_4_UNKN,C150_4_WHITENH,C150_4_BLACKNH,C150_L4_HISPOld, RET_FT4, RET_FTL4, RET_PT4, RET_PTL4))
student1000 <- tail(student,n=1000)

student=subset(student, select=-c(81))
student=subset(student, select=-c(78,79,80))
student=subset(student, select=-c(23,24,25,26,27,28,29,30,31,32))

student=subset(mydata13, select=c(INSTNM,NUM41_PUB,NUM42_PUB,NUM43_PUB,NUM44_PUB,NUM45_PUB))
require(apcluster)
require(proxy)
wo_null <- mydata13[grep("NULL", student$NUM41_PUB, invert = TRUE),]
Jaccard_dist <- simil(student, method = "euclidean")
stud1=subset(student,  !is.null(NUM41_PUB))

for(i in 1:3)
{
  stud=subset(student,  as.numeric(NUM41_PUB)==i)
  stud1=rbind(stud1,stud);
}
str(student)
field=c(UNITID,INSTNM,HBCU,PBI,ANNHI,TRIBAL,AANAPII,HSI,NANTI,MENONLY,WOMENONLY,NPT41_PUB,NPT42_PUB,NPT43_PUB,NPT44_PUB,NPT45_PUB,NUM41_PUB,NUM42_PUB, NUM41_PUB, NUM42_PUB, NUM43_PUB, NUM44_PUB,C150_4_BLACK,C150_4_HISP,C150_4_ASIAN,C150_4_AIAN,C150_4_2MOR, RET_PT4)
student=subset(mydata13, select=c(UNITID,INSTNM,HBCU,PBI,ANNHI,TRIBAL,AANAPII,HSI,NANTI,MENONLY,WOMENONLY,NPT41_PUB,NPT42_PUB,NPT43_PUB,NPT44_PUB,NPT45_PUB,NUM41_PUB,NUM42_PUB, NUM41_PUB, NUM42_PUB, NUM43_PUB, NUM44_PUB,C150_4_BLACK,C150_4_HISP,C150_4_ASIAN,C150_4_AIAN,C150_4_2MOR, RET_PT4))
field=c("UNITID") /#,"INSTNM","HBCU","PBI","ANNHI","TRIBAL");#,"AANAPII","HSI","NANTI","MENONLY","WOMENONLY","NPT41_PUB","NPT42_PUB","NPT43_PUB","NPT44_PUB","NPT45_PUB","NUM41_PUB","NUM42_PUB"," NUM41_PUB"," NUM42_PUB"," NUM43_PUB"," NUM44_PUB","C150_4_BLACK","C150_4_HISP","C150_4_ASIAN","C150_4_AIAN","C150_4_2MOR"," RET_PT4")
wo_null=student
for(i in field)
{
  print (i);
  wo_null <- wo_null[grep("NULL", paste("wo_null$",i,sep=""), invert = TRUE),]
}
black_lis=matrix(,nrow=2355538,ncol=3)
black=subset(mydata13,select=c("UNITID","C150_4_BLACK"))
black=black[grep("NULL", black$C150_4_BLACK, invert = TRUE),]
black=head(black,500)
black_list_row=1
for(i in 1:500)
{
  for(j in (i+1):500)
  {
    black_lis[black_list_row,1]=black[i,1];
    black_lis[black_list_row,2]=black[j,1];
    black_lis[black_list_row,3]=1-as.numeric(as.character(sub("," , ".",black[i,2] )))-as.numeric(as.character(sub("," , ".",black[j,2] )));
    black_list_row=black_list_row+1;
  }
} 
black_graph=data.frame(black_lis)
black_graph=subset(black_graph,X3>0.7)
black_graph=head(black_graph, n=5000)
write.csv(black_graph, file = "black_edgelist.csv",row.names=FALSE)
#field=c("UNITID","INSTNM","HBCU","PBI","ANNHI","TRIBAL","AANAPII","HSI","NANTI","MENONLY","WOMENONLY","NPT41_PUB","NPT42_PUB","NPT43_PUB","NPT44_PUB","NPT45_PUB","NUM41_PUB","NUM42_PUB"," NUM41_PUB"," NUM42_PUB"," NUM43_PUB"," NUM44_PUB","C150_4_BLACK","C150_4_HISP","C150_4_ASIAN","C150_4_AIAN","C150_4_2MOR"," RET_PT4")
hisp_list=matrix(,nrow=2355538,ncol=3)
hisp=subset(mydata13,select=c("UNITID","C150_4_HISP"))
hisp=hisp[grep("NULL", hisp$C150_4_HISP, invert = TRUE),]
hisp_list_row=1
for(i in 1:2171)
{
  for(j in (i+1):2171)
  {
    hisp_list[hisp_list_row,1]=hisp[i,1];
    hisp_list[hisp_list_row,2]=hisp[j,1];
    hisp_list[hisp_list_row,3]=1-as.numeric(as.character(sub("," , ".",hisp[i,2] )))-as.numeric(as.character(sub("," , ".",hisp[j,2] )));
    hisp_list_row=hisp_list_row+1;
  }
}
hisp_list=data.frame(hisp_list)
hisp_list <- head(hisp_list,n=hisp_list_row)
write.csv(hisp_list, file = "hisp_edgelist.csv",row.names=FALSE)

asian_list=matrix(list(),nrow=2355538,ncol=3)
asian=subset(mydata13,select=c("UNITID","C150_4_ASIAN"))
asian=asian[grep("NULL", asian$C150_4_ASIAN, invert = TRUE),]
asian_list_row=1
for(i in 1:2171)
{
  for(j in (i+1):2171)
  {
    asian_list[asian_list_row,1]=asian[i,1];
    asian_list[asian_list_row,2]=asian[j,1];
    asian_list[asian_list_row,3]=1-as.numeric(as.character(sub("," , ".",asian[i,2] )))-as.numeric(as.character(sub("," , ".",asian[j,2] )));
    asian_list_row=asian_list_row+1;
  }
}
asian_list=data.frame(asian_list)
asian_list <- head(asian_list,n=asian_list_row)
write.csv(asian_list, file = "asian_edgelist.csv",row.names=FALSE)
aian_list=matrix(,nrow=2355538,ncol=3)
aian=subset(mydata13,select=c("UNITID","C150_4_AIAN"))
aian=aian[grep("NULL", aian$C150_4_AIAN, invert = TRUE),]
aian_list_row=1
for(i in 1:2171)
{
  for(j in (i+1):2171)
  {
    aian_list[aian_list_row,1]=aian[i,1];
    aian_list[aian_list_row,2]=aian[j,1];
    aian_list[aian_list_row,3]=1-as.numeric(as.character(sub("," , ".",aian[i,2] )))-as.numeric(as.character(sub("," , ".",aian[j,2] )));
    aian_list_row=aian_list_row+1;
  }
}
aian_list=data.frame(aian_list)
aian_list <- head(aian_list,n=aian_list_row)
write.csv(aian_list, file = "aian_edgelist.csv",row.names=FALSE)

black_graph=data.frame(black_lis)
black_graph=subset(black_graph,X3>0.7)
black_graph=head(black_graph, n=5000)
write.csv(black_graph, file = "black_edgelist.csv",row.names=FALSE)