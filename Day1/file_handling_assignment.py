# Write a python program to identify the longest words in a file, a.txt

def fetch_longest_word():
    file_data = []
    with open('a.txt', 'r') as filee:
        file_data = filee.readlines()
    file_data = [line[:-1] for line in file_data]
    word_len = len(file_data[0])
    longest_word = file_data[0]
    for word in file_data:
        if len(word) > word_len:
            longest_word = word
            word_len = len(word)
    return longest_word



if __name__ == "__main__":
    longest_word = fetch_longest_word()
    print(longest_word)





