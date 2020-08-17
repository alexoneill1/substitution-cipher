import sys
from collections import Counter

def char_frequency(words):
    plain_text_dict = {}
    for n in words:
        for letter in n:
            keys = plain_text_dict.keys()
            if letter in keys:
                plain_text_dict[letter] += 1
            else:
                plain_text_dict[letter] = 1
    #print(dict)

    sorted_d = (sorted(plain_text_dict.items(), key=lambda x: x[1], reverse=True))
    # for k, v in sorted_d:
    #     print(str(k) + " occurs " + str(v) + " times.")
    
    i = 1
    numbered_dict = {} 
    for k in sorted_d:
        numbered_dict[i] = k[0]
        i += 1

    print(numbered_dict)

def char_frequency2(words):
    traning_text_dict = {}
    for n in words:
        for letter in n:
            keys = traning_text_dict.keys()
            if letter in keys:
                traning_text_dict[letter] += 1
            else:
                traning_text_dict[letter] = 1
    #print(dict)

    sorted_d = (sorted(traning_text_dict.items(), key=lambda x: x[1], reverse=True))
    # for k, v in sorted_d:
    #     print(str(k) + " occurs " + str(v) + " times.")
    
    i = 1
    numbered_dict2 = {} 
    for k in sorted_d:
        numbered_dict2[i] = k[0]
        i += 1

    print(numbered_dict2)

def main():
    with open(sys.argv[1], "r") as ciphertext:
        words = ciphertext.read().split()

    with open(sys.argv[2], "r") as trainingtext:
        words2 = trainingtext.read().split()
    
    char_frequency(words)

    char_frequency2(words2)

    

    

if __name__ == "__main__":
    main()