### Chao's python 2.7 code for the excersize of 'Kingdom Connectivity'
### Do recursive dfs. During each dfs, keep tracking nodes that can lead to a cycle, and that can lead to the destination. If the cycle_nodes and path_nodes share components, then there is an infinite number of paths.
### At the same time, keep tracking the number of available paths passing each node.
### Recursive dfs is concise to write but hard to understand. It is better to write down the purpose of each line of it to figure out how exactly it works.

N,M=map(int,raw_input().split(' '))
edges={}
for i_m in xrange(M):
    p,q=map(int,raw_input().split(' '))
    if p-1 not in edges:
        edges[p-1]=[q-1]
    else:
        edges[p-1].append(q-1)

cur_path=[]
memo=[0]*N
visited=[False]*N
cycle_nodes=set()
path_nodes=set()

def dfs(node):
    visited[node]=True
    cur_path.append(node)
    if node==N-1:
        update_path_nodes(1)
    elif node in edges:
        for nxt in edges[node]:
            if visited[nxt]:
                update_cycle_nodes(nxt)
            else:
                if memo[nxt]>0:
                    update_path_nodes(memo[nxt])
                if memo[nxt]==0:
                    dfs(nxt)
    if memo[node]==0:
        memo[node]=-1
    visited[node]=False
    cur_path.pop(-1)

def update_cycle_nodes(nd):
    ii=len(cur_path)-1
    while ii>=0 and cur_path[ii]!=nd:
        cycle_nodes.add(cur_path[ii])
        ii-=1
    cycle_nodes.add(nd)

def update_path_nodes(inc):
    for cur in cur_path:
        path_nodes.add(cur)
        memo[cur]+=inc
        memo[cur]%=10**9

def found_infinite_solution():
    for cycle_nd in cycle_nodes:
        if cycle_nd in path_nodes:
            return True
    return False

dfs(0)

if found_infinite_solution():
    print 'INFINITE PATHS'
else:
    print memo[0]
