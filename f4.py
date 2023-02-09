""" In a spy game you have received a letter containing a large sequence of numbers. 
This sequence contains within it a phone number that you must dial in order to save your friend. 
There are multiple duplicates of the digits in the sequence. In order to find the phone number 
you need to extract the unique elements from the array. The final unique array is the phone number 
that you will need to dial. 
Write a program to help you find this number. """

def findUnique(arr, N):
    currArr = []
    for i in range(N):
        if arr[i] not in currArr:
            currArr.append(arr[i])
            print(currArr[i], end=" ")
    
N = 9
arr = [2, 3, 4, 5, 6, 1, 2, 3, 4]
findUnique(arr, N)
