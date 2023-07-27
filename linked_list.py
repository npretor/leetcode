class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None 

def readIntoLinkedList(filepath):
    first_link = Node(None) 
    current_link = first_link 

    line_nums = 0
    line_num_list = []
    with open(filepath) as f:
        while line_nums < 200000:
            word = f.readline() 
            current_link.next = Node(word) 
            current_link = current_link.next 
            line_nums+=1 

    return first_link

def printLinkedList(first_node):
    """Print all the words """
    current = first_link
    # print(current.data)
    while current.next is not None:
        current = current.next
        #print(current.data)

def getMiddleValue(first_node):
    """Get the middle value"""
    fast_node = first_node
    slow_node = first_node
    while fast_node.next is not None:
        fast_node = fast_node.next.next
        slow_node = slow_node.next 
    return slow_node.data


if __name__ == "__main__":
    first_link = readIntoLinkedList('english-words/words.txt')
    print(getMiddleValue(first_link)) 

