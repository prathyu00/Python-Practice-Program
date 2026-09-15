score1=[10,20,30,30,30,30,40,20,]
score2=[10,50,50,60,60,70,80]
unique =set(score1)
unique1 =set(score2)
del(score1[1])
del(score2[4])
total=sum(score1)
total=sum(score2)
print("original list: ",score1,score2)
print("unique numbers: ",unique,unique1)
print("total score",total)

