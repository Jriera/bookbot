

def main():
    with open("./books/fankenstein.txt") as f:
        book_contents = f.read()
        words = word_count(book_contents)
        letters = letter_count(book_contents)
        reporter(words,letters)
    
def word_count(contents):
    words_list = contents.split()
    return len(words_list)

def letter_count(contents):
    lowered_case = contents.lower()
    letter_dictionary = {}
    for letter in lowered_case:
        try:
            letter_dictionary[letter] += 1
        except:
            letter_dictionary.update({letter:1})
    letters_list = formatter(letter_dictionary)
    sorted_list = sorter(letters_list,"count")
    return sorted_list

def formatter(dictionary):
    formatted_dictionary = [] 
    for key in dictionary:
        if(key.isalpha()):
            formatted_dictionary.append({"letter":key,"count":dictionary[key]})
    return formatted_dictionary

def sorter(sortable_list,property):
    def sort_on(dictionary):
        return dictionary[property]
    sortable_list.sort(reverse=True, key=sort_on)
    return sortable_list

def reporter(words,letters):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    for element in letters:
        letter = element["letter"]
        count = element["count"]
        print(f"The '{letter}' is found {count} times in the document")
    print("--- End report ---") 


main()
