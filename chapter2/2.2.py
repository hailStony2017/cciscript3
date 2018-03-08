#!/usr/bin/python

'''
Return Kth to Last

Implement an algorithm to find the kth to last element of a singly linked list.
'''

from classes.LinkedList import LinkedList
import unittest


def find_kth_to_last(ll, k):
    elements = []
    # Find tail of linked list
    curr = ll.head
    while curr.next:
        elements.append(curr.data)
        curr = curr.next
    elements.append(curr.data)

    return elements[-k:]


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        (LinkedList([1,2,3,4,5,6]), 2, [5,6])
    ]

    def test_remove_dup(self):
        for [ll, k, targeted_elements] in self.data:
            elements_found = find_kth_to_last(ll, k)
            self.assertEqual(elements_found, targeted_elements)


if __name__ == "__main__":
    unittest.main()

