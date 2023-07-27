""" Documentation
A trie (pronounced as "try") or prefix tree is 
a tree data structure 
used to efficiently store and retrieve keys 
in a dataset of strings. 

There are various applications of this data structure, 
such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.

void insert(String word) Inserts the string word into the trie.

boolean search(String word) Returns true 
    if the string word is in the trie (i.e., was inserted before), 
    and false otherwise.

boolean startsWith(String prefix) 
    Returns true 
        if there is a previously inserted string word 
    that has the prefix prefix, 
    and false otherwise.
"""

class Node:
    def __init__(self) -> None:
        # self.values = {
        #     'a': Node,
        #     'b': Node
        #     } 

        self.values = {} 
        self.word = False 


class Trie:
    """
    This seems to be a directed graph, where the first node contains the first letters 
    """
    def __init__(self) -> None:
        # self.values = {
        #     'a': Node,
        #     'b': Node
        #     } 

        # self.values = {} 
        # self.word = False 

        self.root = Node()

    def insert(self, word):
        """
        First take in the string. Is the first letter in our lookup table
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

    def search(self, search_word):
        """
        For each character, get the next sub-node in the trie. At the end, check if word is true 
        """
        currentNode = self.root 
        for char in search_word:
            print(char)
            if char in currentNode.values:
                # Set current as the next node 
                currentNode = currentNode.values[char] 
            else:
                return False
            
        return currentNode.word
        
    
    def startsWith(self, prefix):
        """
        Returns all words that start with the prefix. 
        Starting at the root level, check each character to see if it's a word. 
        Check if the character has a Node, and check those. 
        """
        words = [] 
        prefix_plus = [prefix]
        currentNode = self.root 
        # Example, we get 'ca' . Go to the item there 
        
        # Go the the prefix node
        for char in prefix:
            if char in currentNode.values:
                # Set current as the next node 
                currentNode = currentNode.values[char]        
            else:
                return [] 
            
        import ipdb; ipdb.set_trace() 
        

        # We should not be at the node 'a'. 
        # Prefix should be 'ca' 
        def recursive_check(self, currentNode, prefix=prefix, to_check=[]):
            """
            Check if this node is a word, and if so, add it 
            """
            if currentNode.word:
                


            for char in currentNode.values:
                if currentNode.values[char].word:
                    to_check.append(char) 
            pass 


        # Check if each character is a word. 
        # If so, recursively check 
        for char in currentNode.values:
            if currentNode.values[char].word:
                currentNode.values[char] 

                print(currentNode.values[char]) 
        
        return False


if __name__ == "__main__":
    t = Trie() 
    
    t.insert('cat') 
    t.insert('car') 
    t.insert('rat') 
    t.insert('cats')  

    print(t.root.values, t.root.word) 

    print('Searching for cat') 
    print(t.search('cat')) 
    print(t.search('bat')) 
    print(t.search('can')) 
    print(t.search('')) 
    print(t.search(' ')) 

    print(t.startsWith('ca')) 
