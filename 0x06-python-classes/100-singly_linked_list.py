#!/usr/bin/python3
"""class Node that defines a node of a singly linked list by"""


class Node:
    """defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """intialization"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter method for data"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """setter method for data"""
        if (type(value) is not int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """getter method for next_node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """setter method for next_node"""
        if (value is not isinstance(value, Node) and not None):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """defines a singly linked list"""
    def __init__(self):
        """intialization"""
        self.head = None

    def sorted_insert(self, value):
        """inserts a new Node into sorted list"""
        node = Node(value)
        if not self.head:
            self.head = node
            return
        if value < self.head.data:
            node.next_node = self.head
            self.head = node
            return
        ptr = self.head
        while ptr.next_node and ptr.next_node.data < value:
            ptr = ptr.next_node
        if ptr.next_node:
            node.next_node = ptr.next_node
        ptr.next_node = node

    def __str__(self):
        """print the list to stdout"""
        ptr = self.head
        new_string = ""
        while ptr:
            new_string += str(ptr.data) + "\n"
            ptr = ptr.next_node
        return (new_string[:-1])
