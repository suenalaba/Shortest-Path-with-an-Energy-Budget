from queue import PriorityQueue
from constants import ENERGY_BUDGET
from path_properties import PathDetailsWithConstraint, get_path_length, get_path_energy_cost

def uniform_cost_search_with_constraint(g, dist, cost, source, sink):

  # use priority queue to get the current shortest path
  pq = PriorityQueue()

  # maintain a set of visited nodes so we don't revisit nodes already traversed
  visited = []

  initial_path = [source]

  pq.put((0, 0, initial_path))

  while not pq.empty():
    pair = pq.get()

    current_distance, energy_consumed, current_path = pair[0], pair[1], pair[2]

    # current node will be the last node in the path taken
    current_node = current_path[-1]

    # if already visited, don't do anything
    if current_node in visited:
      continue
    # explore node that has yet to be visited
    else:

      visited.append(current_node)

      # return path taken if current node is sink, note we only do goal test on node when we expand it
      if sink == current_node:
        # get description of the shortest path in a printable format
        shortest_path = ""
        for node in current_path:
          shortest_path += node + "->"
        shortest_path = shortest_path[:-2]

        # get total length of path from source to sink
        shortest_path_length = get_path_length(dist, current_path)

        # get total energy cost of path from source to sink
        total_energy_cost = get_path_energy_cost(cost, current_path)

        path_details = PathDetailsWithConstraint(shortest_path_length, shortest_path, total_energy_cost)

        return path_details
      
      # add paths for adjacent nodes into pq
      for adjacent_node in g[current_node]:

        cost_json_key = current_node + "," + adjacent_node
        energy_cost_to_adjacent_node = cost[cost_json_key]
        total_energy_cost = energy_consumed + energy_cost_to_adjacent_node

        # if total energy cost exceeds the energy budget we don't add this node to pq
        if total_energy_cost > ENERGY_BUDGET:
          continue
        else: 
          # we only add this new path to pq if it satisfies our energy constraint
          dist_json_key = current_node + "," + adjacent_node
          dist_to_adjacent_node = dist[dist_json_key]
          total_distance = current_distance + dist_to_adjacent_node

          full_path = list(current_path)
          full_path.append(adjacent_node)
          pq.put((total_distance, total_energy_cost, full_path))

  return PathDetailsWithConstraint()
#endof uniform cost search with energy cost constraint
