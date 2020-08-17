import timeit
#code_to_test = """

import sys
import re
from textwrap import wrap

def create_unigram_count(text):

    dictionary_of_letters = {}

    new_list = []

    for word in text:                                       #iterate every word
        word = re.sub(r'[^a-zA-Z ]+', '', word)             #ensures only letters
        new_list.append(word)

    letters = getNGrams(new_list, 1)                        #split word in to n-grams, unigrams in this case                
       
    letters = frequency(letters, dictionary_of_letters)     #gets the sorted dictionary of letters, in order of frequency

    return letters                                  


def create_bigram_count(text):

    dictionary_of_letters = {}

    new_list = []

    for word in text:                                       
        word = re.sub(r'[^a-zA-Z ]+', '', word)             #ensures only letters
        new_list.append(word)
    
    bigram = getNGrams(new_list, 2)                        
       
    bigram = frequency(bigram, dictionary_of_letters)       #gets the sorted dictionary of letters

    return bigram

def create_trigram_count(text):

    dictionary_of_letters = {}

    new_list = []

    for word in text:                                       
        word = re.sub(r'[^a-zA-Z ]+', '', word)             #ensures only letters
        new_list.append(word)
  
    trigram = getNGrams(new_list, 3)                             
       
    trigram = frequency(trigram, dictionary_of_letters)      #gets the sorted dictionary of letters

    return trigram 


def creating_the_key(ciphertext, trainingtext):
    key = {}                                                #initialise key

    ciphertext_list = list(ciphertext.values())             #this gets the values in order, by turning them into a list
    trainingtext_list = list(trainingtext.values())

    i = 0
    while i < len(ciphertext_list):
        key[ciphertext_list[i]] = trainingtext_list[i]      #they can then be assigned to one another in a new key, to be used for deciphering
        i += 1
    
    return key


def sort_dictionary(dict):
    sorted_d = (sorted(dict.items(), key=lambda x: x[1], reverse=True))
                                                            #i use a lambda fucntion to reverse the order of the list so it is in decending order
    i = 1
    numbered_dict = {}                                      
    for k in sorted_d:
        numbered_dict[i] = k[0]                             #we then assign numbers to the dictionary values to state their order of frequency
        i += 1
    
    return(numbered_dict)

def frequency(list_of_ngrams, dictionary):                  
    
    for gram in list_of_ngrams:                           
            keys = dictionary.keys()                        
            if gram in keys:                                #this will result in the most frequent n-gram having the highest count
                dictionary[gram] += 1
            else:
                dictionary[gram] = 1

    dictionary = sort_dictionary(dictionary)                #we send the dictionary off to be ordered
    return(dictionary)


def getNGrams(wordlist, n):         
    ngrams = []
    for word in wordlist:                               
        for i in range(len(word)-(n-1)):                    
            ngrams.append(word[i:i+n])                      #the n-gram is based on whatever n is the input
    return ngrams       

def main():
    
    with open(sys.argv[1], "r") as ciphertext, open(sys.argv[2], "r") as trainingtext, open("output.txt", "w") as output, open("key.txt", "w") as key_file:
        
        #start one thread here
        ciphertext = (ciphertext.read().split())                                #split text into a list of words

        ciphertext_words = []

        for word in ciphertext:                     
            word = re.sub(r'[^a-zA-Z ]+', '', word)                             #ensures only letters are being considered
            ciphertext_words.append(word)

        uni_ciphertext_word_freq = create_unigram_count(ciphertext_words)       #returns n-gram frequency in a dictionary
        bi_ciphertext_word_freq = create_bigram_count(ciphertext_words)
        tri_ciphertext_word_freq = create_trigram_count(ciphertext_words)

        #start next thread here
        trainingtext = (trainingtext.read().split())

        training_text_words = []

        for word in trainingtext:                     
            word = re.sub(r'[^a-zA-Z ]+', '', word)                                 #ensures only letters
            training_text_words.append(word)

        uni_trainingtext_word_freq = create_unigram_count(training_text_words)
        bi_trainingtext_word_freq = create_bigram_count(training_text_words)
        tri_trainingtext_word_freq = create_trigram_count(training_text_words)      #returns the dictionary of letters and theyre ranking
        

        unikey = creating_the_key(uni_ciphertext_word_freq, uni_trainingtext_word_freq)
        bikey = creating_the_key(bi_ciphertext_word_freq, bi_trainingtext_word_freq)
        trikey = creating_the_key(tri_ciphertext_word_freq, tri_trainingtext_word_freq)

        key_file.write(str(unikey))                                                 #puts n-gram keys into their own file
        key_file.write(str(bikey))      
        key_file.write(str(trikey))

        decrypted = []                                  
        
        for word in ciphertext_words:                                               #we now want to decrypt word for word in the ciphertext file
            
            string = ''
            word = wrap(word, 3)                                                    #the wrap fuction returns argument in tri-grams
            for gram in word:                                                       #iterate through word
                if gram in trikey:                                                  #we then check if it is in any of out keys, if it is, replace it with the corresponding value
                    string += (trikey[gram])
                elif gram in bikey:
                    string += (bikey[gram])
                elif gram in unikey:
                    string += (unikey[gram])
            
            decrypted.append(string)                                                #we then append the word to our decrypted string
            
        output.write(' '.join(decrypted))                                           #it is then joined together in a string, to be written into an output file.


if __name__ == "__main__":
    main()

# """

# elapsed_time = timeit.timeit(code_to_test, number=100)/100
# print(elapsed_time)