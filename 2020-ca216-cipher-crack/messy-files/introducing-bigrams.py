import sys
import re

def create_count(letters):
    
    dictionary_of_letters = {}

    #letters = (elemental(text)) #turns list of strings into only lists of characters

    dictionary_of_letters = frequency(letters, dictionary_of_letters) #gets the sictionary of letters

    return(sort_dictionary(dictionary_of_letters)) #sorts the dictionary

def creating_the_key(ciphertext, trainingtext):
    key = {}

    ciphertext_list = list(ciphertext.values())
    trainingtext_list = list(trainingtext.values())

    i = 0
    while i < len(ciphertext_list):
        key[ciphertext_list[i]] = trainingtext_list[i]
        i += 1
    
    return key

# def bigram(ciphertext):
#     i = 0
#     bigrams = {}
#     while i < len(ciphertext):

        

def decrypt(encrypted_text, key):
    encrypted_text = ' '.join(encrypted_text)
    lst = []
    for letter in encrypted_text:
        if letter in key:
            #print(letter, key[letter])
            lst.append(key[letter])
    
    return lst


def sort_dictionary(dict):
    sorted_d = (sorted(dict.items(), key=lambda x: x[1], reverse=True))

    i = 1
    numbered_dict = {} 
    for k in sorted_d:
        numbered_dict[i] = k[0]
        i += 1
    
    return(numbered_dict)

def frequency(list_of_letters, dictionary):
    
    for letter in list_of_letters:
            keys = dictionary.keys()
            if letter in keys:
                dictionary[letter] += 1
            else:
                dictionary[letter] = 1
        
    return(dictionary)

def bigrams(list_of_words):
    
    all_bigrams = (list(''.join([i for i in list_of_words if i.isalpha()])))

    all_bigrams = [x.lower() for x in all_bigrams]

    create_count(all_bigrams)


def elemental(list_of_words):
    
    all_letters = (list(''.join([i for i in list_of_words if i.isalpha()])))

    all_letters = [x.lower() for x in all_letters]

    create_count(all_letters)


def main():
    
    with open(sys.argv[1], "r") as ciphertext, open(sys.argv[2], "r") as trainingtext, open("output.txt", "w") as output, open("key.txt", "w") as key_file:
        
        ciphertext = (ciphertext.read().split())
        ciphertext_word_freq = create_count(ciphertext)

        trainingtext = (trainingtext.read().split())
        trainingtext_word_freq = create_count(trainingtext)

        #print(ciphertext_word_freq)
        #print(trainingtext_word_freq)
        

        key = creating_the_key(ciphertext_word_freq, trainingtext_word_freq)

        key_file.write(str(key))  #puts key into its own file

        #print(ciphertext)

        decrypted_file = decrypt(ciphertext, key)

        output.write(str(decrypted_file))


if __name__ == "__main__":
    main()
