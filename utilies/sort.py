import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPT_DIR=SCRIPT_DIR.replace('utilies','modules')
sys.path.append(os.path.dirname(SCRIPT_DIR))
import modules.classes



def sort_nodes(nodes):
    if len(nodes) > 1:
        mid = len(nodes) // 2  # Finding the mid of the array
        left = nodes[:mid]  # Dividing the array elements
        right = nodes[mid:]  # into 2 halves

        sort_nodes(left)
        sort_nodes(right)

        i = j = k = 0

        #  data to temp arrays L[] and R[]
        while i < len(left) and j < len(right):
            if left[i].data < right[j].data:
                nodes[k] = left[i]
                i += 1
            else:
                nodes[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            nodes[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nodes[k] = right[j]
            j += 1
            k += 1
    
    





