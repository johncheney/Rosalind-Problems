
def rabbitcounter(n,k):  # Describe the fxｎ
    p = 1
    o = 1 
    pairs = [1,1,]
    for i in range(2, n):        # for loop to loop through 
        o = o + p*k 
        p = o - p*k
        pairs.append(o+p)
        
        #print('parents =' ,p)
    print('offspring =' ,o)
        #print('pairs =' ,pairs)
        
        #print('  ')
       # print('pairs' = pairs)


rabbitcounter(33,5)
