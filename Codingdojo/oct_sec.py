'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

'''

inp = [1,2,3,4,5,6,7]
k =3
for i in range(0,k):
    temp = inp[len(inp)-1]
    for j in range((len(inp)-1),-1,-1):
        print(j)
        inp[j] = inp[j-1]
    inp[0] = temp
print(inp)