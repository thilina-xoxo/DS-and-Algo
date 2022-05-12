# linked list class

class LinkedListNode:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

    # what is this
    def __str__(self):
        return str(self.value)  # to get the value of the linked list node


class LinkedList:
    def __init__(self, values=None):   # constructor
        self.head = None    # this head pointer is used to reffer first node
        self.tale = None    # this tale pointer is used to reffer last node
        # another method to add multiple values

        if values is not None:
            self.add_multiple(values)

    def _iter_(self):
        current = self.head
        while current:
            # result =[]
            # result.append(current)
            # return result
            yield current  # what is yield here this is statement like return
            current = current.next

    def __str__(self):
        values = [str(x) for x in self]
        return "->".join(values)   # what is this join operation

    # lenght of linked list
    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    # what is values return
    def values(self):
        return [x.value for x in self]

    # add node to 6LinkedList
    def add(self, value):
        if self.head is None:  # this is same as head == Null; linked list is empty
            self.tail = self.head = LinkedListNode(value)

        else:
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next

        return self.tail  # this self.tail is linked list contain value, next pointer and prev and this is singly linke list

    # add node in the beginning
    # keep remember to check linked list is empty or not empty
    def add_to_beginning(self, value):
        if self.head is None:
            self.head = self.tail = LinkedListNode(value)
        else:
            self.head = LinkedListNode(value, self.head)
        return self.head

    # add multiple nodes to linked LinkedListNode

    def add_multiple(self, values):  # value is not add to the beginning of the linked list
        for v in values:
            self.add(v)

    # what is @ classmethod
    @classmethod
    def generate(cls, k, min_value, max_value):
        return cls(random.choices(range(min_value, max_value), k=k))

    # this doubly linked list is sigly linked list but can traverse in reverse order


class DoublyLinkedList(LinkedList):

    def add(self, value):
        if self.head is None:
            self.head = self.tail = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value, None, self.tail.prev)
            self.tail = self.tail.next
        return self.tail


# check linke list

ll = LinkedList([1,2,3])
print(type(ll.head))  # this gives object type



