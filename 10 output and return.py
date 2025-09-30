def name (f_name, l_name):
    if f_name =="" or l_name =="" :
        return "no columns should be empty"
    first_name = f_name.title()
    last_name = l_name.title()
    
    print (first_name, last_name)
    return f"{first_name} {last_name}"
    
    
    
print(name(input("what if you first name : "),
 input("what if your last name : ")))
 


def fun( ):
     "Hello"
     # return "Hello"
     
x = fun()
print(x)