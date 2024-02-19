def main():
    path = "books/frank.txt"
    content = get_file(path)
    word_number = wordcount(content)
    print(word_number)
    letters = count_letters(content)
    print(letters)

def wordcount(contents):
    return len(contents.split())

def get_file(path):
    with open(path) as f:
        return f.read()

def count_letters(content):
    dict = {}
    lowercase = content.lower()
    for char in lowercase:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict



main()