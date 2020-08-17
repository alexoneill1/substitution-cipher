import sys
import re

def create_ngram_count(text):

    dictionary_of_letters = {}

    #letters = (elemental(text, 1)) #turns list of strings into only lists of characters

    letters = getNGrams(text, 1)

    bigrams = getNGrams(text, 2)

    trigrams = getNGrams(text, 3)
    print(letters)
    print(bigrams)
    print(trigrams)

    dictionary_of_letters = frequency(letters, dictionary_of_letters) #gets the sictionary of letters

    return(sort_dictionary(dictionary_of_letters)) #sorts the dictionary

    # types_of_ngrams = ['letters', 'bigrams', 'trigrams']
    # dictionary_of_ngrams = {}

    # for type in types_of_ngrams:

        

    #     dictionary_of_ngrams = {}

    #     type = (elemental(text, 1)) #turns list of strings into only lists of characters


    #     dictionary_of_ngrams = frequency(type, dictionary_of_ngrams)

    #     type = (sort_dictionary(dictionary_of_ngrams))

    # return types_of_ngrams

def creating_the_key(ciphertext, trainingtext):
    key = {}

    ciphertext_list = list(ciphertext.values())
    trainingtext_list = list(trainingtext.values())

    i = 0
    while i < len(ciphertext_list):
        key[ciphertext_list[i]] = trainingtext_list[i]
        i += 1
    
    return key

        

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

def frequency(list_of_ngrams, dictionary):
    
    for letter in list_of_ngrams:
            keys = dictionary.keys()
            if letter in keys:
                dictionary[letter] += 1
            else:
                dictionary[letter] = 1
        
    return(dictionary)

def elemental(list_of_words, n):

    #print(list_of_words)
    new_list = []
    n = 1
    #print(list_of_words)

    for word in list_of_words:                      #this is working
        word = re.sub(r'[^a-zA-Z ]+', '', word)
        new_list.append(word)
    
    return new_list

def getNGrams(wordlist, n):
    ngrams = []
    for word in wordlist:   
        for i in range(len(word)-(n-1)):
            ngrams.append(word[i:i+n])
    print(ngrams)

    
                        
    
    # words = 'this is a foo bar sentences and i want to ngramize it'

    # for word in words:
    #     n = 2
    #     word = ngrams(word, n)
    #     print(word)

    
    # ngrams_list = []
 
    # for num in range(0, len(new_list)):
    #     ngram = ' '.join(new_list[num:num + n])
    #     ngrams_list.append(ngram)

    # for grams in sixgrams:
    #     print(grams)
        

    
    
    #all_ngrams = (list(''.join([i for i in new_list if i.isalpha()])))

    #all_ngrams = [x.lower() for x in new]
    #print(new_list)


def main():
    
    with open(sys.argv[1], "r") as ciphertext, open(sys.argv[2], "r") as trainingtext, open("output.txt", "w") as output, open("key.txt", "w") as key_file:
        
        ciphertext = (ciphertext.read().split())
        ciphertext_word_freq = create_ngram_count(ciphertext)

        trainingtext = (trainingtext.read().split())
        #trainingtext_word_freq = create_ngram_count(trainingtext)   #returns the dictionary of letters and theyre ranking

        print(ciphertext_word_freq)
        print(trainingtext_word_freq)
        

        key = creating_the_key(ciphertext_word_freq, trainingtext_word_freq)

        key_file.write(str(key))  #puts key into its own file

        #print(ciphertext)

        decrypted_file = decrypt(ciphertext, key)

        output.write(str(decrypted_file))


if __name__ == "__main__":
    main()
