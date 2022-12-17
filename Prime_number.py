while True:
    
    try:
        a= int(input("Please give a number: "))
    except ValueError :
        print("Please give only a integer number")
        break
        
#stringer veya kesirli sayı girerek döngüyü sonlandırabilirsiniz.        
      
    flag = False

    if a> 1:
            
        for i in range(2, a):
            if (a % i) == 0:
                    
                flag = True
    else:
        flag=True         

    if (flag==True):
        print(a, "isn't a prime number")
    else:
        print(a, "is a prime number")
    
#CEM AKAN  
