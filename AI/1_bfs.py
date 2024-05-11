def bfs(visited,graph,node,queue):
    visited.add(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s,end = " ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

def main():
    visited = set() # TO keep track of BFS visited nodes
    queue = []       # For BFS
    n = int(input("Enter number of nodes : "))
    graph = dict()

    for i in range(1,n+1):
        edges = int(input("Enter number of edges for node {} : ".format(i)))
        graph[i] = list()
        for j in range(1,edges+1):
            node = int(input("Enter edge {} for node {} : ".format(j,i)))
            graph[i].append(node)

    print("The following is BFS")
    bfs(visited, graph, 1, queue)

if __name__=="__main__":
    main()



'''
Enter number of nodes : 9
Enter number of edges for node 1 : 3
Enter edge 1 for node 1 : 2
Enter edge 2 for node 1 : 3
Enter edge 3 for node 1 : 4
Enter number of edges for node 2 : 2
Enter edge 1 for node 2 : 5
Enter edge 2 for node 2 : 6
Enter number of edges for node 3 : 2
Enter edge 1 for node 3 : 7
Enter edge 2 for node 3 : 8
Enter number of edges for node 4 : 1
Enter edge 1 for node 4 : 9
Enter number of edges for node 5 : 0
Enter number of edges for node 6 : 0
Enter number of edges for node 7 : 0
Enter number of edges for node 8 : 0
Enter number of edges for node 9 : 0

The following is BFS
1 2 3 4 5 6 7 8 9



                    1
                  / | \
                 /  |  \
                2   3   4
               / \ / \   \
              5  6 7  8   9
              
              

Enter number of nodes : 4
Enter number of edges for node 1 : 2
Enter edge 1 for node 1 : 2
Enter edge 2 for node 1 : 3
Enter number of edges for node 2 : 1
Enter edge 1 for node 2 : 4
Enter number of edges for node 3 : 0
Enter number of edges for node 4 : 0

        1
       / \
      /   \
     2     3
     |
     4




Enter number of nodes : 6
Enter number of edges for node 1 : 2
Enter edge 1 for node 1 : 2
Enter edge 2 for node 1 : 3
Enter number of edges for node 2 : 1
Enter edge 1 for node 2 : 4
Enter number of edges for node 3 : 1
Enter edge 1 for node 3 : 5
Enter number of edges for node 4 : 0
Enter number of edges for node 5 : 1
Enter edge 1 for node 5 : 6
Enter number of edges for node 6 : 0

        1
       / \
      /   \
     2     3
     |     |
     4     5
          |
          6


'''