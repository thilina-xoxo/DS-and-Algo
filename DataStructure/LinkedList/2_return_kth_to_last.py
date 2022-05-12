from linked_list import LinkedList


def kth_to_last(ll, k):
    runner = current = ll.head

    for i in range(k):
        if not runner:
            return None  # linked list is empty
        runner = runner.next

    while runner:
        runner = runner.next
        current = current.next
        # we should always think one node beyoned tail, if current node in tail runner should point to next null pointer beyond tail

    return current


# writing test case


values = [10, 20, 30, 40, 50]
ll = linked = LinkedList(values)

print(kth_to_last(ll, 1))
