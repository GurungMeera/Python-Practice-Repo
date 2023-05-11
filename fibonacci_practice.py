# this is a practice of Fibonacci sequence using recursive that takes
# a positive integer parameter and returns the number at that position of the Fibonacci sequence.

def fib(index):
    """this  recursive function takes a positive integer as a position
     of the Fib sequence and return the Fib number at that position"""
    if index <= 1:
        return index

    else:
        return fib(index-1) + fib(index-2)


#print(fib(6))


# practice with lists
def fib(index):
    """this function takes positive integer as parameter of
    the fib index to get the Fib number at that index using list"""
    seq = [0,1]
    for i in range(2, index+1):
        seq.append(seq[-1] + seq[-2])  # adds the last number and second to last number on the list
    return seq[-1]

#print(fib(3))


def fib(index):
    """this iterable function takes positive integer as
    the position of Fib sequence and returns the fib number at that position"""
    if index == 0:
        return 0
    if index == 1 and index == 2:
        return 1

    index_1 = 1
    index_2 = 1
    answer = 0

    for index in range(3, index+1):
        answer = index_1 + index_2
        index_1 = index_2
        index_2 = answer

    return answer


#print(fib(6))

