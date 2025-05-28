#!/bin/bash
for ext in txt md py sh jpg; do
    for i in {1..2}; do
        touch "sample${i}.${ext}"
    done
done

# List and count .txt files
count=$(ls -1 *.txt 2>/dev/null | wc -l)

# Compress .txt files if any exist
if [ "$count" -gt 0 ]; then
    zip -q mytxt.zip *.txt
    echo "There are number of $count .txt files and compressed into a .zip file"
else
    echo "There are number of 0 .txt files and nothing to compress."
fi 