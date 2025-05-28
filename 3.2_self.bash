#!/bin/bash
arr=(1 2 3 4 5 6 7 8 9) #testing array
largest=0 #initialising largest number
for i in "${arr[@]}"; do #for loop to iterate through the array
    if [ "$i" -gt "$largest" ]; then #if the current number is greater than the largest number
        largest=$i #update the largest number
    fi #end of if statement
done #end of for loop
echo $largest #print the largest number