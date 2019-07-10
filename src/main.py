def solution(A: list):
    # at first, sort the list
    # if you still need the list, do `sorted_a = sorted(A)`
    A.sort()  # sort in place, it's memory efficient
    len_a = len(A)  # don't always count the list length, do it once

    for i in range(len_a - 1):
        if A[i] > 0:  # simplest case, find a spot between 2 numbers
            # if the difference between 2 consecutive items is more then 1,
            #  then return the 1st item + 1
            if (A[i+1] - A[i]) > 1:
                return A[i] + 1

        # return 1 in case all numbers are negative or there's only 1
        # number > 0
        # - if all previous numbers were not positive
        #    and the last number is anything but 1
        if i == (len_a - 2) and A[i] <= 0 and A[i+1] != 1:
            return 1

    # this covers the rest of the cases
    # - there was no free spot between the sorted numbers
    # - all number but the last one were not positive and last number is 1
    return A[len_a - 1] + 1
