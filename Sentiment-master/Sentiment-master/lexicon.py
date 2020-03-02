f = open('lexicon.txt', "r", encoding='utf-8') # the file that contains the lexicon
f2 = open('foo2.txt', "r", encoding='utf-8') # the file that contains the lexicon
f3 = open('new_file2.txt', "w", encoding='utf-8')  #the out put file

def verify(word,lexicon): #this function verifys if the tweet contains at least one negative or positive word
    if word in lexicon: 
       return True
def normalize (norm):
		norm = norm.replace("ሃ", "ሀ")
		norm = norm.replace("ሐ", "ሀ")
		norm = norm.replace("ሓ", "ሀ")
		norm = norm.replace("ኅ", "ሀ")
		norm = norm.replace("ኃ", "ሀ")
		norm = norm.replace("ኋ", "ኋ")
		norm = norm.replace("ሗ", "ኋ")
		norm = norm.replace("ኁ", "ሁ")
		norm = norm.replace("ኂ", "ሂ")
		norm = norm.replace("ኄ", "ሄ");
		norm = norm.replace("ኅ", "ህ");
		norm = norm.replace("ኆ", "ሆ");
		norm = norm.replace("ሑ", "ሁ");
		norm = norm.replace("ሒ", "ሂ");
		norm = norm.replace("ሔ", "ሄ");
		norm = norm.replace("ሕ", "ህ");
		norm = norm.replace("ሖ", "ሆ");
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
		norm = norm.replace("ጸ", "ፀ");
		norm = norm.replace("ጹ", "ፁ");
		norm = norm.replace("ጺ", "ፂ");
		norm = norm.replace("ጻ", "ፃ");
		norm = norm.replace("ጼ", "ፄ");
		norm = norm.replace("ጽ", "ፅ");
		norm = norm.replace("ጾ", "ፆ");
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
		return norm

lexicon = list() #list that contain all the lexicon

for line in f:
    lexicon.append(normalize(line.strip()))

lines = f2.readlines()

for line in lines:
    for word in line.split(' '):
        if verify(normalize(word),lexicon): #verify if the tweet contains at least one lexicon
            f3.write(line) #write the final out put on the new_file
        
        
            

