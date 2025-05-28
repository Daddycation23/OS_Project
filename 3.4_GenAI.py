import os
from zipfile import ZipFile

# Create sample files for demonstration
for ext in ['txt', 'md', 'py', 'sh', 'jpg']: # for loop to iterate through the extensions
    for i in range(1, 3): # for loop to iterate through the number of files to create
        open(f'sample{i}.{ext}', 'a').close() # create the file

# List all .txt files in the current directory
files = [f for f in os.listdir('.') if f.endswith('.txt')] # list all .txt files in the current directory
count = len(files) # count the number of .txt files

# Compress .txt files if any exist
if count > 0: # if the number of .txt files is greater than 0
    with ZipFile('mytxt.zip', 'w') as zipf: # create the zip file
        for file in files: # for loop to iterate through the files
            zipf.write(file) # write the file to the zip file
    print(f"There are number of {count} .txt files and compressed into a .zip file") # print the number of files and the name of the zip file
else:
    print("There are number of 0 .txt files and nothing to compress.") # print the number of files and the name of the zip file