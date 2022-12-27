#User function Template for python3



def maxArea(A,n):
    
    maxArea = 0
    
    i = 0
    j = n-1
    
    while(i<=j):
        
        if mini(A[i],A[j])*(j-i) > maxArea:
            maxArea = mini(A[i],A[j])*(j-i)
        
        if A[j] > A[i]:
            i += 1
        else:
            j -= 1
    
    return maxArea
        
def mini(A, B):
    if(A>B):
        return B
    else:
        return A


#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    
    n = int(input())
    l = list(map(int,input().split()))
    
    print(maxArea(l,n))
    
    
# } Driver Code Ends
