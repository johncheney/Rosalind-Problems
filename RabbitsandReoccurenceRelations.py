

def rabbitcounter(n,k):  # Describe the fxｎ
    p = 1
    o = 0 
    for i in range(n):        # for loop to loop through 
        pairs=o+p
        #next_gen=
        o = o + p*k 
        p = o  
        
        print('parents =' ,p)
        print('offspring =' ,o)
        print('pairs =' ,pairs)
        
        print('  ')
       # print('pairs' = pairs)


rabbitcounter(5,3)


