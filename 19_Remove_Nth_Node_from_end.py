class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    
    
    # Solution 1 -> chane it to list reverse remove and change it to linked list again
    if head.next == None:
        return None
    lst = []
    head_temp = head
    ln = 1
    while head_temp.next != None:
        head_temp = head_temp.next
        ln+=1
    head_temp = head
    for i in range(ln):
        lst.append(head_temp.val)
        head_temp = head_temp.next
    lst.pop(-n)
    lst.reverse()
    if len(lst) == 1:
        return(ListNode(lst[0]))
    last = ListNode(lst[0])
    for i in range(len(lst)-1):
        first  = ListNode(lst[i+1], last)
        last = first
    return first 
    
    # 2nd solution (most common one ) ->  Remember any link you change on any copy of linked list  all the linked list will effect from that. Like pointers from c/c++
    if head.next == None:
        return None
        
    slow = head
    fast = head
    
    for i in range(n):
        slow = slow.next
    if not slow:
        return head.next
    while slow.next:        
        fast = fast.next
        slow = slow.next
    fast.next = fast.next.next
    
    return head       
            