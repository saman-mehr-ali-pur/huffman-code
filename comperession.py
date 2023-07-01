from modules import classes as cls
from utilies import sort

def text_analyzer(input_string):                # this method find the frequency of all symbles
    symble_frequency={}                         # in text and return a dictionary object 
    for symble in input_string:
        if symble not in symble_frequency.keys():
            symble_frequency[symble] = 1
            continue
        else:
            symble_frequency[symble]+=1

    return symble_frequency



def key_genrator(letters_frequency):                
    keys = list(letters_frequency.keys())
    values = list(letters_frequency.values())   
    nodes = node_genrator(keys,values)
    tree=tree_genrator(nodes)
    codes={}
    for item in keys:
        codes[item]=""

    code_genrator(tree,codes,"")
    return codes





def node_genrator(keys,values):                 #this method gives keys and values
    resultArray = []                            # and return a list object of nodes
    new_node= None
    for i in range(len(keys)):
        new_node = cls.leaf(None,None,values[i],keys[i])
        resultArray.append(new_node)

    return resultArray



def tree_genrator(nodes):                   #this method will make a tree with nodes
    m = len(nodes)
    while(m>1):
        sort.sort_nodes(nodes) 
        new_node = cls.node(nodes[0],nodes[1],nodes[0].data+nodes[1].data)
        nodes.pop(0)
        nodes.pop(0)
        nodes.append(new_node)       
        m=m-1
    return nodes[0]



def code_genrator(tree,codes,str_code):                 #this method will compute huffman code of
    if isinstance(tree,cls.leaf):                       # all symbles
        codes[tree.letter]= str_code
        return
    
    code_genrator(tree.left_child,codes,str_code+"0")
    code_genrator(tree.right_child,codes,str_code+"1")




def compersor(input_file_string):                       #compersor method will return two object
    compesed_string=""                                  #first one is a string object that 
    key_string=''                                       #contains compressed string and another one
    keys=key_genrator(text_analyzer(input_file_string)) #contains key for decompressing
    for symble in input_file_string:
        compesed_string+=keys[symble]

    for i in keys.keys():
        key_string+=i+" : "+keys[i]+'\n'
    return compesed_string,key_string


if __name__=="__main__":

    letters={'f':5,'e':9,'c':12,'a':45,'d':16,'b':13}
    print(key_genrator(letters))

