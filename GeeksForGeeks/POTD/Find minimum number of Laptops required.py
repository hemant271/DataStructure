#User function Template for python3

class Solution: 
    def minLaptops(self, N, start, end):
        
        start.sort()
        end.sort()
        
        laptopNeeded = 1
        result = 1
        
        si = 1
        ei = 0
        
        while(si < N and ei < N):
            
            if(start[si] < end[ei]):
                laptopNeeded += 1
                si += 1
            
            elif(start[si] >= end[ei]):
                laptopNeeded -= 1
                ei += 1
            
            if(laptopNeeded > result):
                result = laptopNeeded
        
        return result
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N = int(input())
        start = list(map(int,input().split()))
        end = list(map(int,input().split()))
            
        ob = Solution()
        print(ob.minLaptops(N, start, end))
        
        T -= 1

# } Driver Code Ends
