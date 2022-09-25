import json
from constants import LINE_DELIMITER
from path_properties import PathDetailsWithNoConstraint

def open_json_data():

  with open("G.json", "r") as file:
    g = json.load(file)
    file.close()

  with open("Dist.json", "r") as file:
    dist = json.load(file)
    file.close()

  with open("Cost.json", "r") as file:
    cost = json.load(file)
    file.close()

  with open("Coord.json", "r") as file:
    coord = json.load(file)
    file.close()

  return g, dist, cost, coord
  
def print_results_no_constraints(taskNumber, path_details: PathDetailsWithNoConstraint):
  print(LINE_DELIMITER)
  print(taskNumber + " results: ")
  print(LINE_DELIMITER + "\n")
  print("Shortest path: " + path_details.path_desc + ".")
  print("Shortest distance: " + str(path_details.path_length) + ".")


