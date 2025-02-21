def count_words(text):
    words = text.split()
    wordcount = 0
    for word in words:
        wordcount += 1
    return wordcount

def sort_1(in_order_alphabet):
    return in_order_alphabet["num"]

def count_alphabet(text):
    ordered_alphabet = []
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
    for letter in lower_case_text:
        if letter.isalpha():
            alphabet[letter] += 1
    #print("Final Dictionary:", alphabet)
    for char, count in alphabet.items():
        let_dict = {"letter": char, "num": count}
        ordered_alphabet.append(let_dict)
    
    ordered_alphabet.sort(reverse=True, key=sort_1)
    return(ordered_alphabet)


def generate_report(ordered_alphabet, wordcount):
    lines = []
    lines.append ("Here is the report of Letters in frankenstein.")
    lines.append(f"{wordcount} words found in the document")
    for char_info in ordered_alphabet:
        line = f"The '{char_info['letter']}' character appears {char_info['num']} times"
        lines.append(line)
    lines.append ("--- End of Report ---")
    return "\n".join(lines)

#put new thing here dont forget to put stuff in main


def main():
    print("Starting to Read...")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        wordcount = count_words(file_contents)
        print(wordcount)
        ordered_chars = count_alphabet(file_contents)
        report = generate_report(ordered_chars, wordcount)
        print(report)
        count_alphabet(file_contents)
        
main()

