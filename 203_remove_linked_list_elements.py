class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


test_elements = [
    [1,2,6,3,4,5,6] ,
    [7,7,7,7]
]

lll = []

for test in test_elements:
    head = ListNode(test[0]) 
    current_node = head 
    for item in test[1:]:
        current_node.next = ListNode(item)
    lll.append(head)
 
for test in lll:
    