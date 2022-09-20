'''def findBigestNum(nums):
    bigest = nums[0]
    for i in nums:
        if i > bigest:
            bigest = i
    return(bigest)

listnum = [4, 5, 17, 3, 2, 9]

print(findBigestNum(listnum))
print(max(listnum))
print(min(listnum))'''

def threeSum(nums):
    Sum3 = nums[0]
    for i in nums:
        if i % Sum3 == 0: #i หาร 3 ลงตัว
            Sum3 += i
    return(Sum3)

listnum = [4, 5, 17, 3, 2, 9]

print(threeSum(listnum))