#!/bin/bash
extensions=('.py' '.txt' '.docx' '.pdf' '.csv' '.json' '.xml' '.html' '.css' '.js' '.php' '.sql' '.md' '.sh' '.bash' '.bat' '.cmd') # extensions to create

for ext in "${extensions[@]}"; do # for loop to iterate through the extensions
    num=$(( RANDOM % 5 + 1)) # generate a random number between 1 and 5
    for (( i=1; i<=num; i++ )); do # for loop to iterate through the number of files to create
        filename="test${i}${ext}" # create the filename
        touch $filename # create the file
    done
done

count=0 # initialise the count
for file in *.txt; do # for loop to iterate through the files
    [[ -e "$file" ]] || continue # if the file does not exist, continue
    ((count++)) # increment the count
done

zip -rq mytxt.zip *.txt # compress the files

echo "There are $count txt files and compressed into a test.zip file" # print the number of files and the name of the zip file


