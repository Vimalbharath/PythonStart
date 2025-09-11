import sys
import os

# Get the absolute path to the directory you want to add.
# This example adds the parent directory of the current script's folder.
directory_to_add = os.path.dirname(os.path.abspath("D:\\Bharath\\Python"))

# Add the directory to the system path.
sys.path.append(directory_to_add)
print(sys.path)