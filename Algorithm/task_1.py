
class Node:
    def __init__(self, distance, previous_node, visited):
        
        # Shortest distance from the predefined source node (S) to the current node
        self.distance = distance 
        
        # Current node’s previous node
        self.previous_node = previous_node
        
        # Whether current node has already been visited
        self.visited = visited
        
    def get_distance(self):
        return self.distance
    
    def get_previous_node(self):
        return self.previous_node
    
    def get_visited(self):
        return self.visited
    
    
def task_1(G,Coord,Dist,Cost,start,end):
    # Initialise the nodes
    nodes = {}
    for i in G:
        nodes[i]= Node(-1, 'NA', False)
        
    # Update starting node
    current_node = start
    nodes[current_node] = Node(0, 'NA', True)
    
    # Create priority queue
    queue = []
    
    # while loop will stop running once target node is reached
    while(current_node != end):
        for i in range(0, len(G[current_node])):
            if nodes[G[current_node][i]].visited == False:
                if nodes[G[current_node][i]].distance == -1:
                    nodes[G[current_node][i]] = Node(Dist[current_node + ',' + G[current_node][i]] + nodes[current_node].distance, current_node, nodes[G[current_node][i]].visited)
                elif nodes[G[current_node][i]].distance > Dist[current_node + ',' + G[current_node][i]] + nodes[current_node].distance:
                    nodes[G[current_node][i]] = Node(Dist[current_node + ',' + G[current_node][i]] + nodes[current_node].distance, current_node, nodes[G[current_node][i]].visited)
        
        # Put into queue according to distance        
        for i in range(0, len(G[current_node])):
            if len(queue) == 0 and nodes[G[current_node][i]].visited == False:
                queue.append(G[current_node][i])
            elif nodes[G[current_node][i]].visited == False:
                queue.append(G[current_node][i])
                for j in range(len(queue)-1, 0, -1):
                    if nodes[queue[j]].distance < nodes[queue[j-1]].distance:
                        swap = queue[j]
                        queue[j] = queue[j-1]
                        queue[j-1] = swap
                    elif queue[j] == queue[j-1]:
                        queue.remove(queue[j-1])
                    else:
                        break 
        
        # Update current node from priority queue
        current_node = queue[0]
        queue.remove(current_node)
        nodes[current_node] = Node(nodes[current_node].distance, nodes[current_node].previous_node, True)
    
    # Retreive path starting from the target node
    current_node = end
    stack = []
    while(current_node != start):
        stack.append(nodes[current_node].previous_node)
        current_node = nodes[current_node].previous_node
    
    # Print the shortest path
    print("Shortest path:", end = " ")
    for i in range(len(stack)-1, 0, -1):
        print(stack[i], end ="->")
    print(stack[0], end = "->")
    print(end)
    
    # Print the shortest distance
    print("Shortest distance:", end = " ")
    print(nodes[end].distance)
    print(" ")


