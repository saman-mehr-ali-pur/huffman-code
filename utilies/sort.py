import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPT_DIR=SCRIPT_DIR.replace('utilies','modules')
sys.path.append(os.path.dirname(SCRIPT_DIR))
import modules.classes



def sort_by_values(keys,values):
    if (len(keys)== 1):
        return keys,values
    if (len(keys) == 2):
        if (values[0]>values[1]):
            values[0],values[1] = values[1],values[0]
            keys[0],keys[1] = keys[1],values[0]
        return keys,values
    

    middle = len(keys)//2

    left_keys,left_values = sort_by_values(keys[:middle+1],values[:middle+1])
    right_keys,right_values = sort_by_values(keys[middle+1:],values[middle+1:])

    return merge(left_keys,left_values,right_keys,right_values)



def merge(left_keys,left_values,right_keys,right_values):
    i=j=0
    result_keys=[]
    result_values=[]
    while(i<len(left_keys) and j<len(right_keys)):
        
        if left_values[i]<right_values[j]:
            result_keys.append(left_keys[i])
            result_values.append(left_values[i])
            i+=1
        else:
            result_values.append(right_values[j])
            result_keys.append(right_keys[j])
            j+=1

       
    while i<len(left_keys):
        result_keys.append(left_keys[i])
        result_values.append(left_values[i])
        i+=1
        

    while j < len(right_keys):
        result_keys.append(right_keys[j])
        result_values.append(right_values[j])
        j+=1
        
    return result_keys,result_values



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
    
    






if __name__=='__main__':
    keys= ['b','c','d','a','e','f']
    values = [1,3,5,2,0,4]

    keys,values=sort_by_values(keys,values)
    print(keys)
    print(values)






