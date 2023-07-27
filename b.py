class Node:
    def __init__(self, val) -> None:
        self.chars = {} 

    def add(self, str):
        if str[0] in self.chars: 
            #self.add(str[1:])
            self.chars[str[0]].add(str[1:])
        else:
            self.chars[str[0]] = Node(str[0]) 



# Save a few words 
words = ['flower', 'float', 'flout']  

t = Node()

t.add('flower')
print(t.chars)

"""
Add the word to the first node. 
    Does it exist? 
    If not add it, and go to that node 

"""