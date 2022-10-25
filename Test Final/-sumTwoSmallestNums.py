def sumTwoSmallestNums (i):
    a = min(i)
    c = i - a
    b = min(c)
    u = a + b
    return u


print(sumTwoSmallestNums([19, 5, 42, 2, 77]))
print(sumTwoSmallestNums([10, 343445353, 3453545353453]))
print(sumTwoSmallestNums([2, 9, 6, -1]))
print(sumTwoSmallestNums([879, 953, 694, -847, 342, 221, -91, -723, 791, -587]))
print(sumTwoSmallestNums([3683, 2902, 3951, -475, 1617, -2385]))