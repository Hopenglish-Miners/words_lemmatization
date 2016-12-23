import json
import nltk
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

f_w=open('video_data_stop_words_removed.json')
v_word = json.load(f_w)

wordListWithoutTag = []


final = []

for x in range(0, len(v_word)):
    wordlist = []
    for word in v_word[x]['stop_word_filtered']:
        if(word.isalpha()):
            if word in wordlist:
                continue
            else:
                f1 = wordnet_lemmatizer.lemmatize(word)
                filteredWord = wordnet_lemmatizer.lemmatize(f1,pos='v')
                if not (filteredWord in  wordlist):
                    wordlist.append(filteredWord)
    video = {
        'postId' : v_word[x]['postId'],
        'wordList' : wordlist
    }
    final.append(video)

            
'''
for x in wordListWithoutTag:
    print x

wordDropRepeat = []

for x in wordListWithoutTag:
    if x in wordDropRepeat:
        print ("I know.")
    else:
        wordDropRepeat.append(x)
'''
writeToFile=open('filteredWords.json','w')

json.dump(final,writeToFile)

writeToFile.close()


