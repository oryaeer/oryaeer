import os

file_path1 = input("Enter path to first file: ")
absolute_path1 = os.path.abspath(file_path1)

file_path2 = input("Enter path to second file: ")
absolute_path2 = os.path.abspath(file_path2)

with open(file_path1, "r") as file1:
    contents1 = file1.read().splitlines()  # Split the file contents into a list of lines
    contents1 = [int(element) for element in contents1]  # Convert each element to an integer

with open(file_path2, "r") as file2:
    contents2 = file2.read().splitlines()  # Split the file contents into a list of lines
    contents2 = [int(element) for element in contents2]  # Convert each element to an integer

# Find the common elements between the two files
common_elements = list(set(contents1) & set(contents2))

# Sort the common elements in ascending order
common_elements.sort()

print(common_elements)

#fdfdfd
