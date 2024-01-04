def test():    
 b = n = 1     
 numbers = [0, 1, 1]      
 for n in range(100):          
    a = b + n           
    b = n            
    n = a            
    numbers.append(n)      
 print(numbers)
def speed_test():  
    import time
    t1 = time.time()  
    test()  
    t2 = time.time()  
    complete = t2-t1  
    print(complete)