def main():
    print("Starting to Read...")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
main()

def wordcount(text):
    words = file_contents.split()

