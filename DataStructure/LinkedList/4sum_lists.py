from linked_list import LinkedList

# check linked list null or not in the beginning

def sum_lists(ll_a,ll_b):
    n1,n2= ll_a.head, ll_b.head
    ll = LinkedList() # this is new linked list to store the answer

    carry = 0

    while n1 or n2: # care full about null pointer exception
        result = carry
        if n1:
            result += n1.value
            n1=n1.next
        if n2:
            result += n2.value
            n2=n2.next

        ll.add(result%10)
        carry = result // 10

        if carry:
            ll.add(carry)
        return ll

def example():
    #ll_a = 6LinkedList.generate(4,0,9)
    #ll_b = 6LinkedList.generate(3,0,9)
    values_a = [1,2,3]
    values_b = [5,4,9]
    ll_a = LinkedList(values_a)
    ll_b = LinkedList(values_b)
    print(sum_lists(ll_a,ll_b))

if __name__ == "__main__":
    example()

