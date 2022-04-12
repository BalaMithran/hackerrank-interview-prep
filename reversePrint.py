#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end='')

        node = node.next

        if node:
            print(sep, end='')

#
# Complete the 'reversePrint' function below.
#
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

# def reversePrint(llist):
#     prev = []
#     while llist:
#         prev.append(llist.data)
#         llist = llist.next
#     prev = prev[::-1]
#     for i in prev:
#         print(i)
def reversePrint(llist):   
   head = llist
   if llist.next:
        reversePrint(llist.next)
   print(head.data) 
        
        
    # Write your code here

if __name__ == '__main__':