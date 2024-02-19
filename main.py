def main():
    path = "books/frank.txt"
    contents = get_file(path)
    word_number = wordcount(contents)
    print(word_number)

def wordcount(contents):
    return len(contents.split())

def get_file(path):
    with open(path) as f:
        return f.read()

main()