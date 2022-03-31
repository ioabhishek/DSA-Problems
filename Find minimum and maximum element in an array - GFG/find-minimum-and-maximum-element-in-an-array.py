#User function Template for python3

def getMinMax(a, n):
    
    mn = a[0]
    mx = a[0]
    
    for i in range(n):
        if a[i] < mn:
            mn = a[i]
        if a[i] > mx:
            mx = a[i]
        
    return (mn, mx) 
#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        
        product = getMinMax(a, n)
        print(product[0], end=" ")
        print(product[1])

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends