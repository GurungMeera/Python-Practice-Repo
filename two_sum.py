# This program checks if the list contains two numbers that would add to the target number.

def two_sums(arr, target):
    """this function returns true if two numbers in the list adds up to equal the target number.
    The run time for this is O(n^2)"""
    # run time is O(n^2) because run time for one for loop is n and second is also n. n*n = n^2
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return True

    return False


# answer = two_sums([1,4,3,7,2,-2], 5)
# print(answer)

def two_sum(arr, target):
    """This function takes two parameters(arr and target) and returns how many unique addition of
    two number equals the target number from the list of numbers passed"""
    # the run time for this function is O(n).
    count = 0
    new_set = set()
    for i in range(len(arr)):
        if target - arr[i] in new_set:
            count += 1
        new_set.add(arr[i])

    return count


# answer = two_sum([1,4,3,7,2,-2], 5)
# print(answer)







