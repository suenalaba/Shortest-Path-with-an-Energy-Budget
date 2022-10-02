# Node class that is pushed into the priority queue used for tracking heuristics.

class Node:
  def __init__(self, node_id, distance, energy_cost, parent):
    self.node_id = node_id
    # self.adjacent_nodes = {} # dictionary that stores k,v pair: adjacent node: distance/energy costs.
    self.distance = distance # distance cost from start node to current node.
    self.energy_cost = energy_cost # energy cost from start node to current node.
    self.parent = parent # track parent node. (This will be a node object.)

  # Overriding the comparison operator of PriorityQueue()
  # this has to be done because Nodes cannot be a comparator for the PQ.
  # Nodes with min distance cost will be popped from the PQ first.
  def __lt__(self, other):
    return self.distance < other.distance

