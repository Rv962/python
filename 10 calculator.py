def add(n1, n2):
    return n1 + n2
    
def substract(n1, n2) :
    return n1-n2
    
def multiply(n1, n2) :
    return (n1 * n2)          
    
def divide(n1, n2) :
    return (n1/n2)    

operations = { "+" : add , "-" : substract , "*" : multiply , "/" : divide }    
# various functions in a dictionary
        
                
def calculator()    :
    n1 = float(input("enter first number : "))
      
    for symbol in operations :
        print (symbol)      
        
     # creating loop for the second number in case of user
     # wants to continue calculating           
    while True : 
                                        
        x = input("choose one operation to perform : ")
    
        n2 = float(input("enter next number : "))  
                      
        answer = operations[x](n1,n2)
        # this calls the dictionary named operations which in turn
        # calls the respective function
    
        print(f"{n1}{x}{n2} = {answer}")    
             
        reapet = input("Do you want to continue, if yes type 'y' :  ")
        if reapet == "y" :
            n1 = answer
        else:
            break            
     
calculator()       