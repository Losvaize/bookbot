def count_words(text):
    words = text.split()
    wordcount = 0
    for word in words:
        wordcount += 1
    return wordcount

def main():
    print("Starting to Read...")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        wordcount = count_words(file_contents)
        print(wordcount)
        #print(file_contents)
main()

