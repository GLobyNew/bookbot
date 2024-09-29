def print_Book():
    with open("books/frankenstein.txt", "r") as f:
        file_content = f.read()
        #print(file_content)


def count_words():
    with open("books/frankenstein.txt", "r") as f:
        file_content = f.read()
        splitted = file_content.split()
        return len(splitted)
    
def convert_dict_to_list(dict):
    characters_list = []
    for entry in dict:
        characters_list.append({"char" : entry, "num" : dict[entry]})
    return characters_list


def create_dict():
    with open("books/frankenstein.txt", "r") as f:
        file_content = f.read()
        file_content = file_content.lower()
        dictionary = {}
        for ch in file_content:
            if ch.isalpha():
                if ch in dictionary:
                    dictionary[ch] += 1
                else:
                    dictionary[ch] = 1
        return dictionary


def count_letters():
    dict_of_chars = create_dict()
    list_of_chars = convert_dict_to_list(dict_of_chars)
    list_of_chars.sort(reverse=True, key=sort_on)
    return list_of_chars
        

def sort_on(dict):
    return dict["num"]


def main():
    print("--- Begin report of books/frankenstein.txt ---")
    #print_Book()
    print(count_words(), "words found in the document", '\n')
    list_of_chars = count_letters()
    for entry in list_of_chars:
        print(f"The '{entry["char"]}' character was found {entry["num"]} times")

if __name__ == "__main__":
    main()
