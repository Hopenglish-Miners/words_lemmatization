import json
import nltk
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

f_w=open('student_dictionary_stop_words_removed.json')
v_word = json.load(f_w)

final = []
for x in range(0, len(v_word)):
    removed = []
    for word in stu[x]['stop_word_filtered'].keys():
        if(word.isalpha()):
            f1 = wordnet_lemmatizer.lemmatize(word)
            filteredWord = wordnet_lemmatizer.lemmatize(f1, pos='v')
            if not (filteredWord in removed):
                # if not duplicated word
                removed.append(filteredWord)
    user = {
        'memberId' : v_word[x]['memberId'],
        'stop_word_filtered' : v_word[x]['stop_word_filtered'],
        'wordList' : v_word[x]['wordList'],
        'lemmatization_filtered': removed
    }
    final.append(user)

writeToFile=open('student_filteredWords.json','w')
json.dump(final, writeToFile)
writeToFile.close()
f_w.close()
