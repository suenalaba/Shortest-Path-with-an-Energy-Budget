from path_properties import heuristic
from queue import PriorityQueue
import sys
from time import process_time
from Node import Node
from utils import get_json_dict_key
from constants import ENERGY_BUDGET

def astar_with_constraint(g, dist, cost, coord, source_id, destination_id):

  start = process_time()

  nodes_explored_counter = 0

  frontier = PriorityQueue() # by default Python implements a min pq

  source_hn = heuristic(coord, source_id, destination_id)

  # f(n) = g(n) + h(n)
  # eval_func = distance from start + Euclidean distance from node to destination
  eval_func = {} # stores k:v pair of {node_id: eval func}
  eval_func[source_id] = 0 + source_hn

  cost_dict = {} # stores K:v pair of {node_id: energy cost from source}
  cost_dict[source_id] = 0 

  #NOTE: This time we have no visited marker because we will ALLOW revisiting.
  # As there may be more optimal shorter paths within the energy budget.
  # Non-greedy approach.

  # source node has no parent node
  source = Node(source_id, 0, 0, None)

  # our PQ will have (f(n) score, node)
  frontier.put((0 + source_hn, source))


  while not frontier.empty():

    fn, current_node = frontier.get()
    nodes_explored_counter += 1
    
    # NOTE: We only do goal test when we expand node not when we add to frontier
    if current_node.node_id == destination_id and current_node.energy_cost <= ENERGY_BUDGET:
      end = process_time()
      total_time = end - start
      return total_time, nodes_explored_counter, current_node

    for adjacent_node_id in g[current_node.node_id]:

      # check to ensure energy cost is within budget (CSP).
      cost_dict_key = get_json_dict_key(current_node.node_id, adjacent_node_id)
      new_energy_cost = current_node.energy_cost + cost[cost_dict_key]

      # if energy budget exceeded, CSP fails.
      # Optimization: We do not want to waste time searching further,
      # when constraints have been violated, so backtrack.
      if ENERGY_BUDGET < new_energy_cost:
        continue
      
      # prevent cyclic loop where you go back and forth between the same nodes
      if current_node.parent != None and current_node.parent.node_id == adjacent_node_id:
        continue

      # new distance = distance to current node + edgelength(curr,adjacent)
      dist_dict_key = get_json_dict_key(current_node.node_id, adjacent_node_id)
      new_distance = current_node.distance + dist[dist_dict_key]

      new_hn = heuristic(coord, adjacent_node_id, destination_id)
      new_fn = new_distance + new_hn

      # we only want to add node to PQ if it has a lower f(n) or more energy efficient
      # if not present in dictionary means is NOT in so default give max value
      # because we will want to add this node
      if new_fn < eval_func.get(adjacent_node_id, sys.maxsize) or new_energy_cost < cost_dict.get(adjacent_node_id, sys.maxsize):
        
        # update cost dict and eval_func dict if potential better path is found
        cost_dict[adjacent_node_id] = new_energy_cost
        eval_func[adjacent_node_id] = new_fn

        # F(N) = g(n) + h(n) 
        new_hn = heuristic(coord, adjacent_node_id, destination_id)
        new_fn = new_distance + new_hn

        # add node to frontier
        adjacent_node = Node(adjacent_node_id, new_distance, new_energy_cost, current_node)

        # the frontier comparator will be overloaded as defined in Node class.
        frontier.put((new_fn, adjacent_node))

  # if path not found we return none. But for this specific instance, this should never happen.
  return None

#endof A* search with constraint satisfaction

