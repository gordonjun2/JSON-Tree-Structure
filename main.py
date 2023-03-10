import ast
import argparse
import re

def generate_tree_structure(data, level=0, printed=[]):
    if isinstance(data, dict):
        if list(data.keys()) not in printed:
            printed.append(list(data.keys()))
            for key, value in data.items():
                print('\t' * level + str(key))
                generate_tree_structure(value, level+1, [])
    elif isinstance(data, list):
        duplicates_flag = False
        for item in data:
            if isinstance(item, dict):
                if list(item.keys()) not in printed:
                    print('\t' * level + "[List]")
                else:
                    duplicates_flag = True
            generate_tree_structure(item, level+1, printed)
        if duplicates_flag == True:
            print('\t' * level + "...")
        printed=[]

# Create a new parser object
parser = argparse.ArgumentParser(description='parse the file with the JSON / dictionary')

# Add a command-line argument for the file name
parser.add_argument('-f', type=str, default='json.txt',
                    help='the name of the file to parse')

# Parse the command-line arguments
args = parser.parse_args()

# Retrieve the file name from the parsed arguments
filename = args.f

# Open the .txt file containing the JSON data
with open(filename, 'r') as file:
    # Read the contents of the file as a string first
    dict_str = file.read()
    dict_str = dict_str.replace("null", "''")
    data = ast.literal_eval(dict_str)

# Generate tree structure of all keys
generate_tree_structure(data)