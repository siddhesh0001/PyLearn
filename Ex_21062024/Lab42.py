#set
#Set to dont store duplicate valuse
#few things are commone link list. ie delete, pop etc

s={2,4,2,6}
print(s) # --> It will print {2,4,6} only. 2 will  be printed only once.

#union in set is possible and it is npt possible in list or tuple

s1={1,2,3}
s2={3,4,5}
set=s1.union(s2)
print(set) #--> It will print {1,2,3,4,5} and it will print 3 once only

#Intersection
set=s1.intersection(s2)
print(set) # it will print 3 only casue  3 is common in both set

#Difference
set=s1.difference(s2) #it will print 1,2 and will skip common and other value of other set
print(set)
set=s2.difference(s1) #it will print 4,5 and will skip common and other value of other set
print(set)
