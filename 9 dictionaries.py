dict = { "rahul" : "that's me" , 
       "book" : "grit by Angela" 
       }
print(dict)

#add items to dictionary
name = input("enter word to add : ")
meaning = input("enter description : ")
dict[name] = meaning
print(dict)

# change item in dictionary
dict["book"] = "mountain is you"
print(dict)

# print key in dictionary
for m in dict :
    print(m)
    

#print value in dictionary
for m in dict :
    print(dict[m])
    
x = input("what do you want to find in dictionary :  ")
if x in dict :
    print(dict[x])
else :
    print("not available")
    
# list inside a dictionary

dictt = {
"alphabet" : [ 'A' , 'B' , 'C' ] ,
"numbers" : [1, 2, 3]
}
print(dictt)

#  list < dictionary <  inside a dictionary

dict2 = {
"month" : {"January" : ["aaa", "bbb", "ccc"]} ,
"day" : { "Sunday" : ["ttt" , "uuu", "ooo"]}
}
print(dict2)
