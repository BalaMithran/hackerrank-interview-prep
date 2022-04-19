#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'sortedInsert' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_DOUBLY_LINKED_LIST llist
#  2. INTEGER data
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node
def sortedInsert(llist, data):
    head = llist
    new = Node(data = data)
    while head.data < new.data and head.next!=None and head.next.data < new.data :
        head = head.next
    new.prev = head
    new.next = head.next
    head.next = new
    if new.next:
        new.next.prev = new
    return llist
    # nxt  = prev.next
    # prv = None
    # if nxt: prv = nxt.prev
    # data_node = DoublyLinkedListNode(data)
    # prev.next = data_node
    # prv.prev = data_node
    # data_node.next = prv
    # data_node.prev = prev
    # return head  
    # # Write your code here

if __name__ == '__main__':
