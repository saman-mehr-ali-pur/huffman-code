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
    if (len(nodes == 1)):
        return nodes
    elif (len(nodes)==2):
        if (nodes[0].data>nodes[1].data):
            nodes[0].data,nodes[1].data = nodes[1].data,nodes[0].data
        
        return nodes
    

    middle = len(nodes)+1

    left_nodes = sort_nodes(nodes[:middle])
    right_nodes = sort_nodes(nodes[middle:])

    result=[]

    i=j=0

    while i< len(left_nodes) and j< len(right_nodes):

        if left_nodes[i].data<right_nodes[j].data:
            result.append(left_nodes[i])
            i+=1

        else:
            result.append(right_nodes[j])
            j+=1

        while i <len(left_nodes):
            result.append(left_nodes[i])
            i+=1

        while j < len(right_nodes):
            result.append(right_nodes)
            j+=1


    return result






if __name__=='__main__':
    keys= ['b','c','d','a','e','f']
    values = [1,3,5,2,0,4]

    keys,values=sort_by_values(keys,values)
    print(keys)
    print(__file__)



