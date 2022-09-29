from queue import PriorityQueue
import sys
from Node import Node
from utils import get_json_dict_key
import math


def astar_search_no_constraint(g, dist, cost, coord, source_id, destination_id):

  nodes_explored_counter = 0

  pq = PriorityQueue() # by default Python implements a min pq

  visited = [] # marker to indicate whether a node has been visited

  # source node has no parent node
  source = Node(source_id, 0, 0, None,sys.maxsize)
  dictOfNodes=dict()
  dictOfNodes[source_id]=source

  pq.put(source)

  while not pq.empty():
    #Pop node with the smallest heuristic
    current_node = pq.get()
    nodes_explored_counter += 1
    
    # NOTE: We only do goal test when we expand node not when we add to frontier
    if current_node.node_id == destination_id:
      return nodes_explored_counter,current_node

    # mark node as visited
    visited.append(current_node.node_id)

    #Iterate through adjacent nodes
    for adjacent_node_id in g[current_node.node_id]:
      #Check if node has already been explored
      if adjacent_node_id in visited:
        continue

      # Calculate heuristic function
      dist_dict_key = get_json_dict_key(current_node.node_id, adjacent_node_id)
      distanceFromStart = current_node.distance + dist[dist_dict_key]
      x2=coord[adjacent_node_id][0]-coord[destination_id][0]
      y2=coord[adjacent_node_id][1]-coord[destination_id][1]
      distanceFromEnd=math.sqrt(x2**2+y2**2)
      heuristic=distanceFromStart+distanceFromEnd

      if adjacent_node_id in dictOfNodes:
          tempNode=dictOfNodes.get(adjacent_node_id)
          if heuristic < tempNode.heuristic:
            # update energy cost
            # this is trivial for the unconstrained uniform cost search
            cost_dict_key = get_json_dict_key(current_node.node_id, adjacent_node_id)

            #Update node in priority queue
            tempNode.cost = current_node.energy_cost + cost[cost_dict_key]
            tempNode.distance=distanceFromStart
            tempNode.heuristic=heuristic
            pq.put(tempNode)

      else:
          # update energy cost
          cost_dict_key = get_json_dict_key(current_node.node_id, adjacent_node_id)
          new_energy_cost = current_node.energy_cost + cost[cost_dict_key]

          # add node to frontier
          adjacent_node = Node(adjacent_node_id, distanceFromStart, new_energy_cost, current_node, heuristic)
          
          #Add node to dictionary
          dictOfNodes[adjacent_node_id]=adjacent_node

          #Add node to priority queue
          pq.put(adjacent_node)

  # if path not found we return none. But for this specific instance, this should never happen.
  return None

#endof Astar search with no constraint satisfaction
