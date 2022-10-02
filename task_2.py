from queue import PriorityQueue
import sys
from time import process_time
from Node import Node
from utils import get_json_dict_key
from constants import ENERGY_BUDGET

# Finding the shortest path with UCS given a constraint that is the path energy cost cannot exceed the budget
def uniform_cost_search_with_constraint(g, dist, cost, source_id, destination_id):

  start = process_time()

  nodes_explored_counter = 0

  frontier = PriorityQueue() # by default Python implements a min pq

  dist_dict = {} # stores k:v pair of {node_id: distance from source}
  dist_dict[source_id] = 0

  cost_dict = {} # stores K:v pair of {node_id: energy cost from source}
  cost_dict[source_id] = 0 

  #NOTE: This time we have no visited marker because we will ALLOW revisiting.
  # As there may be more optimal shorter paths within the energy budget.
  # Non-greedy approach.

  # source node has no parent node
  source = Node(source_id, 0, 0, None)

  frontier.put(source)

  while not frontier.empty():

    current_node = frontier.get()
    nodes_explored_counter += 1
    
    # NOTE: We only do goal test when we expand node not when we add to frontier
    if current_node.node_id == destination_id and current_node.energy_cost <= ENERGY_BUDGET:
      end = process_time()
      total_time = end - start
      return total_time, nodes_explored_counter,current_node

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

      # we only want to add node to PQ if it has a shorter distance or lower energy cost
      if new_distance < dist_dict.get(adjacent_node_id, sys.maxsize) or new_energy_cost < cost_dict.get(adjacent_node_id, sys.maxsize):
        
        # update cost dict and dist dict if potential better path is found
        cost_dict[adjacent_node_id] = new_energy_cost
        dist_dict[adjacent_node_id] = new_distance

        # add node to frontier
        adjacent_node = Node(adjacent_node_id, new_distance, new_energy_cost, current_node)

        # the pq comparator will be overloaded as defined in Node class.
        frontier.put(adjacent_node)

  # if path not found we return none. But for this specific instance, this should never happen.
  return None

#endof uniform cost search with constraint satisfaction


