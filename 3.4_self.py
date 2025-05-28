import random
import os
import zipfile

extensions = ['.py', '.txt', '.docx', '.pdf', '.csv', '.json', '.xml', '.html', '.css', '.js', '.php', '.sql', '.md', '.sh', '.bash', '.bat', '.cmd', '.ps1', '.ps2', '.ps3', '.ps4', '.ps5', '.ps6', '.ps7', '.ps8', '.ps9', '.ps10']

for ext in extensions:
    num = random.randint(1, 10)
    for i in range(num):
        filename = f"test{i}{ext}"
        with open(filename, 'w') as f:
            f.write("")

count = 0
for file in os.listdir("./"):
    if file.endswith(".txt"):
        count += 1

def zip_files():
    with zipfile.ZipFile("test.zip", "w") as zip:
        for file in os.listdir("./"):
            if file.endswith(".txt"):
                zip.write(file)

zip_files()
print(f"There are {count} txt files and compressed into a .zip file")

