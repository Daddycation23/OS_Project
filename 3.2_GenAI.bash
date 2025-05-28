#!/bin/bash
arr=(3 1 4 1 5 9 2 6 5) # testing array
largest=${arr[0]} # initialise largest number
for num in "${arr[@]}"; do # for loop to iterate through the array
    if (( num > largest )); then # if the current number is greater than the largest number
        largest=$num # update the largest number
    fi # end of if statement
done # end of for loop
echo "The largest number is: $largest" # print the largest number