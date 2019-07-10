def solution(A: list):
    A.sort()
    len_a = len(A)
    for i in range(len_a - 1):
        if A[i] > 0:
            if (A[i+1] - A[i]) > 1:
                return A[i] + 1
            elif i == len_a - 2:
                return A[i+1] + 1

    return 1
