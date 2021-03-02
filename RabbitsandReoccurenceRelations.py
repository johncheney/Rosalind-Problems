




pairs = [1, 1,]             # initalize a list to add to  

def rabbitcounter(n,k):                        # Describe the fxｎ
    for i in range(n-1):        # for loop to loop through generations 
                               
                                # add to the list by the formula to find 
                                        # how many pairs will be in n 
        pairs.append(abs(k*(i-1) + i-1))
 
    print(pairs)
    print(sum(pairs))  # A way to total all the pairs in the list
    
    

rabbitcounter(5,3)



