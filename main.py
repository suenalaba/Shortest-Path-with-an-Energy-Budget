#To follow: PEP 8: Function and Variable Names convention.

from utils import open_json_data, print_results_no_constraints
import task_1 as task1
from constants import SOURCE, DESTINATION

def main():
  g, dist, cost, coord = open_json_data()

  #TODO: Task 2 & 3
  get_task1_results(g, dist)

def get_task1_results(g, dist):
    path1_details = task1.uniform_cost_search(g, dist, SOURCE, DESTINATION)
    print_results_no_constraints("Task 1", path1_details)

if __name__ == "__main__":
    main()