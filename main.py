def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    # print(file_contents)
    words = file_contents.split()
    word_count = len(words)
    print(f"Number of words is: {word_count}")
    contents_lowercase = file_contents.lower()
    letter_count = {}
    for char in "abcdefghijklmnopqrstuvwxyz":
        letter_count[contents_lowercase.count(char)] = char
    sorted_count = sorted(letter_count.items(), reverse=True)
    for i in sorted_count:
        print(f"The letter {i[1]} occurred {i[0]} times")
    
main()