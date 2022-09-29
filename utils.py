import json
from constants import LINE_DELIMITER, FILE_PATH
# load in data files of JSON format
def open_json_data():

  with open(FILE_PATH + "G.json", "r") as file:
    g = json.load(file)
    file.close()

  with open(FILE_PATH + "Dist.json", "r") as file:
    dist = json.load(file)
    file.close()

  with open(FILE_PATH + "Cost.json", "r") as file:
    cost = json.load(file)
    file.close()

  with open(FILE_PATH + "Coord.json", "r") as file:
    coord = json.load(file)
    file.close()

  return g, dist, cost, coord

# display results in console in format specified.
def print_results(task_number,full_path_string, total_distance, total_energy_cost,nodes_explored):
  print(LINE_DELIMITER)
  print(task_number + " results: ")
  print(LINE_DELIMITER + "\n")
  print("Shortest path: " + full_path_string)
  print("Shortest distance: " + str(total_distance))
  print("Total energy cost: " + str(total_energy_cost))
  print("Total nodes explored: " + str(nodes_explored))

# getting the json key for both Cost and Dist dictionaries
def get_json_dict_key(current_node_id, adjacent_node_id):
  return current_node_id + ',' + adjacent_node_id

  

