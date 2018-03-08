#!/usr/bin/python

'''
Remove Dups:

Write code to remove duplicates from an unsorted linked list.

FOLLOW UP:

How would you solve this problem if a temporary buffer is not allowed?
'''

from classes.LinkedList import LinkedList
import unittest

def remove_dups_from_linkedlist(orig_ll):
    seen_values = []
    new_ll = LinkedList(None)
    for item in orig_ll:
        if item.data not in seen_values:
            new_ll.add_to_end(item.data)
            seen_values.append(item.data)

    return new_ll

def remove_dups_from_linkedlist_no_buffer(orig_ll):
    print(orig_ll)
    if len(orig_ll) < 2:
        return orig_ll

    first_pt = orig_ll.head
    while first_pt:
        second_pt = first_pt
        while second_pt.next:
            if second_pt.next.data == first_pt.data:
                second_pt.next = second_pt.next.next
            else:
                second_pt = second_pt.next
        first_pt = first_pt.next
    print(orig_ll)
    return orig_ll


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        (LinkedList([1,2,2,3,2,4,4,5]), LinkedList([1,2,3,4,5]))
    ]

    def test_remove_dup(self):
        for [orig_ll, new_ll] in self.data:
            removed_ll = remove_dups_from_linkedlist(orig_ll)
            self.assertEqual(str(new_ll), str(removed_ll))

    def test_remove_dup_no_buffer(self):
        for [orig_ll, new_ll] in self.data:
            removed_ll = remove_dups_from_linkedlist_no_buffer(orig_ll)
            self.assertEqual(str(new_ll), str(removed_ll))

if __name__ == "__main__":
    unittest.main()
