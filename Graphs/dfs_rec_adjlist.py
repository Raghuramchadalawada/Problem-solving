
#https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1#


class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfs(self,i,ans,visited,adj):
        for j in adj[i]:
            #print(adj[k])
            if j not in visited:
                #print(j)
                visited.add(j)
                ans.append(j)
                self.dfs(j,ans,visited,adj)
        
        #return ans
    def dfsOfGraph(self, V, adj):
        # code here
        visited=set()
        ans=[0]
        for i in range(len(adj)):
            if i not in visited:
                visited.add(i)
                self.dfs(i,ans,visited,adj)
        return ans
