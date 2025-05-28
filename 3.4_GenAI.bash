#!/bin/bash
for ext in txt md py sh jpg; do # Loop through specified file extensions    
    for i in {1..2}; do # Loop through the number of files to create
        touch "sample${i}.${ext}" # Create the file with the specified extension
    done
done

# List and count .txt files
count=$(ls -1 *.txt 2>/dev/null | wc -l) # Count the number of .txt files

# Compress .txt files if any exist
if [ "$count" -gt 0 ]; then # If there are .txt files
    zip -q mytxt.zip *.txt # Compress the .txt files into a .zip file
    echo "There are number of $count .txt files and compressed into a .zip file" # Print the number of files and the name of the zip file
else
    echo "There are number of 0 .txt files and nothing to compress." # Print the number of files and the name of the zip file   
fi 