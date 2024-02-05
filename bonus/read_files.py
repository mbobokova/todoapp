import glob

myfiles = glob.glob("../files_bonus/*.txt")

print(myfiles)

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read().upper())