#To follow: PEP 8: Function and Variable Names convention.

from utils import open_json_data, print_results
import task_1 as task1
import task_2 as task2
import task_3 as task3
from constants import SOURCE, DESTINATION
from path_properties import get_printable_path

def main():

  g, dist, cost, coord = open_json_data()
  get_task1_results(g, dist, cost, coord)
  get_task2_results(g, dist, cost)
  get_task3_results(g, dist, cost, coord)


# def get_astar_results(g, dist, cost, coord):
#   destination_node = astar.astar_with__no_constraint(g, dist, cost, coord, SOURCE, DESTINATION)
#   path_as_string = get_printable_path(destination_node)
#   shortest_distance = destination_node.distance
#   energy_cost = destination_node.energy_cost
#   print_results("A star", path_as_string, shortest_distance, energy_cost)


def get_task1_results(g, dist, cost, coord):
  total_time, nodes_explored, destination_node = task1.astar_search_no_constraint(g, dist, cost, coord, SOURCE, DESTINATION)

  path_as_string = get_printable_path(destination_node)
  shortest_distance = destination_node.distance
  energy_cost = destination_node.energy_cost
  print_results("Task 1 with A* Search no constraint", path_as_string, shortest_distance, energy_cost,nodes_explored, total_time)

def get_task2_results(g, dist, cost):
  total_time, nodes_explored, destination_node = task2.uniform_cost_search_with_constraint(g, dist, cost, SOURCE, DESTINATION)
  path_as_string = get_printable_path(destination_node)
  shortest_distance = destination_node.distance
  energy_cost = destination_node.energy_cost
  print_results("Task 2 with UCS with constraint", path_as_string, shortest_distance, energy_cost,nodes_explored, total_time)

def get_task3_results(g, dist, cost, coord):
  total_time, nodes_explored, destination_node = task3.astar_with_constraint(g, dist, cost, coord, SOURCE, DESTINATION)
  path_as_string = get_printable_path(destination_node)
  shortest_distance = destination_node.distance
  energy_cost = destination_node.energy_cost
  print_results("Task 3 with A* Search with constraint", path_as_string, shortest_distance, energy_cost,nodes_explored, total_time)

if __name__ == "__main__":
    main()