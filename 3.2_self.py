def LargestNum(arr): # define function
    largest = 0 # initialise largest number
    for i in range(len(arr)): # for loop to iterate through the array
        if arr[i] > largest: # if the current number is greater than the largest number
            largest = arr[i] # update the largest number
    return largest # return the largest number

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9] # testing array
print(LargestNum(arr)) # print the largest number