pairs = [1, 1,] 

def rabbitcounter(n,k):                        # Describe the fxｎ
    for i in range(3,n):        # for loop to loop through generations 
           # initalize a list to add to 
        # add to the list by the formula to find 
                            # how many pairs will be in n 
        pairs.append((k*(i-2) + (i-1))+k)
 
            #answer = sum.pairs      # A way to total all the pairs in the list
                #print(answer)             # print the total 
    print(sum(pairs))
    
    

rabbitcounter(5,3)

