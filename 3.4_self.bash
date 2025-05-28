extensions=('.py' '.txt' '.docx' '.pdf' '.csv' '.json' '.xml' '.html' '.css' '.js' '.php' '.sql' '.md' '.sh' '.bash' '.bat' '.cmd' '.ps1' '.ps2' '.ps3' '.ps4' '.ps5' '.ps6' '.ps7' '.ps8' '.ps9' '.ps10')

for ext in "${extensions[@]}"; do
    num=$RANDOM
    for i in {1..$num}; do
        filename="test$num$ext"
        touch $filename
    done
done

count=0
for file in "${extensions[@]}"; do
    if [[ "$file" == *.txt ]]; then
        count+=1
    fi
done

zip -r test.zip .

echo "There are $count txt files and compressed into a test.zip file"


