
def arrangeCoins(n):
    i = 1

    while i < n:
        print("n {}\ti {}".format(n, i)) 
        n = n - i 
        i += 1 

arrangeCoins(14)  