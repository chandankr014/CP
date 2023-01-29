""" total number of continuous sub-array whose sum is K """
import random

arr = []
k = 100

for i in range(1000):
    n = random.randint(-1000, 1000)
    arr.append(n)
print(arr)

# function
def find_cont_subarray(arr, k):
    longestSA = []
    for i in range(len(arr)):
        currentLongest = 1
        pivot = arr[i]
        for j in range(i+1, len(arr), 1):
            if pivot <= k:
                pivot = pivot + arr[j]
                currentLongest += 1
                if pivot==k:
                    longestSA.append(currentLongest)
    try:
        print(longestSA)
        print(max(longestSA) ,"is highest continuous subarray")
    except ValueError:
        print("empty array")


if __name__=="__main__":
    # arr = [1,2,3,4,0,5,5,3,2]
    find_cont_subarray(arr, k)