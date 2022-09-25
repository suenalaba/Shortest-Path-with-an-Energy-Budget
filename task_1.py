from queue import PriorityQueue

from path_properties import PathDetailsWithNoConstraint, get_path_length


def uniform_cost_search(g, dist, source, sink):

  # use priority queue to get the current shortest path
  pq = PriorityQueue()

  # maintain a set of visited nodes so we don't revisit nodes already traversed
  visited = []

  initial_path = [source]

  pq.put((0, initial_path))

  while not pq.empty():
    pair = pq.get()

    current_path = pair[1]

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

        shortest_path_length = get_path_length(dist, current_path)

        path_details = PathDetailsWithNoConstraint(shortest_path_length, shortest_path)

        return path_details
      # add paths for adjacent nodes into pq
      for adjacent_node in g[current_node]:
        dist_json_key = current_node + "," + adjacent_node
        dist_to_adjacent_node = dist[dist_json_key]

        total_distance = pair[0] + dist_to_adjacent_node
        full_path = list(pair[1])
        full_path.append(adjacent_node)
        pq.put((total_distance, full_path))

  return PathDetailsWithNoConstraint()
#endof uniform cost search