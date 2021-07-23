from __future__ import print_function

graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set() # Set to keep track of visited nodes.

def dfs_recursive(visited, graph, node):
    if node not in visited:
        print (node, end= ' ')
        visited.add(node)
        for neighbour in graph[node]:
            dfs_recursive(visited, graph, neighbour)

# Driver Code
dfs_recursive(visited, graph, 'A')
print ('\n')
def dfs_stack(graph, node):
    stack = [node]
    visited = set()
    while stack:
        cur_node = stack.pop()
        print (cur_node, end=' ') #visit node
        visited.add(cur_node)
        for child in graph[cur_node]:
            if child not in visited:
                stack.append(child)
    
dfs_stack(graph, 'A')