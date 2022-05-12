# what is tempory buffer
# Write code to remove duplicates from an unsorted linked list
from linked_list import LinkedList


def remove_duplicates(linked_list):
    current = linked_list.head
    previous = None
    seen = set()  # only unique items can store in a set no duplicates

    while current:
        if current.value in seen:
            previous.next = current.next
        else:
            seen.add(current.value)
            previous = current
        current = current.next
    linked_list.tail = previous
    return linked_list

    # follow up method ? what is tempory buffer
