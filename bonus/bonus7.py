# LIST COMPREHENSION
# START with new version of items
filenames = ["x.doc", "x.report", "x.presentation"]

filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]

print(filenames)