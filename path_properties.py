class PathDetailsWithNoConstraint:

  def __init__(self, path_length = -1, path_desc="Path cannot be determined"):

    self.path_length = path_length
    self.path_desc = path_desc


def get_path_length(dist, path):

  total_path_length = 0
  start_flag = True

  for node in path:
    if start_flag:
      prevNode = node
      start_flag = False
    else:
      currNode = node
      nodes_key = prevNode + "," + currNode
      distance_between_nodes = dist[nodes_key]
      total_path_length += distance_between_nodes
      prevNode = node

  return total_path_length
