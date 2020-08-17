import re
import sys
from collections import Counter

def char_frequency(words):
    plain_text_dict = {}
    
    words = (' ' .join(words))
    words = re.sub(r'[^a-zA-Z ]+', '', words)
    words = re.sub("\d+", "", words)
    words = words.lower()
    for n in words:
        for letter in n:
            keys = plain_text_dict.keys()
            if letter in keys:
                plain_text_dict[letter] += 1
            else:
                plain_text_dict[letter] = 1

    sorted_d = (sorted(plain_text_dict.items(), key=lambda x: x[1], reverse=True))
    # for k, v in sorted_d:
    #     print(str(k) + " occurs " + str(v) + " times.")
    
    i = 1
    numbered_dict = {} 
    for k in sorted_d:
        numbered_dict[i] = k[0]
        i += 1

    return numbered_dict

def char_frequency2(words):
    traning_text_dict = {}
    
    words = (' ' .join(words))
    words = re.sub(r'[^a-zA-Z ]+', '', words)
    words = re.sub("\d+", "", words)
    words = words.lower()
    for n in words:
        for letter in n:
            keys = traning_text_dict.keys()
            if letter in keys:
                traning_text_dict[letter] += 1
            else:
                traning_text_dict[letter] = 1

    sorted_d = (sorted(traning_text_dict.items(), key=lambda x: x[1], reverse=True))
    
    i = 1
    numbered_dict2 = {} 
    for k in sorted_d:
        numbered_dict2[i] = k[0]
        i += 1

    return numbered_dict2

def main():
    with open(sys.argv[1], "r") as ciphertext, open(sys.argv[2], "r") as trainingtext, open("output.txt", "w") as output:
        words = ciphertext.read().split()
        first_dict = char_frequency(words)

        words2 = trainingtext.read().split()
        second_dictionary = char_frequency2(words2)

        common_keys = list(set(first_dict.keys()) & set(second_dictionary.keys()))
    
        
        words = ' '.join(words)
        words = re.split(r'(\s+)', words)
        words = ' '.join(words)

        str = ""   
        for letter in words:
            if letter in first_dict.values():
                for k, v in first_dict.items():
                    if v == letter:
                        #if k in second_dictionary:
                        str += second_dictionary[k]
                        #else:
                            #str += "NO"
                    
        
        
        output.write(str)

        print(first_dict)
        print(second_dictionary)

    
    

if __name__ == "__main__":
    main()