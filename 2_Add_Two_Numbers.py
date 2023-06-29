# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    """
    Yes, that is correct. In the ListNode class definition you provided, each node contains a val attribute to store the value of the node and a next attribute to point to the next node in the linked list.

Linked lists are a data structure where elements are connected through references, specifically through the next attribute. Each node in the linked list holds a value (val) and a reference (next) to the next node in the list.

To traverse the linked list and access the next element, you need to follow the next reference of each node. Starting from the head node, you can access the value of the current node and then move to the next node by accessing its next attribute. This process continues until you reach the end of the linked list, where the next attribute of the last node is None.
    """


def addTwoNumbers(l1, l2):
    """You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.




        Args:
            l1 (linkedlist): contains only digits
            l2 (linkedlist): only digits

        Returns:
            linkedlist: digits
    """

    if (
        l1.next is None
    ):  # if linkedlist contains only one digit then no next exist! The only digit will bel1.val
        n1 = l1.val

    else:
        num_1 = []  # this is the list to collect all the digits comes from linked list

        while l1 is not None:  # loop till we get to the end node
            num_1.append(
                str(l1.val)
            )  # collecting the values of l1 linked list at the num_1 list
            l1 = (
                l1.next
            )  # after every single value added to num_1 list ne go the the next node

        num_1.append(
            str(l1.val)
        )  # when we comme to the last node still we have one more value to add!

        num_1 = num_1[::-1]  # reverse the list
        n1 = int("".join(num_1))  # join the string nums and change it to int

    if l2.next is None:
        n2 = l2.val
    else:
        num_2 = []
        while l2.next != None:
            num_2.append(str(l2.val))
            l2 = l2.next

        num_2.append(str(l2.val))
        num_2 = num_2[::-1]
        n2 = int("".join(num_2))

    n_total = (
        n1 + n2
    )  # we get our total here and now we need to take this every character to a linked list

    n_total = str(n_total)  # change it to a str
    n_total = list(n_total)
    n_total = n_total[::-1]

    res = ListNode(
        0
    )  # first link has no next value  it is a dummy object we need the first and the all next values
    temp = res
    for i in range(len(n_total)):
        temp.next = ListNode(int(n_total[i]))
        temp = temp.next
    return res.next
