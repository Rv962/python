score ={
"Ram" : 81,
"shyam" : 67,
"Sita" : 91 }

print(score)

for key in score :
    marks = score[key]
    print(marks)
    if marks > 80 :
        score[key] = "outstanding"
    else :
        score[key] = "average"
        
print(score)
        
     