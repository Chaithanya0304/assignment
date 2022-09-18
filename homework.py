#Assignment

#list

#1 list of characters 
list=["hii"," this","is", "chaitu"]
print(list)
#2 list of numbers
list=["10","20","30"]
print(list)
#3 empty list
list=[]
print(list)
#4 update list
list=["hii"," this","is", "chaitu"]
list[3]=chaithanya
print(list)

#tuple

#1
list=("hii"," this","is","chaitu")
print(list)
#2 trying to modify data 
list=("hii","this","is","chaitu")
list[2]=chaithanya                 # error because tuples are immutable(can't be modified)
print(list)
#3
list=("hii","this","is","chaitu")
list.append("student")
print(list)
#4
list=("hii","this","is","chaitu")
list.remove("hii")
print(list)

#dictionary

#1
list={
      "name":"chaitu",
      "dept":"cse",
      "roll":"556",
      }
 print(list)
#2
list={
      "name":"chaitu",
      "dept":"cse",
      "roll":"556",
      }
 list["roll"]=588
 print(list)
 #3
 list={
      "name":"chaitu",
      "dept":"cse",
      "roll":"556",
      }
  del list["roll"]
  print(lsit)
 #4
 list={
      "name":"chaitu",
      "dept":"cse",
      "roll":"556",
      }
 print(list["name"])    
   
 #negative slicing
 
 #1
 c=datascience
 print(c[-5,-1])
 #2
 c=[1,2,3,4,5]
 print(c[-4,-1])
 
 # frozen set
 
 # frozen set is immutable  can not be  modified
#1
list=[1,2,3,4,5]
a=list[-1]
b=list[-2]
print(a,b)




   
   
  
 

