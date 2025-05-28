import random
import os
import zipfile

extensions = ['.py', '.txt', '.docx', '.pdf', '.csv', '.json', '.xml', '.html', '.css', '.js', '.php', '.sql', '.md', '.sh', '.bash', '.bat', '.cmd']

for ext in extensions: # for loop to iterate through the extensions
    num = random.randint(1, 5) # generate a random number between 1 and 5
    for i in range(1, num + 1): # for loop to iterate through the number of files to create
        filename = f"test{i}{ext}" # create the filename
        with open(filename, 'w') as f: # create the file
            f.write("") # write an empty string to the file

count = 0 # initialise the count
for file in os.listdir("./"): # for loop to iterate through the files
    if file.endswith(".txt"): # if the file ends with .txt
        count += 1 # increment the count

def zip_files(): # define the function
    with zipfile.ZipFile("mytxt.zip", "w") as zip: # create the zip file
        for file in os.listdir("./"): # for loop to iterate through the files
            if file.endswith(".txt"): # if the file ends with .txt
                zip.write(file) # write the file to the zip file

zip_files() # call the function
print(f"There are {count} txt files and compressed into a test.zip file") # print the number of files and the name of the zip file

