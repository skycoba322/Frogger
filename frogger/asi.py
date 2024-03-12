def skeem(n):
    if n == 1:
        return 1
    else:
        return 1 + 2 * skeem(n - 1)
        #return 1 + skeem(n - 1) + skeem(n - 1)
    
print(skeem(5))

