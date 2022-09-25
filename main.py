#To follow: PEP 8: Function and Variable Names convention.

from utils import open_json_data, print_results_no_constraints, print_results_with_constraints
import task_1 as task1
import task_2 as task2
from constants import SOURCE, DESTINATION

def main():
  g, dist, cost, coord = open_json_data()

  #TODO: Task 3
  get_task1_results(g, dist)
  get_task2_results(g, dist, cost)

def get_task1_results(g, dist):
    path1_details = task1.uniform_cost_search(g, dist, SOURCE, DESTINATION)
    print_results_no_constraints("Task 1", path1_details)

def get_task2_results(g, dist, cost):
  path2_details = task2.uniform_cost_search_with_constraint(g, dist, cost, SOURCE, DESTINATION)
  print_results_with_constraints("Task 2", path2_details)

if __name__ == "__main__":
    main()