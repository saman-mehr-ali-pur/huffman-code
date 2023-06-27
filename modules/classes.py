

class node:

    def __init__(self,left_child,right_child,data):
        self.left_child = left_child
        self.right_child = right_child
        self.data= data


class leaf(node):
    def __init__(self, left_child, right_child, data,letter):
        super().__init__(left_child, right_child, data)
        self.letter= letter

    
        