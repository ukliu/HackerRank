### Chao's python code for the excersize of 'roads in hackerland'
### Using Kruskal's Minimum Spanning Tree algorithm and on dfs
### Since all edges are unique 2**n, it is guaranteed that MST algorithm finds the minimum path for all node pairs.

#find the route of each node
def find(i):
    if parent[i]==i:
        return i
    return find(parent[i])

# connect isolated edges
def union(x,y):
    xr=find(x)
    yr=find(y)
    if rank[xr]<rank[yr]:
        parent[xr]=yr
    elif rank[yr]<rank[xr]:
        parent[yr]=xr
    else:
        parent[yr]=xr
        rank[xr]+=1

#read_in
N,M= map(int,raw_input().split(' '))
edges=[]
unvisited=[]
res=[]
for i in xrange(M):
    edges.append(map(int,raw_input().split(' ')))
edges.sort(key=lambda x:x[2])

#rank for edges merging, parent for root-finding
rank=[0]*(N+1)
parent=range(N+1)
ii=0
ee=0
res={}

#N-1 edges connecte all the nodes
while ee<N-1:
    u,v,w=edges[ii]
    x=find(u)
    y=find(v)
    if x!=y:
        ee+=1
        if u not in res:
            res[u]=[]
        if v not in res:
            res[v]=[]
        res[u].append((v,w))
        res[v].append((u,w))
        union(x, y)
    ii+=1

#run dfs to get the number of times for each edges that have been used to connect the node pairs.
#recursive calling to calculate of the node numbers on both sides connected to each edge.
rst={}
def dfs(st,des):
    sz=1
    for eg in res[st]:
        v=eg[0]
        w=eg[1]
        if v==des:
            continue
        t=dfs(v,st)
        if w not in rst:
            rst[w]=0
        rst[w]+=t*(N-t)
        sz+=t
    return sz

dfs(1,-1)
suma=0
for w in rst:
    suma+=(1<<w)*rst[w]

print "{0:b}".format(suma)



