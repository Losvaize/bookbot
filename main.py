def count_words(text):
    words = text.split()
    wordcount = 0
    for word in words:
        wordcount += 1
    return wordcount

def count_alphabet(text):
    alphabet = {
        "a" : 0,
        "b" : 0,
        'c' : 0,
        'd' : 0,
        'e' : 0,
        'f' : 0,
        'g' : 0,
        'h' : 0,
        'i' : 0,
        'j' : 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
        }
    lower_case_text = text.lower()
    for letters in alphabet:
        pass

def main():
    print("Starting to Read...")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        wordcount = count_words(file_contents)
        print(wordcount)
        #print(file_contents)
main()

