heights = input("input heights of students in cms : ").split()
for n in range (0, len(heights)):
    heights[n] = int(heights[n])  # converting string into integers
print (heights)


#first method without using loop function
#sumof = sum(heights)
#numberof = len(heights)
#average = sumof/numberof
#print(average)


#sum function working
total_height = 0
for n in heights:
    total_height = total_height + n
print(total_height)

#len function working
total_students = 0
for x in heights:
    total_students += 1
print(total_students)

average = total_height/total_students
print(f"{average} cms")