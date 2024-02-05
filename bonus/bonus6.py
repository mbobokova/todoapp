contents = ["As the sun set behind the mountains, the sky transformed into a breathtaking "
            "canvas of orange and purple hues.",
            "The old library, with its towering shelves of books, held the whispers of a "
            "thousand stories waiting to be discovered.",
            "In the quiet of the early morning, the only sound was the gentle murmur of the "
            "river as it wound its way through the forest."]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files_bonus/{filename}", 'w')
    file.write(content)
