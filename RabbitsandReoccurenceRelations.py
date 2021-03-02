
def rabbitcounter(n,k):                        # Describe the fxn
  rp = range(n)
  for i in range(n):        # for loop to loop through generations 
    pairs = [1, 1,]        # initalize a list to add to 
                            # add to the list by the formula to find 
                            # how many pairs will be in n 
    pairs.append(k*(n-2) + (n-1))
 
  #answer = sum.pairs      # A way to total all the pairs in the list
  #print(answer)             # print the total 
  print(pairs)
    
rabbitcounter(5,3)
    
