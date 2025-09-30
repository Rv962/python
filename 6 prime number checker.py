def prime_checker(number) :
    is_prime = True
    for numb in range(2, number):        
             
       if number% numb == 0:
           is_prime = False
           
           
    if is_prime == False:
       print("it's not a prime number")
           
    else:
       print("it's a prime number")
                       
n = int(input("enter a number of your choice : "))
prime_checker(n)
       
        
        