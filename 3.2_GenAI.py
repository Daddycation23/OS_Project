def find_largest(arr): # define function
    if not arr: # if the array is empty
        raise ValueError("Array must not be empty") # raise an error
    largest = arr[0] # initialise largest number
    for num in arr[1:]: # for loop to iterate through the array
        if num > largest: # if the current number is greater than the largest number
            largest = num # update the largest number
    return largest # return the largest number

if __name__ == "__main__": # if the file is run directly
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5] # testing array
    print(f"The largest number is: {find_largest(arr)}") # print the largest number