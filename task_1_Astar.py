import json
import math

with open('./data/Dist.json') as dist_file:
    dist_dict = json.load(dist_file)

with open('./data/Coord.json') as coord_file:
    coord_dict = json.load(coord_file)
  
with open('./data/Cost.json') as cost_file:
    cost_dict = json.load(cost_file)
  
with open('./data/G.json') as G_file:
    G_dict = json.load(G_file)


# heuristic function calculator
def straightLineDist(target, coord_dict):
    target_x_coord = coord_dict[target][0]
    target_y_coord = coord_dict[target][1]
    return_dict = {}
    for key, coord_list in coord_dict.items():
        return_dict[key] = math.sqrt((coord_list[0] - target_x_coord)**2 + (coord_list[1] - target_y_coord)**2)
    return return_dict

def shortestDistance(path):
    distance = 0
    for i in range(0, len(path)-1):
        distance += dist_dict[path[i] + ',' + path[i+1]]
    return distance


def aStarAlgo(start_node, stop_node):
    open_set = set(start_node) # nodes that have been visited but neighbors are yet to be explored
    closed_set = set() # node which, along with their neighbours, have been visited
    g = {} # store distance from starting node
    parents = {} # parents contain an adjacency map of all nodes
    heuristic = straightLineDist(stop_node, coord_dict)
    g[start_node] = 0 # distance of starting node from itself is 0
    parents[start_node] = start_node # parent of start_node is itself
    
    while len(open_set) > 0:
        n = None
        
        for v in open_set:
            if n == None or g[v] + heuristic[v] < g[n] + heuristic[n]:
                n = v
        if n == stop_node or G_dict.get(n, 'no neighbours') == 'no neighbours':
            pass
        else:
            for m in G_dict[n]:
                weight = dist_dict[n + ',' + m]
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        if n == None:
            print('Path does not exist!')
            return None
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            return path
        open_set.remove(n)
        closed_set.add(n)
    print('Path does not exist!')
    return None

print(aStarAlgo('1', '50'))
print(len(aStarAlgo('1', '50')))
print(shortestDistance(aStarAlgo('1', '50')))