


class Node:
    def __init__(self) -> None:
        """
        self.values = {
            'a': Node,
            'b': Node
            } 
        """
        self.values = {} 
        self.word = False 


class Trie:
    def __init__(self) -> None:
        self.root = Node() 

    def insert(self, word):
        """ 
        3 cases
            Root is none 
            Root does not have the value 
            Root has the value 

        Loop through each character. 
        If it is in the node, 
            go to the next.
            At the last node/index, 
            add one more empty node with word=True
        """
        currentNode = self.root 

        for character in word:
            # Insert each character 
            if character in currentNode.values:
                currentNode = currentNode.values[character]
            else:
                currentNode.values[character] = Node() 
                currentNode = currentNode.values[character] 

        currentNode.word = True 

        
        # # Root is none 
        # if self.root == None:
        #     self.root = Node()

        # # Root does not have the value 
        # if self.root and word[0] not in self.root.values:
        #     self.root.values[word[0]] = Node 

        # # Root has the value 
        # if word[0] in self.root.values:
        #     # go to the next node in root 


# if __name__ == "__main__":
t = Trie() 
t.insert('cat') 
t.insert('cats') 
import ipdb; ipdb.set_trace()

