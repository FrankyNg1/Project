from collections import defaultdict

def Chain(G, u):
    '''
    Will be using layers data structure to keep track of nodes at each level of the bfs traversal. 
    This helps in organizing nodes by their distance from the starting node u 
    and ensures that each node is processed level by level.
    '''
    # initialize data structures
    # stores parent of each node
    parents = defaultdict(lambda: None) 
    # storing nodes at each layer
    layers = defaultdict(list)  
    # this will be tracking paths starting from u
    layer1path = defaultdict(lambda: None)  
    #store the distance from u
    dist = defaultdict(lambda: float('inf')) 

    # Set initial conditions
    # Path from u to u is just u
    layer1path[u] = u  
    # u is the only node at layer 0
    layers[0] = [u]  
    # set the distance u to itself to 0
    dist[u] = 0  
    i = 0  # Start at layer 0

    # iterate through layers up to a maximum of 3 layers
    while layers[i] and i <= 3:
         # prepare the next layer
        layers[i + 1] = [] 
        # For each node v in the current layer
        for v in layers[i]:  
            # For each neighbor w of v
            for w in G[v]:  
                # If w hasn't been visited yet
                if layer1path[w] is None:  
                    # Mark w as visited by itself
                    layer1path[w] = w  
                elif layer1path[w] is None:  
                    # If w is not part of any path
                    # then inherit path from v
                    layer1path[w] = layer1path[v] 
                elif dist[w] == 6 and layer1path[w] != layer1path[v]:  
                    # checking for our condition of 6 nodes
                    # return True if condition is met
                    return True  
                
                 # If w has not been assigned a parent
                if w not in parents:  
                    # Set v as parent of w
                    parents[w] = v 
                    # update a distance of w
                    dist[w] = dist[v] + 1 
                    # Add w to the next layer
                    layers[i + 1].append(w)  
        #moving to the next layer
        i += 1  
    # Return False if no path of length 6 is found
    return False 


# Test case 1
G1 = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}


u1 = 'A'
print("Result should be false!")
# Test case 1 result:
print(Chain(G1, u1))

#Test case 2
G2 = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'E'],
    'E': ['D', 'F'],
    'F': ['E', 'G'],
    'G': ['F']
}

u2 = 'A'

# Test case 2 result
print("Result should be true!")
print(Chain(G2, u2)) 
