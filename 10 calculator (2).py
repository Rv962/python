def add (n1 , n2) :
    return n1 + n2
def subtract (n1 , n2) :
    return n1 - n2
def multiply (n1 , n2) :
    return n1 * n2
def divide (n1 , n2) :
    return n1 / n2
    
operations = {
"+"  : add, 
"-"   : subtract, 
"*"   :  multiply, 
"/"   :  divide
}

logo = """
     CALCULATOR
| ________________|
||   0123456789   ||
|[ M |#  |C  ][ - ]|
|[ 7 | 8 | 9 ][ + ]|
|[ 4 | 5 | 6 ][ x ]|
|[ 1 | 2 | 3 ][ % ]|
|[ . | O | : ][ = ]|
"---------------------"  
"""
#print(logo)

def calculator ( ):
    print(logo)
    num1 = float(input("enter the first number :  "))
    for symbol in operations:
        print(symbol)
       
    should_continue = True
    while should_continue :
        operation_symbol =input("choose operation '+'  '-'  '*'  '/:  ")
        num2 = float(input("enter the next number :  "))
        
    
        answer = operations[operation_symbol](num1, num2)
        print (f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f"enter  'y if you want to continue with {answer} or n if you want to end :") == "y":
            num1=answer
        else:
            should_continue = False
            calculator ( )
            
calculator ( )
        
        