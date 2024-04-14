import os
import math


RANGE_ASCII=[(48,57),(65,90),(97,122)]#,(128,155),(160,167),(181,183),(192,214),(208,216),(224,237)]
#ASCII_SINGLE=[157,181,182,183,198,199,222]
ASCII_ACCEPT=[]
for begin,end in RANGE_ASCII:
    for n in range(begin,end+1):
        ASCII_ACCEPT.append(n)
#ASCII_ACCEPT+=ASCII_SINGLE
ASCII_ACCEPT.sort()


def add_tuple(words,wordlist,last_word,word):
    if last_word in words.keys():
        words[last_word]+=1
        if word in wordlist[last_word].keys():
            wordlist[last_word][word]+=1
        else:
            wordlist[last_word][word]=1
    else:
        words[last_word]=1
        wordlist[last_word]={}
        wordlist[last_word][word]=1
    return words,wordlist

def create_output(filename):
    with open(f'input/{filename}',"r") as F:
        text=F.read()
    print("Creando expected_csv per:",'{:<30}'.format(filename),"caratteri totali:",len(text))
    words={".":0}
    wordlist={".":{}}
    word=""
    last_word="."
    word_counter=0
    for i,char in enumerate(text):
        char=char.lower()
        if ord(char) in ASCII_ACCEPT:
            word+=char
        elif char=="'":
            if word!="":
                word+=char
                words,wordlist=add_tuple(words,wordlist,last_word,word)
                if word_counter==0:
                    first_word=word
                    word_counter+=1
                last_word=word
                word=""
            elif i+1<len(text) and ord(text[i+1]) in ASCII_ACCEPT:
                word="'"
        elif char in [".","!","?"]:
            if word!="":
                words,wordlist=add_tuple(words,wordlist,last_word,word)
                words,wordlist=add_tuple(words,wordlist,word,str(char))
                if word_counter==0:
                    first_word=word
                    word_counter+=1
                last_word=str(char)
                word=""
            else:
                words,wordlist=add_tuple(words,wordlist,last_word,str(char))
                if word_counter==0:
                    first_word=word
                    word_counter+=1
                last_word=str(char)
                word=""
        else:
            if word!="":
                words,wordlist=add_tuple(words,wordlist,last_word,word)
                if word_counter==0:
                    first_word=word
                    word_counter+=1
                last_word=word
                word=""
    if word!="":
        words,wordlist=add_tuple(words,wordlist,last_word,word)
        if word_counter==0:
                    first_word=word
                    word_counter+=1
        last_word=word
    if last_word!=".":
        words,wordlist=add_tuple(words,wordlist,last_word,first_word)

    
    if len(words)<=1:
        return
    

    outfile=filename.removesuffix(".txt")+"_expected.csv"
    
    with open(f'expected_csv/{outfile}',"w") as F:
        for word, next_words in wordlist.items():
            F.write(word)
            for next_word, counter in next_words.items():
                if counter%words[word]==0:
                    prob=int(counter/words[word])
                else:
                    prob='{:.4f}'.format((counter/words[word]))
                F.write(","+next_word+","+str(prob))
            F.write("\n")




if __name__=="__main__":
    for file in os.listdir("expected_csv"):
        os.remove("expected_csv/"+file)
    for file in os.listdir("input"):
        create_output(file)