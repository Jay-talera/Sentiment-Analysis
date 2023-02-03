import preProcessing as pp
from collections import Counter


emotion_list=[]

with open('emotions.txt','r') as file:
    for line in file:
        clear_line = line.replace("\n","").replace(",","").replace("'","").strip()
        word, emotion = clear_line.split(":")
        
        #print("Word : " + " " +word +"    "+  "Emotion : " +emotion)
        
        if word in pp.final_words:
            emotion_list.append(emotion)
        
print(emotion_list)

count = Counter(emotion_list)
print(count)