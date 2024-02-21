import sys
import os

root_dir = os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 0)[0]
sys.path.append(root_dir)
print(root_dir)