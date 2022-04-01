#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        l = 0
        r = len(arr)-1
        i = 0
        
        def swap(i,j):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            
        while i <= r:
            if arr[i] == 0:
                swap(l,i)
                l += 1
            elif arr[i] == 2:
                swap(i,r)
                r -= 1
                i -= 1
            i += 1
        
        return arr
            


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends