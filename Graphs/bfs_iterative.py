#https://practice.geeksforgeeks.org/problems/bfs-traversal-of-graph/1

from collections import deque
class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # code here
        nodes_to_visit=deque()
        nodes_to_visit.append(0)
        ans=[0]
        visited=set()
        visited.add(0)
        while nodes_to_visit:
            cur=nodes_to_visit.popleft()
            for i in adj[cur]:
                if i not in visited:
                    visited.add(i)
                    nodes_to_visit.append(i)
                    ans.append(i)
        return ans
            
        

#{ 
#  Driver Code Starts



if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends
