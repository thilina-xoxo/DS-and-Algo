T = int(input()) # integer input

A = [] # price of the house

for t in range(T):

    N,B = [int(s) for s in input().split()]
    A = [int(a) for a in input().split()]
    A.sort() # sort the house prices

    count = 0
    sum = 0

    for i in range(len(A)):
        sum += A[i]

        if (sum > B):
            print("Case #{}: {}".format(t+1, count))
            break
        count += 1
    A.clear()







