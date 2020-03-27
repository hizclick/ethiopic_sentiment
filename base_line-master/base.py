text1 = open('this.txt', "r", encoding='utf-8')
text2 = open('negative.txt', "r", encoding='utf-8')
text3 = open('positive.txt', "r", encoding='utf-8')
import re


def count_neg(word,lexicon): #this function verifys if the tweet contains at least one negative or positive word
    if word in lexicon: 
       return True
def normalize (norm):
		norm = norm.replace("ሃ", "ሀ")
		norm = norm.replace("ሐ", "ሀ")
		norm = norm.replace("ሓ", "ሀ")
		norm = norm.replace("ኅ", "ሀ")
		norm = norm.replace("ኻ", "ሀ")
		norm = norm.replace("ኃ", "ሀ")
		norm = norm.replace("ዅ", "ሁ")
		norm = norm.replace("ሗ", "ኋ")
		norm = norm.replace("ኁ", "ሁ")
		norm = norm.replace("ኂ", "ሂ")
		norm = norm.replace("ኄ", "ሄ");
		norm = norm.replace("ዄ", "ሄ");
		norm = norm.replace("ኅ", "ህ");
		norm = norm.replace("ኆ", "ሆ");
		norm = norm.replace("ሑ", "ሁ");
		norm = norm.replace("ሒ", "ሂ");
		norm = norm.replace("ሔ", "ሄ");
		norm = norm.replace("ሕ", "ህ");
		norm = norm.replace("ሖ", "ሆ");
		norm = norm.replace("ኾ", "ሆ");
		norm = norm.replace("ሠ", "ሰ");
		norm = norm.replace("ሡ", "ሱ");
		norm = norm.replace("ሢ", "ሲ");
		norm = norm.replace("ሣ", "ሳ");
		norm = norm.replace("ሤ", "ሴ");
		norm = norm.replace("ሥ", "ስ");
		norm = norm.replace("ሦ", "ሶ");
		norm = norm.replace("ሼ", "ሸ");
		norm = norm.replace("ቼ", "ቸ");
		norm = norm.replace("ዬ", "የ");
		norm = norm.replace("ዲ", "ድ");
		norm = norm.replace("ጄ", "ጀ");
		norm = norm.replace("ፀ", "ጸ");
		norm = norm.replace("ፁ", "ጹ");
		norm = norm.replace("ፂ", "ጺ");
		norm = norm.replace("ፃ", "ጻ");
		norm = norm.replace("ፄ", "ጼ");
		norm = norm.replace("ፅ", "ጽ");
		norm = norm.replace("ፆ", "ጾ");
		norm = norm.replace("ዉ", "ው");
		norm = norm.replace("ዴ", "ደ");
		norm = norm.replace("ቺ", "ች");
		norm = norm.replace("ዪ", "ይ");
		norm = norm.replace("ጪ", "ጭ");
		norm = norm.replace("ዓ", "አ");
		norm = norm.replace("ዑ", "ኡ");
		norm = norm.replace("ዒ", "ኢ");
		norm = norm.replace("ዐ", "አ");
		norm = norm.replace("ኣ", "አ");
		norm = norm.replace("ዔ", "ኤ");
		norm = norm.replace("ዕ", "እ");
		norm = norm.replace("ዖ", "ኦ");
		norm = norm.replace("ኚ", "ኝ");
		norm = norm.replace("ሺ", "ሽ");
		
		norm=re.sub('(ሉ[ዋአ])','ሏ',norm)
		norm=re.sub('(ሙ[ዋአ])','ሟ',norm)
		norm=re.sub('(ቱ[ዋአ])','ቷ',norm)
		norm=re.sub('(ሩ[ዋአ])','ሯ',norm)
		norm=re.sub('(ሱ[ዋአ])','ሷ',norm)
		norm=re.sub('(ሹ[ዋአ])','ሿ',norm)
		norm=re.sub('(ቁ[ዋአ])','ቋ',norm)
		norm=re.sub('(ቡ[ዋአ])','ቧ',norm)
		norm=re.sub('(ቹ[ዋአ])','ቿ',norm)
		norm=re.sub('(ሁ[ዋአ])','ኋ',norm)
		norm=re.sub('(ኑ[ዋአ])','ኗ',norm)
		norm=re.sub('(ኙ[ዋአ])','ኟ',norm)
		norm=re.sub('(ኩ[ዋአ])','ኳ',norm)
		norm=re.sub('(ዙ[ዋአ])','ዟ',norm)
		norm=re.sub('(ጉ[ዋአ])','ጓ',norm)
		norm=re.sub('(ደ[ዋአ])','ዷ',norm)
		norm=re.sub('(ጡ[ዋአ])','ጧ',norm)
		norm=re.sub('(ጩ[ዋአ])','ጯ',norm)
		norm=re.sub('(ጹ[ዋአ])','ጿ',norm)
		norm=re.sub('(ፉ[ዋአ])','ፏ',norm)
		norm=re.sub('[ቊ]','ቁ',norm) 
		norm=re.sub('[ኵ]','ኩ',norm)
		return norm

neg = list()
pos = list()

for line in text2 :
    neg.append(normalize(line.strip()))

for line in text3:
    pos.append(normalize(line.strip()))

lines = text1.readlines()

n = 0
p = 0

nega = dict()
po = dict()
count = 0

test = list()

for line in lines:
	count = count + 1
	for word in line.split():
		if count_neg(normalize(word),neg): #verify if the tweet contains at least one lexicon
			n = n + 1 #write the final out put on the new_file
			test.append(word)
	nega[line.strip()] = n
	n = 0

for line in lines:
    for word in line.split():
        if count_neg(normalize(word),pos): #verify if the tweet contains at least one lexicon
            n = n + 1 #write the final out put on the new_file
    po[line.strip()] = n
    n = 0

sentiment = dict()

for key, value in nega.items():
	if key in po:
		if po[key] > nega[key]:
			sentiment[key] = 1
		elif po[key] < nega[key]:
			sentiment[key] = -1
		elif po[key] == 0 and nega[key]==0:
			sentiment[key] = 0
		elif po[key] == nega[key]:
			sentiment[key] = 2

import pandas as pd

inp = list()

data = pd.read_csv('f.csv') 

for val in data['sentiment']:
	inp.append(val) 



with open('result2.csv', 'w', encoding="utf-8") as f:
    for key in sentiment.keys():
        f.write("%s,%s\n"%(key,sentiment[key]))

