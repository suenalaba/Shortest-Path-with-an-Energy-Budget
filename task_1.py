from queue import PriorityQueue
import sys
from Node import Node
from utils import get_json_dict_key
from path_properties import heuristic
from time import process_time

# A* star for task 1 with no energy constraint
def astar_search_no_constraint(g, dist, cost, coord, source_id, destination_id):

  start = process_time()  # initialise the time

  nodes_explored_counter = 0 # initialise counter to track the nodes explored

  frontier = PriorityQueue() # by default Python implements a min pq

  source_hn = heuristic(coord, source_id, destination_id)

  # eval func represents f(n), where
  # f(n) = g(n) + h(n)
  eval_func = {} # dict that stores {node_id: eval_func}
  eval_func[source_id] = 0 + source_hn

  # source node has no parent node
  source = Node(source_id, 0, 0, None)

  frontier.put((0 + source_hn, source))
  
  while not frontier.empty():

    current_node = frontier.get()[1]

    nodes_explored_counter += 1

    # NOTE: We only do goal test when we expand node not when we add to frontier
    if current_node.node_id == destination_id:
      end = process_time()
      total_time = end - start
      return total_time, nodes_explored_counter,current_node

    for adjacent_node_id in g[current_node.node_id]:
      
      # new distance = distance to current node + edgelength(curr,adjacent)
      dist_dict_key = get_json_dict_key(current_node.node_id, adjacent_node_id)
      new_distance = current_node.distance + dist[dist_dict_key]

      # our h(n) heuristic function measures the shortest distance from node to goal
      new_hn = heuristic(coord, adjacent_node_id, destination_id)

      # new evaluation function calculated by distance from start to node + h(n)
      new_fn = new_distance + new_hn

      # we want to add nodes if the f(n) is lower
      if new_fn < eval_func.get(adjacent_node_id, sys.maxsize):
        
        eval_func[adjacent_node_id] = new_fn 

        # update energy cost for printing purposes
        # this is trivial for the unconstrained A*
        cost_dict_key = get_json_dict_key(current_node.node_id, adjacent_node_id)
        new_energy_cost = current_node.energy_cost + cost[cost_dict_key]

        # add node to frontier
        adjacent_node = Node(adjacent_node_id, new_distance, new_energy_cost, current_node)

        # the pq comparator will be overloaded as defined in Node class.
        frontier.put((new_fn, adjacent_node))

  return nodes_explored_counter, None
#endof A* with no constraint

