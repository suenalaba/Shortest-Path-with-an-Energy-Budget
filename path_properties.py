# this function builds the path by backtracking from destination node, using the parent variable
def get_printable_path(destination_node):
  
  path_str = ""
  path_list = []

  current_node = destination_node

  while current_node is not None:
    
    # parent should appear in front of child in the path.
    # hence, we insert to front of list each time.
    path_list.insert(0, current_node.node_id) 

    # update current node to be parent
    current_node = current_node.parent
  
  # get the path string required
  path_str = '->'.join(path_list)

  return path_str