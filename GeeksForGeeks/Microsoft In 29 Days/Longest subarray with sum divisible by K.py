#User function Template for python3
class Solution:
	def longSubarrWthSumDivByK (self,arr,  n, K) : 
		
		sum = 0
		mx = 0
		mp = {}
		
		for i in range(0, n):
		    
		    sum += arr[i]
		    rem = sum % K
		    
		    if(rem == 0):
		        mx = max(i+1, mx)
		    elif(rem < 0):
		        rem += K
		    elif(rem in mp.keys()):
		        mx = max(mx, i - mp[rem])
		    else:
		        mp[rem] = i
		 
		return mx




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	for _ in range(0,int(input())):
		n, K = map(int ,input().split())
		arr = list(map(int,input().strip().split()))
		ob = Solution()
		res = ob.longSubarrWthSumDivByK(arr, n, K)
		print(res)




# } Driver Code Ends
